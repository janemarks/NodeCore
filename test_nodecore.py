# test_nodecore.py
"""
Tests for NodeCore module.
"""

import unittest
from nodecore import NodeCore

class TestNodeCore(unittest.TestCase):
    """Test cases for NodeCore class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NodeCore()
        self.assertIsInstance(instance, NodeCore)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NodeCore()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
