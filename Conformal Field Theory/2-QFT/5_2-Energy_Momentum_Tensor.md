## Energy-Momentum Tensor

### Equation of Motion for Fields

$$
\partial_{\mu} \left(
    \frac{\partial \mathcal{L}}{\partial \left(\partial_{\mu} \phi \right)}
\right) - \frac{\partial \mathcal{L}}{\partial \phi
}=0
$$

### Canonical Energy-Momentum Tensor

Consider the infinitesimal translation of spacetime

$$
x^{\mu} \to x^{\prime \mu}=x^{\mu}+\epsilon^{\mu}(x)
$$

Here $\epsilon^{\mu}(x)$ *can depends on the position* (non-uniform translation). 

The field transforms according to

$$
\phi (x)\to \phi' \left(x'\right)=\phi (x)+\epsilon^{\mu} \frac{\partial F}{\partial \epsilon^{\mu}}
$$

Then the Jacobian matrix for the transformation is

$$
\frac{\partial x^{\prime \mu}}{\partial x^{\nu}}
= \delta_{\nu}^{\mu}
+ \partial_{\nu} \epsilon^{\mu}(x)
$$

Its inverse (up to $O(\epsilon)$) is

$$
\frac{\partial x^{\mu}}{\partial x^{\prime \nu}}
= \delta_{\nu}^{\mu}
- \partial_{\nu} \epsilon^{\mu}(x)
$$

The determinant of the Jacobian matrix is calculated from

$$
\det (1+A)=1+\text{tr} A+O\left(A^2\right)
$$

This relation can be easily understood if we diagonalize $A$. Hence

