## The Conformal Group in 2D

### Conformal Mappings in 2D

Apply the general constraint on conformal transformation

$$
\partial_{\mu}\epsilon_{\nu}(x) 
+ \partial_{\nu}\epsilon_{\mu}(x)
= \frac{2}{d} 
(\partial_{\rho} \epsilon^{\rho}(x))
\eta_{\mu \nu}
$$

to the $d=2$ case, we find

$$
\partial_0\epsilon_0 = \partial_1\epsilon_1, \quad
\partial_0\epsilon_1 = -\partial_1\epsilon_0
$$

which is the same as the **Cauchy-Riemann relations** between the real and the imaginary parts of a *holomorphic function* in complex analysis. Then it is useful to construct the **holomorphic coordinates** from the Euclidean coordinates $x^0,x^1$:

$$
z=x^0+i x^1, \quad \bar{z}=x^0-i x^1
$$

$$
\epsilon =\epsilon^0+i \epsilon^1, 
\quad
\bar{\epsilon}=\epsilon^0-i \epsilon^1
$$

The two variables in a pair are to be regarded as *independent of each other*.

Now we can conclude that:

*A holomorphic function $f(z)=z+\epsilon (z)$ gives an infinitesimal 2D conformal transformation* $z\to f(z)$.

### Differentiation and Integration in Holomorphic Coordinates

The inverse relations are

$$
x^0 = \frac{1}{2}\left(z+\bar{z}\right),
\quad
x^1 = -\frac{i}{2}\left(z-\bar{z}\right)
$$

We also define the derivatives

$$
\begin{aligned}
    \partial \equiv \partial_z
    &= \frac{\partial x^{\rho}}{\partial z}
    \frac{\partial}{\partial x^{\rho}}
    =\frac{1}{2} (\partial_0 - i\partial_1 ),
    \\
    \bar{\partial} \equiv \partial_{\bar{z}}
    &= \frac{\partial x^{\rho}}{\partial \bar{z}}
    \frac{\partial}{\partial x^{\rho}}
    =\frac{1}{2} (\partial_0 + i \partial_1 )
\end{aligned}
$$

#### Jacobian

$$
\begin{aligned}
    \frac{D(z,\bar{z})}{D(x^0,x^1)}
    &= \det 
    \begin{pmatrix}
        \partial z / \partial x^0 & \partial z / \partial x^1 \\
        \partial \bar{z}/\partial x^0 & \partial \bar{z}/\partial x^1
    \end{pmatrix}
    \\
    &= \det 
    \begin{pmatrix}
        1 & i \\
        1 & -i \\
    \end{pmatrix}
    = -2i
\end{aligned}
$$

Therefore

$$ 
dz \, d\bar{z} = -2i \, dx^0 dx^1
$$

#### Laplacian

In particular, the Laplacian $\partial_{\rho}\partial^{\rho}$
becomes $\partial \bar{\partial}$, since

$$
\begin{aligned}
    \partial \bar{\partial}\phi 
    &= \frac{\partial x^{\rho}}{\partial z}
    \frac{\partial}{\partial x^{\rho}} \left(
        \frac{\partial x^{\sigma}}{\partial\bar{z}}
        \frac{\partial \phi}{\partial x^{\sigma}}
    \right)
    \\
    &= \frac{\partial x^{\rho}}{\partial z}
    \left(
        \frac{\partial}{\partial x^{\rho}}
        \frac{\partial x^{\sigma}}{\partial \bar{z}}
    \right)
    \frac{\partial \phi}{\partial x^{\sigma}}
    +
    \frac{\partial x^{\rho}}{\partial z}
    \frac{\partial x^{\sigma}}{\partial\bar{z}}
    \left(
        \frac{\partial}{\partial x^{\rho}}
        \frac{\partial \phi}{\partial x^{\sigma}}
    \right)
    \\
    &=\frac{\partial x^{\rho}}{\partial z}
    \underbrace{\frac{\partial \delta_{\rho}^{\sigma}}{\partial \bar{z}}}_0
    \frac{\partial \phi}{\partial x^{\sigma}}
    +
\end{aligned}
$$

#### The Metric Tensor

The flat metric in the holomorphic coordinates becomes

$$
g_{i j} =
\begin{pmatrix}
    1 & 0 \\
    0 & 1
\end{pmatrix}
\to
g_{a b} = 
\frac{\partial x^i}{\partial z^a}
\frac{\partial x^j}{\partial z^b}
g_{i j}
= \begin{pmatrix}
    0 & 1/2 \\
    1/2 & 0
\end{pmatrix}
$$

Here $z^0=z, z^1=\bar{z}$. For example:

$$
\begin{aligned}
    g_{z \bar{z}}
    &=\frac{\partial x^i}{\partial z}\frac{\partial x^j}{\partial \bar{z}}g_{i j}
    \\
    &= \frac{\partial x^0}{\partial z}\frac{\partial x^0}{\partial
    \bar{z}}+\frac{\partial x^1}{\partial z}\frac{\partial x^1}{\partial \bar{z}}
    \\
    &=\frac{1}{2}\times \frac{1}{2}+\frac{-i}{2}\times \frac{i}{2}=\frac{1}{2}
\end{aligned}
$$

The inverse of the metric is then

$$
g^{a b}
= \left(g_{a b}\right)^{-1}
= \begin{pmatrix}
    0 & 2 \\
    2 & 0
\end{pmatrix}
$$

### Global Conformal Transformations in 2D

