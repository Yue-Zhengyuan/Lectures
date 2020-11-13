# Unitarity and The Kac Determinant

Now we construct representations of the Virasoro algebra of the holomorphic part

$$
[L_n, L_m]
= (n-m)L_{n+m}
+ \frac{c}{12} n (n^2 - 1) \delta_{n+m, 0}
$$

## Unitary Representation of Virasoro Algebra

A representation of the Virasoro algebra is said to be **unitary** if it contains *no negative-norm states*.

### Simple Necessary Conditions

Some simple conditions are obtained from the norm of $L_{-n}| h\rangle$:

$$
\begin{aligned}
    \langle h |L_n L_{-n} |h \rangle 
    &= \langle h |L_{-n} L_n + [L_n,L_{-n}] |h \rangle 
    \\
    &= \langle h | [L_n,L_{-n}] |h \rangle 
    = \left\langle h \left|2n L_0+\frac{c}{12}n (n^2 - 1) \right|h\right\rangle
    \\
    &= \left(2 n h + \frac{c}{12} n (n^2 - 1) \right)
    \langle h|h\rangle
\end{aligned}
$$

1. If $c<0$, then the above becomes negative for sufficiently large $n$;

2. If $h<0$, then for $n=1$, we obtain negative norm.

Thus *all representations with negative central charge or negative conformal dimensions are non-unitary*.

## The Kac Determinant

The **Kac determinant** is the determinant of the **Gram matrix** defined as

$$
M_{i j}=\langle i|j\rangle
$$

where $| i\rangle , | j\rangle$ are states in the Verma module.
Obviously $M$ is Hermitian.

----

*Theorem*: Negative-norm states occur if and only if $M$ *has negative eigenvalues*. If one of the eigenvalues $\Lambda_i$ vanishes, then there will be singular vectors, and the Verma module will be reducible.

*Proof*:

For a generic state, its norm is calculated by

$$
| a\rangle =\sum_i a_i| i\rangle 
\Rightarrow 
\langle a|a\rangle 
= a_i^*\langle i|j\rangle a_j
= a^{\dagger }M a
$$

We can always diagonalize $M$ (since it is Hermitian) using
$M=U \Lambda  U^{\dagger }$. Define $b=U a$, then

$$
\langle a|a\rangle =\sum_i  \Lambda_i\left| b_i\right| {}^2
$$

Now the theorem is obvious. $\blacksquare$

----

Since descendants of different levels are orthogonal, the Gram matrix is *block-diagonal*, with blocks $M^{(l)}$ corresponding to level $l$. Therefore

$$
\begin{aligned}
    \det M &= \prod_l  \det  M^{(l)}
    \\
    \text{tr} M &= \sum_l  \text{tr} M^{(l)}
\end{aligned}
$$

The first few blocks are

$$
\begin{aligned}
    M^{(0)} &= 1
    \\
    M^{(1)} &= 2h
    \\
    M^{(2)} &= 
    \begin{pmatrix}
        4h(2h+1) & 6h \\
        6h & 4h+c/2 \\
    \end{pmatrix}
\end{aligned}
$$

For example, $M^{(2)}$ corresponds to $L_{-1}L_{-1}, L_{-2}$, and

$$
\begin{aligned}
    M_{22}^{(2)} 
    &\equiv \langle h |L_2L_{-2} |h \rangle 
    \\
    &= \langle h|L_{-2} L_2+ [L_2,L_{-2}] |h \rangle
    =\langle h| [L_2,L_{-2}] |h\rangle 
    \\
    &=\left\langle h\left|
        (2-(-2))L_0
        + \frac{c}{12} 2 (2^2 - 1) \delta_{2-2, 0}
    \right| h \right\rangle 
    \\
    &= \left\langle h\left| 4L_0 + \frac{c}{2} \right|h\right\rangle 
    =4h+\frac{c}{2}
\end{aligned}
$$

Their determinants are

$$
\begin{aligned}
    \det M^{(0)} &= 1
    \\
    \det M^{(1)} &= 2h
    \\
    \det M^{(2)} 
    &= 32 h^3 - 20 h^2 + 4 h^2 c + 2h c \\
    &= 32 (h-h_{1,1}) (h-h_{1,2}) (h-h_{2,1})
\end{aligned}
$$

with

$$
\begin{aligned}
    h_{1,1} &= 0
    \\
    h_{1,2} &= \frac{1}{16} \left(5-c-\sqrt{(1-c)(25-c)}\right)\\
    h_{2,1} &= \frac{1}{16} \left(5-c+\sqrt{(1-c)(25-c)}\right)
\end{aligned}
$$

The general formula is

$$
\det M^{(l)} 
= \alpha_l \prod_{
    \scriptsize
    \begin{matrix}
        r,s\ge 1 \\
        r s\le l
    \end{matrix}
} 
[h - h_{r,s}(c)]^{p(l - rs)}
$$

Here

$$
\begin{aligned}
    p(l-r s) &= \text{number of partitions of } l-r s
    \\
    \alpha_l &=\prod_{
        \scriptsize
        \begin{matrix}
            r,s\ge 1 \\
            r s\le l
        \end{matrix}
    } \left[(2r)^ss!\right]^{m(r, s)}
    \\
    m(r,s) &= p(l-r s) - p(l-r(s+1))
\end{aligned}
$$

![image](Fig-7_1.png)

The functions $h_{r,s}$ can be expressed in many ways:

$h_{r,s}(c)=h_0+\frac{1}{4}\left(r \alpha_++s \alpha_-\right)$
