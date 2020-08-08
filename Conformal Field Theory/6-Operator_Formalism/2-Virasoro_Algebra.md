## Virasoro Algebra

### Laurent Modes of the Energy-Momentum Tensor 

Specially, for the energy momentum tensor

$$
\begin{aligned}
    T(z) &= \sum_n  (z-w)^{-n-2}L_n(w)
    \\
    L_n(w) &= \frac{1}{2 \pi i} \oint_w dz \, z^{n+1}T(z)
\end{aligned}
$$

Then we can write the OPE of $T(z)$ with any field $A(w)$ as

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

### Virasoro Algebra

We expand the energy-momentum tensor:

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

and the infinitesimal conformal change $\epsilon (z)$:

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

### Central Extension of Witt Algebra

#### Central Extension of Lie Groups and Lie Algebra

A **central extension** of a group $G$ is a short exact sequence of groups

$$
1 \to A \to E \to G \to 1
$$

such that $A$ is in $Z(E)$, the **center** of the group $E$, which is the set of elements in $E$ that commute with every element of $E$:

$$
Z(E)\equiv
\{ z\in E \mid z g=g z, \, \forall g\in E\}
$$

Obviously, the center of $E$ is an *invariant* subgroup of $E$.

The set of isomorphism classes of central extensions of $G$ by $A$ (where $G$ acts *trivially* on $A$) is in one-to-one correspondence with the cohomology group $H^2(G,A)$.

#### Virasoro Algebra

There is a *unique* central extension of the Witt algebra, called the **Virasoro algebra**.

We first consider the holomorphic part. The generators $l_n$ are promoted to $L_n$, and a new element $c\in \mathbb{C}$ (the **central charge**) is introduced so that

$$
\begin{aligned}
    [L_n, L_m] &=(n-m)L_{m+n}+c p(n,m)
    \\
    [L_n, c] &= 0\\
    [c,c] &= 0
\end{aligned}
$$

where $p$ is a *bilinear* mapping onto $\mathbb{C}$ (this is required by
the bi-linearity of the Lie bracket). The last two equations mean that
$c$ commutes with all group elements in the Virasoro algebra. Similar
relations hold for the anti-holomorphic part ($\bar{l}_n\to \bar{L}_n$
etc).

Now we determine the explicit form of $p(n,m)$ for Virasoro algebra.

1\. Since the Lie bracket is *anti-symmetric*, we obtain

$\left[L_n,L_m\right]=(n-m)L_{m+n}+c p(n,m)\\
=-\left[L_m,L_n\right]=-(m-n)L_{n+m}-c p(m,n)$

$\Longrightarrow  p(n,m)=-p(m,n)$

2\. We can always make

$p(1,-1)=0, p(n,0)=0$

If they are not zero, we redefine the $L_n$ operators as

$L_n^{\prime}=L_n+\frac{c p(n,0)}{n} (n\neq 0), L_0^{\prime}=L_0+\frac{c p(1,-1)}{2}$

Then

$\left[L_n^{\prime},L_0^{\prime}\right]=\left[L_n,L_0\right]=n L_n+c p(n,0)=n L_n^{\prime}$

$\left[L_1^{\prime},L_{-1}^{\prime}\right]=\left[L_1,L_{-1}\right]=2L_0+c p(1,-1)=2L_0^{\prime}$

The motivation for the redefinition above is now clear.

3\. The Lie bracket should satisfy the *Jacobi identity*

$\left[\left[L_m,L_n\right],L_l\right]+\left[\left[L_l,L_m\right],L_n\right]+\left[\left[L_n,L_l\right],L_m\right]=0$

For $(m,n,l)\to (m,n,0)$, we have

$(m+n)p(n,m)=0 \Longrightarrow p(n,m)=p(n,-n)\delta_{m+n, 0}$

But we still have $p(1,-1)=0$, thus $p(n,-n)\neq 0$ *is possible only
when* $| n| \geq 2$.

For $(m,n,l)\to (-n+1,n,-1)$, we have

$(-2n+1)c p(1,-1)+(n+1)c p(n-1,-n+1)+(n-2)c p(-n,n)=0$

Or

$(n+1) p(n-1,-n+1)=(n-2) p(n,-n)$

which allows us to calculate $p(n,-n)$ recursively:

$p(n,-n)=\frac{n+1}{n-2}p(n-1,-n+1)\\
=\frac{(n+1)n}{(n-2)(n-3)}p(n-2,-n+2)\\
= \cdots =\left(
\begin{array}{c}
 n+1 \\
 3 \\
\end{array}
\right)p(2,-2)$

By convention, we set

$p(2,-2)=\frac{1}{2}$

Summarize all the above calculations, we finally find

$p(n,m)=\frac{1}{12}n\left(n^2-1\right)\delta_{m+n, 0}$

and the Virasoro algebra is

$\left[L_n,L_m\right]=(n-m)L_{n+m}+\frac{c}{12}n\left(n^2-1\right)\delta_{m+n, 0}$

#### Other Commutation Rules in Virasoro Algebra

Adding the anti-holomorphic parts into the algebra, we further obtain

$\left[\bar{L}_n,\bar{L}_m\right]=(n-m)\bar{L}_{n+m}+\frac{\bar{c}}{12}n\left(n^2-1\right)\delta_{m+n, 0}$

Here $\bar{c}$ is the central charge of the anti-holomorphic sector.
Some physical constraints (such as the conformal invariance on a torus)
will fix

$\bar{c}=c$

For the mixed commutator, we still have

$\left[L_n,\bar{L}_m\right]=0$
