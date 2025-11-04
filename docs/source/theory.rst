Supertropical Algebra Theory
============================

This page provides comprehensive mathematical background on supertropical algebra, based on the extended semiring tropical framework.

1. Supertropical Algebra
------------------------

1.1 Extended Semiring Tropical
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

As discussed in max-plus algebra, the tropical algebra structure lacks an inverse element for the addition operation Γèò. This limitation is specifically addressed by introducing the **extended semiring tropical** structure, allowing us to solve systems of linear equations.

Definition 1.1 (Extended Semiring Tropical)
""""""""""""""""""""""""""""""""""""""""""""

An **extended semiring tropical** is defined as :math:`(T, \oplus, \otimes)` where :math:`T = \mathbb{R} \cup \{-\infty\} \cup \mathbb{R}^\nu`, where :math:`\mathbb{R}` is the set of all real numbers and :math:`\mathbb{R}^\nu = \{a^\nu \mid a \in \mathbb{R}\}`.

- The **neutral element** for :math:`T` is :math:`\varepsilon \stackrel{\text{def}}{=} -\infty`
- The **unit element** is :math:`e \stackrel{\text{def}}{=} 0`

The set :math:`\mathbb{R}_{-\infty} = \mathbb{R} \cup \{-\infty\}` represents the **ideal** of :math:`T`, called the **ideal ghost**. 

Meanwhile, a function :math:`v : T \to \mathbb{R}_{-\infty}` defined by :math:`v(x) \stackrel{\text{def}}{=} x, \forall x \in \mathbb{R}_{-\infty}` represents **tangible identity**, and :math:`v(a) = a^\nu, \forall a \in \mathbb{R}` where element :math:`a^\nu` is called the **element ghost** or **ghost** of :math:`a`. The function :math:`v` is called the **ghost mapping**.

Definition 1.2 (Extended Semiring Tropical Order)
""""""""""""""""""""""""""""""""""""""""""""""""""

Given an **extended semiring tropical** :math:`T`, a **partial order** relation :math:`\prec` is defined on :math:`T` as follows:

For any :math:`a, b \in \mathbb{R}`, :math:`a^\nu, b^\nu \in \mathbb{R}^\nu` and :math:`x \in T`:

1. :math:`-\infty \prec x, \forall x \in T \setminus \{-\infty\}`
2. For any real numbers :math:`a \prec b`, then :math:`a \prec a^\nu, a \prec b^\nu, a^\nu \prec b`, and :math:`a^\nu \prec b^\nu`
3. :math:`a \prec a^\nu` for any :math:`a \in \mathbb{R}`

Axiom 1.1 (Extended Semiring Tropical Operations)
""""""""""""""""""""""""""""""""""""""""""""""""""

Given an extended semiring tropical :math:`T`, the operations :math:`\oplus` (max) and :math:`\otimes` (addition) on :math:`T` satisfy the following axioms.

For any :math:`a, b \in \mathbb{R}`, :math:`a^\nu, b^\nu \in \mathbb{R}^\nu` and :math:`x, y \in T`:

1. :math:`-\infty \oplus x = x \oplus -\infty = x, \forall x \in T`
2. :math:`x \oplus y = \max_{\prec} \{x, y\}` provided :math:`x \neq y`
3. :math:`a \oplus a = a^\nu \oplus a^\nu = a \oplus a^\nu = a^\nu \oplus a = a^\nu`
4. :math:`-\infty \otimes x = x \otimes -\infty = -\infty`
5. :math:`a \otimes b = a + b` (classical addition)
6. :math:`a^\nu \otimes b = a \otimes b^\nu = a^\nu \otimes b^\nu = (a + b)^\nu`

**Example 1.1**: Operations in extended semiring tropical :math:`T`:

