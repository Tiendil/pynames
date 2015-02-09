# coding: utf-8

import os

from pynames.from_tables_generator import FromTablesGenerator, FromCSVTablesGenerator

FIXTURES_DIR = os.path.join(os.path.dirname(__file__), 'fixtures')


class GoblinGenerator(FromTablesGenerator):
    SOURCE = os.path.join(FIXTURES_DIR, 'goblin_names_tables.json')


class GobberFullnameGenerator(FromCSVTablesGenerator):
    SOURCE = [
        os.path.join(FIXTURES_DIR, 'IK_gobber_names_settings.csv'),
        os.path.join(FIXTURES_DIR, 'IK_gobber_names_templates.csv'),
        os.path.join(FIXTURES_DIR, 'IK_gobber_names_tables.csv'),
    ]
