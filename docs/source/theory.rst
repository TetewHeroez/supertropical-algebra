Supertropical Algebra TheorySupertropical Algebra Theory

========================================================



This page provides comprehensive mathematical background on supertropical algebra, based on the extended semiring tropical framework.This page provides comprehensive mathematical background on supertropical algebra, based on the extended semiring tropical framework.



**For interactive code examples**, see the :doc:`Interactive Examples <examples/index>` section.**For code examples and interactive demonstrations**, see the :doc:`Interactive Examples <examples/index>` section.



1. Supertropical Algebra1. Supertropical Algebra

------------------------------------------------



1.1 Extended Semiring Tropical1.1 Extended Semiring Tropical

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^



As discussed in max-plus algebra, the tropical algebra structure lacks an inverse element for the addition operation ⊕. This limitation is specifically addressed by introducing the **extended semiring tropical** structure, allowing us to solve systems of linear equations.As discussed in max-plus algebra, the tropical algebra structure lacks an inverse element for the addition operation ⊕. This limitation is specifically addressed by introducing the **extended semiring tropical** structure, allowing us to solve systems of linear equations.



Definition 1.1 (Extended Semiring Tropical)Definition 1.1 (Extended Semiring Tropical)

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""



An **extended semiring tropical** is defined as :math:`(T, \oplus, \otimes)` where :math:`T = \mathbb{R} \cup \{-\infty\} \cup \mathbb{R}^\nu`, where :math:`\mathbb{R}` is the set of all real numbers and :math:`\mathbb{R}^\nu = \{a^\nu \mid a \in \mathbb{R}\}`.An **extended semiring tropical** is defined as :math:`(T, \oplus, \otimes)` where :math:`T = \mathbb{R} \cup \{-\infty\} \cup \mathbb{R}^\nu`, where :math:`\mathbb{R}` is the set of all real numbers and :math:`\mathbb{R}^\nu = \{a^\nu \mid a \in \mathbb{R}\}`.



- The **neutral element** for :math:`T` is :math:`\varepsilon \stackrel{\text{def}}{=} -\infty`- The **neutral element** for :math:`T` is :math:`\varepsilon \stackrel{\text{def}}{=} -\infty`

- The **unit element** is :math:`e \stackrel{\text{def}}{=} 0`- The **unit element** is :math:`e \stackrel{\text{def}}{=} 0`



The set :math:`\mathbb{R}_{-\infty} = \mathbb{R} \cup \{-\infty\}` represents the **ideal** of :math:`T`, called the **ideal ghost**. The set :math:`\mathbb{R}_{-\infty} = \mathbb{R} \cup \{-\infty\}` represents the **ideal** of :math:`T`, called the **ideal ghost**. 



Meanwhile, a function :math:`v : T \to \mathbb{R}_{-\infty}` defined by :math:`v(x) \stackrel{\text{def}}{=} x, \forall x \in \mathbb{R}_{-\infty}` represents **tangible identity**, and :math:`v(a) = a^\nu, \forall a \in \mathbb{R}` where element :math:`a^\nu` is called the **element ghost** or **ghost** of :math:`a`. The function :math:`v` is called the **ghost mapping**.Meanwhile, a function :math:`v : T \to \mathbb{R}_{-\infty}` defined by :math:`v(x) \stackrel{\text{def}}{=} x, \forall x \in \mathbb{R}_{-\infty}` represents **tangible identity**, and :math:`v(a) = a^\nu, \forall a \in \mathbb{R}` where element :math:`a^\nu` is called the **element ghost** or **ghost** of :math:`a`. The function :math:`v` is called the **ghost mapping**.



Definition 1.2 (Extended Semiring Tropical Order)Definition 1.2 (Extended Semiring Tropical Order)

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""



Given an **extended semiring tropical** :math:`T`, a **partial order** relation :math:`\prec` is defined on :math:`T` as follows:Given an **extended semiring tropical** :math:`T`, a **partial order** relation :math:`\prec` is defined on :math:`T` as follows:



