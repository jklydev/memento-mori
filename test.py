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
        results = self.app.get('/results', follow_redirects=True)
        self.assertFalse('Error' in results.data)
        self.assertTrue('Male' in results.data)

    def testResultsData(self):
        results = self.app.get("/results/f/27")
        self.assertFalse('Error' in results.data)
        self.assertTrue('32%' in results.data)

    def testHomePost(self):
        home = self.app.post('/', data=dict(
            sex='f',
            age='27'), follow_redirects=True)
        self.assertFalse('Error' in home.data)
        self.assertTrue('32%' in home.data)

    def testAbout(self):
        about = self.app.get('/about')
        self.assertTrue('About' in about.data)

if __name__ == '__main__':
    unittest.main()
