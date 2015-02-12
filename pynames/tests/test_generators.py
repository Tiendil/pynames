# coding: utf-8

import unittest

from pynames.relations import GENDER
from pynames.utils import get_all_generators


# TODO: test forms:
#       - parameter, that declared, for which language forms specified
#       - how many items in forms (12 for russian)


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
