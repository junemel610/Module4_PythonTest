import unittest

def check(x):

    return x >= 100

class test(unittest.TestCase):
    def test(self):
        self.assertTrue(check(100))

if __name__ == '__main__':

    unittest.main()




