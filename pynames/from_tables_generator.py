# coding: utf-8

from __future__ import unicode_literals

# python lib:
import json
import random
from collections import Iterable

# thirdparties:
import six
import unicodecsv

# pynames:
from pynames import exceptions
from pynames.base import BaseGenerator
from pynames.names import Name
from pynames.relations import GENDER, LANGUAGE, LANGUAGE_FORMS_LANGTH
from pynames.utils import file_adapter


class Template(object):

    __slots__ = ('name', 'probability', 'genders', 'template', 'native_language', 'languages')

    def __init__(self, name, native_language, languages, data):
        self.name = name
        self.native_language = native_language
        self.languages = frozenset(languages)
        self.probability = data['probability']
        self.genders = frozenset(data['genders'])
        self.template = data['template']

    def exists_for(self, genders):
        return genders & self.genders

    def get_names_number(self, tables):
        number = 1
        for slug in self.template:
            number *= len(tables[slug])
        return number

    @classmethod
    def merge_forms(cls, left, right):
        if not isinstance(left, six.string_types):
            if not isinstance(right, six.string_types):
                if len(left) != len(right):
                    raise exceptions.NotEqualFormsLengths(left=left, right=right)
                return [l+r for l, r in zip(left, right)]
            else:
                return [l+right for l in left]
        else:
            if not isinstance(right, six.string_types):
                return [left+r for r in right]
            else:
                return left + right

    def get_name(self, tables):
        languages = dict(
            (lang, '') for lang in self.languages
        )
        for slug in self.template:
            record = random.choice(tables[slug])
            languages = {
                lang: self.merge_forms(forms, record['languages'][lang])
                for lang, forms in six.iteritems(languages)
            }

        genders = dict(
            (gender, languages)
            for gender in self.genders
        )

        return Name(self.native_language, {'genders': genders})

    def __eq__(self, other):
        return (
            self.native_language == other.native_language
            and self.languages == other.languages
            and self.probability == other.probability
            and self.genders == other.genders
            and self.template == other.template
        )

    def __hash__(self):
        return hash((self.native_language, self.languages, self.probability, self.genders, ';'.join(self.template)))

    def __repr__(self):
        return "<pynames.from_tables_generator.Template: %s=%s>" % (self.name, self.template)


class FromTablesGenerator(BaseGenerator):

    SOURCE = None

    def __init__(self):
        super(FromTablesGenerator, self).__init__()
        self.templates_choices = {}
        self.templates = []
        self.tables = {}
        self.source_loader(self.SOURCE)

    def source_loader(self, source):
        if source is None:
            error_msg = 'FromTablesGenerator: you must make subclass of FromTablesGenerator and define attribute SOURCE in it.'
            raise NotImplementedError(error_msg)

        with file_adapter(source) as f:
            data = json.loads(f.read().decode('utf-8'))
            self.native_language = data['native_language']
            self.languages = set(data['languages'])
            self.full_forms_for_languages = set(data.get('full_forms_for_languages', set()))
            self.templates = [
                Template(template_name, self.native_language, self.languages, template_data)
                for template_name, template_data in data['templates'].items()
            ]
            self.tables = data['tables']

    @staticmethod
    def _get_templates_cache_key(genders):
        return 't:%s' % '_'.join(genders)

    def _get_templates_slice(self, genders):
        key = self._get_templates_cache_key(genders)
        genders = frozenset(genders)
        if key not in self.templates_choices:
            self.templates_choices[key] = [template
                                           for template in self.templates
                                           if template.exists_for(genders)]
        return self.templates_choices[key]

    def _get_names_number_for_template(self):
        pass

    def get_names_number(self, genders=GENDER.ALL):
        templates = self._get_templates_slice(genders)
        number = sum([template.get_names_number(self.tables) for template in templates])
        return number

    def get_name(self, genders=GENDER.ALL):
        templates = self._get_templates_slice(genders)
        definition_number = sum([template.probability for template in templates])

        choice = random.randint(1, definition_number)

        for template in templates:
            if choice > template.probability:
                choice -= template.probability
                continue
            return template.get_name(self.tables)

        raise exceptions.WrongTemplateStructureError(genders=genders, soruce=self.SOURCE)

    def get_name_simple(self, gender=GENDER.MALE, language=LANGUAGE.NATIVE):
        name = self.get_name(genders=[gender])
        return name.get_for(gender, language)

    def test_names_consistency(self, test):
        for table_name, table in six.iteritems(self.tables):
            for record in table:
                test.assertEqual(set(record['languages'].keys()) & self.languages, self.languages)

        for template in self.templates:
            last_table = template.template[-1]
            for language in self.full_forms_for_languages:
                for record in self.tables[last_table]:
                    test.assertTrue(isinstance(record['languages'][language], list))
                    test.assertEqual(len(record['languages'][language]), LANGUAGE_FORMS_LANGTH[language])