For any :math:`a, b \in \mathbb{R}`, :math:`a^\nu, b^\nu \in \mathbb{R}^\nu` and :math:`x \in T`:For any :math:`a, b \in \mathbb{R}`, :math:`a^\nu, b^\nu \in \mathbb{R}^\nu` and :math:`x \in T`:



1. :math:`-\infty \prec x, \forall x \in T \setminus \{-\infty\}`1. :math:`-\infty \prec x, \forall x \in T \setminus \{-\infty\}`

2. For any real numbers :math:`a \prec b`, then :math:`a \prec a^\nu, a \prec b^\nu, a^\nu \prec b`, and :math:`a^\nu \prec b^\nu`2. For any real numbers :math:`a \prec b`, then :math:`a \prec a^\nu, a \prec b^\nu, a^\nu \prec b`, and :math:`a^\nu \prec b^\nu`

3. :math:`a \prec a^\nu` for any :math:`a \in \mathbb{R}`3. :math:`a \prec a^\nu` for any :math:`a \in \mathbb{R}`



Axiom 1.1 (Extended Semiring Tropical Operations)Axiom 1.1 (Extended Semiring Tropical Operations)

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""



Given an extended semiring tropical :math:`T`, the operations :math:`\oplus` (max) and :math:`\otimes` (addition) on :math:`T` satisfy the following axioms.Given an extended semiring tropical :math:`T`, the operations :math:`\oplus` (max) and :math:`\otimes` (addition) on :math:`T` satisfy the following axioms.



For any :math:`a, b \in \mathbb{R}`, :math:`a^\nu, b^\nu \in \mathbb{R}^\nu` and :math:`x, y \in T`:For any :math:`a, b \in \mathbb{R}`, :math:`a^\nu, b^\nu \in \mathbb{R}^\nu` and :math:`x, y \in T`:



1. :math:`-\infty \oplus x = x \oplus -\infty = x, \forall x \in T`1. :math:`-\infty \oplus x = x \oplus -\infty = x, \forall x \in T`

2. :math:`x \oplus y = \max_{\prec} \{x, y\}` provided :math:`x \neq y`2. :math:`x \oplus y = \max_{\prec} \{x, y\}` provided :math:`x \neq y`

3. :math:`a \oplus a = a^\nu \oplus a^\nu = a \oplus a^\nu = a^\nu \oplus a = a^\nu`3. :math:`a \oplus a = a^\nu \oplus a^\nu = a \oplus a^\nu = a^\nu \oplus a = a^\nu`

4. :math:`-\infty \otimes x = x \otimes -\infty = -\infty`4. :math:`-\infty \otimes x = x \otimes -\infty = -\infty`

5. :math:`a \otimes b = a + b` (classical addition)5. :math:`a \otimes b = a + b` (classical addition)

6. :math:`a^\nu \otimes b = a \otimes b^\nu = a^\nu \otimes b^\nu = (a + b)^\nu`6. :math:`a^\nu \otimes b = a \otimes b^\nu = a^\nu \otimes b^\nu = (a + b)^\nu`



**Example 1.1**: Operations in extended semiring tropical :math:`T`:**Example 1.1**: Operations in extended semiring tropical :math:`T`:



1. :math:`-\infty \oplus 4 = 4 \oplus -\infty = 4`1. :math:`-\infty \oplus 4 = 4 \oplus -\infty = 4`

2. :math:`-2 \oplus 7 = \max_{\prec} \{-2, 7\} = 7`2. :math:`-2 \oplus 7 = \max_{\prec} \{-2, 7\} = 7`

3. :math:`8 \oplus 8 = 8^\nu \oplus 8^\nu = 8 \oplus 8^\nu = 8^\nu \oplus 8 = 8^\nu`3. :math:`8 \oplus 8 = 8^\nu \oplus 8^\nu = 8 \oplus 8^\nu = 8^\nu \oplus 8 = 8^\nu`

4. :math:`-\infty \otimes 3 = 3 \otimes -\infty = -\infty`4. :math:`-\infty \otimes 3 = 3 \otimes -\infty = -\infty`

