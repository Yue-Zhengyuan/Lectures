# The Operator Formalism

## Math Preliminary on Complex Analysis 

### Cauchy Integral Formula

For any function defined in a region on the complex plane, we have the expansion around the point $z_0$ in that region:

$$
f(z)=\sum_{n=-\infty}^{+\infty} a_n
(z - z_0)^n
$$

The $n<0$ part is called the **pricipal part**, and the normal $n\ge 0$ part is the **analytic part**.
The coefficients can be found by the **Cauchy integral formula**:

$$
a_n = \frac{1}{2\pi i}
\oint_C dz \,
\frac{f(z)}{(z - z_0)^{n+1}}
$$

valid for both positive and negative $n$. The integration path $C$ must
enclose the point $z_0$.

Compare the analytic part with the Taylor series, we find:

1. for $n\ge 0$

    $$
    f^{(n)}(z_0)
    = \frac{n!}{2\pi i}
    \oint_C dz \frac{f(z)}{(z-z_0)^n}
    $$

2. for $n=0$

    $$
    f(z_0)
    = \frac{1}{2\pi i}
    \oint_C dz \, \frac{f(z)}{z-z_0}
    $$

*Explanation of the Cauchy Integral Formula:*

Since the complex integration is *independent of the shape* of the closed path $C$, we can take $C$ to be a circle of radius $R$ around the point $z_0$. Then $C$ can be parametrized as

$$
C = \{ z \mid z_0+R e^{i \theta}, \,
\theta \in [0,2\pi) \}
$$

The complex integral is then reduced to the real integral over

$$
\oint_C dz 
= i R\int_0^{2\pi} e^{i \theta} d\theta
$$

Substituting the Laurent expansion in the RHS of the Cauchy formula:

$$
\begin{aligned}
    &\frac{1}{2 \pi i}
    \oint_C dz \frac{f(z)}{(z-z_0)^{n+1}}
    \\
    &=\frac{1}{2\pi i}
    \sum_{m=-\infty}^{\infty} 
    \oint_C dz \, a_m(z - z_0)^{m-(n+1)}
    \\
    &= \frac{1}{2 \pi i} \sum_{m=-\infty}^{\infty} i R a_m\int_0^{2\pi}d\theta  e^{i \theta} (R e^{i \theta})^{m-(n+1)}
    \\
    &= \frac{1}{2\pi} \sum_{m=-\infty}^{\infty} R^{m-n}a_m\int_0^{2\pi}d\theta  e^{i(m-n)\theta}
    \\
    &= \sum_{m=-\infty}^{\infty} R^{m-n}a_m \delta_{m n}
    = a_n
\end{aligned}
$$

### The Residue Theorem

Suppose that

$$
f(z) = \sum_{n=-m}^{+\infty} a_n (z - z_0)^n
\quad (m\in \mathbb{N})
$$

and let $C$ be a closed path enclosing $z=z_0$ but no other singular points of $f(z)$. Then the **residue theorem** states that

$$
\oint_Cdz f(z)=2 \pi i a_{-1}
$$

This is just the Cauchy Integral Formula for $n=-1$.

## Radial Quantization

### From Cylinder to Complex Plane 

Consider a CFT *compactified on a cylinder*. The axial direction of the
cylinder represents time $t=x^0$. We can use the following mapping to
map the system to the complex plane:

$$
z=e^{x^0+i x^1}
$$

Then constant $t$ points map to a *circle* centered at the origin: the
*radial direction* represent the time.

![image](Operator Formalism_gr1.eps)

### Asymptotic States

We assume the existence of a vacuum state $|0\rangle$ upon which a Hilbert space is constructed by application of creation
operators (or their likes).

In free-field theories, the *vacuum* may be defined as the state
annihilated by the *positive frequency part* of the field.

For an *interacting* field $\phi$, we assume that *the Hilbert space is
the same as for a free field*, except that the actual energy eigenstates
are different.

#### "In" State

Suppose then that the interaction is slowly turned off as
$t\to \pm \infty$ and that the *asymptotic* field

$$
\phi_{\text{in}} \propto \lim_{t\to -\infty} \phi(t,x)
$$

is *free*. Within radial quantization, this asymptotic field reduces to
a single operator, which, upon acting on $|0\rangle$ creates a single
asymptotic "in" state:

$$
|\phi_{\text{in}} \rangle 
= \lim_{z,\bar{z} \to 0} 
\phi(z, \bar{z}) |0\rangle
$$

#### "Out" State


### Radial Ordering

After the mapping from cylinder to complex plane, the time ordering (later time to earlier time) becomes a (farther to closer to the origin). Explicitly

$$
\mathcal{R} \phi_1(z)\phi_2(w)=
\begin{cases}
    \phi_1(z)\phi_2(w), & |z|>|w| \\
    \pm \phi_2(w)\phi_1(z), & |z|<|w| \\
\end{cases}
$$

Here the $+$ sign is for bosons, and the $-$ sign is for fermions.

Let $a(z), b(z)$ be two holomorphic fields, and define two operators

$$
A=\oint dz a(z), \quad
B=\oint dz b(z)
$$

the integration path being any circle around the origin. Now we **claim** that

$$
\oint_0 dz [a(z),b(w)]=\oint_w dz [\mathcal{R} a(z)b(w)]
$$

Then we can integrate over $w$ to obtain

$$
[A,B] = \oint_0 dw \oint_w dz \, [\mathcal{R} a(z)b(w)]
$$

the subscript $0,w$ means circular paths centered at $0,w$. In the
following, we shall always assume radial ordering and omit the
$\mathcal{R}$ notation.

