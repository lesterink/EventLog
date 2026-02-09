# test_eventlog.py
"""
Tests for EventLog module.
"""

import unittest
from eventlog import EventLog

class TestEventLog(unittest.TestCase):
    """Test cases for EventLog class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = EventLog()
        self.assertIsInstance(instance, EventLog)
        
    def test_run_method(self):
        """Test the run method."""
        instance = EventLog()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
