# coding: utf-8

from __future__ import unicode_literals

import json
import random

from pynames.relations import GENDER, LANGUAGE, LANGUAGE_FORMS_LANGTH
from pynames.names import Name
from pynames.base import BaseGenerator
from pynames import exceptions

class FromListGenerator(BaseGenerator):

    SOURCE = None

    def __init__(self):
        super(FromListGenerator, self).__init__()
        self.names_list = []
        self.choices = {}

        if self.SOURCE is None:
            error_msg = 'FromListGenerator: you must make subclass of FromListGenerator and define attribute SOURCE in it.'
            raise NotImplementedError(error_msg)

        with open(self.SOURCE, encoding='utf-8') as f:
            names_data = json.load(f)
            self.native_language = names_data['native_language']
            self.languages = set(names_data['languages'])
            self.full_forms_for_languages = set(names_data.get('full_forms_for_languages', set()))
            for name_data in names_data['names']:
                self.names_list.append(Name(self.native_language, name_data))

        if not self.names_list:
            raise exceptions.NoNamesLoadedFromListError(source=self.SOURCE)

    @staticmethod
    def _get_cache_key(genders):
        return '_'.join(genders)

    def _get_slice(self, genders):
        key = self._get_cache_key(genders)
        genders = frozenset(genders)
        if key not in self.choices:
            self.choices[key] = [name_record
                                 for name_record in self.names_list
                                 if name_record.exists_for(genders)]
        return self.choices[key]

    def get_names_number(self, genders=GENDER.ALL):
        return len(self._get_slice(genders))

    def get_name(self, genders=GENDER.ALL):
        return random.choice(self._get_slice(genders))

    def get_name_simple(self, gender=GENDER.MALE, language=LANGUAGE.NATIVE):
        name = self.get_name(genders=[gender])
        return name.get_for(gender, language)

    def test_names_consistency(self, test):
        # "full_forms_for_languages": ["ru"],
        for name in self.names_list:
            for gender in GENDER.ALL:
                if gender in name.translations:
                    # print name.translations[gender]
                    test.assertEqual(set(name.translations[gender].keys()) & self.languages, self.languages)

                    for language in self.full_forms_for_languages:
                        # print name.translations[gender][language]
                        test.assertTrue(isinstance(name.translations[gender][language], list))
                        test.assertEqual(len(name.translations[gender][language]), LANGUAGE_FORMS_LANGTH[language])
