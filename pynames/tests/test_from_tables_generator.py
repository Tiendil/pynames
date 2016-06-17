# coding: utf-8

from __future__ import unicode_literals

import os
import unittest

import six
from six.moves import xrange

from pynames.relations import GENDER, LANGUAGE
from pynames.from_tables_generator import FromTablesGenerator, FromCSVTablesGenerator

FIXTURES_DIR = os.path.join(os.path.dirname(__file__), 'fixtures')


class TestFromTablesGenerator(unittest.TestCase):

    class TestGenerator(FromTablesGenerator):
        SOURCE = os.path.join(FIXTURES_DIR, 'test_from_tables_generator.json')

    NAMES_RU_MALE = ["T1RU1_m_ru_1", "T1RU2_m_ru_1", "T1RU3_m_ru_1", "T1RU1_m_ru_2", "T1RU2_m_ru_2", "T1RU3_m_ru_2", "T1RU1_m_ru_1'_f_ru_1", "T1RU2_m_ru_1'_f_ru_1", "T1RU3_m_ru_1'_f_ru_1", "T1RU1_m_ru_2'_f_ru_1", "T1RU2_m_ru_2'_f_ru_1", "T1RU3_m_ru_2'_f_ru_1"]
    NAMES_EN_MALE = ["T1EN1_m_en_1", "T1EN2_m_en_1", "T1EN3_m_en_1", "T1EN1_m_en_2", "T1EN2_m_en_2", "T1EN3_m_en_2", "T1EN1_m_en_1'_f_en_1", "T1EN2_m_en_1'_f_en_1", "T1EN3_m_en_1'_f_en_1", "T1EN1_m_en_2'_f_en_1", "T1EN2_m_en_2'_f_en_1", "T1EN3_m_en_2'_f_en_1"]
    NAMES_RU_FEMALE = ["T1RU1_f_ru_1", "T1RU2_f_ru_1", "T1RU3_f_ru_1", "T1RU1_m_ru_1'_f_ru_1", "T1RU2_m_ru_1'_f_ru_1", "T1RU3_m_ru_1'_f_ru_1", "T1RU1_m_ru_2'_f_ru_1", "T1RU2_m_ru_2'_f_ru_1", "T1RU3_m_ru_2'_f_ru_1"]
    NAMES_EN_FEMALE = ["T1EN1_f_en_1", "T1EN2_f_en_1", "T1EN3_f_en_1", "T1EN1_m_en_1'_f_en_1", "T1EN2_m_en_1'_f_en_1", "T1EN3_m_en_1'_f_en_1", "T1EN1_m_en_2'_f_en_1", "T1EN2_m_en_2'_f_en_1", "T1EN3_m_en_2'_f_en_1"]

    NAMES_RU_FEMALE_FORMS = ["T1RU1_f_ru_1_form", "T1RU2_f_ru_1_form", "T1RU3_f_ru_1_form", "T1RU1_m_ru_1'_f_ru_1_form", "T1RU2_m_ru_1'_f_ru_1_form", "T1RU3_m_ru_1'_f_ru_1_form", "T1RU1_m_ru_2'_f_ru_1_form", "T1RU2_m_ru_2'_f_ru_1_form", "T1RU3_m_ru_2'_f_ru_1_form"]


    def test_not_derived(self):
        self.assertRaises(NotImplementedError, FromTablesGenerator)

    def test_wrong_path(self):
        class WrongGenerator(FromTablesGenerator):
            SOURCE = ''
        self.assertRaises(IOError, WrongGenerator)

    def test_base(self):
        generator = self.TestGenerator()
        self.assertEqual(generator.get_names_number(), 15)
        self.assertTrue(generator.get_name_simple() in self.NAMES_EN_MALE)

    def test_male_female_selection(self):
        generator = self.TestGenerator()
        self.assertEqual(generator.get_names_number(genders=[GENDER.MALE]), 12)
        self.assertEqual(generator.get_names_number(genders=[GENDER.FEMALE]), 9)
        self.assertEqual(generator.get_names_number(), 15)

    def test_get_name_simple(self):
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
        generator = self.TestGenerator()

        has_none = set()

        for i in xrange(100):
            name = generator.get_name(genders=[GENDER.MALE])
            self.assertTrue(name.get_for(GENDER.MALE, LANGUAGE.RU) in self.NAMES_RU_MALE)
            has_none.add(name.get_forms_for(GENDER.MALE, LANGUAGE.RU) is None)

        self.assertEqual(has_none, set([True, False]))

        for i in xrange(100):
            name = generator.get_name(genders=[GENDER.FEMALE])
            self.assertTrue(name.get_for(GENDER.FEMALE, LANGUAGE.RU) in self.NAMES_RU_FEMALE)
            self.assertNotEqual(name.get_forms_for(GENDER.FEMALE, LANGUAGE.RU), None)
            self.assertTrue(name.get_forms_for(GENDER.FEMALE, LANGUAGE.RU)[1] in self.NAMES_RU_FEMALE_FORMS)

        has_none = set()

        for i in xrange(100):
            name = generator.get_name(genders=[GENDER.MALE])
            self.assertTrue(name.get_for(GENDER.MALE, LANGUAGE.EN) in self.NAMES_EN_MALE)
            has_none.add(name.get_forms_for(GENDER.MALE, LANGUAGE.RU) is None)

        self.assertEqual(has_none, set([True, False]))

        for i in xrange(100):
            name = generator.get_name(genders=[GENDER.FEMALE])
            self.assertTrue(name.get_for(GENDER.FEMALE, LANGUAGE.EN) in self.NAMES_EN_FEMALE)
            self.assertEqual(name.get_forms_for(GENDER.FEMALE, LANGUAGE.EN), None)


class TestFromCSVTablesGenerator(unittest.TestCase):

    class TestJSONGenerator(FromTablesGenerator):
        SOURCE = os.path.join(FIXTURES_DIR, 'test_from_tables_generator.json')

    class TestCSVGenerator(FromCSVTablesGenerator):
        SOURCE = [
            os.path.join(FIXTURES_DIR, 'test_from_csv_tables_generator_settings.csv'),
            os.path.join(FIXTURES_DIR, 'test_from_csv_tables_generator_templates.csv'),
            os.path.join(FIXTURES_DIR, 'test_from_csv_tables_generator_tables.csv')
        ]

    def test_init_state_equal(self):
        """test that after init CSV and JSON generators have equal 'native_language', 'languages', 'templates', 'tables' attrubytes.

        This is the only test needed because if state after init is the same then
        behaviour is the same.

        """
        json_generator = self.TestJSONGenerator()
        csv_generator = self.TestCSVGenerator()

        for attr_name in ['native_language', 'languages', 'templates', 'tables']:
            json_attr = getattr(json_generator, attr_name)
            csv_attr = getattr(csv_generator, attr_name)
            if isinstance(json_attr, list):
                six.assertCountEqual(self, csv_attr, json_attr)
            else:
                self.assertEqual(csv_attr, json_attr)
