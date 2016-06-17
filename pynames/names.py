# coding: utf-8

from __future__ import unicode_literals

import six

from pynames.relations import GENDER, LANGUAGE
from pynames import exceptions


class Name(object):

    __slots__ = ('genders', 'native_language', 'translations')

    def __init__(self, native_language, data):
        self.native_language = native_language
        self.genders = frozenset(data['genders'].keys())
        self.translations = data['genders']

    def get_for(self, gender, language=LANGUAGE.NATIVE):

        if language == LANGUAGE.NATIVE:
            language = self.native_language

        forms = self.translations[gender][language]

        if not isinstance(forms, six.string_types):
            return forms[0]

        return forms

    def get_forms_for(self, gender, language=LANGUAGE.NATIVE):
        if language == LANGUAGE.NATIVE:
            language = self.native_language

        forms = self.translations[gender][language]

        if not isinstance(forms, six.string_types):
            return list(forms)

        return None

    def exists_for(self, genders):
        return genders & self.genders

    def __unicode__(self):
        for gender in GENDER.ALL:
            if gender in self.genders:
                return self.translations[gender][self.native_language]
        raise exceptions.PynamesException(raw_data=self.genders)

    def __str__(self): return self.__unicode__()
