# coding: utf-8

class PynamesException(Exception):
    pass


class GENDER:
    MALE = 'm'
    FEMALE = 'f'
    MF = ['m', 'f']

    ALL = ['m', 'f']


class LANGUAGE:
    RU = 'ru'
    EN = 'en'
    NATIVE = 'native'

    ALL = ['ru', 'en', 'native']


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
        error_msg = 'Name: can not get default value for name with data: %r' % self.genders
        raise PynamesException(error_msg)

    def __str__(self): return self.__unicode__()
