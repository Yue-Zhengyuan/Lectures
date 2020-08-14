## Operator Product Expansion: <br>Free Boson

### Energy-Momentum Tensor in Complex Coordinates

Euclidean Action:

$$
S = \frac{g}{2} \int d^2 x \,
\partial_\mu \phi \, \partial^\mu \phi
$$

Lagrangian density

$$
\mathcal{L} = \frac{g}{2} 
\partial_\mu \phi \, \partial^\mu \phi
$$

The canonical energy-momentum tensor is found to be

$$
\begin{aligned}
    T_{\mu \nu} 
    &= -\eta_{\mu \nu} \mathcal{L}
    + \frac{\partial \mathcal{L}}{\partial (\partial^\mu \phi)} 
    \partial_\nu \phi
    \\
    &= g \left(
        - \frac{1}{2} \eta_{\mu \nu} 
        \partial_\alpha \phi  \, \partial^\alpha \phi
        + \partial_\mu \phi \, \partial_\nu \phi
    \right)
\end{aligned}
$$

Let us transform it into the complex form: let $z^0=z, z^1=\bar{z}$, then 

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
    \\
    &= g \left(
        - \frac{1}{2} \eta_{\rho \sigma} \eta^{\alpha \beta}
        \partial_\alpha \phi  \, \partial_\beta \phi
        + \partial_\rho \phi \, \partial_\sigma \phi
    \right)
    \frac{\partial x^\rho}{\partial z^\mu}
    \frac{\partial x^\sigma}{\partial z^\nu}
    \\
    &= 
    -\frac{g}{2} \left(
        \eta_{\rho \sigma}
        \frac{\partial x^\rho}{\partial z^\mu}
        \frac{\partial x^\sigma}{\partial z^\nu}
    \right) \left(
        \eta^{\alpha \beta}
        \frac{\partial z^\gamma}{\partial x^\alpha}
        \frac{\partial z^\delta}{\partial x^\beta}
    \right)
    \frac{\partial \phi}{\partial z^\gamma}
    \frac{\partial \phi}{\partial z^\delta}
    + g \frac{\partial \phi}{\partial z^\mu}
    \frac{\partial \phi}{\partial z^\nu}
\end{aligned}
$$

We find 

$$
\eta_{\rho \sigma}
\frac{\partial x^\rho}{\partial z^\mu}
\frac{\partial x^\sigma}{\partial z^\nu}
= \begin{pmatrix}
    0 & 1/2 \\
    1/2 & 0
\end{pmatrix}_{\mu \nu}
$$

$$
\begin{aligned}
    \frac{1}{2} \left(
        \eta^{\alpha \beta} 
        \frac{\partial z^\gamma}{\partial x^\alpha}
        \frac{\partial z^\delta}{\partial x^\beta}
    \right)
    \frac{\partial \phi}{\partial z^\gamma}
    \frac{\partial \phi}{\partial z^\delta}
    &= \begin{pmatrix}
        0 & 1 \\
        1 & 0
    \end{pmatrix}^{\gamma \delta}
    \frac{\partial \phi}{\partial z^\gamma}
    \frac{\partial \phi}{\partial z^\delta}
    \\
    &= 2 \, \partial \phi \, \bar{\partial} \phi
\end{aligned}
$$

Therefore

$$
\begin{aligned}
    T'_{\mu \nu} 
    &= -g \begin{pmatrix}
        0 & \partial\phi \, \bar{\partial}\phi \\
        \partial\phi \, \bar{\partial}\phi & 0
    \end{pmatrix}
    + g \begin{pmatrix}
        \partial\phi \, \partial\phi & \partial\phi \, \bar{\partial}\phi \\
        \partial\phi \, \bar{\partial}\phi & \bar{\partial}\phi \, \bar{\partial}\phi
    \end{pmatrix}
    \\
    &= g \begin{pmatrix}
        \partial\phi \, \partial\phi & 0 \\
        0 & \bar{\partial}\phi \, \bar{\partial}\phi
    \end{pmatrix}
