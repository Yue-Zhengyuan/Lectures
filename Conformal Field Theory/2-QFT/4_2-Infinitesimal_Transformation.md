## Infinitesimal Transformations

### Generators of Infinitesimal Transformation

Now consider **infinitesimal transformations**. Assume that the transformation depends on some set of parameters $\left\{\omega_a\right\}$, i.e.

$$
x^{\mu} \to x'^{\mu}(x,\omega),
\quad
\phi (x)\to \phi' \left(x'(x)\right)=\mathcal{F}(\phi (x),\omega)
$$

$\omega =0$ corresponds to doing nothing:

$$
x'^{\mu}(x,0)=x^{\mu}, 
\quad
\mathcal{F}(\phi (x),0)=\phi (x)
$$

For infinitesimal transformations, the parameters are small. This means that all change in position and field can be approximated by terms linear in $\omega_a$:

$$
\begin{aligned}
    x'^{\mu}(x,\omega)
    & =x^{\mu}+\omega_a\frac{\partial x'^{\mu}}{\partial \omega_a}(x,0)
    \\
    \phi' \left(x'(x)\right)
    &= \phi' \left(x+\omega_a\frac{\partial x'}{\partial \omega_a}(x,0)\right)\\
    &= \mathcal{F}(\phi (x),\omega)=\phi (x)+\omega_a\frac{\partial \mathcal{F}}{\partial \omega_a}(\phi (x),0)
\end{aligned}
$$

The partial derivatives are evaluated at $\omega_a=0$.

The of the infinitesimal transformation is defined by the difference between the new and the old field *at the same position*:

$$
\phi' (x)-\phi (x)=-i \omega_aG_a\phi (x)
$$

The coefficient $-i$ is in consistent with the *active picture* of transformations and produce *Hermitian* generators. For multi-component fields, the generator may be a complicated object (not just a single
number).

The variation of the field is

