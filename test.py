import unittest
import my_func

class TestMyFunc(unittest.TestCase):

    def setUp(self):
        pass

    def test_multiply_five(self):
        self.assertEqual( my_func.cps2368(5), 25)
        
if __name__ == '__main__':
    unittest.main()
