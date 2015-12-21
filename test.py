import unittest
import mori

class TableTest(unittest.TestCase):
    def setUp(self):
        self.M, self.F = mori.make_table("tables/2012.csv")

    def testMq(self):
        self.assertEqual(self.M[0]['q'], 0.004722)

    def testFq(self):
        self.assertEqual(self.F[0]['q'], 0.003785)

    def testMd(self):
        self.assertEqual(self.M[100]['d'], 378.2)

    def testFe(self):
        self.assertEqual(self.F[100]['e'], 2.27)

class MoriTest(unittest.TestCase):
    def setUp(self):
        self.app = mori.app.test_client()

    def testHome(self):
        home = self.app.get('/')
        self.assertTrue('Male' in home.data)

    def testResultsNone(self):
        results = self.app.get('/results')
        self.assertTrue('Data' in results.data)

    def testResultsData(self):
        results = self.app.get("/results/{'age':27}")
        self.assertTrue('27' in results.data)

    def testAbout(self):
        about = self.app.get('/about')
        self.assertTrue('About' in about.data)

if __name__ == '__main__':
    unittest.main()