5. :math:`6 \otimes 9 = 6 + 9 = 15`5. :math:`6 \otimes 9 = 6 + 9 = 15`

6. :math:`7^\nu \otimes 8 = 7 \otimes 8^\nu = 7^\nu \otimes 8^\nu = (7 + 8)^\nu = 15^\nu`6. :math:`7^\nu \otimes 8 = 7 \otimes 8^\nu = 7^\nu \otimes 8^\nu = (7 + 8)^\nu = 15^\nu`



2. Ghost Surpasses Relation2. Ghost Surpasses Relation

--------------------------------------------------------



2.1 Definition2.1 Definition

^^^^^^^^^^^^^^^^^^^^^^^^^^^^



In supertropical semiring :math:`R`, for any :math:`a \in R`, then :math:`a \oplus a = -\infty` only holds when :math:`a = -\infty`. However, for any :math:`a \in T` then :math:`a \oplus a = a^\nu` and for any :math:`x \in G` then :math:`x \oplus x = x`. Therefore, a **ghost surpasses** relation in :math:`R` will be introduced as follows.In supertropical semiring :math:`R`, for any :math:`a \in R`, then :math:`a \oplus a = -\infty` only holds when :math:`a = -\infty`. However, for any :math:`a \in T` then :math:`a \oplus a = a^\nu` and for any :math:`x \in G` then :math:`x \oplus x = x`. Therefore, a **ghost surpasses** relation in :math:`R` will be introduced as follows.



Definition 2.1 (Ghost Surpasses Relation)Definition 2.1 (Ghost Surpasses Relation)

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""



Given a supertropical semiring :math:`R`, a relation :math:`\vDash` is called a **ghost surpasses** relation in :math:`R` defined as:Given a supertropical semiring :math:`R`, a relation :math:`\vDash` is called a **ghost surpasses** relation in :math:`R` defined as:



.. math::.. math::



   x \vDash y \quad \text{if} \quad x = y \oplus z \quad \text{for some} \quad z \in \mathcal{G}_0   x \vDash y \quad \text{if} \quad x = y \oplus z \quad \text{for some} \quad z \in \mathcal{G}_0



where :math:`\mathcal{G}_0` is the set of ghost elements.where :math:`\mathcal{G}_0` is the set of ghost elements.



**Example 2.1**: Ghost surpasses relation in supertropical semiring :math:`R`:**Example 2.1**: Ghost surpasses relation in supertropical semiring :math:`R`:



1. For :math:`9, 10^\nu \in R`, we have :math:`10^\nu \vDash 9` because :math:`10^\nu = 9 \oplus 10^\nu`. Here, :math:`z = 10^\nu` is a value in :math:`\mathcal{G}_0` satisfying :math:`10^\nu = 9 \oplus 10^\nu`.1. For :math:`9, 10^\nu \in R`, we have :math:`10^\nu \vDash 9` because :math:`10^\nu = 9 \oplus 10^\nu`. Here, :math:`z = 10^\nu` is a value in :math:`\mathcal{G}_0` satisfying :math:`10^\nu = 9 \oplus 10^\nu`.



2. For :math:`-5 \in R`, we have :math:`-5^\nu \vDash -5` because :math:`-5^\nu = -5 \oplus z` for some ghost :math:`z \prec -5`. For example, :math:`z = -6^\nu` and :math:`z = -7.5^\nu`. Notice that there are many values of :math:`z \in \mathcal{G}_0` satisfying :math:`-5^\nu = -5 \oplus z`.2. For :math:`-5 \in R`, we have :math:`-5 \vDash -5` because :math:`-5 = -5 \oplus \varepsilon`. Here, :math:`z = \varepsilon \in \mathcal{G}_0` with :math:`z \neq \varepsilon` satisfying :math:`-5 = -5 \oplus z` is :math:`z \prec -5`. For example, :math:`z = -6^\nu` and :math:`z = -7.5^\nu`. Notice that there are many values of :math:`z \in \mathcal{G}_0` satisfying :math:`-5 = -5 \oplus z` other than :math:`z \prec -5`.



