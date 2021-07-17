# Descendant States and Fields

## Descendant States

The state

$$
L_{-k_1}L_{-k_2} \cdots L_{-k_n}|h\rangle 
\qquad (1 \le k_1 \le \cdots \le k_n)
$$

is an eigenstate of $L_0$ with eigenvalue

$$
h' = h + N, \quad 
N \equiv k_1 + k_2 + \cdots + k_n
$$

We call such kind of states **descendant states** (or simply **descendants**) of the asymptotic state $|h\rangle$, although this name is a little bit weird considering that they are produced by *raising* operators $L_{-n}$. The integer $N$ is called the **level** of the descendant.

----

*Theorem*: Descendant states belonging to different levels are **orthogonal**.

*Proof*:

- We first consider the simple case

    $$
    |i\rangle =L_{-M}|h\rangle , \quad |j\rangle =L_{-N}|h\rangle
    \quad (N, M > 0, N \ne M)
    $$

    In the following calculation, since $L_n$ are not Hermitian, we can only apply them to *kets*. With help of some commutators, we obtain

    $$
    \begin{align*}
        \langle i|j \rangle 
        &= \langle h | L_M L_{-N} | h \rangle 
        \\
        &= \langle h | L_{-N} L_M + [L_M,L_{-N}] | h \rangle
        \\
        &=\langle h|L_{-N} \underbrace{L_M|h\rangle}_0
        \\ &\quad
        + \left\langle h \left|
            (M-N) L_{M-N} 
            + \frac{c}{12} M (M^2-1) \delta_{M+N, 0} 
        \right| h\right\rangle
        \\[1em]
        &=(M-N)\left\langle h\left|L_{M-N} \right|h\right\rangle
    \end{align*}
    $$

    Without loss of generality, assume $M>N$, then $L_{M-N}|h\rangle =0$, and we proved that $\langle i|j\rangle =0$. 
    
    (If $M<N$, we can calculate its the complex conjugate $\left\langle h\left|L_{N-M} \right|h\right\rangle =0$, so it is also zero)

- In general, let

    $$
    \begin{align*}
        |i\rangle &= L_{-k_1} \cdots L_{-k_m}|h\rangle , 
        &\quad 
        &k_1 + \cdots + k_m = M
        \\
        |j\rangle &= L_{-l_1} \cdots L_{-l_n}|h\rangle , 
        &\quad
        &l_1 + \cdots + l_n = N \ne M
    \end{align*}
    $$

    We calculate

    $$
    \langle i|j\rangle 
    = \langle h | 
        L_{k_m} \cdots L_{k_1}
        L_{-l_1} \cdots L_{-l_n}
    | h \rangle
    $$

----

## Descendant Fields

Each descendant state can be regarded as the result of the application on the vacuum of a **descendant field**. 

For example, consider the simplest level-$n$ descendant state, for which the integer $n$ is not partitioned at all

$$
L_{-n}|h\rangle =L_{-n} \phi(0)|0\rangle
$$

The descendant field $\phi^{(-n)}$ associated with this state should
satisfy

$$
\phi^{(-n)}(0)|0\rangle =L_{-n}|h\rangle
$$

Since $L_{-n}$ is a Laurent mode of $T(z)$, we can write

$$
L_{-n}|h\rangle =\frac{1}{2 \pi i} \oint dz z^{-n+1}T(z)\phi(0)|0\rangle
$$

Then the descendant field $\phi^{(-n)}$ can be naturally chosen as

$$
\begin{align*}
    \phi^{(-n)}(w)
    &= \frac{1}{2 \pi i} \oint_w dz (z-w)^{-n+1}T(z)\phi(w)
    \\
    &= L_{-n}(w)\phi(w)
    \\
    &\equiv \left(L_{-n} \phi \right)(w)
\end{align*}
$$

As two special cases, according to the general formulas

$$
\left(L_0 A\right)(w) = h_A A(w), \quad
\left(L_{-1} A\right)(w) = \partial_w A(w)
$$

we find

$$
\phi^{(0)}(w) = h \phi(w), \quad
\phi^{(-1)}(w) = \partial \phi(w)
$$

In general, we can partition $n$ into $m$ numbers $k_1+k_2+\cdots+k_m$ and define recursively the corresponding
descendant field as

$$
\begin{align*}
    &\phi^{\left(-k_1,-k_2,\cdots,k_m\right)}(w)
    = (L_{-k_1}L_{-k_2} \cdots L_{-k_m} \phi)(w)
    \\
    &= \frac{1}{2 \pi i} \oint_w dz \, 
    (z-w)^{-k_1+1} T(z) \phi^{(-k_2,...,-k_m)}(w)
\end{align*}
$$

In particular, we need to emphasize that $\phi^{(0,-n)}$ is *not* the same as $\phi^{(-n)}$:

$$
\phi^{(0,-n)}(w) = (h+n)\phi^{(-n)}(w)
$$

Another commonly used relation is

$$ 
\phi^{(-1,-n)}(w) = \partial \phi^{(-n)}(w)
$$

## A Representation of the Conformal Generators

The relations $\phi^{(-1)}(w)=\partial \phi(w)$ and
$\phi^{(-1,-n)}(w)=\partial \phi^{(-n)}(w)$ give us the first hint that $L_{-1}(w)$ somewhat has the same effect as the differential operator $\partial_w$. 

To illustrate what this exactly means, let $X\equiv \phi_1(w_1) \cdots \phi_N(w_N)$ and consider the correlation function

$$
\langle \phi^{(-n)}(w)X \rangle 
\equiv \langle (L_{-n} \phi)(w) X \rangle
$$

we can find a differential operator $\mathcal{L}_{-n}$ such that

$$
\left\langle \left(L_{-n} \phi \right)(w)X\right\rangle =\mathcal{L}_{-n} \langle \phi(w)X\rangle \text{   }(n\ge 1)
$$

with

$$
\mathcal{L}_{-n}
= \sum_{i=1}^N \left[
    \frac{(n-1)h_i}{(w_i-w)^n}
    - \frac{1}{(w_i-w)^{n-1}} \partial_{w_i} 
\right]
$$

In particular

$$
\mathcal{L}_{-1} = \partial_w
$$

----

*Proof*:

----

*Remarks*:

1. In general

    $$
    \langle \phi^{(-k_1, ..., -k_m)}(w)\, X \rangle 
    =\mathcal{L}_{-k_1} \cdots \mathcal{L}_{-k_m} 
    \langle \phi(w)X\rangle
    $$

2. Recall the most primitive operators in Witt algebra

    $$
    l_{-n}=-w^{-n+1} \partial_w
    $$