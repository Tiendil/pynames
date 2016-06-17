==================================
PYNAMES — names generation library
==================================

Pynames intended for generation of all sorts of names. Currently it implements generators for character names of different races and cultures:

* Scandinavian: traditional names;
* Russian: pagan names;
* Mongolian: traditional names;
* Korean: traditional names;
* Elven: DnD names;
* Elven: Warhammer names;
* Goblins: custom names;
* Orcs: custom names;
* Iron Kingdoms: caspian midlunder sulese;
* Iron Kingdoms: dwarf;
* Iron Kingdoms: gobber;
* Iron Kingdoms: iossan nyss;
* Iron Kingdoms: khadoran;
* Iron Kingdoms: ogrun;
* Iron Kingdoms: ryn;
* Iron Kingdoms: thurian morridane;
* Iron Kingdoms: tordoran;
* Iron Kingdoms: trollkin.

There are two supported languages : English & Russian. Russian language names are generated with forms for every case of a noun and time.

Currently implemented two generation algorithms:

* ``pynames.from_list_generator`` — names are created from list of predefined words;
* ``pynames.from_table_generator`` — names are created using templates, every part of template is gotten from separate table;

The library is easily extensible. If you need extra functionality (including new languages), please, contact me, post an issue, or just make a pull request.

*************
Installation
*************

::

   pip install pynames

*************
Usage
*************

.. code:: python

   from pynames import GENDER, LANGUAGE

All generators are divided by "races", so that all generators of elven names are placed in the module ``pynames.generators.elven``, etc.

.. code:: python

   from pynames.generators.elven import DnDNamesGenerator
   elven_generator = DnDNamesGenerator()

Number of different names (male and female) and for each gender separately.

.. code:: python

   In [4]: elven_generator.get_names_number()
   Out[4]: 1952949936

   In [5]: elven_generator.get_names_number(GENDER.MALE)
   Out[5]: 976474968

   In [6]: elven_generator.get_names_number(GENDER.FEMALE)
   Out[6]: 976474968

Fast random name generation.

.. code:: python

   In [7]: elven_generator.get_name_simple()
   Out[7]: u'Elineer'

   In [8]: elven_generator.get_name_simple(GENDER.MALE)
   Out[8]: u'Caslithdar'

   In [9]: elven_generator.get_name_simple(GENDER.MALE, LANGUAGE.EN) # English
   Out[9]: u'Mararon'

   In [10]: print elven_generator.get_name_simple(GENDER.MALE, LANGUAGE.RU)  # Russian
   Ттомусиэл

Instead of text, you can get the Name object with additional functionality.

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

   In [13]: print u'\n'.join(name.get_forms_for(GENDER.MALE, language=LANGUAGE.RU))
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
   Out[14]: frozenset({u'm'}) # all genders