*Proof*:

We first evaluate the integral over $z$.

![image](Operator Formalism_gr2.eps}

$$
\begin{aligned}
    \oint_w dz a(z)b(w)
    &=\oint_{|z|>|w|} dz a(z)b(w)-\oint_{|z|<|w|} dz b(w) a(z)
    \\
    &=\oint_0 dz [a(z),b(w)]
\end{aligned}
$$

Then, after integration over $w$, we immediately obtain

$$
\begin{aligned}
    \oint_0 dw \oint_0 dz [a(z),b(w)]
    &= \left[\oint_0 dz a(z), \oint_0 dw b(w)\right]
    \\
    & = [A,B] 
    \qquad \blacksquare
\end{aligned}
$$

## Energy-Momentum Tensor in 2D 

### *Proposition*: CFT in 2D has **traceless** energy-momentum tensor

*Proof*:

### Holomorphic Components of the Energy-Momentum Tensor 

The energy-momentum tensor $T_{\mu  \nu}$ transforms in the same way as the metric $g_{\mu  \nu}$:

$$
\begin{aligned}
    T_{z z} 
    &=
    \frac{\partial x^0}{\partial z} \frac{\partial x^0}{\partial z}T_{00}+\frac{\partial x^0}{\partial z} \frac{\partial x^1}{\partial z}T_{01}+\frac{\partial
    x^1}{\partial z} \frac{\partial x^0}{\partial z}T_{10}+\frac{\partial x^1}{\partial z} \frac{\partial x^1}{\partial z}T_{11}
    \\
    &= \frac{1}{2} \times \frac{1}{2}T_{00}+\frac{1}{2} \frac{-i}{2}T_{01}+\frac{-i}{2} \frac{1}{2}T_{10}+\frac{-i}{2} \frac{-i}{2}T_{11}
    \\
    &=\frac{1}{4} \left(T_{00}-2i T_{10}-T_{11} \right)
\end{aligned}
$$

Proceeding in the same way, we find

$$
\begin{aligned}
    T_{\bar{z} \bar{z}} 
    &= \frac{1}{4} (T_{00}+2i T_{10}-T_{11})
    \\
    T_{z \bar{z}} = T_{\bar{z}z}
    &= \frac{1}{4} (T_{00}+T_{11})
\end{aligned}
$$

Since the energy-momentum tensor for 2D CFT is traceless, we can
simplify the relations further:

$$
\begin{aligned}
    T_{z z}
    &= \frac{1}{2} (T_{00}-i T_{10})
    \\
    T_{\bar{z} \bar{z}}
    &=\frac{1}{2} (T_{00}+i T_{10})
    \\
    T_{z \bar{z}} = T_{\bar{z}z} &=0
\end{aligned}
$$

We now show that $T_{z z},T_{\bar{z} \bar{z}}$ depends only on $z$ and $\bar{z}$ respectively, so we define

$$
T(z)\equiv 2\pi  T_{z z}(z), 
\quad
\bar{T}(\bar{z}) \equiv 2\pi T_{\bar{z} \bar{z}}(\bar{z})
$$

*Proof*:

Recall that

$$
\partial^{\mu}T_{\mu  \nu}=0
$$

In *Euclidean* spacetime, this is explicitly

$$
\partial_0T_{00}+\partial_1T_{10}
= \partial_0T_{01}+\partial_1T_{11}
= 0
$$

Since the energy-momentum tensor is traceless and symmetric:

$$
\begin{aligned}
    \partial_{\bar{z}}T_{z z}
    &= \frac{1}{4} 
    (\partial_0 + i\partial_1)
    (T_{00} - i T_{10})
    \\
    &= \frac{1}{4} (
        \partial_0T_{00}
        - i \partial_0 T_{10}
        + i \partial_1 T_{00}
        +\partial_1T_{10}
    )
    \\
    &= \frac{1}{4} (
        \partial_0T_{00}
        - i \partial_0 T_{01}
        - i \partial_1 T_{11}
        +\partial_1T_{10}
    )
    \\
    &= \frac{1}{4} [
        (\partial_0T_{00} + \partial_1T_{10})
        - i (\partial_0T_{01} + \partial_1T_{11})
    ]
    = 0
\end{aligned}
$$

Similarly, we can show that $\partial_zT_{\bar{z} \bar{z}}=0$.
$\blacksquare$

### Conformal Ward-Takahashi Identity 

### Conserved Charge of Conformal Symmetry 

The conserved charge corresponding to the conformal transformation $x\to x+\epsilon$ on the cylinder is given by

$$
Q=\int_0^L dx^1 \, j_0
\quad
\text{at } x^0 = \text{const}
$$

Here the current $j_{\mu}=T_{\mu  \nu} \epsilon^{\nu}$, and $L$ is the circumference of the cylinder. 

After mapping to the complex plane using $z=e^{x^0+i x^1}$, constant $x^0$ becomes constant $|z|$. The radius of the integration contour is then $R=\exp \left(x^0\right)$, and

$$
\oint dz \, f(z)
= i R \int_0^{2 \pi R} dx^1 \, e^{i x^1} f(x^1)
$$

Then

$$
\begin{aligned}
    \int_0^{2\pi R} dx^1 \, j_0
    &=\int_0^{2 \pi R} dx^1 \, e^{i x^1}
    \left(j_0 e^{-i x^1} \right)
    \\
    &= \frac{1}{i R} \oint dz 
    \left(j_0 e^{-i x^1} \right)
    =
    \frac{1}{i} \oint dz 
    \left(j_0 e^{-x^0 - i x^1} \right)
    \\
    &=\frac{1}{i} \oint dz \, \frac{j_0}{z}
