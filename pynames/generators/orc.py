# coding: utf-8
import os

from pynames.from_list_generator import FromListGenerator

FIXTURES_DIR = os.path.join(os.path.dirname(__file__), 'fixtures')

class OrcNamesGenerator(FromListGenerator):
    SOURCE = os.path.join(FIXTURES_DIR, 'orc_names_list.json')
