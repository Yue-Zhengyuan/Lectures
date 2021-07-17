# Decomposition of Grassmann Tensors

**Tensor decompositions** are the generalization of the corresponding operations on  matrices:

1. Combine the axes of the tensor into two groups
2. Merge these axes to form two new "big" axes, so that the tensor is reshaped to a *matrix*
3. Perform the decomposition (QR, SVD, etc.) on this matrix
4. Split the "big" axes in the result matrices to recover the tensor shape

The merging (step 2) and splitting (step 4) of axes for ordinary tensors are trivial (in Python, this is done by `numpy.reshape`), but for Grassmann tensors, things are more complicated. This problem is described [here](axis_merging.md) in general.

## The Decomposition Process

(*In the following, we consider **even**-parity Grassmann tensors only.*) 

*Program implementation: `gtensor.qr`, `gtensor.svd`*

Let us decompose a rank-$r$ even-parity Grassmann tensor $T$ at the $q$th axis. First, we reshape it to

$$
T_{(i_1 ... i_q) (i_{q+1} ... i_r)}^{(n_1 ... n_q) (n_{q+1} ... n_r)}
\rightarrow T_{I J}^{M N}
$$

Since $T$ is of even parity, the nonzero components are $T^{0 0}, T^{1 1}$ (I call them the **even block** and the **odd block**, respectively). Now we perform the corresponding [matrix decomposition](#appendix-matrix-decompositions) on the four $T^{MN}$; note that we *tacitly assume* that the decomposition result $A, B$ are both of *even* parity for convenience in physical applications:

$$
T_{I J}^{M N} = A_{I j}^{M N} B_{j J}^{M N} 
\xrightarrow{\text{nonzero}}
\begin{cases}
    T_{I J}^{0 0} = A_{I j}^{0 0} B_{j J}^{0 0} \\
    T_{I J}^{1 1} = A_{I j}^{1 1} B_{j J}^{1 1}
\end{cases}
$$

Here we sum over the new normal index $j$ only. From the properties of the matrix decomposition, $j$ will have dimension

$$
\begin{align*}
    \dim j[0] &= \min{(\dim{I[0]}, \dim{J[0]})}
    \\
    \dim j[1] &= \min{(\dim{I[1]}, \dim{J[1]})}
\end{align*}
$$

which also depends on the corresponding Grassmann index $n$. 

Since $A^{0 1}, A^{1 0}, B^{0 1}, B^{1 0}$ are all zero, this enables us to rewrite the decomposition as

$$
\left.
\begin{align*}
    T_{I J}^{0 0} &= A_{I j}^{0 0} B_{j J}^{0 0} +  A_{I j}^{0 1} B_{j J}^{1 0} \\
    T_{I J}^{0 1} &= A_{I j}^{0 0} B_{j J}^{0 1} +  A_{I j}^{0 1} B_{j J}^{1 1} \\
    T_{I J}^{1 0} &= A_{I j}^{1 0} B_{j J}^{0 0} +  A_{I j}^{1 1} B_{j J}^{1 0} \\
    T_{I J}^{1 1} &= A_{I j}^{1 0} B_{j J}^{0 1} +  A_{I j}^{1 1} B_{j J}^{1 1} \\
\end{align*}
\right\} \Longrightarrow
T_{I J}^{M N} = \sum_{n,j} A_{I j}^{M n} B_{j J}^{n N}
$$

Now we can split the merged indices to recover the tensor shape, obtaining the formula:

$$
T_{i_1 ... i_q,  i_{q+1} ... i_r}^{n_1 ... n_q,  n_{q+1} ... n_r}
= A_{i_1 ... i_q, j}^{n_1 ... n_q, n} B_{j, i_{q+1} ... i_r}^{n, n_{q+1} ... n_r} 
$$

Here summation over $n,j$ is implied. 

## Decomposition of Odd-Parity Tensors

