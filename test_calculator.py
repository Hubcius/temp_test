"""Tests for the calculator module."""

import pytest
from calculator import add, subtract, multiply, divide


class TestAdd:
    """Tests for the add function."""
    
    def test_add_positive_numbers(self):
        """Test adding two positive numbers."""
        assert add(2, 3) == 5
        assert add(10, 20) == 30
    
    def test_add_negative_numbers(self):
        """Test adding two negative numbers."""
        assert add(-5, -3) == -8
        assert add(-10, -20) == -30
    
    def test_add_mixed_signs(self):
        """Test adding numbers with different signs."""
        assert add(5, -3) == 2
        assert add(-5, 3) == -2
    
    def test_add_zero(self):
        """Test adding zero."""
        assert add(5, 0) == 5
        assert add(0, 5) == 5
        assert add(0, 0) == 0


class TestSubtract:
    """Tests for the subtract function."""
    
    def test_subtract_positive_numbers(self):
        """Test subtracting two positive numbers."""
        assert subtract(5, 3) == 2
        assert subtract(20, 10) == 10
    
    def test_subtract_negative_numbers(self):
        """Test subtracting two negative numbers."""
        assert subtract(-5, -3) == -2
        assert subtract(-10, -20) == 10
    
    def test_subtract_mixed_signs(self):
        """Test subtracting numbers with different signs."""
        assert subtract(5, -3) == 8
        assert subtract(-5, 3) == -8
    
    def test_subtract_zero(self):
        """Test subtracting zero."""
        assert subtract(5, 0) == 5
        assert subtract(0, 5) == -5


class TestMultiply:
    """Tests for the multiply function."""
    
    def test_multiply_positive_numbers(self):
        """Test multiplying two positive numbers."""
        assert multiply(2, 3) == 6
        assert multiply(5, 4) == 20
    
    def test_multiply_negative_numbers(self):
        """Test multiplying two negative numbers."""
        assert multiply(-2, -3) == 6
        assert multiply(-5, -4) == 20
    
    def test_multiply_mixed_signs(self):
        """Test multiplying numbers with different signs."""
        assert multiply(2, -3) == -6
        assert multiply(-5, 4) == -20
    
    def test_multiply_by_zero(self):
        """Test multiplying by zero."""
        assert multiply(5, 0) == 0
        assert multiply(0, 5) == 0
        assert multiply(0, 0) == 0


class TestDivide:
    """Tests for the divide function."""
    
    def test_divide_positive_numbers(self):
        """Test dividing two positive numbers."""
        assert divide(6, 2) == 3
        assert divide(20, 4) == 5
    
    def test_divide_negative_numbers(self):
        """Test dividing two negative numbers."""
        assert divide(-6, -2) == 3
        assert divide(-20, -4) == 5
    
    def test_divide_mixed_signs(self):
        """Test dividing numbers with different signs."""
        assert divide(6, -2) == -3
        assert divide(-20, 4) == -5
    
    def test_divide_by_zero(self):
        """Test dividing by zero raises ValueError."""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(5, 0)
    
    def test_divide_zero(self):
        """Test dividing zero by a number."""
        assert divide(0, 5) == 0
        assert divide(0, -5) == 0
