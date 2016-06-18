# coding: utf-8

import os
import json

import six


FIXTURES = ['mongolian/fixtures/mongolian_names_list.json',
            'russian/fixtures/pagan_names_list.json',
            'korean/fixtures/korean_names_list.json',
            'scandinavian/fixtures/scandinavian_names_list.json']


FROM = '/home/tie/repos/other/pynames/pynames/'
TO = '/home/tie/repos/mine/pynames/pynames'

def names_equal(name, original_name):

    for gender in name['genders'].iterkeys():
        if gender not in original_name['genders']:
            continue

        languages = name['genders'][gender]
        original_languages = original_name['genders'][gender]


        for language in languages.iterkeys():
            if language not in original_languages:
                continue

            text = languages[language] if isinstance(languages[language], six.string_types) else languages[language][0]
            original_text = original_languages[language] if isinstance(original_languages[language], six.string_types) else original_languages[language][0]

            if text == original_text:
                return True

    return False


def merge_names(name, original_name):
    for gender, languages in six.iteritems(name['genders']):
        for language, data in six.iteritems(languages):
            original_name['genders'][gender][language] = data


def merge(data_from, data_to):

    for original_name in data_to:
        for name in data_from:
            if names_equal(name, original_name):
                merge_names(name, original_name)


def pretty_dump(data):
    content = []
    content.append(u'{')

    for key, value in six.iteritems(data):
        if key != 'names':
            content.append(u'    "%s": %s,' % (key, json.dumps(value, ensure_ascii=False)))

    content.append(u'    "names": [')

    names_number = len(data['names'])

    for i, name in enumerate(data['names']):
        content.append('    ' + json.dumps(name, ensure_ascii=False) + (u',' if i + 1 < names_number else u'') )

    content.append(u'    ]')
    content.append(u'}')

    return u'\n'.join(content)


for fixture in FIXTURES:

    print 'process: ', fixture

    with open(os.path.join(FROM, fixture)) as f:
        data_from = json.loads(f.read().decode('utf-8'))

    with open(os.path.join(TO, fixture)) as f:
        data_to = json.loads(f.read().decode('utf-8'))

    merge(data_from['names'], data_to['names'])

    with open(os.path.join(TO, fixture), 'w') as f:
        f.write(pretty_dump(data_to).encode('utf-8'))
        # f.write(json.dumps(data_to, indent=2).encode('utf-8'))
