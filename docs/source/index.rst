Supertropical Algebra Documentation
====================================

Welcome to the **Supertropical Algebra** package documentation!

This package provides a complete implementation of supertropical algebra in Python,
featuring tangible and ghost elements, matrix operations, and linear system solving.

.. note::
   **Supertropical algebra** is an algebraic structure where:
   
   - Addition is defined as :math:`a \oplus b = \max(a, b)`
   - Multiplication is defined as :math:`a \odot b = a + b` (classical addition)
   - Elements can be **tangible** (regular) or **ghost** (marked with ν)

Quick Start
-----------

Installation:

.. code-block:: bash

   pip install supertropical-algebra

Basic usage:

.. code-block:: python

   from supertropical import SupertropicalElement, SupertropicalMatrix
   
   # Create elements
   a = SupertropicalElement(5)          # Tangible: 5.0
   b = SupertropicalElement(3, True)    # Ghost: 3.0ν
   
   # Supertropical addition (max operation)
   c = a + b  # Result: 5.0ν (max is 5, becomes ghost)
   
   # Supertropical multiplication (classical addition)
   d = a * b  # Result: 8.0ν (5 + 3 = 8, is ghost)
   
   # Create and solve linear systems
   A = SupertropicalMatrix([[2, 1], [1, 3]])
   b = SupertropicalMatrix([[5], [4]])
   x = A.solve(b)  # Solve Ax = b using Cramer's rule

Features
--------

✨ **Core Features:**

- **Tangible and Ghost Elements**: Full support for both element types
- **Arithmetic Operations**: Supertropical addition ⊕ and multiplication ⊙
- **Matrix Operations**: Matrix multiplication, permanent (supertropical determinant), adjoint
- **Linear System Solver**: Cramer's rule implementation for solving Ax = b
- **Type Safety**: Automatic coercion and type checking
- **NumPy Integration**: Efficient array operations under the hood

Contents
--------

.. toctree::
   :maxdepth: 2
   :caption: User Guide

   theory
   examples/tutorial

.. toctree::
   :maxdepth: 2
   :caption: API Reference

   api/index

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
