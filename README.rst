=======================
Supertropical Algebra
=======================

.. image:: https://img.shields.io/badge/python-3.8+-blue.svg
   :target: https://www.python.org/downloads/
   :alt: Python Version

.. image:: https://img.shields.io/badge/license-MIT-green.svg
   :target: LICENSE
   :alt: License

A comprehensive Python package for **supertropical algebra**, featuring tangible and ghost elements,
matrix operations, and linear system solving using Cramer's rule.

✨ Features
===========

- **🎯 Tangible & Ghost Elements**: Full support for both element types with automatic conversion
- **🧮 Supertropical Operations**: Addition (⊕ as max) and multiplication (⊙ as classical +)
- **📐 Matrix Operations**: Matrix multiplication, permanent (supertropical determinant), adjoint
- **🔧 Linear System Solver**: Cramer's rule implementation for solving Ax = b
- **🚀 NumPy Integration**: Efficient computations using NumPy arrays
- **📚 Comprehensive Documentation**: Full API reference, theory guide, and interactive tutorials
- **✅ Type Safety**: Automatic type coercion and validation

📦 Installation
===============

.. code-block:: bash

   pip install supertropical-algebra

Or install from source:

.. code-block:: bash

   git clone https://github.com/YOUR_USERNAME/supertropical-algebra.git
   cd supertropical-algebra
   pip install -e .

🚀 Quick Start
==============

**Recommended: Use short alias like numpy (np) or tensorflow (tf)**

Creating Elements
-----------------

.. code-block:: python

   import supertropical as suptrop
   
   # Tangible elements (regular)
   a = suptrop.Element(5)
   b = suptrop.Element(3)
   
   # Ghost elements (marked with ν)
   c = suptrop.Element(5, is_ghost=True)
   
   print(a)  # Output: 5.0
   print(c)  # Output: 5.0ν

**Alternative:** You can also import directly:

.. code-block:: python

   from supertropical import Element, Matrix
   # Even shorter!
   a = Element(5)

Supertropical Arithmetic
-------------------------

.. code-block:: python

   import supertropical as suptrop
   
   a = suptrop.Element(5)
   b = suptrop.Element(3)
   c = suptrop.Element(5, is_ghost=True)

   # Addition (⊕): max operation with ghost rules
   result1 = a + b  # 5 ⊕ 3 = 5 (max)
   result2 = a + a  # 5 ⊕ 5 = 5ν (becomes ghost)
   
   # Multiplication (⊙): classical addition
   result3 = a * b  # 5 ⊙ 3 = 8 (5 + 3)
   result4 = a * c  # 5 ⊙ 5ν = 10ν (result is ghost)
   
   # Works with Python numbers
   result5 = a + 7  # Automatic conversion
   result6 = 2 * a  # 2 ⊙ 5 = 7

Matrix Operations
-----------------

.. code-block:: python

   import supertropical as suptrop
   
   # Create matrices
   A = suptrop.Matrix([[2, 1], 
                  [1, 3]])
   
   B = suptrop.Matrix([[5, 4], 
                  [2, 1]])
   
   # Matrix multiplication (supertropical)
   C = A @ B
   
   # Permanent (supertropical determinant)
   perm = A.permanent()
   print(f"Permanent: {perm}")
   
   # Adjoint matrix
   adj = A.adjoint()

Solving Linear Systems
----------------------

.. code-block:: python

   import supertropical as suptrop
   
   # Define system: Ax = b
   A = suptrop.Matrix([[2, 1], 
                  [1, 3]])
   
   b = suptrop.Matrix([[5], 
                  [4]])
   
   # Solve using Cramer's rule
   x = A.solve(b)
   
   print(f"Solution:\n{x}")   # Solve using Cramer's rule
   x = A.solve(b)
   
   print(f"Solution:\\n{x}")

📖 Documentation
================

Full documentation is available at: `GitHub Pages <https://github.com/YOUR_USERNAME/supertropical-algebra>`_

- **Theory Guide**: Mathematical background on supertropical algebra
- **Tutorial**: Interactive Jupyter notebook with executable examples
- **API Reference**: Complete API documentation with examples

🧪 Running Tests
================

.. code-block:: bash

   # Install dev dependencies
   pip install -e ".[dev]"
   
   # Run tests
   pytest
   
   # Run with coverage
   pytest --cov=supertropical

📚 Building Documentation
=========================

.. code-block:: bash

   # Install docs dependencies
   pip install -e ".[docs]"
   
   # Build HTML docs
   cd docs
   sphinx-build -b html source build
   
   # Or use make (on Unix/Mac/Windows with make installed)
   cd docs
   make html

The documentation will be in ``docs/build/index.html``.

🎓 Mathematical Background
===========================

Supertropical algebra extends tropical algebra with ghost elements:

**Operations**:

- **Addition** (⊕): ``a ⊕ b = max(a, b)`` with special ghost rules
- **Multiplication** (⊙): ``a ⊙ b = a + b`` (classical addition)

**Elements**:

- **Tangible**: Regular elements (e.g., ``5.0``)
- **Ghost**: Elements marked with ν (e.g., ``5.0ν``)
- **Zero**: ``-∞`` (additive identity)
- **One**: ``0`` (multiplicative identity)

**Key Properties**:

- Matrix permanent replaces determinant
- Cramer's rule works for nonsingular matrices (permanent is tangible)
- Applications in optimization, algebraic geometry, and phylogenetics

🤝 Contributing
===============

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (``git checkout -b feature/amazing-feature``)
3. Commit your changes (``git commit -m 'Add amazing feature'``)
4. Push to the branch (``git push origin feature/amazing-feature``)
5. Open a Pull Request

📄 License
==========

This project is licensed under the MIT License - see the `LICENSE <LICENSE>`_ file for details.

👥 Authors
==========

- **Supertropical Team**

🙏 Acknowledgments
==================

- Based on research by Izhakian, Z., & Rowen, L. on supertropical algebra
- Inspired by tropical algebra and max-plus algebra implementations

📞 Contact
==========

- GitHub: `https://github.com/YOUR_USERNAME/supertropical-algebra <https://github.com/YOUR_USERNAME/supertropical-algebra>`_
- Issues: `https://github.com/YOUR_USERNAME/supertropical-algebra/issues <https://github.com/YOUR_USERNAME/supertropical-algebra/issues>`_

---

Made with ❤️ for mathematical computing
