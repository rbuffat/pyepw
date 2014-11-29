import os
import tempfile
import unittest
from pyepw.epw import Comments2, EPW


class TestComments2(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_comments_2(self):

        obj = Comments2()
        var_comments_2 = "comments_2"
        obj.comments_2 = var_comments_2

        epw = EPW(comments_2=obj)
        epw.save(self.path, check=False)

        epw2 = EPW()
        epw2.read(self.path)
        self.assertEqual(epw2.comments_2.comments_2, var_comments_2)
