# coding: utf-8

from __future__ import unicode_literals

import os
import unittest

from six.moves import xrange

from pynames.relations import GENDER, LANGUAGE
from pynames.from_list_generator import FromListGenerator

FIXTURES_DIR = os.path.join(os.path.dirname(__file__), 'fixtures')


class TestFromListGenerator(unittest.TestCase):

    class TestGenerator(FromListGenerator):
        SOURCE = os.path.join(FIXTURES_DIR, 'test_from_list_generator.json')

    class TestGeneratorWithForms(FromListGenerator):
        SOURCE = os.path.join(FIXTURES_DIR, 'test_from_list_generator__with_forms.json')

    NAMES_RU_MALE = ['ru_m_name_1', 'ru_m_name_4', 'ru_m_name_5', 'ru_m_name_6']
    NAMES_EN_MALE = ['en_m_name_1', 'en_m_name_4', 'en_m_name_5', 'en_m_name_6']
    NAMES_RU_FEMALE = ['ru_f_name_2', 'ru_f_name_3', 'ru_f_name_4', 'ru_f_name_5', 'ru_f_name_6']
    NAMES_EN_FEMALE = ['en_f_name_2', 'en_f_name_3', 'en_f_name_4', 'en_f_name_5', 'en_f_name_6']

    NAMES_RU_MALE_FORMS = ['ru_m_name_1__form', 'ru_m_name_4__form', 'ru_m_name_5__form', 'ru_m_name_6__form']
    NAMES_RU_FEMALE_FORMS = ['ru_f_name_2__form', 'ru_f_name_3__form', 'ru_f_name_4__form', 'ru_f_name_5__form', 'ru_f_name_6__form']

    def test_not_derived(self):
        self.assertRaises(NotImplementedError, FromListGenerator)

    def test_wrong_path(self):
        class WrongGenerator(FromListGenerator):
            SOURCE = ''
        self.assertRaises(IOError, WrongGenerator)

    def test_base(self):
        generator = self.TestGenerator()
        self.assertEqual(generator.get_names_number(), 6)
        self.assertTrue(generator.get_name_simple() in self.NAMES_RU_MALE)

    def test_male_female_selection(self):
        generator = self.TestGenerator()
        self.assertEqual(generator.get_names_number(genders=[GENDER.MALE]), 4)
        self.assertEqual(generator.get_names_number(genders=[GENDER.FEMALE]), 5)

    def test_get_name__simple(self):
        generator = self.TestGenerator()

        for i in xrange(100):
            name = generator.get_name_simple(gender=GENDER.MALE, language=LANGUAGE.RU)
            self.assertTrue(name in self.NAMES_RU_MALE)

        for i in xrange(100):
            name = generator.get_name_simple(gender=GENDER.FEMALE, language=LANGUAGE.RU)
            self.assertTrue(name in self.NAMES_RU_FEMALE)

        for i in xrange(100):
            name = generator.get_name_simple(gender=GENDER.MALE, language=LANGUAGE.EN)
            self.assertTrue(name in self.NAMES_EN_MALE)

        for i in xrange(100):
            name = generator.get_name_simple(gender=GENDER.FEMALE, language=LANGUAGE.EN)
            self.assertTrue(name in self.NAMES_EN_FEMALE)


    def test_get_name__with_forms(self):
        generator = self.TestGeneratorWithForms()

        for i in xrange(100):
            name = generator.get_name(genders=[GENDER.MALE])
            self.assertTrue(name.get_for(GENDER.MALE, LANGUAGE.RU) in self.NAMES_RU_MALE)
            self.assertNotEqual(name.get_forms_for(GENDER.MALE, LANGUAGE.RU), None)
            self.assertTrue(name.get_forms_for(GENDER.MALE, LANGUAGE.RU)[1] in self.NAMES_RU_MALE_FORMS)

        for i in xrange(100):
            name = generator.get_name(genders=[GENDER.FEMALE])
            self.assertTrue(name.get_for(GENDER.FEMALE, LANGUAGE.RU) in self.NAMES_RU_FEMALE)
            self.assertNotEqual(name.get_forms_for(GENDER.FEMALE, LANGUAGE.RU), None)
            self.assertTrue(name.get_forms_for(GENDER.FEMALE, LANGUAGE.RU)[1] in self.NAMES_RU_FEMALE_FORMS)

        for i in xrange(100):
            name = generator.get_name(genders=[GENDER.MALE])
            self.assertTrue(name.get_for(GENDER.MALE, LANGUAGE.EN) in self.NAMES_EN_MALE)
            self.assertEqual(name.get_forms_for(GENDER.MALE, LANGUAGE.EN), None)

        for i in xrange(100):
            name = generator.get_name(genders=[GENDER.FEMALE])
            self.assertTrue(name.get_for(GENDER.FEMALE, LANGUAGE.EN) in self.NAMES_EN_FEMALE)
            self.assertEqual(name.get_forms_for(GENDER.FEMALE, LANGUAGE.EN), None)
