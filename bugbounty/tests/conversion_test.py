import unittest
import numpy as np
from fp8support import FP8_E4M3  # Adjust import as needed

class TestConversion(unittest.TestCase):
    def test_conversion(self):
        a = FP8_E4M3(448.0)
        self.assertAlmostEqual(a.to_float(), 448.0, places=2)

if __name__ == '__main__':
    unittest.main()
