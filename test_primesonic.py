# test_primesonic.py
"""
Tests for PrimeSonic module.
"""

import unittest
from primesonic import PrimeSonic

class TestPrimeSonic(unittest.TestCase):
    """Test cases for PrimeSonic class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = PrimeSonic()
        self.assertIsInstance(instance, PrimeSonic)
        
    def test_run_method(self):
        """Test the run method."""
        instance = PrimeSonic()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
