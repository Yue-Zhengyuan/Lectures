

### Energy-Momentum Tensor in 2D 

#### *Proposition*: CFT in 2D has traceless energy-momentum tensor

*Proof*:

#### Holomorphic Components of the Energy-Momentum Tensor 

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