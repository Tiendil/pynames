# coding: utf-8

import os

from pynames.from_tables_generator import FromTablesGenerator
from pynames.generators.iron_kingdoms import GobberFullnameGenerator

FIXTURES_DIR = os.path.join(os.path.dirname(__file__), 'fixtures')


class GoblinGenerator(FromTablesGenerator):
    SOURCE = os.path.join(FIXTURES_DIR, 'goblin_names_tables.json')
