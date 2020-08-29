# Introduction to <br>Linear Algebra (Part 1)

<center>

![image](Figures/LA_video.png)

</center>

*Note*: The [*Essence of Linear Algebra*][link] video series (by Grant Sanderson, a.k.a. 3Blue1Brown) really helps when learning the mathematical concepts involved in this material.

[link]: https://youtu.be/fNk_zzaMoSs

## Vector Spaces and Basis Vectors

### Vector Spaces

For the purpose of an introductory physics course, a **vector space** (denoted by $V$) can be regarded as the usual plane (2D) or space (3D), and **vectors** are like arrows in the plane or the space. 

We can perform the following operations on vectors:

- **Addition** of vectors

- **Scalar multiplication** on a vector (by real numbers)

Later in your life you will have to deal with **complex numbers**, but now we restrict ourselves to the real world.

I will not show the general mathematical definition, which can be found on [Wikipedia][vec_space] or in any textbook on linear algebra (I personally recommend Chapter 7 and 8 of *Mathematical Methods for Physics and Engineering* by Riley, Hobson and Bence).

[vec_space]: https://en.wikipedia.org/wiki/Vector_space

### Basis Vectors

Each "**finite-dimensional**" vector space have a set of **basis vectors** $\{e_1,...,e_n\}$, so that any vector $v\in V$ can be *uniquely* represented as

$$
v = \sum_{i=1}^{n} v_i e_i
\qquad v_1,...,v_n\in \mathbb{R}
$$

The number of basis vectors $n$ is called the **dimension** of $V$ (denoted by $\dim V$). 

The number $v_i$ is called the **components** of the vector $v$ along the basis vector $e_i$. Then the vector $v$ can be also written as a **column vector** (without explicit reference to the basis vectors)

$$
v = \begin{bmatrix}
    v_1 \\ \vdots \\ v_n
\end{bmatrix}
$$

The choice of basis vectors is *not unique*: any set of **linearly-independent** $\dim{V}$ vectors can be used as basis vectors. By "linearly-independent", we mean that 

$$
\sum_{i=1}^n v_i e_i = 0 
\, \Leftrightarrow \,
v_1 = \cdots = v_n = 0
$$

*Remark*: the components of the $i$th basis vector are simply given by

$$
v_i = 1 , \quad \text{other components} = 0
$$

e.g. for $\dim{V} = 2$, we have

$$
e_1 = \begin{bmatrix}
    1 \\ 0
\end{bmatrix}, \quad
e_2 = \begin{bmatrix}
    0 \\ 1
\end{bmatrix}
$$

You must be aware that **this does not mean that they are the traditional unit vectors along the $x$, $y$, ... axes**. 

### Note on Notations: Einstein Summation Rule

People are tired of always writing the summation sign $\sum$. Thus the genius Einstein invented the following rule: 

<center>

**If an index appears twice, then sum over it.**

</center>

which allows people to throw away the summation signs. For example:

$$
\sum_i v_i e_i \to v_i e_i
$$

The index $i$ appears twice, thus we should sum over $i$. Unless there might be some ambiguity, we shall always adopt the Einstein summation rule in the following. 

In addition, we are free to choose which letter represents the index to be summed over:

$$
\sum_i v_i e_i = \sum_j v_j e_j  = \cdots
\, \Rightarrow \,
v_i e_i = v_j e_j = \cdots
$$

### Inner Product 

For two vectors $u,v\in V$, we can define an operation called the **inner product** (denoted by $u \cdot v$), which send two vectors *to a real number*: (below is the mathematical description of the same thing)

$$
\_ \cdot \_ : V \times V \to \mathbb{R}
$$

and have the following properties:

- **Symmetry**: $\forall \, u,v \in V$

    $$
    u \cdot v = v \cdot u
    $$

- **Linearity in the second argument**: $\forall \, u,v,w \in V ;\, \alpha,\beta \in \mathbb{R}$
    
    $$
    u \cdot (\alpha v + \beta w) 
    = \alpha (u \cdot v) + \beta(u \cdot w)
    $$

The two properties combined gives linearity in the first argument, too (show this by yourself; thus we say that the inner product is a **bi-linear** function):

$$
(\alpha v + \beta w) \cdot u
= \alpha (v \cdot u) + \beta(w \cdot u)
$$

*Remark*: Some concepts derived from the inner product

- Two vectors are said to be **orthogonal** to each other if their inner product is 0.
- The **length** of a vector $v$ is defined as $\sqrt{v \cdot v}$. 

### Orthonormal Basis Vectors

Until now we have not described how to really calculate the inner product. For two vectors $u,v \in V$

$$
u = u_i e_i, \quad v = v_i e_i
$$

Due to bi-liearity of inner product, $u \cdot v$ can be reduced to the linear combination of the inner product of basis vectors:

$$
u \cdot v = u_i v_j (e_i \cdot e_j)
$$

The numbers $e_i \cdot e_j$ are still undetermined, and depends on both the choice of basis vectors, which is *not unique*. Now we pick a *special* choice of basis vectors such that

$$
e_i \cdot e_j = \delta_{ij} 
= \begin{cases}
    1 & i = j \\
    0 & i \ne j
\end{cases}
$$

i.e. each basis vector has length 1, and is orthogonal to all other basis vectors. You can just imagine them as the unit vector along the $x$, $y$-axes. Such a set of basis vectors is called an **orthonormal basis**.

Then we recover something you already know:

$$
u \cdot v = u_i v_j \delta_{ij} = u_i v_i
$$

We emphasize that this definition is valid only when we are using the components of $u,v$ under an orthonormal set of basis.

