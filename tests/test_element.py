"""
Unit tests for SupertropicalElement class.
"""
import pytest
import math
from src.supertropical import SupertropicalElement


class TestSupertropicalElementCreation:
    """Test element creation and initialization."""
    
    def test_create_tangible_element(self):
        """Test creating a tangible element."""
        elem = SupertropicalElement(5)
        assert elem.value == 5.0
        assert not elem.is_ghost
        
    def test_create_ghost_element(self):
        """Test creating a ghost element."""
        elem = SupertropicalElement(5, is_ghost=True)
        assert elem.value == 5.0
        assert elem.is_ghost
        
    def test_create_from_int(self):
        """Test creating element from integer."""
        elem = SupertropicalElement(3)
        assert elem.value == 3.0
        assert isinstance(elem.value, float)
        
    def test_create_from_float(self):
        """Test creating element from float."""
        elem = SupertropicalElement(3.5)
        assert elem.value == 3.5
        
    def test_create_zero_element(self):
        """Test creating the zero element (-inf)."""
        zero = SupertropicalElement(-math.inf)
        assert zero.value == -math.inf
        assert zero.is_ghost  # -inf is always ghost
        
    def test_invalid_type_raises_error(self):
        """Test that invalid types raise TypeError."""
        with pytest.raises(TypeError):
            SupertropicalElement("not a number")


class TestSupertropicalAddition:
    """Test supertropical addition (⊕)."""
    
    def test_addition_different_values(self):
        """Test a ⊕ b = max(a, b) when a ≠ b."""
        a = SupertropicalElement(5)
        b = SupertropicalElement(3)
        result = a + b
        assert result.value == 5.0
        assert not result.is_ghost
        
    def test_addition_same_values_tangible(self):
        """Test a ⊕ a = aν (becomes ghost)."""
        a = SupertropicalElement(5)
        b = SupertropicalElement(5)
        result = a + b
        assert result.value == 5.0
        assert result.is_ghost
        
    def test_addition_tangible_and_ghost_same_value(self):
        """Test a ⊕ aν = aν."""
        a = SupertropicalElement(5)
        b = SupertropicalElement(5, is_ghost=True)
        result = a + b
        assert result.value == 5.0
        assert result.is_ghost
        
    def test_addition_two_ghosts(self):
        """Test aν ⊕ bν = max(a, b)ν."""
        a = SupertropicalElement(5, is_ghost=True)
        b = SupertropicalElement(3, is_ghost=True)
        result = a + b
        assert result.value == 5.0
        assert result.is_ghost
        
    def test_addition_with_python_int(self):
        """Test addition with Python int."""
        a = SupertropicalElement(5)
        result = a + 7
        assert result.value == 7.0
        assert not result.is_ghost
        
    def test_right_addition_with_python_int(self):
        """Test right addition with Python int."""
        a = SupertropicalElement(5)
        result = 7 + a
        assert result.value == 7.0
        assert not result.is_ghost
        
    def test_addition_with_zero(self):
        """Test addition with zero element (-inf)."""
        a = SupertropicalElement(5)
        zero = SupertropicalElement(-math.inf)
        result = a + zero
        assert result.value == 5.0


class TestSupertropicalMultiplication:
    """Test supertropical multiplication (⊙)."""
    
    def test_multiplication_two_tangibles(self):
        """Test a ⊙ b = a + b (classical addition)."""
        a = SupertropicalElement(5)
        b = SupertropicalElement(3)
        result = a * b
        assert result.value == 8.0
        assert not result.is_ghost
        
    def test_multiplication_tangible_and_ghost(self):
        """Test a ⊙ bν = (a + b)ν."""
        a = SupertropicalElement(5)
        b = SupertropicalElement(3, is_ghost=True)
        result = a * b
        assert result.value == 8.0
        assert result.is_ghost
        
    def test_multiplication_two_ghosts(self):
        """Test aν ⊙ bν = (a + b)ν."""
        a = SupertropicalElement(5, is_ghost=True)
        b = SupertropicalElement(3, is_ghost=True)
        result = a * b
        assert result.value == 8.0
        assert result.is_ghost
        
    def test_multiplication_with_python_int(self):
        """Test multiplication with Python int."""
        a = SupertropicalElement(5)
        result = a * 3
        assert result.value == 8.0
        assert not result.is_ghost
        
    def test_right_multiplication_with_python_int(self):
        """Test right multiplication with Python int."""
        a = SupertropicalElement(5)
        result = 3 * a
        assert result.value == 8.0
        assert not result.is_ghost
        
    def test_multiplication_with_zero(self):
        """Test multiplication with zero (0) - multiplicative identity."""
        a = SupertropicalElement(5)
        zero = SupertropicalElement(0)
        result = a * zero
        assert result.value == 5.0
        assert not result.is_ghost


