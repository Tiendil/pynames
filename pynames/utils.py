# coding: utf-8

from __future__ import unicode_literals

import contextlib
import importlib
import pkgutil
import os


def get_all_generators():

    from .base import BaseGenerator
    from .from_list_generator import FromListGenerator
    from .from_tables_generator import FromTablesGenerator, FromCSVTablesGenerator

    submodules = []

    pynames_root = os.path.join(os.path.split(os.path.abspath(__file__))[0], 'generators')

    for _, module_name, _ in pkgutil.iter_modules([pynames_root], prefix='pynames.generators.'):
        module = importlib.import_module(module_name)
        submodules.append(module)

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


@contextlib.contextmanager
def file_adapter(file_or_path, mode='rb'):
    """Context manager that works similar to ``open(file_path)``but also accepts already openned file-like objects."""
    if is_file(file_or_path):
        file_obj = file_or_path
    else:
        file_obj = open(file_or_path, mode)
    yield file_obj
    file_obj.close()
