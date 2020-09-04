# Virasoro Algebra

## Laurent Modes of the Energy-Momentum Tensor 

The Laurent modes energy momentum tensor are denoted by $L_n$:

$$
\begin{aligned}
    T(z) &= \sum_n  (z-w)^{-n-2}L_n(w)
    \\
    L_n(w) &= \frac{1}{2 \pi i} \oint_w dz \, z^{n+1}T(z)
\end{aligned}
$$

Then we can write the OPE of $T(z)$ with any (primary) field $A(w)$ as

$$
T(z)A(w) = \sum_n (z-w)^{-n-2} L_n(w) A(w)
$$

Comparing with the old result ($h_A$ is the conformal dimension of $A(z)$)

$$
\begin{aligned}
    T(z)A(w) 
    &= \frac{h_A}{(z-w)^2}A(w) 
    + \frac{1}{z-w} \partial_w A(w)
    + \text{reg.}
    \\
    \text{reg.} 
    &= (T A)(w)
    + (z-w)\partial (T A)(w)
    \\ &\qquad
    + \frac{1}{2!}(z-w)^2\partial^2(T A)(w)
    + \cdots
\end{aligned}
$$

We see that for the singular part

$$
(L_0 A)(w) = h_A A(w), \quad
(L_{-1} A)(w) = \partial A(w)
$$

and for the regular part

$$
(L_{-n-2} A)(w)
= \frac{1}{n!} \partial^n (T A)(w)
$$

In particular, when $A$ is the identity $\mathbf{1}$, we get

$$
(L_{-n-2} \mathbf{1})(w)
= \frac{1}{n!} \partial^nT(w)
$$

## Virasoro Algebra

We expand the energy-momentum tensor at the origin $(w = 0)$:

$$
\begin{aligned}
    T(z)
    &= \sum_n z^{-n-2} L_n, \quad 
    L_n = \frac{1}{2 \pi i} \oint dz \, 
    z^{n+1} T(z)
    \\
    \bar{T}(\bar{z})
    &= \sum_n \bar{z}^{-n-2} \bar{L}_n, \quad
    \bar{L}_n = \frac{1}{2 \pi i} \oint d\bar{z} \, 
    \bar{z}^{n+1} \bar{T}(\bar{z})
\end{aligned}
$$

We also expand infinitesimal conformal change $\epsilon (z)$ at the origin:

$$
\epsilon(z) 
= \sum_n  z^{n+1} \epsilon_n, \quad
\epsilon_n 
= \frac{1}{2 \pi i} \oint dz \,
z^{-n-2} \epsilon (z)
$$

Then

$$
\begin{aligned}
    Q_{\epsilon}
    &= \frac{1}{2 \pi i} \oint dz \, T(z)\epsilon (z)
    \\
    &= \frac{1}{2 \pi i} \oint dz 
    \sum_n  z^{-n-2} L_n
    \sum_m  z^{m+1} \epsilon_m
    \\
    &= \frac{1}{2 \pi i} \sum_{n,m} \oint dz \, 
    z^{-(n-m)-1}L_n\epsilon_m
    \\
    &= \sum_{n,m} \frac{1}{(n-m)!} \frac{d^{n-m}}{dz^{n-m}} (L_n\epsilon_m)
\end{aligned}
$$

The term is nonzero only when $n=m$. Then

$$
Q_{\epsilon} = \sum_n \epsilon_n L_n
$$

The algebra of the generators $L_n,\bar{L}_n$ is the so-called **Virasoro algebra**:

$$
\begin{aligned}
    [L_n, L_m]
    &= (n-m)L_{n+m}
    + \frac{c}{12} n (n^2 - 1) \delta_{n+m, 0} 
    \\
    [\bar{L}_n, \bar{L}_m]
    &= (n-m) \bar{L}_{n+m}
    + \frac{c}{12} n (n^2 - 1) \delta_{n+m, 0}
    \\
    [L_n, \bar{L}_m] &= 0
\end{aligned}
$$

*Proof*:

Using

$$
[A,B] = \oint_0 dw \oint_w dz \, a(z)b(w)
$$

we obtain

$$
\begin{aligned}
    [L_n, L_m]
    &= \frac{1}{(2 \pi i)^2} \left[
        \oint dz \, z^{n+1} T(z),
        \oint dw \, w^{m+1} T(w)
    \right]
    \\
    &= \frac{1}{(2 \pi i)^2} 
    \oint_0 dw \, w^{m+1} 
    \oint_w dz \, z^{n+1} 
    \underbrace{T(z)T(w)}_{\text{use OPE}} 
    \\
    &= \frac{1}{(2 \pi i)^2} 
    \oint_0 dw \, w^{m+1} 
    \oint_w dz \, z^{n+1} 
    \\ &\qquad
    \left[
        \frac{c/2}{(z-w)^4}
        + \frac{2T(w)}{(z-w)^2}
        + \frac{\partial_w T(w)}{z-w}
        + \text{reg.}
    \right]
\end{aligned}
$$

Integrate over $z$ using Cauchy Integral Formula

$$
\begin{aligned}
    &\frac{1}{2 \pi i} \oint_w dz \, z^{n+1} 
    \left[
        \frac{c/2}{(z-w)^4}
        + \frac{2T(w)}{(z-w)^2}
        + \frac{\partial_w T(w)}{z-w}
        + \text{reg.}
    \right]
    \\
    &= \frac{1}{3!} \left[
        \frac{d^3}{dz^3} (z^{n+1} c/2)
    \right]_{z=w}
    \\ &\qquad
    + \frac{1}{1!} \left[
        \frac{d}{dz} (2z^{n+1} T(w))
    \right]_{z=w}
    + \left[
        z^{n+1} \partial_wT(w)
    \right]_{z=w} 
    \\
    &= \frac{c}{12} n (n^2 - 1) w^{n-2}
    + 2(n + 1) w^n T(w)
    + w^{n+1} \partial_w T(w)
\end{aligned}
$$

Then complete the integration over $w$

$$
\begin{aligned}
    [L_n, L_m]
    &= \frac{1}{2 \pi i} \oint_0 dw \left(
        \frac{c}{12} n (n^2 - 1) w^{m+n-1}
        \right. 
        \\ &\qquad \qquad \qquad
        \left.
        + 2(n+1)w^{m+n+1}T(w)
        + \underbrace{w^{m+n+2} \partial_w T(w)}_{\text{integrate by parts}} 
    \right)
    \\
    &= \frac{1}{2 \pi i} \oint_0 \, dw \left(
        \frac{c}{12}n(n^2 - 1) w^{m+n-1}
        \right.
        \\ &\qquad \qquad 
        \left.
        + 2 (n + 1) w^{m+n+1} T(w)
        - (m+n+2) w^{m+n+1} T(w)
    \right)
    \\
    &= \frac{c}{12}n(n^2 - 1) \frac{1}{1!} 
    \left[\frac{d}{dw} \left(w^{m+n} \right)\right]_{w=0}
    \\ &\qquad \qquad
    + 2(n+1) L_{m+n}
    - (m+n+2) L_{m+n} 
    \\
    &= \frac{c}{12} n (n^2 - 1) \delta_{m+n, 0}
    + (n-m) L_{m+n}
\end{aligned}
$$

$[\bar{L}_n, \bar{L}_m]$ can be found in the same way using the OPE of $\bar{T} (\bar{z})$ with itself.

Finally, from $T(z)\bar{T} \left(\bar{w} \right)\sim 0$, we have $[L_n, \bar{L}_m]=0$. $\blacksquare$