3. Meanwhile, for :math:`7, 6 \in R`, we have :math:`7 \nvDash 6` because the value of :math:`z` satisfying :math:`7 = 6 \oplus z` is only :math:`z = 7 \notin \mathcal{G}_0`.3. Meanwhile, for :math:`7, 6 \in R`, we have :math:`7 \nvDash 6` because the value of :math:`z` satisfying :math:`7 = 6 \oplus z` is only :math:`z = 7 \notin \mathcal{G}_0`.



3. Supertropical Matrices2.2 Python Implementation

--------------------------^^^^^^^^^^^^^^^^^^^^^^^^^



3.1 Matrix OperationsThe ``ghost_surpasses()`` method checks if one element ghost-surpasses another:

^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

The set of all :math:`m \times n` matrices over supertropical semiring is denoted as :math:`M_{m \times n}(R)`, where matrix elements are members of :math:`R`. When the dimension of a matrix is square, denoted as :math:`M_n(R)`, the binary operations ⊕ and ⊗ in :math:`R` can be extended to matrix operations in :math:`M_n(R)`. Furthermore, the ghost surpasses relation in :math:`R` can also be extended to matrices in :math:`M_n(R)`.

   import supertropical as suptrop

If :math:`A \vDash B` then :math:`a_{i,j} \vDash b_{i,j}` for any :math:`i` and :math:`j` in :math:`\underline{n}`.

   # Example 1: 10ν ⊨ 9

**Matrix Addition**   x = suptrop.Element(10, is_ghost=True)  # 10ν

   y = suptrop.Element(9)                   # 9

For matrices :math:`A, B \in M_{m \times n}(R)`, the addition :math:`A \oplus B` is defined as:   print(f"{x} ⊨ {y}: {x.ghost_surpasses(y)}")  # True



.. math::   # Example 2: -5 ⊨ -5

   a = suptrop.Element(-5)

   [A \oplus B]_{i,j} = a_{i,j} \oplus b_{i,j}   print(f"{a} ⊨ {a}: {a.ghost_surpasses(a)}")  # False (same tangible)

   

for :math:`i \in \underline{m}` and :math:`j \in \underline{n}`.   # But -5ν ⊨ -5

   a_ghost = suptrop.Element(-5, is_ghost=True)

**Matrix Multiplication**   print(f"{a_ghost} ⊨ {a}: {a_ghost.ghost_surpasses(a)}")  # True



For matrix :math:`A \in M_{m \times p}(R)` and :math:`B \in M_{p \times n}(R)`, the multiplication :math:`A \otimes B` is defined as:   # Example 3: 7 ⊭ 6

   x = suptrop.Element(7)

.. math::   y = suptrop.Element(6)

   print(f"{x} ⊨ {y}: {x.ghost_surpasses(y)}")  # False

   [A \otimes B]_{i,j} = \bigoplus_{k=1}^{p} a_{i,k} \otimes b_{k,j}

3. Supertropical Matrices

for :math:`i \in \underline{m}` and :math:`j \in \underline{n}`.--------------------------



3.2 Advanced Matrix Operations3.1 Matrix Operations

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^



**Matrix Transpose**The set of all :math:`m \times n` matrices over supertropical semiring is denoted as :math:`M_{m \times n}(R)`, where matrix elements are members of :math:`R`. When the dimension of a matrix is square, denoted as :math:`M_n(R)`, the binary operations ⊕ and ⊗ in :math:`R` can be extended to matrix operations in :math:`M_n(R)`. Furthermore, the ghost surpasses relation in :math:`R` can also be extended to matrices in :math:`M_n(R)`.



For matrix :math:`A`, the transpose :math:`A^T` is defined as:If :math:`A \vDash B` then :math:`a_{i,j} \vDash b_{i,j}` for any :math:`i` and :math:`j` in :math:`\underline{n}`.