- *Case 1*: A is even, B is odd (used in SVD and LQ)

    $$
    T_{I J}^{M N} = A_{I j}^{M N} B_{j J}^{M N} 
    \xrightarrow{\text{nonzero}}
    \begin{cases}
        T_{I J}^{0 1} = A_{I j}^{0 0} B_{j J}^{0 1} \\
        T_{I J}^{1 0} = A_{I j}^{1 1} B_{j J}^{1 0}
    \end{cases}
    $$

    The new index $j$ will have the dimension

    $$
    \begin{align*}
        \dim j[0] &= \min{(\dim{I[0]}, \dim{J[1]})}
        \\
        \dim j[1] &= \min{(\dim{I[1]}, \dim{J[0]})}
    \end{align*}
    $$

- *Case 2*: A is odd, B is even (used in QR)

    $$
    T_{I J}^{M N} = A_{I j}^{M N} B_{j J}^{M N} 
    \xrightarrow{\text{nonzero}}
    \begin{cases}
        T_{I J}^{0 1} = A_{I j}^{0 1} B_{j J}^{1 1} \\
        T_{I J}^{1 0} = A_{I j}^{1 0} B_{j J}^{0 0}
    \end{cases}
    $$

    The new index $j$ will have the dimension

    $$
    \begin{align*}
        \dim j[0] &= \min{(\dim{I[1]}, \dim{J[0]})}
        \\
        \dim j[1] &= \min{(\dim{I[0]}, \dim{J[1]})}
    \end{align*}
    $$

In both cases, we can still write the decomposition as (similar to the decomposition of even-parity Grassmann tensors)

$$
T_{I J}^{M N} = \sum_{n,j} A_{I j}^{M n} B_{j J}^{n N}
$$

## Appendix: Matrix Decompositions

### (Reduced) QR and LQ Decompositions

*Program implementation: `numpy.linalg.qr`*

The (reduced) **QR decomposition** of an $m \times n$ matrix $M_{i j}$ is defined as

$$
M_{i j} = Q_{i k} R_{k j}
$$

where (define $p \equiv \min{(m,n)}$):

- $Q$ is an $m \times p$ *unitary* matrix in the sense that 

$$Q^\dagger Q = 1$$

- $R$ is an $p \times n$ *upper-right triangular* matrix

It is easy to obtain the (reduced) **LQ decomposition** of $M$ from QR with proper transpositions:

$$
M^\top \xlongequal{QR} Q^\top L^\top 
\xrightarrow{\text{transpose}} M = L Q
$$

therefore

- $Q$ is an $p \times n$ *unitary* matrix in the sense that 

$$Q Q^\dagger = 1$$

- $L$ is an $m \times p$ *lower-left triangular* matrix


### Singular Value Decomposition (SVD)

*Program implementation: `numpy.linalg.svd`*

The **singular value decomposition** of an $m \times n$ matrix $M_{i j}$ is defined as

$$
M_{i j} = \sum_{k} U_{i k} s_k V^\dagger_{k j}
$$

where (as before, define $p \equiv \min{(m,n)}$):

- $U$ (shape $m \times p$), $V^\dagger$ (shape $p \times n$) are *unitary* matrices in the sense that

$$ U^\dagger U = I, V^\dagger V  = 1 $$

- $s$ is a series of *non-negative real* numbers, called the **singular values** of the matrix $M$

#### Truncation of Singular Value Spectrum 

We can discard some small singular values (thus decreasing $\dim j$) to approximate the original tensor. At the same time, the corresponding columns/rows of $U, V^\dagger$ should also be removed. Obviously, the parity of $S_1, S_2$ will not be affected by the truncation.

#### Absorbing Singular Values into $U, V^\dagger$

Usually, we combine the singular value spectrum $s$ with $U$ and $V^\dagger$ and define:

$$
(S_1)_{i k} \equiv U_{i k} \sqrt{s_k}, \quad
(S_2)_{k j} \equiv \sqrt{s_k} V^\dagger_{k j}
$$

Here we do *not* sum over $k$. Then

$$
M_{i j} = (S_1)_{i k} (S_2)_{k j}
$$
