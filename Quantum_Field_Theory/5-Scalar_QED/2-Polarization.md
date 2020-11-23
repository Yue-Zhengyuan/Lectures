# Polarization

## Unitary Irreducible Representation of Poincaré Group

The group of translations and Lorentz transformations in (3+1)-dimensional spacetime is called the **Poincaré group**. To some extent, different kinds of **particles** that exist in the spacetime can be regarded as **unitary irreducible representations (irreps)** of the Poincaré group. 

By **unitary** representation of a group $G$, we mean that under the basis vectors of this representation, every group member $g \in G$ is represented by a unitary matrix:

$$
D^\dagger(g) = D^{-1}(g)
$$

The Poincaré group does *not* have *finite*-dimensional unitary irreducible representation. But **Wigner's classification** states that:

- The unitary irreps of Poincaré group are *infinite*-dimensional;

- Each unitary irrep is characterized by two labels $m$ and $J$, having the physical meaning of the particle **rest mass** and **spin angular momentum**:
    
    - The mass $m$ is a *non-negative real number* ($m \ge 0$);
    - The spin $J$ is a *non-negative half-integer* ($J = 0, \frac{1}{2}, 1, \frac{3}{2}, ...$)

- The number of *independent states* in each irrep is described by the following:

    - If $J > 0$, for *each* value of the 4-momentum with $p^2 = m^2$ (on-shell):

        - If $m > 0$, there are $2J + 1$ independent states
        - If $m = 0$, there are 2 states
        
        These states correspond to linearly independent **polarizations** of particles. The infinite dimension of the vector space is due to the continuous possible values of $p = (E, \mathbf{p})$. 

    - If $J = 0$, there is only 1 state for any $m$. The particle has no polarization.

## Spin-0 Particles

The spin-0 particles are described by the real scalar field $\phi(x)$:

$$
\mathcal{L} 
= \frac{1}{2}[(\partial \phi)^2 - m \phi^2]
$$

The equation of motion is

$$
(\partial^2 + m^2) \phi(x) = 0
$$

## Massive Spin-1 Particles

For massive spin-1, we definitely needs fields with more degrees of freedom. We naturally turn to the 4-vector real field $A_\mu(x)$. However, one degree of freedom needs to be removed for $A_\mu$ to represent a spin-1 particle. 

### Proca Lagrangian

A natural guess based on real scalar field theory is

$$
\begin{aligned}
    \mathcal{L} 
    &= - \frac{1}{2} \partial_\mu A_\nu \partial^\mu A^\nu
    + \frac{1}{2} m^2 A_\mu A^\mu
\end{aligned}
$$

But in this theory, the decoupling $3 = 1 \oplus 1 \oplus 1$ (into three spin-0 particles) occurs, as can be seen from the equations of motion:

$$
(\partial^2 + m^2) A_\mu = 0
$$

In order to prevent this unwanted decoupling, we shall deliberately introduce some coupling terms into the Lagrangian: the simplest possible Lorentz invariant choice is

$$
\mathcal{L} 
= -\frac{a}{2} \partial_\mu A_\nu \partial^\mu A^\nu
+ \underbrace{\frac{b}{2} (\partial^\mu A_\mu)^2}_{\text{coupling term}}
+ \frac{1}{2} m^2 A_\mu A^\mu
$$

The ($\mu$th) equation of motion is

$$
a \partial^\nu \partial_\nu A_\mu 
- b \partial_\mu \partial^\nu A_\nu
+ m^2 A_\mu = 0
$$

We see that the four components are all involved through the second term in this equation. Take the derivative $\partial_\mu$, we obtain

$$
[(a - b)\partial^2 + m^2](\partial^\mu A_\mu) = 0
$$

If $a = b$ (we have assumed $m \ne 0$), this reduces to 

$$
\partial^\mu A_\mu = 0
$$

which removes one degree of freedom. Taking $a = b = 1$, the Lagrangian becomes (called the **Proca Lagrangian**)

$$
\begin{aligned}
    \mathcal{L} 
    &= - \frac{1}{2} \partial_\mu A_\nu \partial^\mu A^\nu
    + \frac{1}{2} (\partial^\mu A_\mu)^2
    + \frac{1}{2} m^2 A_\mu A^\mu
