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
