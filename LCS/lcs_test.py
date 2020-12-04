import unittest
from lcs import length_lcs
from lcs import lcs

class Test_lcs(unittest.TestCase):

    def test_lcs(self):
        x = 'shirish'
        y = 'sigdyal'
        m = len(x)
        n = len(y)
        (array, length) = length_lcs(x, y, m, n)
        self.assertEqual(length, 2)
        result = lcs(x, y, array, length)
        self.assertListEqual(result, ['s', 'i'])
       
if __name__ == "__main__":
    unittest.main()