1. :math:`-\infty \oplus 4 = 4 \oplus -\infty = 4`
2. :math:`-2 \oplus 7 = \max_{\prec} \{-2, 7\} = 7`
3. :math:`8 \oplus 8 = 8^\nu \oplus 8^\nu = 8 \oplus 8^\nu = 8^\nu \oplus 8 = 8^\nu`
4. :math:`-\infty \otimes 3 = 3 \otimes -\infty = -\infty`
5. :math:`6 \otimes 9 = 6 + 9 = 15`
6. :math:`7^\nu \otimes 8 = 7 \otimes 8^\nu = 7^\nu \otimes 8^\nu = (7 + 8)^\nu = 15^\nu`

2. Ghost Surpasses Relation
----------------------------

2.1 Definition
^^^^^^^^^^^^^^

In supertropical semiring :math:`R`, for any :math:`a \in R`, then :math:`a \oplus a = -\infty` only holds when :math:`a = -\infty`. However, for any :math:`a \in T` then :math:`a \oplus a = a^\nu` and for any :math:`x \in G` then :math:`x \oplus x = x`. Therefore, a **ghost surpasses** relation in :math:`R` will be introduced as follows.

Definition 2.1 (Ghost Surpasses Relation)
""""""""""""""""""""""""""""""""""""""""""

Given a supertropical semiring :math:`R`, a relation :math:`\vDash` is called a **ghost surpasses** relation in :math:`R` defined as:

.. math::

   x \vDash y \quad \text{if} \quad x = y \oplus z \quad \text{for some} \quad z \in \mathcal{G}_0

where :math:`\mathcal{G}_0` is the set of ghost elements.

**Example 2.1**: Ghost surpasses relation in supertropical semiring :math:`R`:

1. For :math:`9, 10^\nu \in R`, we have :math:`10^\nu \vDash 9` because :math:`10^\nu = 9 \oplus 10^\nu`. Here, :math:`z = 10^\nu` is a value in :math:`\mathcal{G}_0` satisfying :math:`10^\nu = 9 \oplus 10^\nu`.

2. For :math:`-5 \in R`, we have :math:`-5 \vDash -5` because :math:`-5 = -5 \oplus \varepsilon`. Here, :math:`z = \varepsilon \in \mathcal{G}_0` with :math:`z \neq \varepsilon` satisfying :math:`-5 = -5 \oplus z` is :math:`z \prec -5`. For example, :math:`z = -6^\nu` and :math:`z = -7.5^\nu`. Notice that there are many values of :math:`z \in \mathcal{G}_0` satisfying :math:`-5 = -5 \oplus z` other than :math:`z \prec -5`.

3. Meanwhile, for :math:`7, 6 \in R`, we have :math:`7 \nvDash 6` because the value of :math:`z` satisfying :math:`7 = 6 \oplus z` is only :math:`z = 7 \notin \mathcal{G}_0`.

3. Supertropical Matrices
--------------------------

3.1 Matrix Operations
^^^^^^^^^^^^^^^^^^^^^

The set of all :math:`m \times n` matrices over supertropical semiring is denoted as :math:`M_{m \times n}(R)`, where matrix elements are members of :math:`R`. When the dimension of a matrix is square, denoted as :math:`M_n(R)`, the binary operations Γèò and Γèù in :math:`R` can be extended to matrix operations in :math:`M_n(R)`. Furthermore, the ghost surpasses relation in :math:`R` can also be extended to matrices in :math:`M_n(R)`.

If :math:`A \vDash B` then :math:`a_{i,j} \vDash b_{i,j}` for any :math:`i` and :math:`j` in :math:`\underline{n}`.

**Matrix Addition**

For matrices :math:`A, B \in M_{m \times n}(R)`, the addition :math:`A \oplus B` is defined as:

.. math::

   [A \oplus B]_{i,j} = a_{i,j} \oplus b_{i,j}

for :math:`i \in \underline{m}` and :math:`j \in \underline{n}`.

**Matrix Multiplication**

For matrix :math:`A \in M_{m \times p}(R)` and :math:`B \in M_{p \times n}(R)`, the multiplication :math:`A \otimes B` is defined as:

