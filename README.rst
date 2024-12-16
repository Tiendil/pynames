===================================
PYNAMES — Name Generation Library
===================================

Pynames is a library designed for generating various types of names. It currently supports name generators for characters of different races and cultures, including:

* **Scandinavian**: traditional names
* **Russian**: pagan names
* **Mongolian**: traditional names
* **Korean**: traditional names
* **Elven**:
   * DnD
   * Warhamme
* **Goblins**: custom names
* **Orcs**: custom names
* **Iron Kingdoms**:
   * Caspian, Midlunder, Sulese
   * Dwarf
   * Gobber
   * Iossan, Nyss
   * Khadoran
   * Ogrun
   * Ryn
   * Thurian, Morridane
   * Tordoran
   * Trollkin

The library supports two languages: **English** and **Russian**. For Russian, names are generated with forms for every grammatical case and tense.

Two name generation algorithms are implemented:

* ``pynames.from_list_generator`` — names are created from a predefined list of words.
* ``pynames.from_table_generator`` — names are created using templates, with each part of the template drawn from a separate table.

The library is highly extensible. If you need additional functionality (including support for new languages), feel free to contact the author, post an issue, or submit a pull request.

*************
Installation
*************

Install the library via pip:

::

   pip install pynames

********
Usage
********

.. code:: python

   from pynames import GENDER, LANGUAGE

All generators are organized by "races," so, for instance, all elven name generators are in the module ``pynames.generators.elven``.

.. code:: python

   from pynames.generators.elven import DnDNamesGenerator
   elven_generator = DnDNamesGenerator()

You can retrieve the total number of unique names or the count for a specific gender:

.. code:: python

   In [4]: elven_generator.get_names_number()
   Out[4]: 1952949936

   In [5]: elven_generator.get_names_number(GENDER.MALE)
   Out[5]: 976474968

   In [6]: elven_generator.get_names_number(GENDER.FEMALE)
   Out[6]: 976474968

Generate random names quickly:

.. code:: python

   In [7]: elven_generator.get_name_simple()
   Out[7]: u'Elineer'

   In [8]: elven_generator.get_name_simple(GENDER.MALE)
   Out[8]: u'Caslithdar'

   In [9]: elven_generator.get_name_simple(GENDER.MALE, LANGUAGE.EN)  # English
   Out[9]: u'Mararon'

   In [10]: print(elven_generator.get_name_simple(GENDER.MALE, LANGUAGE.RU))  # Russian
   Ттомусиэл

Instead of just text, you can retrieve a `Name` object with additional functionality:

.. code:: python

   In [11]: name = elven_generator.get_name()

   In [12]: name.translations  # all translations
   Out[12]:
   {u'm': {u'en': u"ae'Angaithnyn",
           u'ru': [u"\u0430\u044d'\u0410\u043d\u0433\u0430\u0438\u0442\u0442\u043d\u0438\u0438\u043d",
                   u"\u0430\u044d'\u0410\u043d\u0433\u0430\u0438\u0442\u0442\u043d\u0438\u0438\u043d\u0430",
                   u"\u0430\u044d'\u0410\u043d\u0433\u0430\u0438\u0442\u0442\u043d\u0438\u0438\u043d\u0443",
                   u"\u0430\u044d'\u0410\u043d\u0433\u0430\u0438\u0442\u0442\u043d\u0438\u0438\u043d\u0430",
                   u"\u0430\u044d'\u0410\u043d\u0433\u0430\u0438\u0442\u0442\u043d\u0438\u0438\u043d\u043e\u043c",
                   u"\u0430\u044d'\u0410\u043d\u0433\u0430\u0438\u0442\u0442\u043d\u0438\u0438\u043d\u0435",
                   u"\u0430\u044d'\u0410\u043d\u0433\u0430\u0438\u0442\u0442\u043d\u0438\u0438\u043d\u044b",
                   u"\u0430\u044d'\u0410\u043d\u0433\u0430\u0438\u0442\u0442\u043d\u0438\u0438\u043d\u043e\u0432",
                   u"\u0430\u044d'\u0410\u043d\u0433\u0430\u0438\u0442\u0442\u043d\u0438\u0438\u043d\u0430\u043c",
                   u"\u0430\u044d'\u0410\u043d\u0433\u0430\u0438\u0442\u0442\u043d\u0438\u0438\u043d\u043e\u0432",
                   u"\u0430\u044d'\u0410\u043d\u0433\u0430\u0438\u0442\u0442\u043d\u0438\u0438\u043d\u0430\u043c\u0438",
                   u"\u0430\u044d'\u0410\u043d\u0433\u0430\u0438\u0442\u0442\u043d\u0438\u0438\u043d\u0430\u0445"]}}

   In [13]: print(u'\n'.join(name.get_forms_for(GENDER.MALE, language=LANGUAGE.RU)))
   аэ'Ангаиттниин
   аэ'Ангаиттниина
   аэ'Ангаиттниину
   аэ'Ангаиттниина
   аэ'Ангаиттниином
   аэ'Ангаиттниине
   аэ'Ангаиттниины
   аэ'Ангаиттниинов
   аэ'Ангаиттниинам
   аэ'Ангаиттниинов
   аэ'Ангаиттниинами
   аэ'Ангаиттниинах

   In [14]: name.genders
   Out[14]: frozenset({u'm'})  # all genders