\end{aligned}
$$

We can write it into an equivalent neater form:

$$
\mathcal{L} 
= -\frac{1}{4} F_{\mu \nu} F^{\mu \nu}
+ \frac{1}{2} m^2 A_\mu A^\mu
$$

where $F_{\mu \nu}$ is the electromagnetic tensor

$$
F_{\mu \nu} = \partial_\mu A_\nu - \partial_\nu A_\mu
$$

----

*Verify*: We only process the first two terms.

$$
\begin{aligned}
    -\frac{1}{4} F_{\mu \nu} F^{\mu \nu}
    &= -\frac{1}{4}(
        \partial_\mu A_\nu \partial^\mu A^\nu
        - \partial_\mu A_\nu \partial^\nu A^\mu
        \\ &\qquad \quad
        - \partial_\nu A_\mu \partial^\mu A^\nu
        + \partial_\nu A_\mu \partial^\nu A^\mu
    )
    \\
    &= \frac{1}{2}(
        - \partial_\mu A_\nu \partial^\mu A^\nu
        + \partial_\mu A_\nu \partial^\nu A^\mu
    )
\end{aligned}
$$

Up to an integration by parts (removal of surface integral at infinity), the terms $\partial_\mu A_\nu \partial^\nu A^\mu$ and $(\partial^\mu A_\mu)^2$ are equivalent:

$$
\begin{aligned}
    &\int d^4 x \, \partial_\mu A_\nu \partial^\nu A^\mu
    \\
    &= \int d^4 x \, [
        \partial_\mu(A_\nu \partial^\nu A^\mu)
        - A_\nu \partial_\mu \partial^\nu A^\mu
    ]
    \\
    &\to - \int d^4 x \, A_\nu \partial_\mu \partial^\nu A^\mu
    \\[2em]
    &\int d^4 x \, (\partial^\mu A_\mu)^2
    = \int d^4 x \, (\partial_\mu A^\mu)
    (\partial^\nu A_\nu)
    \\
    &= \int d^4 x \, [
        \partial_\mu(A^\mu \partial^\nu A_\nu)
        - A^\mu \partial_\mu \partial^\nu A_\nu
    ]
    \\
    &\to - \int d^4 x \, A^\mu \partial_\mu \partial^\nu A_\nu
    \\
    &= - \int d^4 x \, A^\mu \partial^\nu \partial_\mu A_\nu 
    \qquad \blacksquare
\end{aligned}
$$

----

Now the equations of motion implies

$$
\begin{aligned}
    &\partial^\nu \partial_\nu A_\mu 
    - \partial_\mu 
    \underbrace{\partial^\nu A_\nu}_{=0}
    + m^2 A_\mu
    \\
    &= (\partial^2 + m^2) A_\mu = 0
\end{aligned}
$$

which is the same as the scalar field. But now we have $\partial^\mu A_\mu = 0$ so that the fields do not decouple. 

### Polarization Vectors

Since the equations of motion is linear in $A_\mu$, the 3 degrees of freedom can be linearly introduced to the mode expansion of $A_\mu$ as the (complex) **polarization vectors** $\epsilon_\mu^j(\mathbf{p})$: 

$$
\begin{aligned}
    A_\mu(x) &= \int \frac{d^3p}{(2\pi)^3} \frac{1}{\sqrt{2E_\mathbf{p}}}
    \sum_{j=1}^3 (
        \epsilon^j_\mu(\mathbf{p}) a_{\mathbf{p},j} e^{-ipx}
        + \epsilon^{j*}_\mu(\mathbf{p}) a_{\mathbf{p},j}^\dagger e^{+ipx}
    )
\end{aligned}
$$

also with $p^0 = E_\mathbf{p} = \sqrt{|\mathbf{p}|^2 + m^2}$. 

The constraint $\partial^\mu A_\mu = 0$ gives

