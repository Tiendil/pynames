# coding: utf-8

class PynamesError(Exception):
    MSG = None

    def __init__(self, **kwargs):
        super(PynamesError, self).__init__(self.MSG % kwargs)



class NoDefaultNameValue(PynamesError):
    MSG = u'Name: can not get default value for name with data: %(raw_data)r'


class FromListGeneratorError(PynamesError):
    pass

class NoNamesLoadedFromListError(FromListGeneratorError):
    MSG = u'no names loaded from "%(source)s"'


class FromTablesGeneratorError(PynamesError):
    pass

class WrongTemplateStructureError(FromTablesGeneratorError):
    MSG = u'wrong template structure - cannot choose template for genders %(genders)r with template source: "%(source)s"'


class NotEqualFormsLengths(FromTablesGeneratorError):
    MSG = u'not equal forms lengths: [%(left)r] and [%(right)r]'
