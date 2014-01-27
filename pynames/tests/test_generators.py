# coding: utf-8

import os
import importlib
import unittest

import pynames

from pynames.relations import GENDER
from pynames.base import BaseGenerator
from pynames.from_list_generator import FromListGenerator
from pynames.from_tables_generator import FromTablesGenerator


# TODO: test forms:
#       - parameter, that declared, for which language forms specified
#       - how many items in forms (12 for russian)


def get_all_generators():

    submodules = []

    root_dir = os.path.dirname(pynames.__file__)

    for dirname in os.listdir(root_dir):
        module_path = os.path.join(root_dir, dirname)
        if not os.path.isdir(module_path):
            continue

        try:
            module_name = 'pynames.%s' % dirname
            module = importlib.import_module(module_name)
            submodules.append(module)
        except Exception:
            continue

    generators = []

    for module in submodules:
        for generator in module.__dict__.values():
            if not isinstance(generator, type) or not issubclass(generator, BaseGenerator):
                continue

            if generator in (FromTablesGenerator, FromListGenerator):
                continue

            generators.append(generator)

    return generators



class TestGenerators(unittest.TestCase):
    pass



def create_test_method(generator_class):

    def test_method(self):
        generator = generator_class()

        self.assertTrue(generator.get_names_number() > 0)
        self.assertTrue(generator.get_names_number(GENDER.MALE) + generator.get_names_number(GENDER.FEMALE) >= generator.get_names_number())
        self.assertTrue(generator.get_name_simple())
        self.assertTrue(generator.get_name())

        generator.test_names_consistency(self)

    test_method.__name__ = 'test_%s' % generator.__name__

    return test_method


for generator in get_all_generators():
    test_method = create_test_method(generator)
    setattr(TestGenerators, test_method.__name__, test_method)
