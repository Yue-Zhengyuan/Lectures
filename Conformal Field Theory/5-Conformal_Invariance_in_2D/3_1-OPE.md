## Operator Product Expansion

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