$$
\begin{aligned}
    \partial^\mu A_\mu(x) 
    &= \int \frac{d^3p}{(2\pi)^3} \frac{1}{\sqrt{2E_\mathbf{p}}} \times
    \\ &\quad
    \sum_{j=1}^3 (
        -ip^\mu \epsilon^j_\mu(\mathbf{p}) a_{\mathbf{p},j} e^{-ipx}
        + ip_\mu \epsilon^{j*}_\mu(\mathbf{p}) a_{\mathbf{p},j}^\dagger e^{+ipx}
    )
    \\
    &= 0
\end{aligned}
$$

The only way to achieve this is

$$
p^\mu \epsilon_\mu^j(\mathbf{p}) = 0 \qquad
\text{for each } j
$$

This can be regarded as a linear equation system

$$
\begin{bmatrix}
    p^0 & -p^1 & -p^2 & -p^3
\end{bmatrix}
\begin{bmatrix}
    \epsilon_0 \\ \epsilon_1 \\ \epsilon_2 \\ \epsilon_3
\end{bmatrix} = 0
$$

When $p^2 = m^2 > 0$, the matrix $[p^0, -p^1, -p^2, -p^3]$ must be of rank 1. Thus this equation can only give 3 linearly independent solutions of $\epsilon^j$, as expected. 

The polarization vectors are usually normalized by

$$
\epsilon_\mu^{i*} (\epsilon^j)^\mu = -\delta^{ij}
$$

The 3 polarization vectors are conventionally chosen as the following: let $\mathbf{p}$ be along the $z$-axis, i.e.

$$
p^\mu = (E, 0, 0, p_z) \quad (E^2 - p_z^2 = m^2)
$$

Then we have two **transverse polarizations**

$$
\epsilon_\mu^1 = (0, 1, 0, 0), \quad
\epsilon_\mu^2 = (0, 0, 1, 0)
$$

and one **longitudinal (forward) polarization** (denoted by $f$)

$$
\epsilon_\mu^f = \left(
    \frac{p_z}{m}, 0, 0, \frac{E}{m}
\right)
$$

The two transverse polarizations can be rearranged to left and right **circular polarizations**:

$$
\epsilon_\mu^L = \frac{1}{\sqrt{2}}(0,1,-i,0),
\quad
\epsilon_\mu^R = \frac{1}{\sqrt{2}}(0,1,i,0)
$$

## Massless Spin-1 Particles and Gauge Fixing

Wigner's classification states that there can be only 2 polarizations for massless spin-1 particles. This extra constraint comes from the **gauge invariance** of the Lagrangian

$$
\mathcal{L} = -\frac{1}{4} F_{\mu \nu} F^{\mu \nu}
$$

which is invariant under the **gauge transformation**

$$
A_\mu(x) \to A_\mu(x) + \partial_\mu \alpha(x)
$$

where $\alpha(x)$ is any scalar function.

The equations of motion when $m = 0$ are

$$
\partial^2 A_\mu 
- \partial_\mu \partial^\nu A_\nu = 0
$$

It helps to separate this into time and space parts:

$$
\begin{aligned}
    \text{time:} \quad &\partial^2 A_0 
    - \partial_0 \partial^\nu A_\nu
    \\
    &= (\partial_0^2 - \partial_j^2) A_0
    - \partial_0 (\partial_0 A_0 - \partial_j A_j)
    \\
    &= -\partial_j^2 A_0 + \partial_0 \partial_j A_j
    = 0
    \\[1em]
    \text{space:} \quad &\partial^2 A_i 
    - \partial_i \partial^\nu A_\nu
    \\
    &= \partial^2 A_i
    - \partial_i (\partial_0 A_0 - \partial_j A_j)
    = 0
\end{aligned}
$$

Under the gauge transformation, 

$$
\partial_j A_j \to \partial_j A_j + \partial_j^2 \alpha
$$

Now we choose $\alpha$ so that (the **Coulomb gauge**)

$$
\partial_j A_j = \nabla \cdot \mathbf{A} = 0
$$

Then

$$
\begin{aligned}
    \text{time:} \quad & 
    \partial_j^2 A_0 = 0
    \\[0.5em]
    \text{space:} \quad &
    \partial^2 A_i
    - \partial_i \partial_0 A_0 
    = 0
\end{aligned}
$$
