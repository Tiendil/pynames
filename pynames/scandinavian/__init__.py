# coding: utf-8
import os

from ..from_list_generator import FromListGenerator

FIXTURES_DIR = os.path.join(os.path.dirname(__file__), 'fixtures')

class ScandinavianNamesGenerator(FromListGenerator):
    SOURCE = os.path.join(FIXTURES_DIR, 'scandinavian_names_list.json')

