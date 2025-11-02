# Supertropical Algebra=======================

Supertropical Algebra

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)=======================

[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

.. image:: https://img.shields.io/badge/python-3.8+-blue.svg

A comprehensive Python package for **supertropical algebra**, featuring tangible and ghost elements, matrix operations, and linear system solving using Cramer's rule.   :target: https://www.python.org/downloads/

   :alt: Python Version

## ✨ Features

.. image:: https://img.shields.io/badge/license-MIT-green.svg

- **🎯 Tangible & Ghost Elements**: Full support for both element types with automatic conversion   :target: LICENSE

- **🧮 Supertropical Operations**: Addition (⊕ as max) and multiplication (⊙ as classical +)   :alt: License

- **📐 Matrix Operations**: Matrix multiplication, permanent (supertropical determinant), adjoint

- **🔧 Linear System Solver**: Cramer's rule implementation for solving Ax = bA comprehensive Python package for **supertropical algebra**, featuring tangible and ghost elements,

- **🚀 NumPy Integration**: Efficient computations using NumPy arraysmatrix operations, and linear system solving using Cramer's rule.

- **📚 Comprehensive Documentation**: Full API reference, theory guide, and interactive tutorials

- **✅ Type Safety**: Automatic type coercion and validation✨ Features

===========

## 📦 Installation

- **🎯 Tangible & Ghost Elements**: Full support for both element types with automatic conversion

```bash- **🧮 Supertropical Operations**: Addition (⊕ as max) and multiplication (⊙ as classical +)

pip install supertropical-algebra- **📐 Matrix Operations**: Matrix multiplication, permanent (supertropical determinant), adjoint

```- **🔧 Linear System Solver**: Cramer's rule implementation for solving Ax = b

- **🚀 NumPy Integration**: Efficient computations using NumPy arrays

Or install from source:- **📚 Comprehensive Documentation**: Full API reference, theory guide, and interactive tutorials

- **✅ Type Safety**: Automatic type coercion and validation

```bash

git clone https://github.com/YOUR_USERNAME/supertropical-algebra.git📦 Installation

cd supertropical-algebra===============

pip install -e .

```.. code-block:: bash



## 🚀 Quick Start   pip install supertropical-algebra



**Recommended: Use short alias (like numpy as np or tensorflow as tf)**Or install from source:



### Creating Elements.. code-block:: bash



```python   git clone https://github.com/YOUR_USERNAME/supertropical-algebra.git

import supertropical as suptrop   cd supertropical-algebra

   pip install -e .

# Tangible elements (regular)

a = suptrop.Element(5)🚀 Quick Start

b = suptrop.Element(3)==============



# Ghost elements (marked with ν)**Recommended: Use short alias like numpy (np) or tensorflow (tf)**

c = suptrop.Element(5, is_ghost=True)

Creating Elements

print(a)  # Output: 5.0-----------------

print(c)  # Output: 5.0ν

```.. code-block:: python



**Alternative:** You can also import directly:   import supertropical as suptrop

   

```python   # Tangible elements (regular)

from supertropical import Element, Matrix   a = suptrop.Element(5)

# Even shorter!   b = suptrop.Element(3)

a = Element(5)   

```   # Ghost elements (marked with ν)

   c = suptrop.Element(5, is_ghost=True)

### Supertropical Arithmetic   

   print(a)  # Output: 5.0

```python   print(c)  # Output: 5.0ν

import supertropical as suptrop

**Alternative:** You can also import directly:

a = suptrop.Element(5)

b = suptrop.Element(3).. code-block:: python

c = suptrop.Element(5, is_ghost=True)

   from supertropical import Element, Matrix

# Addition (⊕): max operation with ghost rules   # Even shorter!

result1 = a + b  # 5 ⊕ 3 = 5 (max)   a = Element(5)

result2 = a + a  # 5 ⊕ 5 = 5ν (becomes ghost)

Supertropical Arithmetic

# Multiplication (⊙): classical addition-------------------------

result3 = a * b  # 5 ⊙ 3 = 8 (5 + 3)

result4 = a * c  # 5 ⊙ 5ν = 10ν (result is ghost).. code-block:: python



# Works with Python numbers   import supertropical as suptrop

result5 = a + 7  # Automatic conversion   

result6 = 2 * a  # 2 ⊙ 5 = 7   a = suptrop.Element(5)

```   b = suptrop.Element(3)

   c = suptrop.Element(5, is_ghost=True)

### Matrix Operations

   # Addition (⊕): max operation with ghost rules

```python   result1 = a + b  # 5 ⊕ 3 = 5 (max)

import supertropical as suptrop   result2 = a + a  # 5 ⊕ 5 = 5ν (becomes ghost)

   

# Create matrices   # Multiplication (⊙): classical addition

A = suptrop.Matrix([[2, 1],    result3 = a * b  # 5 ⊙ 3 = 8 (5 + 3)

                    [1, 3]])   result4 = a * c  # 5 ⊙ 5ν = 10ν (result is ghost)

   

B = suptrop.Matrix([[5, 4],    # Works with Python numbers

                    [2, 1]])   result5 = a + 7  # Automatic conversion

   result6 = 2 * a  # 2 ⊙ 5 = 7

# Matrix multiplication (supertropical)

C = A @ BMatrix Operations

-----------------

# Permanent (supertropical determinant)

perm = A.permanent().. code-block:: python

print(f"Permanent: {perm}")

   import supertropical as suptrop

# Adjoint matrix   

adj = A.adjoint()   # Create matrices

```   A = suptrop.Matrix([[2, 1], 

                  [1, 3]])

### Solving Linear Systems   

   B = suptrop.Matrix([[5, 4], 

```python                  [2, 1]])

import supertropical as suptrop   

   # Matrix multiplication (supertropical)

# Define system: Ax = b   C = A @ B

A = suptrop.Matrix([[2, 1],    

                    [1, 3]])   # Permanent (supertropical determinant)

   perm = A.permanent()

b = suptrop.Matrix([[5],    print(f"Permanent: {perm}")

                    [4]])   

   # Adjoint matrix

# Solve using Cramer's rule   adj = A.adjoint()

x = A.solve(b)

Solving Linear Systems

print(f"Solution:\n{x}")----------------------

```

.. code-block:: python

## 📖 Documentation

   import supertropical as suptrop

Full documentation is available at: [GitHub Pages](https://github.com/YOUR_USERNAME/supertropical-algebra)   

   # Define system: Ax = b

- **Theory Guide**: Mathematical background on supertropical algebra   A = suptrop.Matrix([[2, 1], 

- **Tutorial**: Interactive Jupyter notebook with executable examples                  [1, 3]])

- **API Reference**: Complete API documentation with examples   

   b = suptrop.Matrix([[5], 

## 🧪 Running Tests                  [4]])

   

```bash   # Solve using Cramer's rule

# Install dev dependencies   x = A.solve(b)

pip install -e ".[dev]"   

   print(f"Solution:\n{x}")   # Solve using Cramer's rule

# Run tests   x = A.solve(b)

pytest   

   print(f"Solution:\\n{x}")

# Run with coverage

pytest --cov=supertropical📖 Documentation

```================



## 📚 Building DocumentationFull documentation is available at: `GitHub Pages <https://github.com/YOUR_USERNAME/supertropical-algebra>`_



```bash- **Theory Guide**: Mathematical background on supertropical algebra

# Install docs dependencies- **Tutorial**: Interactive Jupyter notebook with executable examples

pip install -e ".[docs]"- **API Reference**: Complete API documentation with examples



# Build HTML docs🧪 Running Tests

cd docs================

sphinx-build -b html source build

.. code-block:: bash

# Or use make (on Unix/Mac/Windows with make installed)

cd docs   # Install dev dependencies

make html   pip install -e ".[dev]"

```   

   # Run tests

The documentation will be in `docs/build/index.html`.   pytest

   

## 🎓 Mathematical Background   # Run with coverage

   pytest --cov=supertropical

Supertropical algebra extends tropical algebra with ghost elements:

📚 Building Documentation

**Operations**:=========================

- **Addition** (⊕): `a ⊕ b = max(a, b)` with special ghost rules

- **Multiplication** (⊙): `a ⊙ b = a + b` (classical addition).. code-block:: bash



**Elements**:   # Install docs dependencies

- **Tangible**: Regular elements (e.g., `5.0`)   pip install -e ".[docs]"

- **Ghost**: Elements marked with ν (e.g., `5.0ν`)   

- **Zero**: `-∞` (additive identity)   # Build HTML docs

- **One**: `0` (multiplicative identity)   cd docs

   sphinx-build -b html source build

**Key Properties**:   

- Matrix permanent replaces determinant   # Or use make (on Unix/Mac/Windows with make installed)

- Cramer's rule works for nonsingular matrices (permanent is tangible)   cd docs

- Applications in optimization, algebraic geometry, and phylogenetics   make html



## 🤝 ContributingThe documentation will be in ``docs/build/index.html``.



Contributions are welcome! Please feel free to submit a Pull Request.🎓 Mathematical Background

===========================

1. Fork the repository

2. Create your feature branch (`git checkout -b feature/amazing-feature`)Supertropical algebra extends tropical algebra with ghost elements:

3. Commit your changes (`git commit -m 'Add amazing feature'`)

4. Push to the branch (`git push origin feature/amazing-feature`)**Operations**:

5. Open a Pull Request

- **Addition** (⊕): ``a ⊕ b = max(a, b)`` with special ghost rules

## 📄 License- **Multiplication** (⊙): ``a ⊙ b = a + b`` (classical addition)



This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.**Elements**:



## 👥 Authors- **Tangible**: Regular elements (e.g., ``5.0``)

- **Ghost**: Elements marked with ν (e.g., ``5.0ν``)

- **Supertropical Team**- **Zero**: ``-∞`` (additive identity)

- **One**: ``0`` (multiplicative identity)

## 🙏 Acknowledgments

**Key Properties**:

- Based on research by Izhakian, Z., & Rowen, L. on supertropical algebra

- Inspired by tropical algebra and max-plus algebra implementations- Matrix permanent replaces determinant

- Cramer's rule works for nonsingular matrices (permanent is tangible)

## 📞 Contact- Applications in optimization, algebraic geometry, and phylogenetics



- GitHub: https://github.com/YOUR_USERNAME/supertropical-algebra🤝 Contributing

- Issues: https://github.com/YOUR_USERNAME/supertropical-algebra/issues===============



---Contributions are welcome! Please feel free to submit a Pull Request.



Made with ❤️ for mathematical computing1. Fork the repository

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
