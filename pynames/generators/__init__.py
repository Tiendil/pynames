# coding: utf-8
import os
import pkgutil
import importlib

__all__ = []

generators_root = os.path.os.path.split(os.path.abspath(__file__))[0]

for _, module_name, _ in pkgutil.iter_modules([generators_root]):
    module = importlib.import_module('pynames.generators.' + module_name)
    __all__.append(module_name)
    globals()[module_name] = module