\end{aligned}
$$

Find the holomorphic components of the current

$$
\begin{aligned}
    j_0 
    &= \frac{\partial z}{\partial x^0}j_z+\frac{\partial \bar{z}}{\partial x^0}j_{\bar{z}}
    = j_z+j_{\bar{z}}
    \\
    &= T_{z z} \epsilon (z)+T_{\bar{z} \bar{z}} \epsilon (\bar{z})
    \\
    &= \frac{1}{2\pi} (
        T(z) \epsilon(z)
        + \bar{T}(\bar{z}) \bar{\epsilon}(\bar{z})
    )
\end{aligned}
$$

When integrating, we need to treat $\bar{z}$ as the complex conjugate of $z$:

$$
\frac{1}{i} \oint dz
= \frac{1}{i} \oint d\bar{z}
= -\frac{1}{i} \oint d\bar{z}
$$

So the integration is converted to a contour integration around the origin:

$$
Q
\equiv Q_{\epsilon} + Q_{\bar{\epsilon}}
= \frac{1}{2 \pi i} \left(
    \oint dz \, T(z)\epsilon (z)
    + \oint d\bar{z} \, \bar{T}(\bar{z}) \bar{\epsilon}(\bar{z})
\right)
$$

Both contours are counter-clockwise. The *Ward identity* implies that $Q$ is the generator of conformal transformations, i.e.

$$
\begin{aligned}
    \delta_{\epsilon ,\bar{\epsilon}} \phi(w,\bar{w})
    &= -\left[Q, \phi(w,\bar{w})\right]
    \\
    &= -\frac{1}{2 \pi i} \oint dz \, [
        T(z)\epsilon (z), 
        \phi(w,\bar{w})
    ]
    \\ &\quad
    - \frac{1}{2 \pi i} \oint d\bar{z} \, [
        \bar{T}(\bar{z}) \bar{\epsilon}(\bar{z}),
        \phi(w,\bar{w})
    ]
\end{aligned}
$$

Using normal ordering, we can simplify further to

$$
\delta_{\epsilon ,\bar{\epsilon}} \phi(w,\bar{w})
= -\frac{1}{2 \pi i} \oint_w dz \, 
\epsilon (z) T(z)\phi(w,\bar{w})
+ \text{anti-holomorphic}
$$

### Operator Product Expansion (OPE)

Previously, we have derived that for a quasi-primary field

$$
\delta_{\epsilon ,\bar{\epsilon}} \phi 
=
- (h \phi  \partial \epsilon + \epsilon \partial \phi)
- (
    \bar{h} \phi \bar{\partial} \bar{\epsilon}
    + \bar{\epsilon} \bar{\partial} \phi
)
$$

We identify that

$$
\begin{aligned}
    &h \phi(w,\bar{w}) \partial_w \epsilon (w) + \epsilon (w) \partial_w \phi(w,\bar{w})
    \\ &\qquad
    =\frac{1}{2 \pi i} \oint_w dz \epsilon
    (z) T(z)\phi(w,\bar{w})
\end{aligned}
$$

