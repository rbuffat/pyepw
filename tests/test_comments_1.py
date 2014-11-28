import os
import tempfile
import unittest
from pyepw.epw import Comments1, EPW


class TestComments1(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_comments_1(self):

        obj = Comments1()
        var_comments_1 = "comments_1"
        obj.comments_1 = var_comments_1

        epw = EPW(comments_1=obj)
        epw.save(self.path)

        epw2 = EPW()
        epw2.read(self.path)
        self.assertEqual(epw2.comments_1.comments_1, var_comments_1)
