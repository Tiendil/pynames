# coding: utf-8

from __future__ import unicode_literals


class PynamesError(Exception):
    MSG = None

    def __init__(self, **kwargs):
        super(PynamesError, self).__init__(self.MSG % kwargs)


class NoDefaultNameValue(PynamesError):
    MSG = 'Name: can not get default value for name with data: %(raw_data)r'


class FromListGeneratorError(PynamesError):
    pass


class NoNamesLoadedFromListError(FromListGeneratorError):
    MSG = 'no names loaded from "%(source)s"'


class FromTablesGeneratorError(PynamesError):
    pass


class WrongTemplateStructureError(FromTablesGeneratorError):
    MSG = 'wrong template structure - cannot choose template for genders %(genders)r with template source: "%(source)s"'


class NotEqualFormsLengths(FromTablesGeneratorError):
    MSG = 'not equal forms lengths: [%(left)r] and [%(right)r]'


class WrongCSVData(FromTablesGeneratorError):
    def __init__(self, msg, **kwargs):
        self.MSG = msg
        super(WrongCSVData, self).__init__(**kwargs)
