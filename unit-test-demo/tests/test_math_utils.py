"""
Unit tests for math_utils module.
"""

from src.math_utils import add

def test_add():
    """Test that add(a, b) returns the correct sum."""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
