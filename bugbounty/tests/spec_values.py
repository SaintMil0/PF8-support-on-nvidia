import unittest
import numpy as np
from fp8support import FP8_E4M3

class TestFP8SpecialValues(unittest.TestCase):

    def test_fp8_e4m3_nan(self):
        a = FP8_E4M3(float('nan'))
        self.assertTrue(np.isnan(a.to_float()))

    def test_fp8_e5m2_inf(self):
        b = FP8_E5M2(float('inf'))
        self.assertTrue(np.isinf(b.to_float()))

if __name__ == '__main__':
    unittest.main()