and similarly for the anti-holomorphic part. But we can write the LHS as integral around the point $w$ using Cauchy integral formula (acting on the coordinate change $\epsilon$ only:

$$
\begin{aligned}
    h \phi(w,\bar{w}) \partial_w\epsilon (w)
    &= \frac{1}{2 \pi i} \oint_w dz \frac{\epsilon(z)}{(z-w)^2}h \phi(w,\bar{w})
    \\
    \epsilon (w)\partial_w\phi(w,\bar{w})
    &= \frac{1}{2 \pi i} \oint_w dz \frac{\epsilon(z)}{z-w} \partial_w\phi(w,\bar{w})
\end{aligned}
$$

Therefore

$$
\begin{aligned}
    T(z)\phi(w,\bar{w})
    &= \frac{h}{(z-w)^2} \phi(w,\bar{w})
    + \frac{1}{z-w} \partial_w \phi(w,\bar{w})
    + \text{reg.}
    \\
    \bar{T} (\bar{z}) \phi(w,\bar{w})
    &= \frac{\bar{h}}{(\bar{z}-\bar{w})^2} \phi(w,\bar{w})
    + \frac{1}{\bar{z}-\bar{w}} \partial_{\bar{w}} \phi(w,\bar{w})
    +\text{reg.}
\end{aligned}
$$

### Conformal Ward-Takahashi Identity

## OPE of Energy-Momentum Tensor with Itself

### Laurent Mode Expansion of the Fields

#### Around the Origin

A field $\phi(z, \bar{z})$ of conformal dimensions
$(h, \bar{h})$ can be expanded as a Laurent series around the
origin 0:

$$
\phi(z, \bar{z})
= \sum_{m=-\infty}^{\infty} \sum_{n=-\infty}^{\infty} 
z^{-m-h} \bar{z}^{-n-\bar{h}} \phi_{m,n}
$$

Using the Cauchy Integral Formula, the modes are

$$
\phi_{m,n} = 
\frac{1}{2 \pi i} \oint dz \, z^{m+h-1} 
\frac{1}{2 \pi i} \oint d\bar{z} \, \bar{z}^{n+\bar{h}-1} \phi(z, \bar{z})
$$

Taking the Hermitian conjugate of the field:

$$
\phi^\dagger(z, \bar{z})
= \sum_{m=-\infty}^{\infty} \sum_{n=-\infty}^{\infty} 
\bar{z}^{-m-h} z^{-n-\bar{h}} \phi_{m,n}^\dagger
$$

Meanwhile, we have

$$
\begin{aligned}
    \phi^\dagger(z, \bar{z})
    &= \bar{z}^{-2h}z^{-2\bar{h}} 
    \phi \left(\frac{1}{\bar{z}}, \, \frac{1}{z} \right)
    \\
    &=\bar{z}^{-2h}z^{-2\bar{h}} 
    \sum_{m=-\infty}^{\infty} \sum_{n=-\infty}^{\infty} 
    \bar{z}^{m+h} z^{n+\bar{h}} \phi_{m,n} 
    \\
    &= \sum_{m=-\infty}^{\infty} \sum_{n=-\infty}^{\infty}
    \bar{z}^{m-h} z^{n-\bar{h}} \phi_{m,n}
\end{aligned}
$$

Now we find that

$$
\phi_{-m,-n} = \phi_{m,n}^\dagger
$$

#### Around Any Point 

For simplicity, we now focus on holomorphic fields depending only on $z$. It is possible to expand around an arbitrary point $w$, instead of the origin:

$$
\begin{aligned}
    \phi(z) 
    &= \sum_n (z-w)^{-n-h} \phi_n(w), 
    \\
    \phi_n(w)
    &=\frac{1}{2 \pi i} \oint_w dz \, z^{n+h-1} \phi(z)
\end{aligned}
$$

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

## Normal Ordering

From the general form of the OPE of two operators $A,B$

$$
A(z)B(w)
= \sum_{n=-\infty}^N 
\frac{\{A B\}_n (w)}{(z - w)^n} \quad
(N\in \mathbb{N})
$$

we *define* the **normal ordered product** of $A(w),B(w)$ as

$$
(A B)(w)=\{A B\}_0(w)
$$

There are several ways to write this expression more concretely.

### Contraction

The **contraction** of $A(z)B(w)$ is *defined* as the sum of all *singular* terms of the OPE:

$$
A(z)B(w) \equiv 
\sum_{n=1}^N \frac{\{A B\}_n(w)}{(z-w)^n}
$$

Then

$$
(A B)(w)
= \lim_{z\to w} \left(
    A(z) B(w) - A(z) B(w)
\right)
$$

### Contour Integration

$$
(A B)(w) = 
\frac{1}{2 \pi i} \oint_w \frac{dz}{z-w} A(z) B(w)
$$

Here *radial ordering* is implicitly assumed in the integral.

*Proof*: By direct verification

$$
\begin{aligned}
    \text{RHS}
    &= \sum_{n=-\infty}^N \frac{1}{2 \pi i} 
    \oint_w dz \frac{\{A B\}_n(w)}{(z-w)^{n+1}}
    \\
    &= \sum_{n=-\infty}^N \frac{1}{n!} \left[
        \frac{d^n}{dz^n} (\{AB\}_n(w))
    \right]_{z=w}
\end{aligned}
$$

Only the $n=0$ term survives:

$$
\text{RHS} = \{A B\}_0(w)
\equiv (A B)(w)
\quad \blacksquare
$$

### Mode Expansion

We Laurent expand the normal ordered product around the origin as

$$
(A B)(w)=\sum_n  w^{-n-h_A-h_B} (A B)_n
$$

Then the modes $(A B)_n$ are found to be

$$
(A B)_n
= \sum_{m \le -h_A} A_m B_{n-m}
+ \sum_{m \ge -h_A} B_{n-m} A_m
$$

*Proof*:

![image](Operator Formalism_gr3.eps)

$$
\begin{aligned}
    &(A B)(w)
    =\frac{1}{2 \pi i} \oint_w\frac{dz}{z-w}A(z)B(w)
    \\
    &\quad
    =\frac{1}{2 \pi i} 
    \oint_{|z|>|w|} \frac{dz}{z-w}A(z)B(w)
    - \frac{1}{2 \pi i} 
    \oint_{|z|<|w|} \frac{dz}{z-w}B(w)A(z)
\end{aligned}
$$

Now we evaluate the two terms separately. First, expand $A(z)$ and
$B(w)$ around the same point $x$:

$$
\begin{aligned}
    A(z) &= \sum_m (z-x)^{-m - h_A} A_m(x)\\
    B(w) &= \sum_p (w-x)^{-p - h_B} B_p(x)
\end{aligned}
$$

- For 1st term:

    We further impose the requirement $|z|>|x|>|w|$ so that we can also expand the $1/(z-w)$ factor in the integrals as

    $$
    \begin{aligned}
        \frac{1}{z-w} 
        &= \frac{1}{(z-x)-(w-x)}
        \\
        &= \frac{1}{(z-x)} \left(
            1 - \frac{w-x}{z-x} 
        \right)^{-1}
        \\
        &=\sum_{l\ge 0} \frac{(w-x)^l}{(z-x)^{l+1}}
    \end{aligned}
    $$

    Then

    $$
    \begin{aligned}
        \text{1st term}
        &\equiv \frac{1}{2 \pi i} 
        \oint_{|z|>|w|} \frac{dz}{z-w} A(z) B(w)\\
        &= \sum_{m,p} \sum_{l\ge 0} 
        \frac{1}{2 \pi i} \oint_{|z|>|w|} dz 
        \frac{(w-x)^{l-p-h_B} A_m(x) B_p(x)}
            {(z-x)^{m+h_A+l+1}}
    \end{aligned}
    $$

    In this integral, the only singular point in the integration path is $x$. By the Residue Theorem, only the term with $m+h_A+l+1=1$ contributes. Since $l\ge 0$, the summation range of $m$ is now $m\le -h_A$:

    $$
    \text{1st term}
    =\sum_{p} \sum_{m\le -h_A} 
    (w-x)^{-m-p-h_A-h_B} A_m(x) B_p(x)
    $$

- For term 2:

    Now $|w|>|x|>|z|$, thus the $1/(z-w)$ factor should be expanded as

    $$
    \begin{aligned}
        \frac{1}{z-w}
        &= -\frac{1}{(w-x)-(z-x)}
        \\
        &= -\frac{1}{(w-x)} \left(1-\frac{z-x}{w-x} \right)^{-1}
        \\
        &=-\sum_{l\ge 0} \frac{(z-x)^l}{(w-x)^{l+1}}
    \end{aligned}
    $$

    Then

    $$
    \begin{aligned}
        \text{2nd term} &\equiv
        -\frac{1}{2 \pi i} 
        \oint_{|z|<|w|} \frac{dz}{z-w} B(w) A(z)
        \\
        &=\sum_{m,p} \sum_{l\ge 0} \frac{1}{2 \pi i} \oint_{|z|<|w|}dz \frac{(w-x)^{-l-1-p-h_B}B_p(x)A_m(x)}{(z-x)^{m+h_A-l}}
    \end{aligned}
    $$

    Only the term with $m+h_A-l=1$ contributes. Then the summation range of $m$ becomes $m\ge -h_A+1$, or $m>-h_A$:

    $$
    \text{2nd term} 
    = \sum_{p} \sum_{m > -h_A} 
    (w-x)^{-m-p-h_A-h_B} B_p(x) A_m(x)
    $$

Collect the two terms:

$$
\begin{aligned}
    (A B)(w)
    &= \sum_{p} \sum_{m\le -h_A} (w-x)^{-m-p-h_A-h_B}A_m(x)B_p(x)
    \\ &\qquad
    + \sum_{p} \sum_{m>-h_A} (w-x)^{-m-p-h_A-h_B}B_p(x)A_m(x)
\end{aligned}
$$

Define $n=m+p$, and change summation over $p$ to over $n$, then

$$
\begin{aligned}
    (A B)(w)
    &= \sum_{n} \sum_{m\le -h_A} (w-x)^{-n-h_A-h_B} A_m(x) B_{n-m}(x)
    \\ &\qquad
    + \sum_{n} \sum_{m>-h_A} (w-x)^{-n-h_A-h_B} B_{n-m}(x) A_m(x)
    \\
    &=\sum_n (w-x)^{-n-h_A-h_B} 
    \\ &\qquad \times
    \left(
        \sum_{m\le -h_A} A_m(x) B_{n-m}(x)
        + \sum_{m>-h_A} B_{n-m}(x) A_m(x)
    \right) \blacksquare
\end{aligned}
$$

## Descendant States and Fields

### Descendants States

#### Conformal Operators Acting on the Vacuum State

The energy of the ground state is fixed to zero. This requires that

$$
T(z)|0\rangle
= \sum_n z^{-n-2} L_n |0\rangle
$$

and the anti-holomorphic $\bar{T}(\bar{z}) |0\rangle$ are well-defined as $z, \bar{z} \to 0$ (no divergence). Then we must have

$$
\begin{cases}
    L_n|0\rangle =0 \\
    \bar{L}_n|0\rangle =0
\end{cases}
\quad
\text{for } -n - 2 \le -1 
\text{ or } n \ge -1
$$

These include the invariance of the vacuum with respect to the *global* conformal transformations generated by $L_{-1},L_0,L_1$ and their anti-holomorphic counterparts, which means that $|0\rangle$ *must be annihilated by these operators*.

Now we also have

$$
\langle 0| T(z) |0\rangle 
= \langle 0 | \bar{T}(\bar{z}) | 0\rangle =0
$$

#### Conformal Operators Acting on the Asymptotic State

Consider the $L_n, \bar{L}_n$ operators acting on the *asymptotic state*

$$
|h,\bar{h} \rangle 
\equiv \phi(0,0) |0\rangle
$$

Here $\phi(z, \bar{z})$ is a *primary field* with conformal dimensions $(h, \bar{h})$. Because we have already know the action on the vacuum, we may calculate

$$
[L_n,\phi(0,0)] |0\rangle 
= L_n\phi(0,0)|0\rangle -  \phi(0,0)L_n|0\rangle
$$

When $n\ge -1$, the second term vanishes. Then

$$
[L_n,\phi(0,0)] |0\rangle 
= L_n\phi(0,0) |0\rangle 
= L_n |h,\bar{h} \rangle
$$

Now we evaluate the commutator

$$
\begin{aligned}
    [L_n,\phi(w,\bar{w})]
    &= \frac{1}{2 \pi i} \oint_w dz \,
    z^{n+1} \underbrace{T(z)\phi(w,\bar{w})}_{\text{use OPE}} 
    \\
    &= \frac{1}{2 \pi i} \oint_w dz \,
    z^{n+1} \left[
        \frac{h \phi(w,\bar{w})}{(z-w)^2}
        + \frac{\partial_w\phi(w,\bar{w})}{z-w}
        + \text{reg.}
    \right]
    \\
    &= \left[
        \frac{d}{dz} \left(z^{n+1}h \phi(w,\bar{w})\right)
    \right]_{z=w} + \left[
        z^{n+1} \partial_w\phi(w,\bar{w})
    \right]_{z=w} 
    \\
    &= h(n+1) w^n \phi(w,\bar{w})
    + w^{n+1} \partial_w \phi(w,\bar{w})
\end{aligned}
$$

Similarly

$$
[\bar{L}_n, \phi(w,\bar{w})]
= \bar{h}(n+1)\bar{w}^n \phi(w,\bar{w})
+ \bar{w}^{n+1} \partial_{\bar{w}} \phi(w,\bar{w})
$$

Finally

$$
\begin{aligned}
    L_0|h,\bar{h} \rangle &= h|h,\bar{h} \rangle
    \\
    \bar{L}_0|h,\bar{h} \rangle &= \bar{h}|h,\bar{h} \rangle
    \\ 
    L_n|h,\bar{h} \rangle &= 0
    \\
    \bar{L}_n|h,\bar{h} \rangle &= 0
    \qquad (n > 0)
\end{aligned}
$$

Since $L_0+\bar{L}_0$ is proportional to the system Hamiltonian, we find
that $|h,\bar{h} \rangle$ *is an energy eigenstate*.

### Ladder Operators

To find excited states above the asymptotic state, we need the *ladder operators*. It turns out that they can be chosen as the *Laurent modes* $\phi_n$ *of the holomorphic field* $\phi(w)$ *with conformal dimension* $h$.

$$
\phi(z) = \sum_n z^{-n-h} \phi_n, \quad
\phi_n = \frac{1}{2 \pi i} \oint dz \, z^{n+h-1} \phi(z)
$$

To show this, we calculate the commutator $[L_n, \phi_m]$ using the equation

$$
[A,B] = \oint_0 dw \oint_w dz \, a(z) b(w)
$$

Recall that

$$
L_n = \frac{1}{2 \pi i} \oint dz z^{n+1} T(z)
$$

then

$$
\begin{aligned}
    &\left[L_n,\phi_m\right]
    \\
    &= \frac{1}{2 \pi i} \oint_0 dw \, w^{m+h-1} 
    \frac{1}{2 \pi i} \oint_w dz \, z^{n+1}T(z)\phi(w)
    \\
    &= \frac{1}{2 \pi i} \oint_0 dw \, w^{m+h-1} 
    \frac{1}{2 \pi i} \oint_w dz \, z^{n+1} 
    \left[
        \frac{h \phi(w)}{(z-w)^2}
        + \frac{\partial_w\phi(w)}{z-w}
        + \text{reg.}
    \right]
    \\
    &= \frac{1}{2 \pi i} \oint_0 dw w^{m+h-1} 
    \left(
        h (n+1) w^n \phi(w) 
        + w^{n+1} \partial_w \phi(w)
    \right)
    \\
    &= \frac{1}{2 \pi i} \oint_0 dw \left(
        h (n+1) w^{m+n+h-1} \phi(w)
        + \underbrace{w^{m+n+h} \partial_w\phi(w)}_{\text{integrate by parts}}
    \right)
    \\
    &= \frac{1}{2 \pi i} \oint_0 dw \left(
        h(n+1)w^{m+n+h-1} \phi(w)
        - (m+n+h) w^{m+n+h-1} \phi(w)
    \right)
    \\
    &= \frac{1}{2 \pi i} \oint_0 dw 
    (n(h-1)-m) w^{m+n+h-1} \phi(w)
\end{aligned}
$$

This implies that

$$
[L_n, \phi_m] = (n(h-1)-m) \phi_{n+m}
$$

In particular,

$$
\begin{aligned}
    [L_0, \phi_m] &= -m \phi_m\\
    [L_0, \phi_{-m}] &= m \phi_{-m}
\end{aligned}
$$

This means that $\phi_{\pm m} (m>0)$ act as *lowering and raising operators for the eigenstates of* $L_0$: from $L_0|h\rangle =h|h\rangle$ we obtain

$$
\begin{aligned}
    L_0 (\phi_{\pm m}|h\rangle )
    &= [L_0, \phi_{\pm m}] |h\rangle 
    + \phi_{\pm m} L_0 |h\rangle 
    \\
    &= \mp m \phi_{\pm m} |h\rangle 
    + h \phi_{\pm m} |h\rangle 
    \\
    &= (h\mp m) (\phi_m |h\rangle)
\end{aligned}
$$

i.e. $\phi_{\pm m}|h\rangle$ is the eigenstate of $L_0$ with
eigenvalue $h\mp m$.

But we still have another choice. Recall that in the Virasoro algebra

$$
[L_n, L_m] 
= (n-m) L_{n+m}
+ \frac{c}{12} n (n^2 - 1) \delta_{n+m, 0}
$$

Specially, for $n=0$

$$
\begin{aligned}
    [L_0, L_m] &= -m L_m\\
    [L_0, L_{-m}] &= m L_{-m}
\end{aligned}
$$

which has the *same* form as $\left[L_0,\phi_{\pm m} \right]$. Therefore, $L_{\pm m} (m>0)$ can also *lower and raise the conformal dimension*.

Finally, we remark that

$$ L_{-n}=L_n^\dagger $$

### Descendant States {#descendant-states .unnumbered .unnumbered}

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

*Theorem*: Descendant states belonging to different levels are orthogonal.

*Proof*:

- We first consider the simple case

    $$
    |i\rangle =L_{-M}|h\rangle , \quad |j\rangle =L_{-N}|h\rangle
    \quad (N, M > 0, N \ne M)
    $$

    In the following calculation, since $L_n$ are not Hermitian, we can only apply them to *kets*. Then

    $$
    \begin{aligned}
        \langle i|j \rangle 
        &= \langle h | L_M L_{-N} | h \rangle 
        = \langle h | L_{-N} L_M + [L_M,L_{-N}] | h \rangle
        \\
        &=\langle h|L_{-N} \underbrace{L_M|h\rangle}_0
        \\ &\qquad
        + \left\langle h \left|
            (M-N) L_{M-N} 
            + \frac{c}{12} M (M^2-1) \delta_{M+N, 0} 
        \right| h\right\rangle
        \\
        &=(M-N)\left\langle h\left|L_{M-N} \right|h\right\rangle
    \end{aligned}
    $$

    Without loss of generality, assume $M>N$, then $L_{M-N}|h\rangle =0$, and we proved that $\langle i|j\rangle =0$. 
    
    (If $M<N$, we can calculate its the complex conjugate $\left\langle h\left|L_{N-M} \right|h\right\rangle =0$, so it is also zero)

- In general, let

    $$
    \begin{aligned}
        |i\rangle &= L_{-k_1} \cdots L_{-k_m}|h\rangle , 
        &\quad 
        &k_1 + \cdots + k_m = M
        \\
        |j\rangle &= L_{-l_1} \cdots L_{-l_n}|h\rangle , 
        &\quad
        &l_1 + \cdots + l_n = N \ne M
    \end{aligned}
    $$

    We calculate

    $$
    \langle i|j\rangle 
    = \langle h | 
        L_{k_m} \cdots L_{k_1}
        L_{-l_1} \cdots L_{-l_n}
    | h \rangle
    $$


#### Highest-Weight Representation

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

### Verma Module

There are obviously $p(N)$ *linearly independent* states at level $N$, where $p(N)$ is the *number of partitions of the integer* $N$. It can be generated from the Taylor expansion of the Euler function

$$
\frac{1}{\varphi (q)} 
\equiv \prod_{n=1}^{\infty} \frac{1}{1-q^n}
= \sum_{n=0}^{\infty} p(n)q^n
$$

The subset of the full Hilbert space generated by the asymptotic state $|h\rangle$ and its descendants is closed under the action of the Virasoro generators. Thus it forms a *representation* (more correctly, a **module**) of the Virasoro algebra. This subspace is called a **Verma module**, denoted $V(c,h)$. The notation specifies the central charge $c$ and the highest weight $h$.

The following table lists the first few levels of a Verma module.

$$
\begin{array}{ccl}
\hline
l & p(l) & \text{Descendants} \\
\hline
0 & 1 & |h\rangle  \\
1 & 1 & L_{-1}|h\rangle  \\
2 & 2 & L_{-1}^2|h\rangle , L_{-2}|h\rangle  \\
3 & 3 & L_{-1}^3|h\rangle \text{,}L_{-1}L_{-2}|h\rangle \text{,}L_{-3}|h\rangle  \\
\end{array}
$$

In addition, the Verma module generated by the anti-holomorphic
operators $\{\bar{L}_{-n} \}$ is denoted by
$\bar{V}(c,\bar{h})$.

#### Virasoro Characters

For a Verma module $V(c,h)$, we define its **character** as

$$
\chi_{(c,h)}(\tau)
= \text{Tr} q^{L_0-c/24}
= \sum_{n=0}^{\infty} \dim (h+n) \times q^{n+h-c/24}
$$

Here $q\equiv \exp (2 \pi i \tau) \, (\tau \in \mathbb{C})$, and $\dim (h+n)$ is the number of linearly independent states at level $n$, which is equal to $p(n)$. Hence

$$
\chi_{(c,h)}(\tau)
= q^{h-c/24} \sum_{n=0}^{\infty} p(n) q^n
=\frac{q^{h-c/24}}{\varphi (q)}
$$

Using the **Dedekind function**

$$
\eta (\tau)\equiv q^{1/24} \varphi (q)=q^{1/24} \prod_{n=1}^{\infty}  \left(1-q^n\right)
$$

then

$$
\chi_{(c,h)}(\tau)
=\frac{q^{h+(1-c)/24}}{\eta (\tau)}
$$

#### Reducible Verma Modules

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

### Descendant Fields

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
\begin{aligned}
    \phi^{(-n)}(w)
    &= \frac{1}{2 \pi i} \oint_w dz (z-w)^{-n+1}T(z)\phi(w)
    \\
    &= L_{-n}(w)\phi(w)
    \\
    &\equiv \left(L_{-n} \phi \right)(w)
\end{aligned}
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
\begin{aligned}
    &\phi^{\left(-k_1,-k_2,\cdots,k_m\right)}(w)
    = (L_{-k_1}L_{-k_2} \cdots L_{-k_m} \phi)(w)
    \\
    &= \frac{1}{2 \pi i} \oint_w dz \, 
    (z-w)^{-k_1+1} T(z) \phi^{(-k_2,...,-k_m)}(w)
\end{aligned}
$$

In particular, we need to emphasize that $\phi^{(0,-n)}$ is *not* the same as $\phi^{(-n)}$:

$$
\phi^{(0,-n)}(w) = (h+n)\phi^{(-n)}(w)
$$

Another commonly used relation is

$$ 
\phi^{(-1,-n)}(w) = \partial \phi^{(-n)}(w)
$$

### A Representation of the Conformal Generators

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
    \frac{(n-1)h_i}{\left(w_i-w\right)^n}
    - \frac{1}{\left(w_i-w\right)^{n-1}} \partial_{w_i} 
\right]
$$

