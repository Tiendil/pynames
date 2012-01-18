# coding: utf-8
import json
import random

from .generators import GENDER, LANGUAGE, Name, BaseGenerator, PynamesException

class FromListGenerator(BaseGenerator):

    SOURCE = None

    def __init__(self):
        super(FromListGenerator, self).__init__()
        self.names_list = []
        self.choices = {}

        if self.SOURCE is None:
            error_msg = 'FromListGenerator: you must make subclass of FromListGenerator and define attribute SOURCE in it.'
            raise NotImplementedError(error_msg)

        with open(self.SOURCE) as f:
            names_data = json.load(f)
            for name_data in names_data['names']:
                self.names_list.append(Name(names_data['native_language'], name_data))

        if not self.names_list:
            raise PynamesException('FromListGenerator: no names loaded from "%s"' % self.SOURCE)

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