class FromCSVTablesGenerator(FromTablesGenerator):

    """Variation of :py:calss:`FromTablesGenerator` that accepts path to 3 csv files as SOURCE.

    Read docs of :py:meth:`source_loader` for more details.

    """

    def source_loader(self, source_paths, create_missing_tables=True):
        """Load source from 3 csv files.

        First file should contain global settings:

        * ``native_lagnauge,languages`` header on first row
        * appropriate values on following rows

        Example::

            native_lagnauge,languages
            ru,ru
              ,en

        Second file should contain templates:

        * ``template_name,probability,genders,template`` header on first row
        * appropriate values on following rows (separate values with semicolon ";" in template column)

        Example::

            template_name,probability,genders,template
            male_1,5,m,prefixes;male_suffixes
            baby_1,1,m;f,prefixes;descriptive

        Third file should contain tables with values for template slugs in all languages:

        * first row should contain slugs with language code after colon for each
        * appropriate values on following rows. Multiple forms may be specified using semicolon as separator

        Example::

            prefixes:ru,prefixes:en,male_suffixes:ru,male_suffixes:en,descriptive:ru,descriptive:en
            Бж,Bzh,пра,pra,быстряк;быстряку,fasty
            дон;дону,don,Иван;Ивану,Ivan,Иванов;Иванову,Ivanov

        Note: you may use slugs without ":lang_code" suffix in csv header of tables file. Such headers will be treated as headers for native language

        If tables are missing for some slug then it is automatically created with values equeal to slug itself.
        So you may use some slugs without specifying tables data for them. Example for apostrophe and space:

            male_1,5,m,prefixes;';male_suffixes
            male_full,5,m,first_name; ;last_name

        """
        if not isinstance(source_paths, Iterable) or len(source_paths) < 3:
            raise TypeError('FromCSVTablesGenerator.source_loader accepts list of 3 paths as argument. Got `%s` instead' % source_paths)
        self.native_language = ''
        self.languages = []
        self.templates = []
        self.tables = {}

        self.load_settings(source_paths[0])
        template_slugs = self.load_templates(source_paths[1])
        self.load_tables(source_paths[2])

        if create_missing_tables:
            self.create_missing_tables(template_slugs)

        self.full_forms_for_languages = set()

    def load_settings(self, settings_source):
        with file_adapter(settings_source) as settings_file:
            reader = unicodecsv.DictReader(settings_file, encoding='utf-8')
            for row in reader:
                new_native_language = row.get('native_language', '').strip()
                if new_native_language and not self.native_language:
                    self.native_language = new_native_language
                elif self.native_language and new_native_language and self.native_language != new_native_language:
                    raise exceptions.WrongCSVData(
                        'Wrong settings csv file. Native language is already set to "%(native_language)s" but new value "%(new_value)s" is present on some row',
                        native_language=self.native_language,
                        new_value=new_native_language
                    )

                new_language = row.get('languages', '').strip()
                if new_language:
                    self.languages.append(new_language)
        self.languages = set(self.languages)

    def load_templates(self, templates_source):
        template_slugs = []

        with file_adapter(templates_source) as templates_file:
            reader = unicodecsv.DictReader(templates_file, encoding='utf-8')
            for row in reader:
                template_data = {
                    'probability': float(row['probability']),
                    'genders': row['genders'].replace(' ', '').split(';'),
                    'template': row['template'].split(';'),
                }
                self.templates.append(
                    Template(row['template_name'], self.native_language, self.languages, template_data)
                )
                template_slugs.extend(template_data['template'])

        template_slugs = set(template_slugs)
        return template_slugs

    def load_tables(self, tables_source):
        with file_adapter(tables_source) as tables_file:
            reader = unicodecsv.DictReader(tables_file, encoding='utf-8')
            slugs = set([fieldname.split(':')[0] for fieldname in reader.fieldnames])
            for slug in slugs:
                self.tables[slug] = []
            for row in reader:
                for slug in slugs:
                    table_item = {}
                    for language in self.languages:
                        value = row.get('%s:%s' % (slug, language), '')
                        if not value and language == self.native_language:
                            value = row.get(slug, '')
                        if value:
                            if value.find(';') > 0:
                                value = value.split(';')
                            table_item.setdefault('languages', {})[language] = value
                        elif table_item:
                            # some language already present but current is missing
                            raise exceptions.WrongCSVData(
                                'Missing language "%(language)s" for table "%(slug)s" with partial datum "%(table_item)s"',
                                language=language, slug=slug, table_item=table_item,
                            )
                    if table_item:
                        self.tables[slug].append(table_item)
        return

    def create_missing_tables(self, template_slugs):
        for slug in template_slugs:
            if not self.tables.get(slug, ''):
                table_item = {'languages': {}}
                for language in self.languages:
                    table_item['languages'][language] = slug

                self.tables.setdefault(slug, []).append(table_item)
