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
        self.assertTrue('Male' in results.data)

    def testResultsData(self):
        results = self.app.get("/results/{'x':27, 's':'m', 'q':0.2, 'd':0.8, 'e':23}")
        self.assertTrue('27' in results.data)

    def testHomePost(self):
        home = self.app.post('/', data=dict(
            sex='f',
            age='27'), follow_redirects=True)
        self.assertFalse('Error' in home.data)
        self.assertTrue('27' in home.data)
        self.assertTrue('56' in home.data)

    def testAbout(self):
        about = self.app.get('/about')
        self.assertTrue('About' in about.data)

if __name__ == '__main__':
    unittest.main()
