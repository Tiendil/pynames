# coding: utf-8
import setuptools

setuptools.setup(
    name='Pynames',
    version='0.2.3',
    description='name generation library',
    long_description=open('README.rst').read(),
    url='https://github.com/Tiendil/pynames',
    author='Aleksey Yeletsky <Tiendil>',
    author_email='a.eletsky@gmail.com',
    license='BSD',
    classifiers=[
        'Development Status :: 5 - Production/Stable',

        'Intended Audience :: Developers',

        'Topic :: Games/Entertainment',
        'Topic :: Software Development :: Libraries :: Python Modules',

        'License :: OSI Approved :: BSD License',

        'Natural Language :: English',
        'Natural Language :: Russian'],
    keywords=['gamedev', 'game', 'game development', 'names', 'names generation'],
    packages=setuptools.find_packages(),
    install_requires=['six', 'unicodecsv'],
    include_package_data=True,
    test_suite = 'tests',
    )
