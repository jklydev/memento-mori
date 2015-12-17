import unittest
import mori

class TableTestCase(unittest.TestCase):
    def setUp(self):
        self.M, self.F = mori.make_table("tables/2012.csv")

class MoriTest(TableTestCase):
    def test1(self):
        self.assertEqual(self.M[0]['q'], 0.004722)

    def test2(self):
        self.assertEqual(self.F[0]['q'], 0.003785)

    def test3(self):
        self.assertEqual(self.M[100]['d'], 378.2)

    def test4(self):
        self.assertEqual(self.F[100]['e'], 2.27)

if __name__ == '__main__':
    unittest.main()