$$
f(z)=\frac{a z+b}{c z+d}, \quad
\text{with }
\det \begin{pmatrix}
    a & b \\
    c & d 
\end{pmatrix} =1
$$

### The Witt Algebra

The generators of 2D conformal transformation can be found from the Laurent expansion (about the origin) of the mapping $z\to z+\epsilon (z)$: mathematically, we write

$$
z'= z + \sum_n \epsilon_n z^n
$$

However, in CFT, people adopt the convention

$$
z'=z+\sum_n  z^{n+1} \epsilon_n
$$

Then, for the transformation of a particular $n$, we have

$$
z' = z + z^{n+1} \epsilon_n
\equiv \left(1-l_n\right)z
$$

where $l_n$ is defined as the differential operator

$$
l_n \equiv -z^{n+1} \partial_z
$$

so that a finite transformation is the exponentiation $e^{-l_n}$. Thus $l_n$ is interpreted as a transformation **generator**.

Similarly, for the anti-holomorphic part, people write

$$
\bar{z}'
= \bar{z}+\sum_n  \bar{z}^{n+1} \bar{\epsilon}_n
= \left(1 - \sum_n \bar{l}_n\right) \bar{z}
$$

with

$$
\bar{l}_n=-\bar{z}^{n+1}\partial_{\bar{z}}
$$

The commutation rules of the generators $l_n,\bar{l}_n$ are

$$
\begin{aligned}
    [l_n, l_m] &= (n-m)l_{m+n}
    \\
    [\bar{l}_n, \bar{l}_m]
    &= (n-m)\bar{l}_{m+n}
    \\
    [l_n, \bar{l}_m] &= 0
\end{aligned}
$$

called the **Witt algebra**.

### Primary Fields


Fields *only depending on* $z$ (i.e. $\phi (z)$) are called **chiral fields**.

Fields *only depending on* $\bar{z}$ (i.e. $\phi (\bar{z})$) are called **anti-chiral fields**.

If a field $\phi (z, \bar{z})$ transforms under *any* (global or local) conformal transformations $z\to w(z)$ according to

$$
\phi (z, \bar{z}) 
\to 
\phi' (w, \bar{w})
= \left(\frac{dw}{dz}\right)^{-h}
\left(\frac{d\bar{w}}{d\bar{z}}\right)^{-\bar{h}}
\phi(z, \bar{z})
$$

then it is called a **primary field** with $\left(h,\bar{h}\right)$. If this transformation holds only for *global* conformal transformations, then $\phi$ is called a **quasi-primary fields**.

The conformal dimensions are related to the **scaling dimension** and the **planar spin** of the field by

$$
h=\frac{1}{2}(\Delta +s), \quad
\bar{h}=\frac{1}{2}(\Delta -s)
$$

#### Variation under Infinitesimal Conformal Transformations

Consider the infinitesimal transformation

$$
\begin{aligned}
    z &\to 
    w(z)=z+\epsilon (z)
    \\
    \bar{z} &\to 
    \bar{w}(\bar{z}) = \bar{z} + \bar{\epsilon}(\bar{z})
\end{aligned}
$$

($\epsilon (z)$ and $\bar{\epsilon}(\bar{z})$ are two *independent* transformations) for which

$$
\left(\frac{dw}{dz}\right)^{-h}
= (1 + \partial_z\epsilon)^{-h}
= 1 - h \partial_z \epsilon (z)
+ O(\epsilon^2)
$$

$$
\left(\frac{d\bar{w}}{d\bar{z}}\right)^{-\bar{h}}
= (1 + \partial_{\bar{z}}\bar{\epsilon})^{-\bar{h}}
= 1 - \bar{h}\partial_{\bar{z}}\bar{\epsilon}(\bar{z})
+ O(\bar{\epsilon}^2)
$$

Then

$$
\phi' (w, \bar{w})
\simeq \left(
    1 - h\partial_z\epsilon (z)
    - \bar{h}\partial_{\bar{z}}\bar{\epsilon}(\bar{z})
\right) \phi (z, \bar{z})
$$

Meanwhile, Taylor expansion gives

$$
\phi' (z, \bar{z})
\simeq \phi' (w, \bar{w})
- \epsilon (z)\partial \phi (z, \bar{z})
- \bar{\epsilon}(\bar{z})\bar{\partial} \phi (z, \bar{z})
$$

Thus the variation of the field is

$$
\begin{aligned}
    \delta_{\epsilon ,\bar{\epsilon}}\phi 
    &\equiv \phi' (z, \bar{z}) - \phi (z, \bar{z})
    \\
    &= - (
        h \phi \partial_z\epsilon 
        + \epsilon \partial_z\phi
    ) - (
        \bar{h} \phi \partial_{\bar{z}}\bar{\epsilon}
        + \bar{\epsilon}\partial_{\bar{z}}\phi
    )
\end{aligned}
$$

The subscript of $\delta$ means that the variation is due to both
$\epsilon$ and $\bar{\epsilon}$.

### Restriction on Correlation Functions

The conformal invariance imposes strong restriction on the possible
forms of the correlation functions of (quasi-)primary fields.

#### Two-Point Functions

$$
\langle \phi_i(z, \bar{z})\phi_j(w, \bar{w})\rangle 
= \frac{C_{i j} \delta_{h_i h_j} \delta_{\bar{h}_i \bar{h}_j}}
{(z-w)^{2h_i} (\bar{z}-\bar{w})^{2\bar{h}_i}}
$$

The Kronecker-deltas mean that the two-point function vanishes if the
conformal dimensions of the two fields are different.

#### Three-Point Functions