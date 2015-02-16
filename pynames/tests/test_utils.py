# coding: utf-8

import unittest
import tempfile

from pynames.utils import is_file

try:
    from django.core.files import File
    from django.core.files.base import ContentFile
    from django.core.files.uploadedfile import UploadedFile
except:
    UploadedFile = None
    File = None
    ContentFile = None


class TestName(unittest.TestCase):

    def test_is_file(self):
        some_file = tempfile.NamedTemporaryFile()
        self.assertTrue(is_file(some_file))
        some_file.close()

    def test_is_file_on_django_files(self):
        if File and UploadedFile and ContentFile:
            self.assertTrue(is_file(UploadedFile('mock')))
            self.assertTrue(is_file(File('mock')))
            self.assertTrue(is_file(ContentFile('mock')))
