## Operator Product Expansion: <br>General Description

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

Both contours are counter-clockwise. Recall from the general QFT that the conserved charge $Q$ is the generator of the corresponding conformal transformation:

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

We identify that

$$
\begin{aligned}
    &h \phi(w,\bar{w}) \partial \epsilon (w) + \epsilon (w) \partial \phi(w,\bar{w})
    \\ &
    =\frac{1}{2 \pi i} \oint_w dz \, \epsilon
    (z) T(z)\phi(w,\bar{w})
\end{aligned}
$$

and similarly for the anti-holomorphic part. But we can write the LHS as integral around the point $w$ using Cauchy integral formula (acting on the coordinate change $\epsilon$ only:

$$
\begin{aligned}
    h \phi(w,\bar{w}) \partial\epsilon (w)
    &= \frac{1}{2 \pi i} \oint_w dz \frac{\epsilon(z)}{(z-w)^2}h \phi(w,\bar{w})
    \\
    \epsilon (w)\partial\phi(w,\bar{w})
    &= \frac{1}{2 \pi i} \oint_w dz \frac{\epsilon(z)}{z-w} \partial\phi(w,\bar{w})
\end{aligned}
$$

Therefore

$$
\begin{aligned}
    T(z)\phi(w,\bar{w})
    &= \frac{h}{(z-w)^2} \phi(w,\bar{w})
    + \frac{1}{z-w} \partial \phi(w,\bar{w})
    + \text{reg.}
    \\
    \bar{T} (\bar{z}) \phi(w,\bar{w})
    &= \frac{\bar{h}}{(\bar{z}-\bar{w})^2} \phi(w,\bar{w})
    + \frac{1}{\bar{z}-\bar{w}} \bar{\partial} \phi(w,\bar{w})
    +\text{reg.}
\end{aligned}
$$
