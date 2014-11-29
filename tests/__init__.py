import unittest
from pyepw.epw import EPW


class TestReadEPW(unittest.TestCase):

    def test_read_epw(self):

        epw = EPW()
        epw.read(r"data/USA_CA_San.Francisco.Intl.AP.724940_TMY3.epw")