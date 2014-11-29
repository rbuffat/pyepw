import os
import tempfile
import unittest
from pyepw.epw import EPW


class TestReadEPW(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_read_epw(self):

        epw = EPW()
        epw.read(r"tests/data/USA_CA_San.Francisco.Intl.AP.724940_TMY3.epw")

        epw.save(self.path)
        epw2 = EPW()
        epw2.read(self.path)
