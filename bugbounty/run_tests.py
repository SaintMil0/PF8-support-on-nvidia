import unittest
import os
import sys

# Add the current directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

# Discover and load all test cases from the 'tests' directory
def load_tests(loader, tests, pattern):
    # Customize the pattern to match your test files
    return loader.discover('tests', pattern='*_test.py')

if __name__ == '__main__':
    # Load tests
    loader = unittest.TestLoader()
    suite = load_tests(loader, None, None)
    
    # Run the tests
    runner = unittest.TextTestRunner()
    runner.run(suite)
