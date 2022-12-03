import unittest
from main import count_digits

class Testing(unittest.TestCase):
    def test_wrong_type(self):
        with self.assertRaises(TypeError):
            count_digits(1212)

    def test_empty(self):
        self.assertEqual(count_digits(''), 0)

    def test_function_1(self):
        a = count_digits('акр1лорь2123тоыфа')
        b = 8
        self.assertEqual(a, b)

if __name__ == '__main__':
    unittest.main()