import numpy as np
import unittest
from fp8support import FP8_E4M3

class TestFP8E4M3Arithmetic(unittest.TestCase):
    
    def test_addition(self):
        a = FP8_E4M3(1.0)
        b = FP8_E4M3(2.0)
        result = a + b
        self.assertAlmostEqual(result.to_float(), 3.0, places=2)

    def test_multiplication(self):
        a = FP8_E4M3(2.0)
        b = FP8_E4M3(3.0)
        result = a * b
        self.assertAlmostEqual(result.to_float(), 6.0, places=2)

    def test_addition_with_underflow(self):
        a = FP8_E4M3(1e-10)
        b = FP8_E4M3(1e-10)
        result = a + b
        self.assertAlmostEqual(result.to_float(), 0.0, places=2)

    def test_multiplication_with_overflow(self):
        a = FP8_E4M3(1e10)
        b = FP8_E4M3(1e10)
        result = a * b
        self.assertTrue(result.to_float() == float('inf'))

if __name__ == '__main__':
    unittest.main()
