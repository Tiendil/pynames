# coding: utf-8

import os

from pynames.from_tables_generator import FromTablesGenerator

FIXTURES_DIR = os.path.join(os.path.dirname(__file__), 'fixtures')

class WarhammerNamesGenerator(FromTablesGenerator):
    SOURCE = os.path.join(FIXTURES_DIR, 'elven_warhammer_names_tables.json')

class DnDNamesGenerator(FromTablesGenerator):
    SOURCE = os.path.join(FIXTURES_DIR, 'elven_dnd_names_tables.json')