In particular

$$
\mathcal{L}_{-1} = \partial_w
$$

*Proof*:

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

## Conformal Families

The set consisting of a *primary field* $\phi$ and *all of its descendants* is called a **conformal family**, sometimes denoted by $[\phi]$. The members of a family *transform amongst themselves under conformal transformations*.

### OPE of $T(z)$ with Descendant Fields

### The Operator Algebra

## Conformal Blocks

## Example: Free Boson

Here $L$ is the circumference of the cylinder. This means that the space is *compactified* with the length $L$, and we take the periodic boundary condition:

$$
\phi(t,x+L) = \phi(t,x)
$$

### Hamiltonian

Due to the periodicity in space, we expand the field as a Fourier series:

$$
\begin{aligned}
    \phi(t,x) 
    &= \sum_n \exp \left(\frac{2\pi i n}{L}x\right)
    \phi_n(t)
    \\
    \phi_n(t) &= \frac{1}{L} 
    \int dx \exp \left(-\frac{2\pi i n}{L}x\right)
    \phi(t,x)
\end{aligned}
$$

Since the field is real, we get

$$ 
\phi_{-n}=\phi_n^\dagger
$$

Now we recast the Lagrangian using the Fourier modes (in the process of canonical quantization, we always use the Minkowski space)

$$
\begin{aligned}
    \mathcal{L}
    &=\frac{1}{2}h\int dx \left[\left(\partial_t\phi \right)^2-\left(\partial_x\phi \right)^2\right]
    \\
    &= \frac{1}{2}h\int dx \left[
        \sum_{n,m}  
        \exp \left(i\frac{2\pi  n}{L}x\right)
        \exp \left(i\frac{2\pi  m}{L}x\right)
        \dot{\phi}_n(t) \dot{\phi}_m(t)
        \right.
        \\ &\qquad
        \left.
        -\left(\frac{2\pi i}{L} \right)^2
        \sum_{n,m}  n m 
        \exp \left(i\frac{2\pi  n}{L}x\right)
        \exp \left(i\frac{2\pi  m}{L}x\right)
        \phi_n(t) \phi_m(t)
    \right]
