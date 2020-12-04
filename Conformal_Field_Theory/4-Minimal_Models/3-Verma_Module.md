# Verma Modules

## Highest-Weight Representation

Recall that

$$
L_n|h\rangle = 0, \quad n>0
$$

but $L_n (n>0)$ are lowering operators. This means that $|h\rangle$ *cannot be lowered any more*. We say that $|h\rangle$ is the **highest-weight state** of the representation of Virasoro algebra.

This is similar to the theory of the angular momentum: for a system of angular momentum $j$, we have

$$
J_- |j;m=-j\rangle =0
$$

i.e. the $z$-component of the angular momentum of the state
$|j;m=-j\rangle$ cannot be lowered any more.

## Verma Module

There are obviously $p(N)$ *linearly independent* states at level $N$, where $p(N)$ is the *number of partitions of the integer* $N$. It can be generated from the Taylor expansion of the Euler function

$$
\frac{1}{\varphi (q)} 
\equiv \prod_{n=1}^{\infty} \frac{1}{1-q^n}
= \sum_{n=0}^{\infty} p(n)q^n
$$

The subset of the full Hilbert space generated by the asymptotic state $|h\rangle$ and its descendants is closed under the action of the Virasoro generators. Thus it forms a *representation* (more correctly, a **module**) of the Virasoro algebra. This subspace is called a **Verma module**, denoted $V(c,h)$. The notation specifies the central charge $c$ and the highest weight $h$.

The following table lists the first few levels of a Verma module.

$$
\def \arraystretch{1.5}
\begin{array}{ccl}
\hline
l & p(l) & \text{Descendants (act on $|h\rangle$)} \\
\hline
0 & 1 & 1  \\
1 & 1 & L_{-1}  \\
2 & 2 & L_{-1}^2, L_{-2}  \\
3 & 3 & L_{-1}^3, L_{-1}L_{-2}, L_{-3}
\end{array}
$$

In addition, the Verma module generated by the anti-holomorphic
operators $\{\bar{L}_{-n} \}$ is denoted by
$\bar{V}(c,\bar{h})$.



## Reducible Verma Modules

It may happen that the representation of the Virasoro algebra
compromising all the states of the form $L_{-k_1}L_{-k_2} \cdots|h\rangle$ is **reducible**. This means that there is a
subspace (or) that is itself a valid representation of the Virasoro algebra, and the states of this submodule transform *amongst themselves* (**closed**) under any conformal transformation.

Such a sub-module is also generated from a highest-weight state $|\chi \rangle$, i.e.

$$
L_n|\chi \rangle =0
\quad \forall n>0
$$

but it also has the form $L_{-k_1}L_{-k_2} \cdots|h\rangle$. The
submodule is denoted $V_{\chi}$.

In general, any such state (*other than the highest-weight state*) which is annihilated by all the lowering operators $L_n (n>0)$ is called a **null state** (or a **singular vector**).

*Theorem*: Singular vectors and all of its descendants are **orthogonal** to the whole Verma module.

*Proof*: 

For any state $L_{-k_1}L_{-k_2} \cdots L_{-k_n}|h\rangle$ in
the module, and any descendants $L_{-l_1}L_{-l_2} \cdots L_{-l_m}|\chi \rangle$ (whose "conjugate" is $\langle \chi |L_{l_m} \cdots L_{l_2}L_{l_1}$), we have

$$
\begin{aligned}
    &\langle \chi |L_{l_m} \cdots L_{l_2}L_{l_1}L_{-k_1}L_{-k_2} \cdots L_{-k_n} |h \rangle 
    \\
    &=\langle h |L_{k_n} \cdots L_{k_2}L_{k_1}L_{-l_1}L_{-l_2} \cdots L_{-l_m} |\chi \rangle^*
    =0. \quad \blacksquare
\end{aligned}
$$