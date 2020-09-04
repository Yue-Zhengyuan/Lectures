# Primary Fields

If a field $\phi (z, \bar{z})$ transforms under *any* (global or local) conformal transformations $z\to w(z)$ according to

$$
\phi (z, \bar{z}) 
\to 
\phi' (w, \bar{w})
= \left(\frac{dw}{dz}\right)^{-h}
\left(\frac{d\bar{w}}{d\bar{z}}\right)^{-\bar{h}}
\phi(z, \bar{z})
$$

then it is called a **primary field**. The number $h \, (\bar{h})$ is called the **holomorphic (anti-holomorphic) conformal dimension**. 

If this transformation holds only for *global* conformal transformations, then $\phi$ is called a **quasi-primary fields**.

## Chiral Fields

If $\phi$ only depends on $z$, it is called a **chiral field**; if $\phi$ only depends on $\bar{z}$, it is an called **anti-chiral field**.

## Scaling Dimension and Spin

The conformal dimensions are related to the **scaling dimension** and the **planar spin** of the field by

$$
h=\frac{1}{2}(\Delta +s), \quad
\bar{h}=\frac{1}{2}(\Delta -s)
$$

## Variation under Infinitesimal Conformal Transformations

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

Thus the variation of the field due to both $\epsilon$ and $\bar{\epsilon}$ is

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

## Restriction on Correlation Function by Conformal Symmetry

The conformal invariance imposes strong restriction on the possible
forms of the correlation functions of (quasi-)primary fields.

### Two-Point Functions

$$
\langle \phi_a(z, \bar{z}) \phi_b(w, \bar{w}) \rangle 
= \frac{C_{a b}}{(z-w)^{2h} (\bar{z}-\bar{w})^{2\bar{h}}} 
\quad \text{if }
\begin{cases}
    h_a = h_b = h \\
    \bar{h}_a = \bar{h}_b = \bar{h}
\end{cases}
$$

Otherwise the correlation function vanishes.

### Three-Point Functions