.. math::**Matrix Addition**



   [A^T]_{i,j} = A_{j,i}For matrices :math:`A, B \in M_{m \times n}(R)`, the addition :math:`A \oplus B` is defined as:



**Matrix Power**.. math::



For matrix :math:`A` and positive integer :math:`k`:   [A \oplus B]_{i,j} = a_{i,j} \oplus b_{i,j}



.. math::for :math:`i \in \underline{m}` and :math:`j \in \underline{n}`.



   A^k = \underbrace{A \otimes A \otimes \cdots \otimes A}_{k \text{ times}}**Matrix Multiplication**



**Identity Matrix**For matrix :math:`A \in M_{m \times p}(R)` and :math:`B \in M_{p \times n}(R)`, the multiplication :math:`A \otimes B` is defined as:



The identity matrix :math:`I_n` is defined as:.. math::



.. math::   [A \otimes B]_{i,j} = \bigoplus_{k=1}^{p} a_{i,k} \otimes b_{k,j}



   [I]_{i,j} = \begin{cases} for :math:`i \in \underline{m}` and :math:`j \in \underline{n}`.

   0 & \text{if } i = j \\ 

   -\infty^\nu & \text{if } i \neq j 3.2 Python Implementation

   \end{cases}^^^^^^^^^^^^^^^^^^^^^^^^^



**Pseudo-Zero Matrix****Creating Matrices**:



The pseudo-zero matrix :math:`Z_G` has all entries equal to :math:`-\infty^\nu` (ghost)... code-block:: python



3.3 Permanent (Supertropical Determinant)   import supertropical as suptrop

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   # Create a 2×2 matrix

The **permanent** of matrix :math:`A` is the supertropical analog of determinant:   A = suptrop.Matrix([[2, 1], 

                       [1, 3]])

.. math::   print("Matrix A:")

   print(A)

   \text{per}(A) = \bigoplus_{\sigma \in S_n} \bigotimes_{i=1}^{n} a_{i,\sigma(i)}

   # Create matrix with ghost elements

where :math:`S_n` is the set of all permutations of :math:`\{1, 2, \ldots, n\}`.   ghost_elem = suptrop.Element(4, is_ghost=True)

   B = suptrop.Matrix([[5, ghost_elem], 

**Properties**:                       [2, 1]])

   print("\nMatrix B (with ghost):")

- If :math:`\text{per}(A)` is **tangible** → matrix is **nonsingular**   print(B)

- If :math:`\text{per}(A)` is **ghost** → matrix is **singular**

**Matrix Addition**:

3.4 Pseudo-Inverse

^^^^^^^^^^^^^^^^^^.. code-block:: python



The **pseudo-inverse** :math:`A^\nabla` of matrix :math:`A` is defined as:   # Element-wise max operation

   C = A + B

.. math::   print("A ⊕ B:")

   print(C)

   A^\nabla = (\text{per}(A))^{-1} \otimes \text{adj}(A)

**Matrix Multiplication**:

where :math:`a^{-1} = -a` in max-plus algebra (inverse element).

.. code-block:: python

**Properties**:

   # Supertropical matrix multiplication

1. :math:`A \otimes A^\nabla \otimes A = A` (weak inverse property)   C = A * B

2. :math:`A^\nabla \otimes A \otimes A^\nabla = A^\nabla`   print("A ⊗ B:")

3. If :math:`\text{per}(A)` is tangible, then :math:`A^\nabla` provides a unique solution structure   print(C)



4. Linear Systems over Supertropical Algebra**Matrix Transpose**:

---------------------------------------------

.. code-block:: python

4.1 Homogeneous and Non-Homogeneous Systems

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^   # Transpose: [A^T]_ij = A_ji

   A_T = A.transpose()

As in ordinary linear algebra, linear systems over supertropical algebra can be classified into **homogeneous systems** and **non-homogeneous systems**. In supertropical algebra, the **ghost surpasses relation** will be used instead of the equality relation :math:`=`.   print("A^T:")

   print(A_T)