$$
\left| \frac{\partial x'}{\partial x} \right|
= 1 + \partial_{\rho} \epsilon^{\rho}(x)
$$

The action after the transformation is (keeping terms up to $O(\omega)$):

$$
\begin{aligned}
    S'
    &=\int d^dx'
    \mathcal{L} \left[
        \phi' ,
        \frac{\partial \phi'}{\partial x^{\prime \mu}} 
    \right]
    \\
    &= \int d^dx 
    \left|\frac{\partial x'}{\partial x} \right|\mathcal{L} \left[
        \phi
        +\epsilon^{\rho} \frac{\partial F}{\partial \epsilon^{\rho}}, 
        \frac{\partial x^{\nu}}{\partial x^{\prime \mu}}
        \frac{\partial \phi'}{\partial x^{\nu}}
    \right]
    \\
    &= \int d^dx \, (1 + \partial_\rho \epsilon^\rho) 
    \\ &\qquad \quad \times
    \mathcal{L} \left[
        \phi +\epsilon^{\rho} \frac{\partial F}{\partial \epsilon^{\rho}},
        (\delta_{\mu}^{\nu}-\partial_{\mu} \epsilon^{\nu})
        \partial_{\nu} \left(
            \phi +\epsilon^{\rho} \frac{\partial F}{\partial \epsilon^{\rho}} 
        \right)
    \right]
    \\
    &=\int d^dx \, (1 + \partial_\rho \epsilon^\rho) 
    \\ &\qquad \quad \times
    \mathcal{L} \left[\phi +\epsilon^{\rho} \frac{\partial F}{\partial \epsilon
    ^{\rho}},\partial_{\mu} \phi +\partial_{\mu} \left(\epsilon^{\rho} \frac{\partial F}{\partial \epsilon^{\rho}} \right)-\left(\partial
    _{\mu} \epsilon^{\nu} \right)\partial_{\nu} \phi \right]
    \\
    &=\int d^dx \, (1 + \partial_\rho \epsilon^\rho) 
    \\ &\qquad \quad \times
    \left[
        \mathcal{L} [\phi ,\partial_{\mu} \phi]
        +
        \epsilon^{\rho}
        \frac{\partial F}{\partial \epsilon^{\rho}}
        \frac{\partial \mathcal{L}}{\partial \phi}
    \right.
    \\ &\qquad \qquad \qquad
    \left.
        +
        \left(
            \partial_{\mu} \left(
            \epsilon^{\rho}
            \frac{\partial F}{\partial \epsilon^{\rho}} \right)
            -
            (\partial_{\mu} \epsilon^{\nu})
            \partial_{\nu} \phi 
        \right)
        \frac{\partial \mathcal{L}}{\partial \left(\partial_{\mu} \phi \right)}
    \right]
    \\
    &= \int d^dx 
    \left[
        \mathcal{L}
        +
        (\partial_{\rho} \epsilon^{\rho}) \mathcal{L}
        +
        \epsilon^{\rho}
        \frac{\partial F}{\partial \epsilon^{\rho}}
        \frac{\partial \mathcal{L}}{\partial \phi}
    \right.
    \\ &\qquad \qquad \qquad
    \left.
        +
        \left(
            \partial_{\mu}
            \left(
                \epsilon^{\rho} \frac{\partial F}{\partial \epsilon^{\rho}}
            \right)
            -
            (\partial_{\mu} \epsilon^{\nu})
            \partial_{\nu} \phi 
        \right)
        \frac{\partial \mathcal{L}}{\partial (\partial_{\mu} \phi)}
    \right]
\end{aligned}
$$

To apply the equation of motion, we integrate by parts for the fourth term:

$$
\begin{aligned}
    S' 
    &= \int d^dx 
    \left[
        \mathcal{L}
        +
        \left(\partial_{\rho} \epsilon^{\rho} \right)\mathcal{L}
        +
        \epsilon^{\rho}
        \frac{\partial F}{\partial \epsilon^{\rho}}
        \frac{\partial \mathcal{L}}{\partial \phi}
    \right.
    \\ &\qquad \qquad \qquad
    \left.
        -
        \epsilon^{\rho}
        \frac{\partial F}{\partial \epsilon^{\rho}} \partial_{\mu} 
        \left(
            \frac{\partial
            \mathcal{L}}{\partial \left(\partial_{\mu} \phi \right)}
        \right)
        -
        (\partial_{\mu} \epsilon^{\nu})
        (\partial_{\nu} \phi)
        \frac{\partial \mathcal{L}}{\partial (\partial_{\mu} \phi)}
    \right]
    \\
    &= \int d^dx 
    \left[
        \mathcal{L}
        +
        \left(\partial_{\rho} \epsilon^{\rho} \right)\mathcal{L}
        -
        \left(\partial_{\mu} \epsilon^{\nu} \right)\partial_{\nu} \phi 
        \frac{\partial \mathcal{L}}{\partial (\partial_{\mu} \phi)}
    \right.
    \\ &\qquad \qquad \qquad
    \left.
        + \,
        \epsilon^{\rho}
        \frac{\partial F}{\partial \epsilon^{\rho
        }}
        \underbrace{
            \left(
                \frac{\partial \mathcal{L}}{\partial \phi}
                -
                \partial_{\mu} \left(
                    \frac{\partial \mathcal{L}}{\partial (\partial_{\mu} \phi)}
                \right)
            \right)
        }_{\text{EOM}=0} \right]
    \\
    &= \int d^dx 
    \left[
        \mathcal{L}
        +
        (\partial_{\rho} \epsilon^{\rho}) \mathcal{L}
        -
        (\partial_{\mu} \epsilon^{\nu})
        (\partial_{\nu} \phi)
        \frac{\partial \mathcal{L}}{\partial (\partial_{\mu} \phi)}
    \right]
\end{aligned}
$$

Then the variation of the action is

$$
\delta S=\int d^dx \left[\left(\partial_{\nu} \epsilon^{\nu} \right)\mathcal{L}-\left(\partial_{\mu} \epsilon^{\nu} \right)\left(\partial
_{\nu} \phi \right)\frac{\partial \mathcal{L}}{\partial \left(\partial_{\mu} \phi \right)} \right]
$$

We continue to integrate by parts to convert the $\partial \epsilon$ to $\epsilon$:

$$
\begin{aligned}
    \delta S
    &= \int d^dx \left[
        - \epsilon^{\nu} \partial_{\nu} \mathcal{L}
        +
        \epsilon^{\nu} \partial_{\mu} \left(
            \frac{\partial \mathcal{L}}
            {\partial (\partial_{\mu} \phi)}
            \partial_{\nu} \phi 
        \right)
    \right]
    \\
    &= \int d^dx \,
    \epsilon^{\nu} 
    \partial_{\mu} \left(
        -\delta_{\nu}^{\mu} \mathcal{L}
        +
        \frac{\partial \mathcal{L}}{\partial (\partial_{\mu} \phi)}
        \partial_{\nu} \phi 
    \right)
\end{aligned}
$$

Define the **(canonical) energy-momentum tensor** as

$$
{T^{\mu}}_{\nu}
=
-\delta_{\nu}^{\mu} \mathcal{L}
+
\frac{\partial \mathcal{L}}{\partial (\partial_{\mu} \phi)}
\partial_{\nu} \phi
$$

or using superscripts only

$$
T^{\mu  \nu}
= -g^{\mu \nu} \mathcal{L}
+
\frac{\partial \mathcal{L}}{\partial (\partial_{\mu} \phi)}
\partial^{\nu} \phi
$$

Then

$$
\begin{aligned}
    \delta S
    &= \int d^dx \, 
    \partial_{\mu}T^{\mu}{}_{\nu} \epsilon^{\nu}(x)
    \\
    &= \int d^dx \,
    \partial_{\mu}T^{\mu  \nu} \epsilon_{\nu}(x)
    \overset{!}{=}0
\end{aligned}
$$

Because of the arbitrariness of the variation $\epsilon$ in coordinates, we conclude that symmetry with respect to spacetime translation is related to the conservation law

$$
\partial_{\mu}T^{\mu \nu}=0
$$

Thus we reach the conclusion that

> $T^{\mu \nu}$ is the $\mu$-component of the (classically) conserved current corresponding to the variation in the $\nu$-component of the coordinates.

The corresponding conserved *charge* is the **four-momentum**

$$
P^\nu = \int d^{d-1}x \, T_c^{0 \nu}
$$

*Remark*: The energy is then given by

$$
P^0 = \int d^{d-1}x \, T_c^{0 0}
= \int d^{d-1}x \, \left[
    \frac{\partial \mathcal{L}}{\partial \dot{\Phi}} 
    \partial \dot{\Phi}
    - \mathcal{L}
\right]
$$

The integrand is just the usual definition of Hamiltonian (density). 

### Belinfante Energy-Momentum Tensor

Since the variation of the action under spacetime translation (even if it is non-uniform, i.e. depend on the coordinates) is

$$
\delta S = -\int d^d x \, \partial_\mu T^{\mu \nu} \epsilon_\nu(x)
$$

we have the freedom to add a term to the energy-momentum tensor:

$$
T_B^{\mu \nu} = T_c^{\mu \nu} + \partial_\rho B^{\rho \mu \nu}, \quad
B^{\rho \mu \nu} = -B^{\mu \rho \mu}
$$

The tensor $B$ is *anti-symmetric* in the first two indices. This modification does not change the divergence of $T$:

$$
\partial_\mu T_B^{\mu \nu} = \partial_\mu T_c^{\mu \nu}
$$

It is possible to choose a special $B$ so that $T_B$ will become *symmetric*. Such a tensor $B$ is called the **Belinfante (energy-momentum) tensor**. 

