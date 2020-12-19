# Eigenvalues and Eigenvectors of Grassmann Tensors

In ordinary linear algebra, the eigenvalues and eigenvectors belong to *matrices*: they are defined by

$$
T v = \lambda v \, 
\xrightarrow{\text{Components}} \,
T_{i j} v_j = \lambda v_i
$$


The generalization to tensors means that we first merge axes of the tensor to make it become a matrix, then we talk about the eigenvalues and eigenvectors of this matrix. 

Thus we first discuss the eigenvalues and eigenvectors of a Grassmann *matrix*.

## Grassmann Matrix 

A **Grassmann matrix** is a special kind of Grassmann tensor of only 2 axes. For a Grassmann matrix $\mathbf{T}_{i j}^{m n}$, its eigenvalues and eigenvectors are obtained by solving

$$
\mathbf{T}\mathbf{v} = \lambda \mathbf{v}
$$

where $\lambda \in \mathbb{C}$ and $\mathbf{v}$ is a **Grassmann vector** (i.e. Grassmann tensor with only one axis). The expression $\mathbf{T}\mathbf{v}$ means the *contraction* of the *second* axis of $\mathbf{T}$ with $\mathbf{v}$.

Graphically (with $g = +1$):

```
    0---T---1 → 0---v = λ ( 0---v )
```

First we notice that **an odd-parity Grassmann matrix cannot have eigenvalues and eigenvectors** as defined above. This can be seen by checking parity of both sides:

$$
P(\mathbf{T} \mathbf{v}) = P(\mathbf{T}) + P(\mathbf{v})
\overset{!}{=} P(\mathbf{v})
$$

Therefore $P(\mathbf{T})$ can only be zero. 

### Reduction to Ordinary Matrix Equation

We write down the components of $\mathbf{T}\mathbf{v} = \lambda \mathbf{v}$ explicitly (omitting the common string of Grassmann variables):

$$
\begin{aligned}
    \sum_{j, n} g_{21}^n T_{i j}^{m n} v_j^n
    = \lambda v_i^m 
\end{aligned}
$$

where $g_{21}$ is the Grassmann metric for the contraction of the 2nd axis of $T$ and the 1st axis of $v$. But we know that if $g_{21} = -1$, we can use the function `flip_gSign` to change it to $+1$, i.e. redefine the matrix $T$ to

$$
\tilde{T}_{i j}^{m n} = (-1)^n T_{i j}^{m n}
$$

From now on, we shall always assume that the contraction metric is $+1$ (represented by an arrow from $T$ to $v$ on diagrams). Then

$$
\sum_{j,n} T_{i j}^{m n} v_j^n = \lambda v_i^m
$$

But $T$ is of even-parity, therefore we can separate the equation above to two nonzero sectors (sum over $j$ is implied):

$$
\begin{aligned}
    &\text{when $v$ is of even-parity: }
    &T_{i j}^{0 0} v_j^0 = \lambda v_i^0
    \\
    &\text{when $v$ is of odd-parity: }
    &T_{i j}^{1 1} v_j^1 = \lambda v_i^1
\end{aligned}
$$

Thus we conclude that **a (square) Grassmann matrix has two spectrums of eigenvalues, belonging to the ordinary matrices $T^{00}, T^{11}$. The corresponding eigenvectors are of even-parity and odd-parity, respectively**.

### Eigenvectors on the Left

In ordinary linear algebra, after obtaining $T v = \lambda v$, we can transpose (or take Hermitian conjugate) the equation to obtain

$$
v^\top T^\top = \lambda v^\top \quad
\text{or} \quad
v^\dagger T^\dagger = \lambda^* v^\dagger
$$

For Grassmann tensors, we can take the **Grassmann conjugate** of the eigenvalue equation to obtain

$$
(\mathbf{T} \mathbf{v})^\dagger 
= \mathbf{v}^\dagger \mathbf{T}^\dagger
= \lambda^* \mathbf{v}^\dagger
$$

where $\mathbf{v}^\dagger \mathbf{T}^\dagger$ means the contraction of $\mathbf{v}^\dagger$ and the 1st axis of $\mathbf{T}^\dagger$, with Grassmann metric $+1$ (represented by an arrow from $\mathbf{v}^\dagger$ to $\mathbf{T}^\dagger$). 

Graphically (with $g = +1$):

```
    v†--0 → 0---T†--1 = λ* ( v†--0 )
```

Let us verify this by writing down the components of $\mathbf{v}^\dagger \mathbf{T}^\dagger = \lambda^* \mathbf{v}^\dagger$:

$$
\sum_{j,n} (v^\dagger)_j^n (T^\dagger)_{j i}^{n m}
= \lambda^* (v^\dagger)_i^m
$$

As before, we have two nonzero sectors:

$$
\begin{aligned}
    &\text{when $v^\dagger$ is of even-parity: }
    &(v^\dagger)_j^0 (T^\dagger)_{j i}^{00}= \lambda^* (v^\dagger)_j^0
    \\
    &\text{when $v^\dagger$ is of odd-parity: }
    &(v^\dagger)_j^1 (T^\dagger)_{j i}^{11}= \lambda^* (v^\dagger)_j^1
\end{aligned}
$$

Now we can recover the original eigenvalue equations by taking the Hermitian conjugate.

## Grassmann Tensor