# src/supertropical/element.py
import functools
import math

# Use @functools.total_ordering to automatically generate
# comparison methods (>=, >, <=) 
# from just __eq__ and __lt__. [31, 32]
@functools.total_ordering
class SupertropicalElement:
    """
    Represents a single element in supertropical algebra,
    which can be either tangible or ghost.
    """

    def __init__(self, value: float, is_ghost: bool = False):
        """
        Initializes the element.

        Args:
            value (float): The numerical value of the element (e.g., 5.0).
            is_ghost (bool): True if this element is a ghost (e.g., 5.0ν).
        """
        # Using -math.inf as the representation for the zero element $-\infty$
        if not isinstance(value, (int, float)):
            raise TypeError("Value must be an int or float.")
            
        self.value = float(value)
        self.is_ghost = is_ghost

    def _coerce(self, other):
        """Converts int, float, or other elements for operations."""
        if isinstance(other, SupertropicalElement):
            return other
        if isinstance(other, (int, float)):
            # Standard numbers are treated as tangible elements
            return SupertropicalElement(other)
        return NotImplemented

    # --- Arithmetic Methods  ---

    def __add__(self, other):
        """
        Performs supertropical addition (oplus, $\oplus$).

        Rules:
        1. a + b = max(a, b)
        2. a + a = aν (becomes ghost)
        3. a + aν = aν
        4. aν + aν = aν
        """
        other = self._coerce(other)
        if other is NotImplemented:
            return NotImplemented

        # Rules 3 & 4: If one or both are ghost
        if self.is_ghost or other.is_ghost:
            # a + bν -> max(a, b)ν (if a!= b)
            # aν + bν -> max(a, b)ν
            # a + aν -> aν
            new_val = max(self.value, other.value)
            return SupertropicalElement(new_val, is_ghost=True)

        # Rules 1 & 2: Both are tangible
        if self.value == other.value:
            # Rule 2: a + a = aν 
            return SupertropicalElement(self.value, is_ghost=True)
        else:
            # Rule 1: a + b = max(a, b)
            return SupertropicalElement(max(self.value, other.value))

    def __radd__(self, other):
        # Ensures '5 + element' works [34]
        return self.__add__(other)

    def __mul__(self, other):
        """
        Performs supertropical multiplication (odot, $\odot$).

        Rules:
        1. a * b = a + b (classical addition)
        2. a * bν = (a + b)ν
        3. aν * bν = (a + b)ν
        """
        other = self._coerce(other)
        if other is NotImplemented:
            return NotImplemented

        # Rules 1, 2, 3: Classical addition on values
        new_val = self.value + other.value
        
        # The result is ghost if either operand is ghost
        new_is_ghost = self.is_ghost or other.is_ghost
        
        return SupertropicalElement(new_val, new_is_ghost)

    def __rmul__(self, other):
        # Ensures '5 * element' works [35]
        return self.__mul__(other)

    # --- Representation & Comparison Methods [36, 37] ---
    
    def __repr__(self):
        """Formal representation for debugging."""
        return f"SupertropicalElement({self.value}, is_ghost={self.is_ghost})"

    def __str__(self):
        """Readable string representation."""
        if self.value == -math.inf:
            return "-inf"
        suffix = "ν" if self.is_ghost else ""
        return f"{self.value}{suffix}"

    def __eq__(self, other):
        """Equality check: a == b."""
        other = self._coerce(other)
        if other is NotImplemented:
            return False
        return self.value == other.value and self.is_ghost == other.is_ghost

    def __lt__(self, other):
        """Less than check: a < b."""
        other = self._coerce(other)
        if other is NotImplemented:
            return NotImplemented
        
        # Primary comparison is by value
        if self.value < other.value:
            return True
        if self.value > other.value:
            return False
            
        # If values are equal, tangible (False) < ghost (True)
        return not self.is_ghost and other.is_ghost

    # --- Property Methods ---
    
    def is_tangible(self) -> bool:
        """Returns True if this element is tangible."""
        return not self.is_ghost