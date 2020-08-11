## Energy-Momentum Tensor in 2D 

### *Proposition*: CFT in 2D has traceless energy-momentum tensor

*Proof*:

### Holomorphic Components of the Energy-Momentum Tensor 

The energy-momentum tensor $T_{\mu  \nu}$ transforms in the same way as the metric $g_{\mu  \nu}$:

$$
\begin{aligned}
    T'_{\mu \nu}
    &= \begin{pmatrix}
        T_{zz} & T_{z \bar{z}} \\
        T_{\bar{z} z} & T_{\bar{z}\bar{z}}
    \end{pmatrix}
    = T_{\rho \sigma}
    \frac{\partial x^\rho}{\partial z^\mu}
    \frac{\partial x^\sigma}{\partial z^\nu}
\end{aligned}
$$

For example:

$$
\begin{aligned}
    T_{z z} 
    &=
    \frac{\partial x^0}{\partial z} \frac{\partial x^0}{\partial z}T_{00}
    + \frac{\partial x^0}{\partial z} \frac{\partial x^1}{\partial z}T_{01}
    \\ &\qquad
    +\frac{\partial x^1}{\partial z} \frac{\partial x^0}{\partial z}T_{10}
    + \frac{\partial x^1}{\partial z} \frac{\partial x^1}{\partial z}T_{11}
    \\
    &= \frac{1}{2} \frac{1}{2}T_{00}
    + \frac{1}{2} \frac{-i}{2}T_{01}
    + \frac{-i}{2} \frac{1}{2}T_{10}
    + \frac{-i}{2} \frac{-i}{2}T_{11}
    \\
    &= \frac{1}{4} (T_{00} - 2i T_{10} - T_{11})
\end{aligned}
$$

Proceeding in the same way, we find

$$
\begin{aligned}
    T_{\bar{z} \bar{z}} 
    &= \frac{1}{4} (T_{00} + 2i \, T_{10} - T_{11})
    \\
    T_{z \bar{z}} = T_{\bar{z}z}
    &= \frac{1}{4} (T_{00}+T_{11})
\end{aligned}
$$

Since the energy-momentum tensor for 2D CFT is *traceless*, we can further simplify the relations to:

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
T(z)\equiv -2\pi  T_{z z}(z), 
\quad
\bar{T}(\bar{z}) \equiv -2\pi T_{\bar{z} \bar{z}}(\bar{z})
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