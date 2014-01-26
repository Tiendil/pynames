# coding: utf-8
import json
import random

from .generators import GENDER, LANGUAGE, Name, BaseGenerator, PynamesException


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

    def get_name(self, tables):
        languages = dict( (lang, u'') for lang in self.languages)
        for slug in self.template:
            record = random.choice(tables[slug])
            for lang in languages:
                languages[lang] += record['languages'][lang]
        genders = dict( (gender, languages) for gender in self.genders)
        return Name(self.native_language, {'genders': genders})


class FromTablesGenerator(BaseGenerator):

    SOURCE = None

    def __init__(self):
        super(FromTablesGenerator, self).__init__()
        self.templates_choices = {}
        self.templates = []
        self.tables = {}

        if self.SOURCE is None:
            error_msg = 'FromTablesGenerator: you must make subclass of FromTablesGenerator and define attribute SOURCE in it.'
            raise NotImplementedError(error_msg)

        with open(self.SOURCE) as f:
            data = json.load(f)
            self.native_language = data['native_language']
            self.languages = set(data['languages'])
            self.templates = [ Template(template_name, self.native_language, self.languages, template_data)
                               for template_name, template_data in data['templates'].items() ]
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

        raise PynamesException('FromTablesGenerator: wrong template structure - cannot choose template for genders %r with template source: "%s"' % (genders, self.SOURCE) )

    def get_name_simple(self, gender=GENDER.MALE, language=LANGUAGE.NATIVE):
        name = self.get_name(genders=[gender])
        return name.get_for(gender, language)

    def test_names_consistency(self, test):
        for table_name, table in self.tables.iteritems():
            for record in table:
                test.assertEqual(set(record['languages'].keys()) & self.languages, self.languages)
