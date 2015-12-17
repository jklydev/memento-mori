import unittest
import mori

class MoriTest(unittest.TestCase):

    def test1(self):
        M, F = mori.make_table("tables/2012.csv")
        self.assertEqual(M[0]['q'], 0.004722)

if __name__ == '__main__':
    unittest.main()