\end{aligned}
$$

The non-diagonal elements vanish, as expected. We extract the diagonal elements:

$$
\begin{aligned}
    T(z) &\equiv -2\pi T_{zz} 
    = -2\pi g \,
    \mathcal{N}[\partial\phi \, \partial\phi]
    \\
    \bar{T}(\bar{z}) &\equiv -2\pi T_{\bar{z}\bar{z}}
    = -2\pi g \,
    \mathcal{N}[\bar{\partial}\phi \, \bar{\partial}\phi]
\end{aligned}
$$

Here we imposed *normal ordering*, which means that (e.g. for $T(z)$):

$$
\mathcal{N}[\partial\phi(z) \partial\phi(z)]
= \lim_{w \to z}
(\partial \phi(z) \partial \phi(w)
- \langle \partial \phi(z) \partial \phi(w) \rangle)
$$

### OPE of Field with Itself

Recall that the field correlation function for free boson is

$$
\langle \phi(x) \phi(y) \rangle
= -\frac{1}{4\pi g} \ln(x-y)^2 + \text{const.}
$$

In complex coordinates ($z = x^1+ix^2, w = y^1+iy^2$), we have

$$
\langle \phi(z,\bar{z}) \phi(w,\bar{w}) \rangle
= -\frac{1}{4\pi g} \{
    \ln(z - w) + \ln(\bar{z} - \bar{w})
\} + \text{const.}
$$

Then the correlation function of the derivative of the field is

$$
\begin{aligned}
    \langle \partial_z \phi(z,\bar{z}) \partial_w \phi(w,\bar{w}) \rangle
    &= \partial_z \partial_w \langle \phi(z,\bar{z}) \phi(w,\bar{w}) \rangle
    \\
    &= -\frac{1}{4\pi g} \frac{1}{(z-w)^2}
\end{aligned}
$$

$$
\begin{aligned}
    \langle \partial_{\bar{z}} \phi(z,\bar{z}) \partial_{\bar{w}} \phi(w,\bar{w}) \rangle
    &= \partial_{\bar{z}} \partial_{\bar{w}} \langle \phi(z,\bar{z}) \phi(w,\bar{w}) \rangle
    \\
    &= -\frac{1}{4\pi g} \frac{1}{(\bar{z}-\bar{w})^2}
\end{aligned}
$$

Therefore, we obtain the OPE

$$
\partial\phi(z) \partial\phi(w) 
\sim -\frac{1}{4\pi g} \frac{1}{(z-w)^2}
$$

*Remark*: Exchanging the two fields ($z$ and $w$) does not affect the correlation function, es expected for bosons.

### OPE of Field and Energy-Momentum Tensor

Using a generalized Wick's theorem $(\phi_{23}(w) \equiv \phi_2(w) \phi_3(w))$

$$
\overgroup{\phi_1(z) \, \mathcal{N}(\phi_{23}(w))} 
= \overgroup{\phi_1(z) \phi_2(w)} \mathcal{N}\phi_3(w)
+ \overgroup{\phi_1(z) \phi_3(w)} \mathcal{N}\phi_2(w)
$$

we obtain

$$
\begin{aligned}
    T(z) \partial \phi(w)
    &= -2\pi g \,
    \mathcal{N}[\partial\phi(z) \partial\phi(z)] \,
    \partial\phi(w)
    \\
    &=  
\end{aligned}
$$

### OPE of Energy-Momentum Tensor with Itself

$$
\begin{aligned}
    T(z) T(w) 
    &= (-2\pi g)^2 \,
    \mathcal{N}[\partial\phi(z) \partial\phi(z)] \,
    \mathcal{N}[\partial\phi(w) \partial\phi(w)]
    \\
    &= \frac{1/2}{(z-w)^4}
    + \frac{2T(w)}{(z-w)^2}
    + \frac{\partial T(w)}{z-w} + \text{reg.}
\end{aligned}
$$