class TestSupertropicalComparison:
    """Test comparison operations."""
    
    def test_equality_same_tangible(self):
        """Test equality of same tangible elements."""
        a = SupertropicalElement(5)
        b = SupertropicalElement(5)
        assert a == b
        
    def test_equality_same_ghost(self):
        """Test equality of same ghost elements."""
        a = SupertropicalElement(5, is_ghost=True)
        b = SupertropicalElement(5, is_ghost=True)
        assert a == b
        
    def test_inequality_different_values(self):
        """Test inequality of different values."""
        a = SupertropicalElement(5)
        b = SupertropicalElement(3)
        assert a != b
        
    def test_inequality_tangible_vs_ghost(self):
        """Test inequality between tangible and ghost of same value."""
        a = SupertropicalElement(5)
        b = SupertropicalElement(5, is_ghost=True)
        assert a != b
        
    def test_less_than_by_value(self):
        """Test less than comparison by value."""
        a = SupertropicalElement(3)
        b = SupertropicalElement(5)
        assert a < b
        assert not (b < a)
        
    def test_less_than_tangible_before_ghost(self):
        """Test tangible < ghost when values are equal."""
        a = SupertropicalElement(5)
        b = SupertropicalElement(5, is_ghost=True)
        assert a < b
        assert not (b < a)
        
    def test_greater_than(self):
        """Test greater than comparison."""
        a = SupertropicalElement(5)
        b = SupertropicalElement(3)
        assert a > b
        
    def test_less_than_or_equal(self):
        """Test less than or equal comparison."""
        a = SupertropicalElement(3)
        b = SupertropicalElement(5)
        c = SupertropicalElement(3)
        assert a <= b
        assert a <= c
        
    def test_greater_than_or_equal(self):
        """Test greater than or equal comparison."""
        a = SupertropicalElement(5)
        b = SupertropicalElement(3)
        c = SupertropicalElement(5)
        assert a >= b
        assert a >= c


class TestSupertropicalRepresentation:
    """Test string representation."""
    
    def test_str_tangible(self):
        """Test string representation of tangible element."""
        elem = SupertropicalElement(5)
        assert str(elem) == "5.0"
        
    def test_str_ghost(self):
        """Test string representation of ghost element."""
        elem = SupertropicalElement(5, is_ghost=True)
        assert str(elem) == "5.0ν"
        
    def test_str_zero(self):
        """Test string representation of zero element."""
        zero = SupertropicalElement(-math.inf)
        assert str(zero) == "-inf"
        
    def test_repr_tangible(self):
        """Test repr of tangible element."""
        elem = SupertropicalElement(5)
        assert repr(elem) == "SupertropicalElement(5.0, is_ghost=False)"
        
    def test_repr_ghost(self):
        """Test repr of ghost element."""
        elem = SupertropicalElement(5, is_ghost=True)
        assert repr(elem) == "SupertropicalElement(5.0, is_ghost=True)"


class TestSupertropicalProperties:
    """Test element properties."""
    
    def test_is_tangible_method(self):
        """Test is_tangible() method."""
        tangible = SupertropicalElement(5)
        ghost = SupertropicalElement(5, is_ghost=True)
        assert tangible.is_tangible()
        assert not ghost.is_tangible()
        
    def test_is_ghost_attribute(self):
        """Test is_ghost attribute."""
        tangible = SupertropicalElement(5)
        ghost = SupertropicalElement(5, is_ghost=True)
        assert not tangible.is_ghost
        assert ghost.is_ghost


class TestSupertropicalMathematicalProperties:
    """Test mathematical properties."""
    
    def test_addition_commutative(self):
        """Test commutativity of addition."""
        a = SupertropicalElement(5)
        b = SupertropicalElement(3)
        assert (a + b) == (b + a)
        
    def test_multiplication_commutative(self):
        """Test commutativity of multiplication."""
        a = SupertropicalElement(5)
        b = SupertropicalElement(3)
        assert (a * b) == (b * a)
        
    def test_addition_associative(self):
        """Test associativity of addition."""
        a = SupertropicalElement(5)
        b = SupertropicalElement(3)
        c = SupertropicalElement(7)
        assert ((a + b) + c) == (a + (b + c))
        
    def test_multiplication_associative(self):
        """Test associativity of multiplication."""
        a = SupertropicalElement(5)
        b = SupertropicalElement(3)
        c = SupertropicalElement(2)
        assert ((a * b) * c) == (a * (b * c))
        
    def test_distributivity(self):
        """Test distributivity: a ⊙ (b ⊕ c) = (a ⊙ b) ⊕ (a ⊙ c)."""
        a = SupertropicalElement(2)
        b = SupertropicalElement(5)
        c = SupertropicalElement(3)
        
        left = a * (b + c)
        right = (a * b) + (a * c)
        
        # Both should give the same result
        assert left.value == right.value
        assert left.is_ghost == right.is_ghost
