# test_wrkbenchmark.py
"""
Tests for WrkBenchmark module.
"""

import unittest
from wrkbenchmark import WrkBenchmark

class TestWrkBenchmark(unittest.TestCase):
    """Test cases for WrkBenchmark class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = WrkBenchmark()
        self.assertIsInstance(instance, WrkBenchmark)
        
    def test_run_method(self):
        """Test the run method."""
        instance = WrkBenchmark()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
