# coding: utf-8

import os
import unittest

from .generators import Name, GENDER, LANGUAGE, FromListGenerator

FIXTURES_DIR = os.path.join(os.path.dirname(__file__), 'fixtures')

class TestName(unittest.TestCase):

    def test_base(self):
        name = Name({'lang': 'ru',
                     'genders': {'m': {'ru': 'ru_name'}}})
        self.assertEqual(unicode(name), 'ru_name')
        self.assertEqual(name.get_for(GENDER.MALE, LANGUAGE.RU), 'ru_name')
        self.assertEqual(name.get_for(GENDER.MALE), 'ru_name')

    def test_genders(self):
        name = Name({'lang': 'ru',
                     'genders': {'m': {'ru': 'ru_m_name'},
                                 'f': {'ru': 'ru_f_name'}}})
        self.assertEqual(unicode(name), 'ru_m_name')
        self.assertEqual(name.get_for(GENDER.MALE, LANGUAGE.RU), 'ru_m_name')
        self.assertEqual(name.get_for(GENDER.FEMALE, LANGUAGE.RU), 'ru_f_name')

    def test_languages(self):
        name = Name({'lang': 'ru',
                     'genders': {'m': {'ru': 'ru_m_name',
                                       'en': 'en_m_name'},
                                 'f': {'ru': 'ru_f_name',
                                       'en': 'en_f_name'}}})
        self.assertEqual(unicode(name), 'ru_m_name')
        self.assertEqual(name.get_for(GENDER.MALE, LANGUAGE.RU), 'ru_m_name')
        self.assertEqual(name.get_for(GENDER.FEMALE, LANGUAGE.RU), 'ru_f_name')
        self.assertEqual(name.get_for(GENDER.MALE, LANGUAGE.EN), 'en_m_name')
        self.assertEqual(name.get_for(GENDER.FEMALE, LANGUAGE.EN), 'en_f_name')
        self.assertEqual(name.get_for(GENDER.MALE), 'ru_m_name')
        self.assertEqual(name.get_for(GENDER.FEMALE), 'ru_f_name')


class TestFromListGenerator(unittest.TestCase):

    class TestGenerator(FromListGenerator):
        SOURCE = os.path.join(FIXTURES_DIR, 'test_from_list_generator.json')

    NAMES_RU_MALE = ['ru_m_name_1', 'ru_m_name_4', 'ru_m_name_5', 'ru_m_name_6']
    NAMES_EN_MALE = ['en_m_name_1', 'en_m_name_4', 'en_m_name_5', 'en_m_name_6']
    NAMES_RU_FEMALE = ['ru_f_name_2', 'ru_f_name_3', 'ru_f_name_4', 'ru_f_name_5', 'ru_f_name_6']
    NAMES_EN_FEMALE = ['en_f_name_2', 'en_f_name_3', 'en_f_name_4', 'en_f_name_5', 'en_f_name_6']

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

    def test_get_name(self):
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
