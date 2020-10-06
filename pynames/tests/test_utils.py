# coding: utf-8

from __future__ import unicode_literals

import os
import tempfile
import unittest

from pynames.utils import is_file, file_adapter
import pynames

DJANGO_INSTALLED = False

UploadedFile = None
File = None
ContentFile = None

try:
    from django.core.files import File
    from django.core.files.base import ContentFile
    from django.core.files.uploadedfile import UploadedFile

    DJANGO_INSTALLED = True
except ImportError:
    pass


class TestName(unittest.TestCase):

    def test_is_file(self):
        some_file = tempfile.NamedTemporaryFile()
        self.assertTrue(is_file(some_file))
        some_file.close()

    def test_is_file_on_django_files(self):
        if not DJANGO_INSTALLED:
            return

        self.assertTrue(is_file(UploadedFile('mock')))
        self.assertTrue(is_file(File('mock')))
        self.assertTrue(is_file(ContentFile('mock')))

    def test_file_adapter(self):
        if not DJANGO_INSTALLED:
            return

        root_dir = os.path.dirname(pynames.__file__)

        test_file_path = os.path.join(root_dir, 'tests', 'fixtures', 'test_from_list_generator.json')

        with open(test_file_path, 'rb') as f:
            target_content = f.read()

        with file_adapter(test_file_path) as f:
            self.assertEqual(f.read(), target_content)

        django_file_object = ContentFile(target_content)
        classic_file_object = open(test_file_path, 'rb')

        for tested_file_object in [django_file_object, classic_file_object]:
            with file_adapter(tested_file_object) as f:
                self.assertEqual(f.read(), target_content)
