# coding: utf-8

from __future__ import unicode_literals

import six
import unittest

from pynames.relations import GENDER, LANGUAGE
from pynames.names import Name


class TestName(unittest.TestCase):

    def test_base(self):
        name = Name('ru', {'genders': {'m': {'ru': 'ru_name'}}})
        self.assertEqual(six.text_type(name), 'ru_name')
        self.assertEqual(name.get_for(GENDER.MALE, LANGUAGE.RU), 'ru_name')
        self.assertEqual(name.get_for(GENDER.MALE), 'ru_name')
        self.assertEqual(name.get_forms_for(GENDER.MALE), None)

    def test_genders(self):
        name = Name('ru', {'genders': {'m': {'ru': 'ru_m_name'},
                                       'f': {'ru': 'ru_f_name'}}})
        self.assertEqual(six.text_type(name), 'ru_m_name')
        self.assertEqual(name.get_for(GENDER.MALE, LANGUAGE.RU), 'ru_m_name')
        self.assertEqual(name.get_for(GENDER.FEMALE, LANGUAGE.RU), 'ru_f_name')

    def test_languages(self):
        name = Name('ru', {'genders': {'m': {'ru': 'ru_m_name',
                                             'en': 'en_m_name'},
                                       'f': {'ru': 'ru_f_name',
                                             'en': 'en_f_name'}}})
        self.assertEqual(six.text_type(name), 'ru_m_name')
        self.assertEqual(name.get_for(GENDER.MALE, LANGUAGE.RU), 'ru_m_name')
        self.assertEqual(name.get_for(GENDER.FEMALE, LANGUAGE.RU), 'ru_f_name')
        self.assertEqual(name.get_for(GENDER.MALE, LANGUAGE.EN), 'en_m_name')
        self.assertEqual(name.get_for(GENDER.FEMALE, LANGUAGE.EN), 'en_f_name')
        self.assertEqual(name.get_for(GENDER.MALE), 'ru_m_name')
        self.assertEqual(name.get_for(GENDER.FEMALE), 'ru_f_name')


    def test_forms(self):
        name = Name('ru', {'genders': {'m': {'ru': ['form_1', 'form_2']}}})
        self.assertEqual(name.get_forms_for(GENDER.MALE), ['form_1', 'form_2'])
