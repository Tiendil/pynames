# coding: utf-8

import os

from pynames.from_tables_generator import FromCSVTablesGenerator

FIXTURES_DIR = os.path.join(os.path.dirname(__file__), 'fixtures')


class GobberFullnameGenerator(FromCSVTablesGenerator):
    SOURCE = [
        os.path.join(FIXTURES_DIR, 'IK_en_settings.csv'),
        os.path.join(FIXTURES_DIR, 'IK_gobber_names_templates.csv'),
        os.path.join(FIXTURES_DIR, 'IK_gobber_names_tables.csv'),
    ]


class ThurianMorridaneFullnameGenerator(FromCSVTablesGenerator):
    SOURCE = [
        os.path.join(FIXTURES_DIR, 'IK_en_settings.csv'),
        os.path.join(FIXTURES_DIR, 'IK_simple_fullname.csv'),
        os.path.join(FIXTURES_DIR, 'IK_thurian_morridane_names_tables.csv'),
    ]

ThurianFullnameGenerator = ThurianMorridaneFullnameGenerator
MorridaneFullnameGenerator = ThurianMorridaneFullnameGenerator


class TordoranFullnameGenerator(FromCSVTablesGenerator):
    SOURCE = [
        os.path.join(FIXTURES_DIR, 'IK_en_settings.csv'),
        os.path.join(FIXTURES_DIR, 'IK_simple_fullname.csv'),
        os.path.join(FIXTURES_DIR, 'IK_tordoran_names_tables.csv'),
    ]


class RynFullnameGenerator(FromCSVTablesGenerator):
    SOURCE = [
        os.path.join(FIXTURES_DIR, 'IK_en_settings.csv'),
        os.path.join(FIXTURES_DIR, 'IK_simple_fullname.csv'),
        os.path.join(FIXTURES_DIR, 'IK_ryn_names_tables.csv'),
    ]


class DwarfFullnameGenerator(FromCSVTablesGenerator):
    SOURCE = [
        os.path.join(FIXTURES_DIR, 'IK_en_settings.csv'),
        os.path.join(FIXTURES_DIR, 'IK_simple_fullname.csv'),
        os.path.join(FIXTURES_DIR, 'IK_dwarf_names_tables.csv'),
    ]


class IossanNyssFullnameGenerator(FromCSVTablesGenerator):
    SOURCE = [
        os.path.join(FIXTURES_DIR, 'IK_en_settings.csv'),
        os.path.join(FIXTURES_DIR, 'IK_simple_fullname.csv'),
        os.path.join(FIXTURES_DIR, 'IK_iossan_nyss_names_tables.csv'),
    ]


class CaspianMidlunderSuleseFullnameGenerator(FromCSVTablesGenerator):
    SOURCE = [
        os.path.join(FIXTURES_DIR, 'IK_en_settings.csv'),
        os.path.join(FIXTURES_DIR, 'IK_simple_fullname.csv'),
        os.path.join(FIXTURES_DIR, 'IK_caspian_midlunder_sulese_names_tables.csv'),
    ]


class KhadoranFullnameGenerator(FromCSVTablesGenerator):
    SOURCE = [
        os.path.join(FIXTURES_DIR, 'IK_en_settings.csv'),
        os.path.join(FIXTURES_DIR, 'IK_khadoran_templates.csv'),
        os.path.join(FIXTURES_DIR, 'IK_khadoran_names_tables.csv'),
    ]


class OgrunFullnameGenerator(FromCSVTablesGenerator):
    SOURCE = [
        os.path.join(FIXTURES_DIR, 'IK_en_settings.csv'),
        os.path.join(FIXTURES_DIR, 'IK_simple_fullname.csv'),
        os.path.join(FIXTURES_DIR, 'IK_ogrun_names_tables.csv'),
    ]


class TrollkinFullnameGenerator(FromCSVTablesGenerator):
    SOURCE = [
        os.path.join(FIXTURES_DIR, 'IK_en_settings.csv'),
        os.path.join(FIXTURES_DIR, 'IK_simple_fullname.csv'),
        os.path.join(FIXTURES_DIR, 'IK_trollkin_names_tables.csv'),
    ]
