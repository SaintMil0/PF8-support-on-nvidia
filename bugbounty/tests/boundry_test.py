import unittest
import numpy as np
# Adjust import as needed
from fp8support import FP8_E4M3
class TestBoundary(unittest.TestCase):
    def test_fp8_e4m3_underflow(self):
        a = FP8_E4M3(1e-10)
        self.assertAlmostEqual(a.to_float(), 0.0, places=2)

if __name__ == '__main__':
    unittest.main()