\end{aligned}
$$

First, we integrate over $x$ and make use of the completeness relation

$$
\int_0^Ldx 
\exp \left(\frac{2\pi i}{L} (n-m)x\right)
=L \delta_{n m}
$$

Then

$$
\mathcal{L}
= \frac{1}{2} h L
\sum_n \left[
    \dot{\phi}_n \dot{\phi}_{-n}
    - \left( \frac{2\pi n}{L} \right)^2 \phi_n \phi_{-n}
\right]
$$

We can now construct the Hamiltonian: the momentum conjugate to $\phi_n$ is

$$
\pi_n
= \frac{\partial \mathcal{L}}{\partial \dot{\phi}_n}
= h L \dot{\phi}_{-n}
$$

(the sum over all $n$ contributes a factor of 2) and we impose the commutation relation $\left[\phi_n,\pi_m\right]=i \delta_{n m}$.

Because $\phi_{-n}=\phi_n^\dagger$, we have for the momentum

$$
\pi_{-n}=\pi_n^\dagger
$$

Then

$$
\begin{aligned}
    H &=\sum_n  \pi_n\dot{\phi}_n-\mathcal{L} 
    \\
    &= \sum_n  \pi_n \frac{\pi_{-n}}{h L}
    - \frac{1}{2} h L \sum_n \frac{\pi_{-n}}{h L} \frac{\pi_n}{h L}
    + \frac{1}{2} h L \sum_n  \left(\frac{2\pi  n}{L} \right)^2 \phi_n \phi_{-n} 
    \\
    &=\frac{1}{2 h L} \sum_n  \left[
        \pi_n\pi_{-n}
        + (2\pi n h)^2 \phi_n \phi_{-n} 
    \right]
