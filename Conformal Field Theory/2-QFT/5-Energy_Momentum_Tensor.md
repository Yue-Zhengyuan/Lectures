## Energy-Momentum Tensor

### Noether's Theorem

**Noether's Theorem** states that:

To every continuous symmetry of the action, one may associate a current
that is classically conserved.

By " *classically*", we mean that the holds:

$$
\partial_{\rho} \left(
    \frac{\partial \mathcal{L}}{\partial \left(\partial_{\rho} \phi \right)}
\right) - \frac{\partial \mathcal{L}}{\partial \phi
}=0
$$

### Energy-Momentum Tensor

Consider the infinitesimal transformation

$$
x^{\mu} \to x^{\prime \mu}=x^{\mu}+\epsilon^{\mu}(x)
$$

Here $\epsilon^{\mu}(x)$ *depends on the position*. It plays the role of $\omega_a$ above.

Under this transformation, the field changes by

$$
\phi (x)\to \phi' \left(x'\right)=\phi (x)+\epsilon^{\mu} \frac{\partial \mathcal{F}}{\partial \epsilon^{\mu}}
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
=c1+\partial_{\rho} \epsilon^{\rho}(x)
$$

The action after the operation is (keeping terms up to $O(\omega)$):

$$
\begin{aligned}
    S'
    &=\int d^dx'\mathcal{L} \left[\phi' ,\frac{\partial \phi' }{\partial x^{\prime \mu}} \right]
    \\
    &= \int d^dx\left|\frac{\partial x'}{\partial x} \right|\mathcal{L} \left[
        \phi
        +\epsilon^{\rho} \frac{\partial \mathcal{F}}{\partial \epsilon^{\rho}}, \,
        \frac{\partial x^{\nu}}{\partial x^{\prime \mu}}
        \frac{\partial \phi' }{\partial
        x^{\nu}}
    \right]
    \\
    &= \int d^dx \left(1+\partial_{\rho} \epsilon^{\rho} \right)
    \\ &\qquad \quad \times
    \mathcal{L} \left[\phi +\epsilon^{\rho} \frac{\partial \mathcal{F}}{\partial \epsilon^{\rho}},
    \left(\delta_{\mu}^{\nu}-\partial_{\mu} \epsilon^{\nu} \right)\partial_{\nu} \left(\phi +\epsilon^{\rho} \frac{\partial \mathcal{F}}{\partial
    \epsilon^{\rho}} \right)\right]
    \\
    &=\int d^dx \left(1+\partial_{\rho} \epsilon^{\rho} \right)
    \\ &\qquad \quad \times
    \mathcal{L} \left[\phi +\epsilon^{\rho} \frac{\partial \mathcal{F}}{\partial \epsilon
    ^{\rho}},\partial_{\mu} \phi +\partial_{\mu} \left(\epsilon^{\rho} \frac{\partial \mathcal{F}}{\partial \epsilon^{\rho}} \right)-\left(\partial
    _{\mu} \epsilon^{\nu} \right)\partial_{\nu} \phi \right]
    \\
    &=\int d^dx \left(1+\partial_{\rho} \epsilon^{\rho} \right)
    \\ &\qquad \quad \times
    \left[
        \mathcal{L} [\phi ,\partial_{\mu} \phi]
        +
        \epsilon^{\rho}
        \frac{\partial\mathcal{F}}{\partial \epsilon^{\rho}}
        \frac{\partial \mathcal{L}}{\partial \phi}
    \right.
    \\ &\qquad \qquad \qquad
    \left.
        +
        \left(
            \partial_{\mu} \left(
            \epsilon^{\rho}
            \frac{\partial \mathcal{F}}{\partial \epsilon^{\rho}} \right)
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
        \frac{\partial \mathcal{F}}{\partial \epsilon^{\rho}}
        \frac{\partial \mathcal{L}}{\partial \phi}
    \right.
    \\ &\qquad \qquad \qquad
    \left.
        +
        \left(
            \partial_{\mu}
            \left(
                \epsilon^{\rho} \frac{\partial \mathcal{F}}{\partial \epsilon^{\rho}}
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
        \frac{\partial \mathcal{F}}{\partial \epsilon^{\rho}}
        \frac{\partial \mathcal{L}}{\partial \phi}
    \right.
    \\ &\qquad \qquad \qquad
    \left.
        -
        \epsilon^{\rho}
        \frac{\partial \mathcal{F}}{\partial \epsilon^{\rho}} \partial_{\mu} 
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
        \frac{\partial \mathcal{F}}{\partial \epsilon^{\rho
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

Define

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
    &= \int d^dx \epsilon^{\nu}(x)\partial_{\mu}T^{\mu}{}_{\nu}
    \\
    &= \int d^dx \epsilon_{\nu}(x)\partial_{\mu}T^{\mu  \nu} \overset{!}{=}0
\end{aligned}
$$

Because of the arbitrariness of the variation $\epsilon$ in coordinates, we conclude that

$$
\partial_{\mu}T^{\mu \nu}=0
$$

Thus we reach the conclusion that

> $T^{\mu \nu}$ is the $\mu$-component of the (classically) conserved current corresponding to the variation in the $\nu$-component of the coordinates.

It is called the **energy-momentum tensor** of the system.

### The General Current

Suppose that the coordinate variation $\epsilon$ is further dependent of a set of parameters $\omega_a$. Since we are dealing with infinitesimal
transformations, we can keep only the linear terms:

$$
\epsilon^{\mu}
=
\omega_a 
\left.
    \frac{\partial \epsilon^{\mu}}{\partial \omega_a}
\right|_{\omega =0}
$$

### Symmetrizing the Energy-Momentum Tensor

### Energy-Momentum Tensor and the Metric

Since the tensor $T^{\mu \nu}$ can be made symmetric, we can write

$$
\begin{aligned}
    \delta S
    &= \int d^dx \epsilon_{\nu} \partial_{\mu}T^{\mu  \nu}
    = -\int d^dx T^{\mu  \nu} \partial_{\mu} \epsilon_{\nu}
    \\
    &= -\frac{1}{2} \int d^dx \,
    T^{\mu \nu} (
        \partial_{\mu} \epsilon_{\nu}
        + \partial_{\nu} \epsilon_{\mu}
    )
\end{aligned}
$$

But in flat spacetime, we recognize that

$$
\delta  g_{\mu  \nu}
= -(
    \partial_{\mu} \epsilon_{\nu}
    +\partial_{\nu} \epsilon_{\mu}
)
$$

Therefore, we may generalize the energy-momentum tensor as the
functional derivative of the action with respect to the metric:

$$
\delta  S = -\frac{1}{2} \int d^dx T^{\mu  \nu} \delta  g_{\mu  \nu}
$$

which is also applicable to curved spacetime.