## Linear Transformations

A **linear transformation** (denoted by $A$) on a $V$ maps a vector $u \in V$ to another vector $v = Au \in V$:

$$
A: V \to V
$$

The transformation must satisfy the following two *defining* requirements (called the **linearity conditions**):

- $\forall \, u, v\in V \quad A(u + v)=A u + A v$

- $\forall \, v\in V, c\in \mathbb{C} \quad A(c u) = c (A u)$

In other words, it does not matter whether you perform linear transformations before or after vector addition and scalar multiplication. 

### Matrix Representation of Linear Transformations

Due to the linearity, a linear transformation $A$ can be *fully* described by specifying its action $e_i \to A e_i$ on *each* basis vector ($i = 1, ..., n$). Then for any vector $v$, we have

$$
A v = A (v_i e_i) = v_i (A e_i)
$$

Nothing prevents us to express $A e_i$ as linear combination of the basis vectors: 

$$
e'_i = A e_i = e_j A_{j i} \qquad (i = 1, ..., n)
$$

The numbers $A_{j i}$ are linear combination coefficients. We do not write $A_{i j} e_j$, which is just a matter of convention. 

For example, when $\dim{V} = 2$:

$$
\begin{aligned}
    e'_1 &= A e_1 = A_{11} e_1 + A_{21} e_2
    = \begin{bmatrix}
        A_{11} \\ A_{21}
    \end{bmatrix}
    \\
    e'_2 &= A e_2 = A_{12} e_1 + A_{22} e_2
    =\begin{bmatrix}
        A_{12} \\ A_{22}
    \end{bmatrix}
\end{aligned}
$$

Then we combine this two column vectors to form a **matrix** that represents the linear transformation $A$:

$$
A = \begin{bmatrix}
    A_{11} & A_{12} \\
    A_{21} & A_{22}
\end{bmatrix} \quad
\text{(under the basis $\{e_1, e_2\}$)}
$$

In this construction, $A_{i j}$ means the matrix element at the $i$th row and the $j$th column.

Remember the meaning of each column of the transformation matrix: **the $i$th column is the transformation result of the $i$th basis vector**. 

### Examples of Linear Transformations (in 2D)

- **Rotation**

- **Reflection**

- **Scaling (Dilation)**

*Remark*: **Translation** ($T: v \to v + t$, where $t$ is the translation vector) is not a linear transformation! You can easily verify, for two vectors $v, w \in V$

$$
\left.
\begin{aligned}
    T (v + w) &= (v + w) + t
    \\
    T v + T w &= (v + w) + 2t
\end{aligned}
\right\} \Rightarrow
T(v + w) \ne Tv + Tw
$$

You can read [this Wikipedia entry][affine_trans] to see how to use matrices *in $(d+1)$ dimension* to represent $d$-dimensional translations. 

[affine_trans]: https://en.wikipedia.org/wiki/Affine_transformation#Representation

## Matrix-Vector Multiplication

Using the linearity $A$, we can find the new vector $A v$ to which the vector $v$ is sent by the linear transformation $A$: 

$$
\begin{aligned}
    v' &= Av = A(v_j e_j) = v_j (A e_j)
    \\
    &= v_j (e_i A_{i j}) = (A_{i j} v_j) e_i
\end{aligned}
$$

Therefore, the components of $A v$ are given by

$$
(A v)_i = A_{i j} v_j
$$

This is *defined* as the rule of the multiplication of matrix $A$ and column vector $v$.

For example, when $\dim{V} = 2$:

$$
A v =
\begin{bmatrix}
    A_{11} & A_{12} \\
    A_{21} & A_{22}
\end{bmatrix}
\begin{bmatrix}
    v_1 \\
    v_2
\end{bmatrix}
= \begin{bmatrix}
    A_{11} v_1 + A_{12} v_2 \\
    A_{21} v_1 + A_{22} v_2
\end{bmatrix}
$$

### EXERCISE

<center>

![image](Figures/Mat_on_vec.png)

</center>

Compute the components of $A v$ when

$$
A = \begin{bmatrix}
    3 & 1 \\
    1 & 2
\end{bmatrix} \quad
v = \begin{bmatrix}
    -1 \\ 2
\end{bmatrix}
$$

## Matrix Product

Suppose we have two linear transformations $A, B$. We first apply $B$ onto a vector $v$, then apply $A$. The result is

$$
\begin{aligned}
    [A (B v)]_{i}
    = A_{i j} (B v)_{j}
    = A_{i j} (B_{j k} v_k)
    = A_{i j} B_{j k} v_k
\end{aligned}
$$

We discover that if we define a new matrix $C$ by

$$
C_{i k} \equiv A_{i j} B_{j k}
$$

We obtain

$$
[A(B v)]_i = C_{ik} v_k
$$

This means that *$C$ is the representation matrix of the combined transformation $AB$*. Thus we define that the **product** of the representation matrices $A, B$ is given by

$$
(AB)_{i k} \equiv A_{i j} B_{j k}
$$

For example, when $\dim{V} = 2$

$$
AB = \begin{bmatrix}
    A_{11} B_{11} + A_{12} B_{21} & A_{11} B_{12} + A_{12} B_{22} \\
    A_{21} B_{11} + A_{22} B_{21} & A_{21} B_{12} + A_{22} B_{22}
\end{bmatrix}
$$

### EXERCISE

The matrix product defined in this way has the following properties:

- **Associativity**: $(AB)C = A(BC)$
- **Non-commutativity**: In general $AB \ne BA$

Please prove (or verify) them. 

