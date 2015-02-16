# coding: utf-8

import os
import importlib

import pynames


def get_all_generators():

    from pynames.base import BaseGenerator
    from pynames.from_list_generator import FromListGenerator
    from pynames.from_tables_generator import FromTablesGenerator, FromCSVTablesGenerator

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

            if generator in (FromTablesGenerator, FromListGenerator, FromCSVTablesGenerator):
                continue

            generators.append(generator)

    return generators


def is_file(obj):
    """Retrun True is object has 'next', '__enter__' and '__exit__' methods.

    Suitable to check both builtin ``file`` and ``django.core.file.File`` instances.

    """
    return all(
        [callable(getattr(obj, method_name, None)) for method_name in ('__enter__', '__exit__')]
        +
        [any([callable(getattr(obj, method_name, None)) for method_name in ('next', '__iter__')])]
    )
