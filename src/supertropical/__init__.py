"""
Supertropical Algebra Package
==============================

A Python package for working with supertropical algebra, featuring:
- Tangible and ghost elements
- Matrix operations over supertropical semiring
- Linear system solving using Cramer's rule

Basic usage:
    >>> from supertropical import SupertropicalElement, SupertropicalMatrix
    >>> a = SupertropicalElement(5)  # tangible
    >>> b = SupertropicalElement(5, is_ghost=True)  # ghost (5ν)
    >>> print(a + b)  # supertropical addition
    5.0ν
"""

from .element import SupertropicalElement
from .matrix import SupertropicalMatrix

__version__ = "0.1.0"
__all__ = ["SupertropicalElement", "SupertropicalMatrix"]
