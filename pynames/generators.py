# coding: utf-8

import json
import random


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

    def __init__(self, data):
        self.native_language = data['native_language']
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


class FromListGenerator(BaseGenerator):

    SOURCE = None

    def __init__(self):
        self.names_list = []
        self.choices = {}

        if self.SOURCE is None:
            error_msg = 'FromListGenerator: you must make subclass of FromListGenerator and defined attribute SOURCE in it.'
            raise NotImplementedError(error_msg)

        with open(self.SOURCE) as f:
            names_data = json.load(f)
            for name_data in names_data['names']:
                self.names_list.append(Name(name_data))

        if not self.names_list:
            raise PynamesException('FromListGenerator: no names loaded from "%s"' % self.SOURCE)

    def _get_cache_key(self, genders):
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