A linear system over supertropical algebra is stated as :math:`A \otimes x \vDash b`. Meanwhile, if :math:`b = \mathcal{E}` where :math:`\mathcal{E}` is a vector whose elements are all :math:`\varepsilon`, then the system :math:`A \otimes x \vDash \mathcal{E}` is called a **homogeneous system** over supertropical algebra.

**Matrix Power**:

4.2 Solution Analysis

^^^^^^^^^^^^^^^^^^^^^.. code-block:: python



As has been explained in max-plus algebra theory, the max-plus algebra structure :math:`\mathbb{R}_{\max} = (\mathbb{R}_{\varepsilon}, \oplus, \otimes)` lacks inverse elements for the :math:`\oplus` operation. In other words, if :math:`a \in \mathbb{R}_{\varepsilon}`, there does not exist :math:`x \in \mathbb{R}_{\varepsilon}` satisfying :math:`a \oplus x = \varepsilon` if and only if :math:`a = \varepsilon`. This limitation makes it difficult to directly solve homogeneous linear systems :math:`A \otimes x = b` in :math:`\mathbb{R}_{\max}`.   # Matrix exponentiation: A^k = A * A * ... * A

   A_squared = A ** 2

As a motivation from the discussion of homogeneous systems in :math:`\mathbb{R}_{\max}`, the solution for non-homogeneous linear systems :math:`A \otimes x \vDash b` will be provided.   print("A^2:")

   print(A_squared)

4.3 Cramer's Rule

^^^^^^^^^^^^^^^^^   A_cubed = A ** 3

   print("A^3:")

The solution to the system :math:`A \otimes x \vDash b` can be found using **Cramer's rule** in supertropical algebra:   print(A_cubed)



.. math::**Special Matrices**:



   x = \text{adj}(A) \otimes b \otimes (\text{per}(A))^{-1}.. code-block:: python



where:   # Identity matrix: [I]_ij = 0 if i=j, -∞ν otherwise

   I = suptrop.Matrix.identity(3)

- :math:`\text{per}(A)` is the **permanent** (supertropical determinant)   print("Identity matrix:")

- :math:`\text{adj}(A)` is the **adjoint matrix**   print(I)

- :math:`(\text{per}(A))^{-1} = -\text{per}(A)` in supertropical algebra

   # Pseudo-zero matrix: all entries are -∞ν (ghost)

The matrix is **nonsingular** (has unique solution) if :math:`\text{per}(A)` is **tangible** (not ghost).   Z_G = suptrop.Matrix.pseudo_zero(3)

   print("Pseudo-zero matrix:")

**Solution Steps**:   print(Z_G)



1. Calculate :math:`\text{per}(A)` to check nonsingularity**Permanent (Supertropical Determinant)**:

2. If :math:`\text{per}(A)` is tangible, calculate :math:`\text{adj}(A)`

3. Apply Cramer's rule: :math:`x = \text{adj}(A) \otimes b \otimes (-\text{per}(A))`.. code-block:: python

4. Verify: :math:`A \otimes x \vDash b`

   # Calculate permanent

References   perm_A = A.permanent()

----------   print(f"Permanent of A: {perm_A}")

   print(f"Is tangible (nonsingular)? {perm_A.is_tangible()}")

- Izhakian, Z., & Rowen, L. (2010). *Supertropical algebra*. Advances in Mathematics.

- Subiono (2022). *Aljabar Min-Max Plus dan Terapannya*. Departemen Matematika ITS, Surabaya, 22 February 2022.**Pseudo-Inverse**:



Implementation Notes.. code-block:: python

--------------------

   # Calculate A^♯ (pseudo-inverse)

This package implements the supertropical semiring with:   A_sharp = A.pseudo_inverse()

   print("A^♯:")

- **Tangible elements**: Standard numerical values   print(A_sharp)

- **Ghost elements**: Values marked with the ``is_ghost`` flag, displayed with ν

- **Zero element**: Represented as ``-math.inf``4. Linear Systems over Supertropical Algebra

