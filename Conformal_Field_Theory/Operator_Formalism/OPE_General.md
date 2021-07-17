<style>
    .katex {
        font-size: 1.1em;
    }
    .remark {
        border-radius: 15px;
        padding: 20px;
        background-color: SeaGreen;
        color: White;
    }
    .result {
        border-radius: 15px;
        padding: 20px;
        background-color: DarkSlateBlue;
        color: White;
    }
</style>

# Operator Product Expansion: <br>General Description

## Conserved Current of Conformal Transformation

*(Reference: [Physics Stack Exchange](https://physics.stackexchange.com/q/489906/222821))*

Recall that the Hilbert energy-momentum tensor $T^{\mu \nu}$ is defined as (in Euclidean space)

$$
\delta S = \frac{1}{2} \int d^d x
\sqrt{g} T^{\mu \nu} \delta g_{\mu \nu}
$$

For any infinitesimal coordinate transformation $x^\mu \mapsto x^\mu + \epsilon^\mu(x)$, one can show that the variation of the metric is ($D_\mu$ is the covariant derivative)

$$
\delta g_{\mu \nu} = D_\mu \epsilon_\nu + D_\nu \epsilon_\mu
$$

Then

$$
\begin{align*}
    \delta \mathcal{L} &= \frac{1}{2}
    \sqrt{g} T^{\mu \nu} \delta g_{\mu \nu}
    \\
    &= \frac{1}{2} \sqrt{g} T^{\mu \nu}
    (D_\mu \epsilon_\nu + D_\nu \epsilon_\mu)
    \\
    &= \sqrt{g} T^{\mu \nu}
    D_\mu \epsilon_\nu \qquad (T^{\mu\nu} = T^{\nu\mu})
    \\
    &= D_\mu (\sqrt{g} T^{\mu\nu} \epsilon_\nu) 
    \quad \, (D_\mu T^{\mu \nu}, D_\mu g^{\mu \nu} = 0)
    \\
    &\to \p_\mu (T^{\mu\nu} \epsilon_\nu) 
    \quad \, \, \, \quad (\text{flat limit})
\end{align*}
$$

Now we define

<div class="result">

**Current associated with conformal transformation:**

$$
j^\mu = T^{\mu \nu} \epsilon_\nu
$$

</div><br>

For common CFTs, $T^{\mu\nu}$ is traceless. Then we can prove that this current is indeed conserved:

$$
\begin{align*}
    \p_\mu j^\mu 
    &= \p_\mu (T^{\mu \nu} \epsilon_\nu)
    = T^{\mu \nu} \p_\mu \epsilon_\nu \\
    &= \frac{1}{2} T^{\mu \nu} (
        \p_\mu \epsilon_\nu
        + \p_\mu \epsilon_\nu
    ) \\
    &= \frac{1}{2} T^{\mu \nu} \times
    \frac{2}{d} (\p \cdot \epsilon) \eta_{\mu\nu}
    \\
    &= \frac{1}{d} (\p \cdot \epsilon) {T^\mu}_\mu
    = 0
\end{align*}
$$

## Conserved Current on Complex Plane

Consider the usual coordinate complexification on the plane (or the cylinder)

$$
x^0 = \frac{1}{2}(z+\bar{z}),
\quad
x^1 = -\frac{i}{2}(z-\bar{z})
$$

The conserved current $j^\mu$, which is a vector, will transform according to the law ($z^{0,1} = z, \bar{z}$)

$$
j'_\mu = \frac{\p x^\nu}{\p z^\mu} j_\nu, \quad
\frac{\p x^\nu}{\p z^\mu}
= \begin{pmatrix}
    \frac{\p x^0}{\p z} & \frac{\p x^1}{\p z} \\[0.3em]
    \frac{\p x^0}{\p \bar{z}} & \frac{\p x^1}{\p \bar{z}}
\end{pmatrix} = \begin{pmatrix}
    \frac{1}{2} & -\frac{i}{2} \\[0.3em]
    \frac{1}{2} & \frac{i}{2}
\end{pmatrix}
$$

Thus we find (which applies to all vectors)

<div class="result">

**Vectors in complex coordiantes:**

$$
j_z = \frac{1}{2} (j_0 - i j_1), \quad
j_{\bar{z}} = \frac{1}{2} (j_0 + i j_1)
$$

</div><br>

<div class="remark">

*Remark*: This is consistent with the transformation of the derivatives

$$
\p_z
= \frac{1}{2} (\p_0 - i\p_1 ),
\quad
\p_{\bar{z}}
= \frac{1}{2} (\p_0 + i \p_1 )
$$

</div><br>

In particular, let us calculate the current associated with the conformal transformation in complex coordinates. First, the infinitesimal transformation $\epsilon^\mu$, which is also a vector, is transformed to

$$
\begin{align*}
    \epsilon_z &= \frac{1}{2}(\epsilon_0 - i \epsilon_1)
    = \frac{1}{2} \bar{\epsilon} (\bar{z})
    \\
    \epsilon_{\bar{z}} &= \frac{1}{2}(\epsilon_0 + i \epsilon_1)
    = \frac{1}{2} \epsilon(z)
\end{align*}
$$

And we derived earlier that the metric in the complex coordinates is

$$
\begin{pmatrix}
    g^{zz} & g^{z \bar{z}} \\
    g^{\bar{z} z} & g^{\bar{z}\bar{z}}
\end{pmatrix} = \begin{pmatrix}
    0 & 2 \\ 2 & 0
\end{pmatrix}
$$

Then, using $j_\mu = {T_\mu}^\nu \epsilon_\nu = T_{\mu \rho} g^{\rho \nu} \epsilon_\nu$ in complex coordinates, we obtain

$$
\begin{align*}
    \begin{pmatrix}
        j_z \\ j_{\bar{z}}
    \end{pmatrix} &= \begin{pmatrix}
        T_{zz} & 0 \\ 0 & T_{\bar{z} \bar{z}}
    \end{pmatrix} \begin{pmatrix}
        0 & 2 \\ 2 & 0
    \end{pmatrix} \begin{pmatrix}
        \epsilon_z \\ \epsilon_{\bar{z}}
    \end{pmatrix}
    \\
    &= \begin{pmatrix}
        2 T_{zz} \epsilon_{\bar{z}} \\
        2 T_{\bar{z}\bar{z}} \epsilon_z
    \end{pmatrix} = \begin{pmatrix}
        T_{zz} \epsilon(z) \\
        T_{\bar{z}\bar{z}} \bar{\epsilon}(\bar{z})
    \end{pmatrix}
\end{align*}
$$

We defined earlier $T(z) = -2\pi T_{zz}, \bar{T}(\bar{z}) = -2\pi T_{\bar{z}\bar{z}}$; then we arrive at

<div class="result">

**Current associated with conformal symmetry in complex plane:**

$$
j_z(z) = -\frac{1}{2\pi} \epsilon(z) T(z) ,\quad
j_{\bar{z}}(\bar{z}) 
= -\frac{1}{2\pi} \bar{\epsilon}(\bar{z}) \bar{T}(\bar{z}) 
$$

</div><br>

<div class="remark">

*Remark*: Now we have the experience that the chiral component of a rank-$r$ tensor (with lower indices) behaves as a *quasi*-primary field with conformal dimension $(h,\bar{h}) = (r,0)$ (and similarly for the anti-chiral tensors). For example
    
- Conserved current $j_z(z)$: $(h,\bar{h}) = (1,0)$
- Energy-momentum tensor $T(z)$: $(h,\bar{h}) = (2,0)$

However, it is not necessarily *primary* when things go quantum and non-global transformations are involved, as we shall see for $T(z)$.

</div><br>

## Conserved Charge on Complex Plane

Recall that the conserved charge is expressed using the real coordinates as

$$
Q = \int d^{d-1}x \, j_0(x)
$$

With periodic boundary condition on $x^1$, the expression becomes 

$$
Q = \int_0^{L} dx^1 j_0^\text{cyl}(x)
$$

The current is defined on the cylinder. Let us apply the cylinder-plane mapping to convert this into a complex integral. In this section, $z$ is on the cylinder, and $w$ is on the plane. 

First, the current $j^0$ is decoupled into a chiral part and an anti-chiral part:

$$
j_0^\text{cyl}(x)
= j^{\text{cyl}}_z(z) + j^{\text{cyl}}_{\bar{z}}(\bar{z})
$$

For the coordinate transformation

$$
z = \frac{1}{\omega} \ln w, \quad
\bar{z} = \frac{1}{\omega} \ln \bar{w}
$$

The Jacobian matrix is diagonal ($z^0,z^1 = z,\bar{z}$, and similarly for $w$)

$$
\frac{\p z^\nu}{\p w^\mu}
= \begin{pmatrix}
    \frac{\p z^0}{\p w^0} & \frac{\p z^1}{\p w^0} \\[0.3em]
    \frac{\p z^0}{\p w^1} & \frac{\p z^1}{\p w^1}
\end{pmatrix} = \begin{pmatrix}
    \frac{1}{\omega w} & 0 \\[0.3em]
    0 & \frac{1}{\omega \bar{w}}
\end{pmatrix}
$$

Then we can easily write the conversion from the cylinder current to the plane current

$$
\begin{gathered}
    j_w(w) = \frac{1}{\omega w} j_z^\text{cyl}(z), \quad
    j_{\bar{w}}(\bar{w}) = \frac{1}{\omega \bar{w}} 
    j_{\bar{z}}^\text{cyl}(\bar{z})
    \\[1em] \Rightarrow \quad
    j_0^\text{cyl}(x)
    = \omega w j_w(w) + \omega \bar{w} j_{\bar{w}}(\bar{w})
\end{gathered}
$$

What we have obtained so far is

$$
Q = \int_0^{L} dx^1 \, [
    \omega w j_w(w) + \omega \bar{w} j_{\bar{w}}(\bar{w})
]
$$

With radial quantization, constant $x^1$ lines is mapped to a circle (let us call it $C(0)$) centered at the origin; its radius (or the value of $x^0$) is irrelevant. Then we transform the integration measure to $dw, d\bar{w}$:

$$
\begin{align*}
    w = e^{\omega(x^0 + ix^1)} 
    \quad &\Rightarrow \quad
    dw = i \omega w \, dx^1
    \\
    \bar{w} = e^{\omega(x^0 - ix^1)} 
    \quad &\Rightarrow \quad
    d\bar{w} = -i \omega \bar{w} \, dx^1
\end{align*}
$$

- For the first term depending on $w$: 

    $$
    \int_0^L dx^1 
    \to \frac{1}{i \omega} \oint_{C(0)} \frac{1}{w} dw 
    $$

- For the second term depending on $\bar{w}$, we have a similar expression:

    $$
    \begin{align*}
        \int_0^L dx^1 
        &\to \frac{1}{-i\omega} \oint_{-C(0)} 
        \frac{1}{\bar{w}} d\bar{w} 
        \\
        &= \frac{1}{i\omega} \oint_0 \frac{1}{\bar{w}} d\bar{w} 
    \end{align*}
    $$

    where the extra minus sign changed the clockwise integration to a counter-clockwise one. 

Fortunately, the $\omega w$ factor is cancelled out. Once this conversion is done, the result is independent of the shape of the contour (as long as it still encloses the origin):

$$
Q = \frac{1}{i} \oint dw \, j_w(w)
+ \frac{1}{i} \oint d\bar{w} \,
j_{\bar{w}} (\bar{w})
$$

Finally, plug in the expression of $j_w, j_{\bar{w}}$ in terms of the  $T(w)$ and $\epsilon(w)$ defined on the complex plane (not the cylinder):

<div class="result">

**Conserved charge of conformal symmetry:**

$$
Q = -\frac{1}{2\pi i} \oint dw \, \epsilon(w) T(w)
- \frac{1}{2\pi i} \oint d\bar{w} \,
\bar{\epsilon}(\bar{w}) \bar{T}(\bar{w}) 
$$

The integration paths (both counter-clockwise) enclose the origin 0. 

</div><br>

<div class="remark">

*Notation Note:* From now on, the variables $z, w$ and the fields are all in the plane (unless otherwise stated, as in the last section).

</div><br>

## Operator Product Expansion (OPE)

Now consider the action of $Q$ on a primary field. We know that it is the generator of the symmetry transformation according to the Ward identity:

$$
[Q, \phi] = \delta \phi
$$

Let us evaluate the commutator: note that $\epsilon$ is just a coordinate transformation function, which brought out of the commutator

$$
\begin{align*}
    \left[Q, \phi(w,\bar{w})\right]
    &= -\frac{1}{2 \pi i} \oint dz \, \epsilon(z) [
        T(z), \phi(w,\bar{w})
    ]
    \\ &\quad
    - \frac{1}{2 \pi i} \oint d\bar{z} \, 
    \bar{\epsilon}(\bar{z}) [
        \bar{T}(\bar{z}), \phi(w,\bar{w})
    ]
\end{align*}
$$

Now we impose radial (time) ordering: using the theorem we proved at the beginning

$$
\oint_0 dz [a(z),b(w)]
= \oint_w dz \,R [a(z) b(w)]
$$

for the chiral part, we obtain ($\epsilon(z)$ is just a coordinate-change function, not an operator)

$$
\begin{align*}
    \oint dz \, \epsilon(z) [
        T(z), \phi(w,\bar{w})
    ]
    &= \oint dz \, [
        \epsilon(z) T(z), \phi(w,\bar{w})
    ] 
    \\
    &= \oint_w dz \, \epsilon (z) R[T(z) \phi(w,\bar{w})]
\end{align*}
$$

and similarly for the anti-chiral part. Let us record this intermediate result:

<div class="result">

**Alternative transformation rule of quasi-primary fields:**

$$
\delta \phi(w,\bar{w})
= -\frac{1}{2\pi i} \oint_w dz \,
\epsilon (z) R[T(z) \phi(w,\bar{w})]
+ \text{anti-chiral}
$$

</div><br>

Recall that the change of a primary field under a conformal transformation is

$$
\begin{align*}
    \delta \phi(w, \bar{w}) &= - [
        h \phi(w, \bar{w}) \p_w \epsilon(w) 
        + \epsilon(w) \p_w \phi(w, \bar{w})
     ] \\ &\quad + \text{anti-chiral}
\end{align*}
$$

which can be expressed as a contour integral using the Cauchy integral formula (see [appendix](#a-cauchy-integral-formula)): for the chiral part

$$
\begin{align*}
    \p_w \epsilon(w, \bar{w}) 
    &= \frac{1}{2\pi i} \oint_w dz \, 
    \frac{\epsilon(z)}{(z - w)^2}
    \\
    \epsilon(w)
    &= \frac{1}{2\pi i} \oint_w dz \, 
    \frac{\epsilon(z)}{z - w}
\end{align*}
$$

Then

$$
\begin{align*}
    & \frac{1}{2\pi i} \oint_w dz \, 
    \epsilon (z) R[T(z) \phi(w,\bar{w})]
    \\
    &= \frac{1}{2\pi i} \oint_w dz \, \left[
        \frac{\epsilon(z)}{(z-w)^2} h \phi(w,\bar{w})
        + \frac{\epsilon(z)}{z-w} \p_w \phi(w,\bar{w})
    \right]
\end{align*}
$$

which leads to the local expression (we add the anti-chiral result below, and omit the radial ordering symbol)

<div class="result">

**Operator product expansion: <br>Energy-momentum tensor with primary field**

$$
\begin{align*}
    T(z) \phi(w,\bar{w})
    &= \frac{1}{(z-w)^2} h \phi(w,\bar{w})
    \\ &\quad 
    + \frac{1}{z-w} \p_w \phi(w,\bar{w})
    + \text{Regular terms} 
    \\[1.5em]
    \bar{T}(\bar{z}) \phi(w,\bar{w})
    &= \frac{1}{(\bar{z}-\bar{w})^2} \bar{h} \phi(w,\bar{w})
    \\ &\quad 
    + \frac{1}{\bar{z}-\bar{w}} \p_{\bar{w}} \phi(w,\bar{w})
    + \text{Regular terms}
\end{align*}
$$

</div><br>