\end{aligned}
$$

Now we change $n\to -n$:

$$
\begin{aligned}
    H 
    &=\frac{1}{2 h L} \sum_n \left[
        \pi_{-n} \pi_n
        + (2\pi  n h)^2\phi_{-n} \phi_n
    \right]
    \\
    &=\sum_n \left[
        \frac{1}{2h L} \pi_n^\dagger \pi_n
        + \frac{1}{2} h L \left(\frac{2\pi n}{L} \right)^2 \phi_n^\dagger \phi_n
    \right]
\end{aligned}
$$

This represents a sum of *decoupled harmonic oscillators* of frequencies

$$
\omega_n=\frac{2\pi  |n|}{L} \quad
\left(
    \text{comparing with } 
    \frac{p^2}{2m}+\frac{1}{2}m \omega^2x^2, 
    \text{with } m=h L
\right)
$$

However, *the* $n=0$ *mode vanishes*: it is a consequence of the absence of a mass term, which, with the boundary conditions chosen, is the same as conformal invariance.

### Creation and Annihilation Operators

For each mode $n$, we can define the creation and annihilation operators in a way analogous to the simple harmonic oscillator:

SHO:

$$
H=\frac{1}{2}m \omega^2x^2+\frac{1}{2m}p^2 
\Rightarrow
a=\sqrt{\frac{m \omega}{2}} \left(x+\frac{i}{m \omega}p\right)
$$

Free boson CFT:

$$
\begin{aligned}
    a_n 
    &=\sqrt{\frac{1}{2}h L \frac{2\pi  |n|}{L}} \left(\phi_n+\frac{i}{2\pi h L |n|/L} \pi_n\right)
    \\
    &=\sqrt{\pi h |n|} \left(
        \phi_n + \frac{i}{2\pi  |n| h} \pi_n
    \right)
    \\
    &=\frac{1}{\sqrt{4\pi |n| h}} (
        2\pi |n| h \phi_n+i \pi_n
    )
\end{aligned}
$$

We now have

$$
\left[a_n,a_m\right]=0, \left[a_n,a_m^\dagger \right]=\delta_{n m}
$$

But this definition does not apply to the $n=0$ mode.
