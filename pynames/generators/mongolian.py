# coding: utf-8
import os

from pynames.from_list_generator import FromListGenerator

FIXTURES_DIR = os.path.join(os.path.dirname(__file__), 'fixtures')

class MongolianNamesGenerator(FromListGenerator):
    SOURCE = os.path.join(FIXTURES_DIR, 'mongolian_names_list.json')
