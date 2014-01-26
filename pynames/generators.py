# coding: utf-8

from pynames.relations import GENDER, LANGUAGE


class PynamesException(Exception):
    pass


class BaseGenerator(object):
    pass


class Name(object):

    __slots__ = ('genders', 'native_language', 'translations')

    def __init__(self, native_language, data):
        self.native_language = native_language
        self.genders = frozenset(data['genders'].keys())
        self.translations = data['genders']

    def get_for(self, gender, language=LANGUAGE.NATIVE):
        if language == LANGUAGE.NATIVE:
            language = self.native_language
        return self.translations[gender][language]

    def exists_for(self, genders):
        return genders & self.genders

    def __unicode__(self):
        for gender in GENDER.ALL:
            if gender in self.genders:
                return self.translations[gender][self.native_language]
        error_msg = u'Name: can not get default value for name with data: %r' % self.genders
        raise PynamesException(error_msg)

    def __str__(self): return self.__unicode__()
