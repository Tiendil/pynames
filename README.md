# PYNAMES - библиотека для генерации имён

**Name generation library - [see English description here](https://github.com/Tiendil/pynames/wiki/EN_README)**

Основное назначение библиотеки - генерация имён персонажей в играх. Например, эльфийски, дварфских, корейских, монгольских, в общем - любых.

Библиотека легко расширяема, если Вам нужен дополнительный функционал (или дополнительные языки), свяжитесь со мной (или просто запостите issue), а лучше реализуейте и сделайте pull-запрос.

## Пример использования

```python
from pynames.generators import GENDER,  LANGUAGE
```

Все генераторы разбиты по языкам (или по рассам), так, что все генераторы эльфийских имён находятся в модуле pynames.elven

```python
from pynames.elven import DnDNamesGenerator
elven_generator = DnDNamesGenerator()
```

количество различных имён (мужских и женских) и для каждого пола в отдельности

```python
In [4]: elven_generator.get_names_number()
Out[4]: 1952949936

In [5]: elven_generator.get_names_number(GENDER.MALE)
Out[5]: 976474968

In [6]: elven_generator.get_names_number(GENDER.FEMALE)
Out[6]: 976474968
```

Быстрое получение просто случайного имени

```python
In [7]: elven_generator.get_name_simple()
Out[7]: u'Elineer'

In [8]: elven_generator.get_name_simple(GENDER.MALE)
Out[8]: u'Caslithdar'

In [9]: elven_generator.get_name_simple(GENDER.MALE, LANGUAGE.EN) # English transcription
Out[9]: u'Mararon'
```

вместо текста можно получить объект имени с подробной информацией

```python
In [10]: name = elven_generator.get_name()

In [11]: name.translations
Out[11]: {u'f': {u'en': u"mil'Jashoreti"}} # all transcriptions

In [12]: name.genders
Out[12]: frozenset([u'f']) # all genders
```

На текущий момент реализовано два алгоритма генерации имён:

* выбор из списка - в основном для реальных народов (например, русские языческие имена)
* табличная генерация - составление имён из частей

Сущестующие генераторы:

* pynames.elven.DnDNamesGenerator
* pynames.elven.WarhammerNamesGenerator
* pynames.goblin.GobberFullnameGenerator
* pynames.goblin.GoblinGenerator
* pynames.iron_kingdoms.CaspianMidlunderSuleseFullnameGenerator
* pynames.iron_kingdoms.DwarfFullnameGenerator
* pynames.iron_kingdoms.GobberFullnameGenerator == pynames.goblin.GobberFullnameGenerator
* pynames.iron_kingdoms.IossanNyssFullnameGenerator
* pynames.iron_kingdoms.KhadoranFullnameGenerator
* pynames.iron_kingdoms.OgrunFullnameGenerator
* pynames.iron_kingdoms.RynFullnameGenerator
* pynames.iron_kingdoms.ThurianMorridaneFullnameGenerator
* pynames.iron_kingdoms.TordoranFullnameGenerator
* pynames.iron_kingdoms.TrollkinFullnameGenerator
* pynames.korean.KoreanNamesGenerator
* pynames.mongolian.MongolianNamesGenerator
* pynames.orc.OrcNamesGenerator
* pynames.russian.PaganNamesGenerator
* pynames.scandinavian.ScandinavianNamesGenerator


Можно получить список всех классов генераторов следующим образом:

```python
In [1]: from pynames.utils import get_all_generators

In [2]: get_all_generators()
Out[2]:
[pynames.elven.DnDNamesGenerator,
 pynames.elven.WarhammerNamesGenerator,
 pynames.iron_kingdoms.OgrunFullnameGenerator,
 pynames.iron_kingdoms.ThurianMorridaneFullnameGenerator,
 pynames.iron_kingdoms.TordoranFullnameGenerator,
 pynames.iron_kingdoms.RynFullnameGenerator,
 pynames.iron_kingdoms.KhadoranFullnameGenerator,
 pynames.iron_kingdoms.ThurianMorridaneFullnameGenerator,
 pynames.iron_kingdoms.TrollkinFullnameGenerator,
 pynames.iron_kingdoms.IossanNyssFullnameGenerator,
 pynames.iron_kingdoms.CaspianMidlunderSuleseFullnameGenerator,
 pynames.iron_kingdoms.GobberFullnameGenerator,
 pynames.iron_kingdoms.ThurianMorridaneFullnameGenerator,
 pynames.iron_kingdoms.DwarfFullnameGenerator,
 pynames.russian.PaganNamesGenerator,
 pynames.orc.OrcNamesGenerator,
 pynames.scandinavian.ScandinavianNamesGenerator,
 pynames.korean.KoreanNamesGenerator,
 pynames.mongolian.MongolianNamesGenerator,
 pynames.goblin.GoblinGenerator,
 pynames.iron_kingdoms.GobberFullnameGenerator,
 pynames.korean.KoreanNamesGenerator]
```