.. math::

   [A \otimes B]_{i,j} = \bigoplus_{k=1}^{p} a_{i,k} \otimes b_{k,j}

for :math:`i \in \underline{m}` and :math:`j \in \underline{n}`.

4. Linear Systems over Supertropical Algebra
---------------------------------------------

4.1 Homogeneous and Non-Homogeneous Systems
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

As in ordinary linear algebra, linear systems over supertropical algebra can be classified into **homogeneous systems** and **non-homogeneous systems**. In supertropical algebra, the **ghost surpasses relation** will be used instead of the equality relation :math:`=`.

A homogeneous linear system over supertropical algebra is stated as :math:`A \otimes x \vDash b`. Meanwhile, if :math:`b = \mathcal{E}` where :math:`\mathcal{E}` is a vector whose elements are all :math:`\varepsilon`, then the system :math:`A \otimes x \vDash \mathcal{E}` is called a **homogeneous system** over supertropical algebra.

4.2 Solution Analysis
^^^^^^^^^^^^^^^^^^^^^

As has been explained in max-plus algebra theory, the max-plus algebra structure :math:`\mathbb{R}_{\max} = (\mathbb{R}_{\varepsilon}, \oplus, \otimes)` lacks inverse elements for the :math:`\oplus` operation. In other words, if :math:`a \in \mathbb{R}_{\varepsilon}`, there does not exist :math:`x \in \mathbb{R}_{\varepsilon}` satisfying :math:`a \oplus x = \varepsilon` if and only if :math:`a = \varepsilon`. This limitation makes it difficult to directly solve homogeneous linear systems :math:`A \otimes x = b` in :math:`\mathbb{R}_{\max}`.

As a motivation from the discussion of homogeneous systems in :math:`\mathbb{R}_{\max}`, the solution for non-homogeneous linear systems :math:`A \otimes x \vDash b` will be provided.

4.3 Cramer's Rule
^^^^^^^^^^^^^^^^^

The solution to the system :math:`A \otimes x \vDash b` can be found using **Cramer's rule** in supertropical algebra:

.. math::

   x = \text{adj}(A) \otimes b \otimes (\text{per}(A))^{-1}

where:

- :math:`\text{per}(A)` is the **permanent** (supertropical determinant)
- :math:`\text{adj}(A)` is the **adjoint matrix**
- :math:`(\text{per}(A))^{-1} = -\text{per}(A)` in supertropical algebra

The matrix is **nonsingular** (has unique solution) if :math:`\text{per}(A)` is **tangible** (not ghost).

References
----------

- Izhakian, Z., & Rowen, L. (2010). *Supertropical algebra*. Advances in Mathematics.
- Subiono (2022). *Aljabar Min-Max Plus dan Terapannya*. Departemen Matematika ITS, Surabaya, 22 February 2022.

Implementation Notes
--------------------

This package implements the supertropical semiring with:

- **Tangible elements**: Standard numerical values
- **Ghost elements**: Values marked with the ``is_ghost`` flag, displayed with ╬╜
- **Zero element**: Represented as ``-math.inf``
- **Efficient operations**: Using NumPy arrays for matrix computations

What is Supertropical Algebra?
-------------------------------

Supertropical algebra is an algebraic structure that extends tropical algebra
by introducing **ghost elements**. It provides a framework for solving 
optimization problems and has applications in algebraic geometry, phylogenetics,
and computer science.

Basic Definitions
-----------------

Elements
^^^^^^^^

A supertropical semiring contains two types of elements:

- **Tangible elements**: Regular elements, denoted as :math:`a`
- **Ghost elements**: Special elements marked with :math:`\nu`, denoted as :math:`a^\nu`

The **zero element** is :math:`-\infty` (additive identity).

The **one element** is :math:`0` (multiplicative identity).

Operations
^^^^^^^^^^

**Supertropical Addition** (:math:`\oplus`):

.. math::

   a \oplus b = \begin{cases}
   \max(a, b) & \text{if } a \neq b \\
   a^\nu & \text{if } a = b
   \end{cases}

