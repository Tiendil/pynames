# coding: utf-8
import setuptools

setuptools.setup(
    name = 'Pynames',
    version = '0.1.0',
    author = 'Aleksey Yeletsky',
    author_email = 'a.eletsky@gmail.com',
    packages = setuptools.find_packages(),
    url = 'https://github.com/Tiendil/pynames',
    license = 'LICENSE',
    description = "characters' name generation library",
    long_description = open('README.md').read(),
    include_package_data = True, # setuptools-git MUST be installed
    test_suite = 'tests',
    package_data = { '': ['*.json'] }
)