$$
\begin{aligned}
    \phi' (x)-\phi (x)
    &=\phi \left(x-\omega_a\frac{\partial x'}{\partial \omega_a}(x,0)\right)
    \\ &\quad
    +\omega_a \frac{\partial \mathcal{F}}{\partial \omega_a} \left(
        \phi \left(x-\omega_a\frac{\partial x'}{\partial \omega_a}(x,0)\right), 0
    \right)
    -\phi (x)
\end{aligned}
$$

discarding terms of $O\left(\omega^2\right)$:

$$
\begin{aligned}
    \phi' (x)-\phi (x)
    &= -\omega_a\frac{\partial x'^{\mu}}{\partial \omega_a}(x,0)\frac{\partial \phi}{\partial x^{\mu}}(x)
    +\omega_a\frac{\partial
    \mathcal{F}}{\partial \omega_a}(\phi (x),0)
    \\
    &=-i \omega_aG_a\phi (x)
\end{aligned}
$$

Therefore, the generator is given by

$$
i G_a\phi (x)
= \frac{\partial x'^{\mu}}{\partial \omega_a}(x,0)\partial_{\mu} \phi (x)
- \frac{\partial \mathcal{F}}{\partial \omega_a}(\phi
(x),0)
$$

### Common Infinitesimal Transformation Generators on Scalar Fields

#### Rigid Translation

The translation is *defined* by its effect on the position:

$$
x'^{\mu}=x^{\mu}+\epsilon^{\mu}
$$

The amount of moving $\epsilon$ is the same for every parts of the
system, which plays the role of $\omega$. Then we obtain

$$
\frac{\partial x'^{\mu}}{\partial \epsilon^{\nu}}(x,0)=\delta_{\nu}^{\mu}
$$

*All fields* (no matter it is a scalar or a vector or anything) should not be affected by the rigid translation, i.e. the mapping $\mathcal{F}$ is *always* identity. Hence

$$
\phi' \left(x'\right)
=\mathcal{F}(\phi (x),\epsilon)=\phi (x) 
\Longrightarrow
\frac{\partial \mathcal{F}}{\partial \epsilon^{\mu}}(\phi (x),0)=0
$$

We obtain (using $P_{\mu}$ to denote the generators)

$$
i P_{\nu} \phi (x)
= \delta_{\nu}^{\mu} \partial_{\mu} \phi (x)
= \partial_{\nu} \phi (x)
$$

Thus, the corresponding generator (called the operator) is

$$
P_{\mu} = \frac{1}{i} \partial_{\mu}
= -i \partial_{\mu}
$$

#### Lorentz Transformation

The Lorentz transformation is also *defined* by its effect on the
position:

$$
x'^{\mu} = {\Lambda^{\mu}}_{\nu}x^{\nu}
$$

Because of the invariance of the proper time

$$
ds^2
= \eta_{\mu \nu} dx'^{\mu} dx'^{\nu} 
(
    =\eta_{\mu \nu} {\Lambda^{\mu}}_{\rho} {\Lambda^{\nu}}_{\sigma} dx^{\rho} dx^{\sigma}
)
=\eta_{\rho \sigma} dx^{\rho} dx^{\sigma}
$$

The coordinate transformation matrices $\Lambda$ must satisfy the
requirement

$$
\eta_{\mu \nu} 
{\Lambda^{\mu}}_{\rho} {\Lambda^{\nu}}_{\sigma}
= \eta_{\rho \sigma}
$$

The infinitesimal Lorentz transformation matrix must be close to
identity, and can be written as

$$
{\Lambda^{\mu}}_{\nu}
= \delta^{\mu}_{\nu} + {\omega^{\mu}}_{\nu}
$$

The coordinate transformation is therefore

$$
x'^{\mu}
= x^{\mu} + {\omega^{\mu}}_{\sigma} x^{\sigma}
= x^{\mu} + \eta^{\mu \rho} \omega_{\rho \sigma}x^{\sigma}
$$

The requirement $\eta_{\mu \nu} {\Lambda^{\mu}}_{\rho} {\Lambda^{\nu}}_{\sigma}=\eta_{\rho \sigma}$ restrict the form of the matrix $\omega_{\mu \nu}$:

$$
\begin{aligned}
    \text{LHS}
    &= \eta_{\mu \nu}
    (\delta^{\mu}_{\rho} + {\omega^{\mu}}_{\rho})
    (\delta^{\nu}_{\sigma} + {\omega^{\nu}}_{\sigma})
    \\
    &= (\eta_{\nu \rho} + \omega_{\nu \rho})
    (\delta^{\nu}_{\sigma} + {\omega^{\nu}}_{\sigma})
    = \eta_{\rho \sigma}
    + \omega_{\rho \sigma} + \omega_{\sigma \rho}
    + O(\omega^2)
\end{aligned}
$$

$$
\Rightarrow 
\omega_{\rho \sigma} = -\omega_{\sigma  \rho}
$$

i.e. $\omega_{\mu \nu}$ *is* *antisymmetric*. 

Therefore, when we calculate the derivative $\partial x'^{\mu}/\partial \omega_{\rho \sigma}$, we will get two terms and a factor of 1/2:

$$
\begin{aligned}
    \frac{\partial x'^{\mu}}{\partial \omega_{\rho \sigma}}(x,0)
    &= \frac{\partial}{\partial \omega_{\rho \sigma}} 
    \left(
        x^{\mu}
        + \frac{1}{2} \eta^{\mu \rho} \omega_{\rho \sigma}x^{\sigma}
        + \underbrace{\frac{1}{2} \eta^{\mu \sigma} \omega_{\sigma \rho}x^{\rho}}_{\text{rename } \sigma \text{ and } \rho} 
    \right)
    \\
    &= \frac{\partial}{\partial \omega_{\rho \sigma}} 
    \left(
        x^{\mu}
        + \frac{1}{2} \eta^{\mu \rho} \omega_{\rho \sigma}x^{\sigma}
        - \frac{1}{2} \eta^{\mu  \sigma} \omega_{\rho \sigma}x^{\rho} 
    \right)
    \\
    &=\frac{1}{2} (
        \eta^{\mu \rho} x^{\sigma}
        - \eta^{\mu \sigma} x^{\rho}
    )
\end{aligned}
$$

By definition of a *scalar* field, it should be invariant under Lorentz
transformation, i.e.

$\phi' \left(x'\right)=\mathcal{F}(\phi (x),\epsilon)=\phi (x) \Longrightarrow  \frac{\partial \mathcal{F}}{\partial \omega_a}(\phi (x),0)=0$

Now we find the generator (denoted $L^{\rho \sigma}$)

$$
\begin{aligned}
    i L^{\rho \sigma} \phi (x)
    &=\frac{\partial x'^{\mu}}{\partial \omega_{\rho \sigma}}(x,0) \, 
    \partial_{\mu} \phi (x)
    \\
    &= \frac{1}{2} (
        \eta^{\mu \rho} x^{\sigma}
        - \eta^{\mu \sigma} x^{\rho}
    ) \, \partial_{\mu} \phi (x)
    \\
    &= \frac{1}{2} (
        x^{\sigma} \partial^{\rho}
        - x^{\rho} \partial^{\sigma}
    ) \, \phi (x)
\end{aligned}
$$

Because of the anti-symmetry of the $\omega$ matrix, we slightly modify
the left-hand side to include an additional factor of 1/2:

$$
\frac{1}{2}i L^{\rho \sigma} \phi (x)
= \frac{1}{2} (
    x^{\sigma} \partial^{\rho}
    - x^{\rho} \partial^{\sigma} 
) \, \phi (x)
$$

We finally obtain the corresponding generator (called the orbital **angular momentum operator**)

$$
L^{\rho \sigma}
= i \left(x^{\rho} \partial^{\sigma}-x^{\sigma} \partial^{\rho} \right)
$$

It is also anti-symmetric, as expected.

#### Scaling (Dilation)

A scaling in the position means

$$
x'^{\mu} = \alpha x^{\mu}
$$

where $\alpha$ is the constant scaling factor, serving as the parameter $\omega$.

$$
i G_a\phi (x)
= \frac{\partial x'^{\mu}}{\partial \omega_a}(x,0) \,
\partial_{\mu} \phi (x)
- \frac{\partial \mathcal{F}}{\partial \omega_a}(\phi(x),0)
$$

Then we easily find

$$
\frac{\partial x'^{\mu}}{\partial \alpha} = x^{\mu}
$$

For a scalar field invariant under scaling, we again have
$\partial \mathcal{F}/\partial \alpha =0$. Denoting the scaling generator by $D$ (for "dilation"), we obtain

$$
i D \phi (x) = x^{\mu} \partial_{\mu} \phi (x)
$$

Therefore

$$
D = -i x^{\mu} \partial_{\mu}
$$

#### Special Conformal Transformation (SCT)

The finite SCT is defined as

$$
x'^{\mu} = 
\frac{x^{\mu} - b^{\mu} x^2}{1 - 2b \cdot x + b^2 x^2}
$$

The parameters are the vector $b^{\mu}$. Then we evaluate the derivative (which is somewhat complicated)

$$
\begin{aligned}
    \frac{\partial x'^{\nu}}{\partial b^{\mu}}
    &= \frac{\partial}{\partial b^{\mu}} \left(
        \frac{
            x^{\nu} - b^{\nu}x^2
        }{
            1 - 2b^{\rho}x_{\rho}
            + g_{\rho \sigma} b^{\rho} b^{\sigma} x^2
        } 
    \right)
    \\
    &= \frac{1}{(1-2b\cdot x+b^2x^2)^2} 
    (
        -\delta_{\mu}^{\nu}x^2
        (1 - 2b\cdot x + b^2 x^2)
        \\ &\qquad \qquad
        - (x^{\nu} - b^{\nu} x^2)(
            - 2\delta_{\mu}^{\rho} x_{\rho}
            + g_{\rho \sigma} x^2 (
                \delta_{\mu}^{\rho}b^{\sigma}
                +b^{\rho} \delta_{\mu}^{\sigma}
            )
        )
    \\
    &= - \frac{\delta_{\mu}^{\nu} x^2}
        {1 - 2b\cdot x + b^2x^2} 
    - \frac{
        (x^{\nu} - b^{\nu} x^2)
        (-2x_{\mu} + 2b_{\mu} x^2)
    }{
        (1 - 2b\cdot x + b^2 x^2)^2
    }
    \\
    &\xrightarrow{b=0}
    - \delta_{\mu}^{\nu} x^2 
    + 2 x^{\nu} x_{\mu}
\end{aligned}
$$

Denote the SCT generator by $K_{\mu}$. For scalar field, we then have

$$
i K_{\mu} \phi (x)
=\frac{\partial x'^{\nu}}{\partial b^{\mu}}(x,0) \,
\partial_{\nu} \phi (x)
= -\delta_{\mu}^{\nu}x^2+2x^{\nu}x_{\mu}
$$

Thus

$$
K_{\mu} 
= -i \,(2x_{\mu}x^{\nu} \partial_{\nu} - x^2 \partial_{\mu})
$$

### Conserved Charge

The associated with the current $j_a$ is defined as

$$
Q_a=\int d^{d-1}x \, j_a^0
$$

The integration is carried in the spatial part only. We verify that its time ($x^0$) derivative indeed vanishes:

$$
\frac{dQ_a}{dx^0}
= \int d^{d-1}x \, (\partial_0 j_a^0)
=-\int d^{d-1}x \, (\partial_i j_a^i)
$$

In the second equality we used $\partial_{\mu}j_a^{\mu}=0$. 

Gauss' Theorem then converts the integral to a surface integral at infinity, which gives zero provided that the current vanished sufficiently rapidly as $x\to \infty$.