Rules:

1. :math:`a \oplus b = \max(a, b)` when :math:`a \neq b` (tangible result)
2. :math:`a \oplus a = a^\nu` (becomes ghost)
3. :math:`a \oplus a^\nu = a^\nu` (ghost absorbs tangible of same value)
4. :math:`a^\nu \oplus b^\nu = \max(a, b)^\nu` (ghost addition)

**Supertropical Multiplication** (:math:`\odot`):

.. math::

   a \odot b = a + b

Rules:

1. :math:`a \odot b = a + b` (classical addition)
2. :math:`a \odot b^\nu = (a + b)^\nu` (result is ghost if any operand is ghost)
3. :math:`a^\nu \odot b^\nu = (a + b)^\nu`

Properties
^^^^^^^^^^

- **Associativity**: Both :math:`\oplus` and :math:`\odot` are associative
- **Commutativity**: Both operations are commutative
- **Distributivity**: :math:`a \odot (b \oplus c) = (a \odot b) \oplus (a \odot c)`
- **Idempotency**: :math:`a \oplus a = a^\nu` (not strictly idempotent due to ghost)

Matrix Operations
-----------------

Supertropical Matrix Multiplication
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Given matrices :math:`A` (size :math:`m \times n`) and :math:`B` (size :math:`n \times p`),
the product :math:`C = A \odot B` is:

.. math::

   C_{ij} = \bigoplus_{k=1}^{n} (A_{ik} \odot B_{kj})

This means:

- For each entry: sum over products (using supertropical operations)
- Products use :math:`\odot` (classical addition)
- Sums use :math:`\oplus` (max operation with ghost rules)

Permanent (Supertropical Determinant)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The **permanent** of a square matrix :math:`A` is the supertropical analogue
of the determinant:

.. math::

   \text{per}(A) = \bigoplus_{\pi \in S_n} \bigodot_{i=1}^{n} a_{i,\pi(i)}

where :math:`S_n` is the set of all permutations of :math:`\{1, 2, \ldots, n\}`.

A matrix is **nonsingular** if its permanent is tangible (not ghost).

Linear Systems
--------------

Solving :math:`Ax = b` using Cramer's Rule
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For a nonsingular matrix :math:`A` (permanent is tangible), the solution to
:math:`Ax = b` can be found using:

.. math::

   x = \text{adj}(A) \odot b \odot (\text{per}(A))^{-1}

where:

- :math:`\text{adj}(A)` is the adjoint matrix
- :math:`\text{per}(A)` is the permanent
- :math:`(\text{per}(A))^{-1} = -\text{per}(A)` in supertropical algebra

The adjoint matrix :math:`\text{adj}(A)` has entries:

.. math::

   \text{adj}(A)_{ij} = \text{per}(M_{ji})

where :math:`M_{ji}` is the minor obtained by removing row :math:`j` and column :math:`i`.

Example
^^^^^^^

Consider the system:

.. math::

   \begin{pmatrix} 2 & 1 \\ 1 & 3 \end{pmatrix} x = \begin{pmatrix} 5 \\ 4 \end{pmatrix}

1. Calculate permanent: :math:`\text{per}(A) = (2 + 3) \oplus (1 + 1) = 5 \oplus 2 = 5`
2. Calculate adjoint matrix entries using minors
3. Apply Cramer's formula to find :math:`x`

References
----------

- Izhakian, Z., & Rowen, L. (2010). *Supertropical algebra*. Advances in Mathematics.
- Subiono (2022). *Aljabar Min-Max Plus dan Terapannya*. Departemen Matematika ITS, Surabaya, 22 February 2022.

Implementation Notes
--------------------

This package implements the supertropical semiring with:

- **Tangible elements**: Standard numerical values
- **Ghost elements**: Values marked with the ``is_ghost`` flag, displayed with ╬╜
- **Zero element**: Represented as ``-math.inf``
- **Efficient operations**: Using NumPy arrays for matrix computations