- **Efficient operations**: Using NumPy arrays for matrix computations---------------------------------------------



**For interactive code examples with execution output**, see:4.1 Homogeneous and Non-Homogeneous Systems

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- :doc:`examples/01_supertropical_elements` - Elements and basic operations

- :doc:`examples/02_ghost_surpasses` - Ghost surpasses relationAs in ordinary linear algebra, linear systems over supertropical algebra can be classified into **homogeneous systems** and **non-homogeneous systems**. In supertropical algebra, the **ghost surpasses relation** will be used instead of the equality relation :math:`=`.

- :doc:`examples/03_matrices` - Matrix operations and permanent

- :doc:`examples/04_linear_systems` - Solving linear systems with Cramer's ruleA homogeneous linear system over supertropical algebra is stated as :math:`A \otimes x \vDash b`. Meanwhile, if :math:`b = \mathcal{E}` where :math:`\mathcal{E}` is a vector whose elements are all :math:`\varepsilon`, then the system :math:`A \otimes x \vDash \mathcal{E}` is called a **homogeneous system** over supertropical algebra.


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

4.4 Python Implementation
^^^^^^^^^^^^^^^^^^^^^^^^^

**Solving Linear Systems**:

.. code-block:: python

   import supertropical as suptrop

   # Define system: A ⊗ x ⊨ b
   A = suptrop.Matrix([[2, 1], 
                       [1, 3]])
   b = suptrop.Matrix([[5], 
                       [4]])

   print("System to solve:")
   print(f"A =\n{A}")
   print(f"\nb =\n{b}")

   # Solve the system using Cramer's rule
   x = A.solve(b)
   print("\nSolution x:")
   print(x)

**Verifying Solution**:

.. code-block:: python

   # Verify: A ⊗ x should ghost-surpass b
   result = A * x
   print("\nVerification A ⊗ x:")
   print(result)
   print(f"\nOriginal b:")
   print(b)

**Larger System Example**:

.. code-block:: python

   # 3×3 system
   A3 = suptrop.Matrix([[1, 2, 0],
                        [0, 1, 2],
                        [2, 0, 1]])
   b3 = suptrop.Matrix([[5],
                        [4],
                        [6]])

   print("3×3 System:")
   print(f"A =\n{A3}")
   print(f"\nb =\n{b3}")

   # Check if matrix is nonsingular
   perm3 = A3.permanent()
   print(f"\nPermanent: {perm3}")

   if perm3.is_tangible():
       x3 = A3.solve(b3)
       print(f"\nSolution:\n{x3}")
   else:
       print("Matrix is singular (permanent is ghost)")

**Complete Example**:

.. code-block:: python

   import supertropical as suptrop

   # System setup
   A = suptrop.Matrix([[2, 1], [1, 3]])
   b = suptrop.Matrix([[5], [4]])

   # Calculate permanent (check nonsingularity)
   perm = A.permanent()
   print(f"Permanent: {perm}")
   print(f"Is nonsingular: {perm.is_tangible()}")

   # Calculate adjoint
   adj_A = A.adjoint()
   print(f"\nAdjoint:\n{adj_A}")

   # Solve system
   x = A.solve(b)
   print(f"\nSolution:\n{x}")

   # Verify solution
   verification = A * x
   print(f"\nVerification A ⊗ x:\n{verification}")
   print(f"Original b:\n{b}")

References
----------

- Izhakian, Z., & Rowen, L. (2010). *Supertropical algebra*. Advances in Mathematics.
- Subiono (2022). *Aljabar Min-Max Plus dan Terapannya*. Departemen Matematika ITS, Surabaya, 22 February 2022.

Implementation Notes
--------------------

This package implements the supertropical semiring with:

- **Tangible elements**: Standard numerical values
- **Ghost elements**: Values marked with the ``is_ghost`` flag, displayed with ν
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
- **Ghost elements**: Values marked with the ``is_ghost`` flag, displayed with ν
- **Zero element**: Represented as ``-math.inf``
- **Efficient operations**: Using NumPy arrays for matrix computations
