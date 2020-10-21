# Infinitesimal Transformations

## Generators of Infinitesimal Transformation

Now consider **infinitesimal transformations**. Assume that the transformation depends on some set of parameters $\left\{\omega_a\right\}$, i.e.

$$
x^{\mu} \to x'^{\mu}(x,\omega),
\quad
\phi (x)\to \phi' \left(x'(x)\right)=F(\phi (x),\omega)
$$

$\omega =0$ corresponds to doing nothing:

$$
x'^{\mu}(x,0)=x^{\mu}, 
\quad
F(\phi (x),0)=\phi (x)
$$

For infinitesimal transformations, the parameters are small. This means that all change in position and field can be approximated by terms linear in $\omega_a$:

$$
\begin{aligned}
    x'^{\mu}(x,\omega)
    & =x^{\mu}
    + \omega_a \frac{\partial x'^{\mu}}{\partial \omega_a}(x,0)
    \\
    \phi' (x')
    &= \phi' \left(x+\omega_a\frac{\partial x'}{\partial \omega_a}(x,0)\right)\\
    &= \phi (x)+\omega_a\frac{\partial F}{\partial \omega_a}(\phi (x),0)
    \\
    &= F(\phi (x),\omega)
\end{aligned}
$$

The partial derivatives are evaluated at $\omega_a=0$.

The **generator** $G_a$ of the infinitesimal transformation is defined by the difference between the new and the old field *at the same position*:

$$
\phi' (x)-\phi (x)=-i \omega_aG_a\phi (x)
$$

The coefficient $-i$ is the conventional choice required by the *active picture* of transformations and produce *Hermitian* generators. Continue calculation: 

$$
\begin{aligned}
    \text{LHS}
    &=\phi \left(x-\omega_a\frac{\partial x'}{\partial \omega_a}(x,0)\right)
    \\ &\quad
    +\omega_a \frac{\partial F}{\partial \omega_a} \left(
        \phi \left(x-\omega_a\frac{\partial x'}{\partial \omega_a}(x,0)\right), 0
    \right)
    -\phi (x)
\end{aligned}
$$

discarding terms of $O\left(\omega^2\right)$:

$$
\begin{aligned}
    \text{LHS}
    = -\omega_a\frac{\partial x'^{\mu}}{\partial \omega_a}(x,0)\frac{\partial \phi}{\partial x^{\mu}}(x)
    +\omega_a\frac{\partial
    F}{\partial \omega_a}(\phi (x),0)
\end{aligned}
$$

Therefore, the generator is given by

$$
i G_a\phi (x)
= \frac{\partial x'^{\mu}}{\partial \omega_a}(x,0)
\, \partial_{\mu} \phi (x)
- \frac{\partial F}{\partial \omega_a}(\phi(x),0)
$$

## Infinitesimal Transformation Generators on Scalar Fields

For *scalar* fields, the functional $F$ depends on the parameters $\omega$ only through the coordinates $x$. Therefore

$$
\begin{aligned}
    \frac{\partial F}{\partial \omega_a} \overset{!}{=} 0
    \quad \Rightarrow \quad
    i G_a\phi (x)
    = \frac{\partial x'^{\mu}}{\partial \omega_a}(x,0)
    \, \partial_{\mu} \phi (x)
\end{aligned}
$$

Now we give some examples. 

## Rigid Translation

The *rigid* translation is

$$
x'^{\mu}=x^{\mu}+\epsilon^{\mu}
$$

where the amount of translation $\epsilon$ is uniform throughout the system. The transformation parameter is just $\epsilon$. Then we obtain

$$
\frac{\partial x'^{\mu}}{\partial \epsilon^{\nu}}(x,0)=\delta_{\nu}^{\mu}
$$

We obtain the generator $P_{\mu}$ corresponding to $\epsilon^\mu$:

$$
i P_{\nu} \phi (x)
= \delta_{\nu}^{\mu} \partial_{\mu} \phi (x)
= \partial_{\nu} \phi (x)
$$

Simplify:

$$
P_{\mu} = -i \partial_{\mu}
$$

## Lorentz Transformation

The Lorentz transformation is also *defined* by its effect on the
position:

$$
x'^{\mu} = {\Lambda^{\mu}}_{\nu}x^{\nu}
$$

Because of the invariance of the spacetime interval

$$
ds^2
= \eta_{\mu \nu} dx'^{\mu} dx'^{\nu} 
(
    =\eta_{\mu \nu} {\Lambda^{\mu}}_{\rho} {\Lambda^{\nu}}_{\sigma} dx^{\rho} dx^{\sigma}
)
=\eta_{\rho \sigma} dx^{\rho} dx^{\sigma}
$$

We have the following constraint on the transformation matrix $\Lambda$

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

Now we see that $\omega_{\mu \nu}$ should be *antisymmetric*: 

$$
\omega_{\rho \sigma} = -\omega_{\sigma  \rho}
$$

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

Now we find the generator $L^{\rho \sigma}$ corresponding to $\omega_{\rho \sigma}$:

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

Because of the anti-symmetry of the $\omega$ matrix, we slightly modify the left-hand side to include an additional factor of 1/2:

$$
\frac{1}{2}i L^{\rho \sigma} \phi (x)
= \frac{1}{2} (
    x^{\sigma} \partial^{\rho}
    - x^{\rho} \partial^{\sigma} 
) \, \phi (x)
$$

Finally

$$
L^{\rho \sigma}
= i \left(x^{\rho} \partial^{\sigma}-x^{\sigma} \partial^{\rho} \right)
$$

It is also anti-symmetric, as expected.

*Remark*: The spatial part of the generator $L$

$$
\begin{aligned}
    L_1 &\equiv L^{32} 
    = -i(x^2 \partial^3 - x^3 \partial^2)
    \\
    L_2 &\equiv L^{13} 
    = -i(x^3 \partial^2 - x^2 \partial^3)
    \\
    L_3 &\equiv L^{21} 
    = -i(x^1 \partial^2 - x^2 \partial^1)
\end{aligned}
$$

are called the **orbital angular momentum operators**. They can be collectively written using vector notation

$$
\boldsymbol{L} = \boldsymbol{x} \times \boldsymbol{p}
$$

## Scaling (Dilation)

A scaling in the position means

$$
x'^{\mu} = \alpha x^{\mu}
$$

where $\alpha$ is the constant scaling factor, serving as the transformation parameter.

$$
i G_a\phi (x)
= \frac{\partial x'^{\mu}}{\partial \omega_a}(x,0) \,
\partial_{\mu} \phi (x)
- \frac{\partial F}{\partial \omega_a}(\phi(x),0)
$$

Then we easily find

$$
\frac{\partial x'^{\mu}}{\partial \alpha} = x^{\mu}
$$

The scaling generator $D$ (for "dilation") corresponding to $\alpha$ is

$$
i D \phi (x) = x^{\mu} \partial_{\mu} \phi (x)
$$

Therefore

$$
D = -i x^{\mu} \partial_{\mu}
$$

## Special Conformal Transformation (SCT)

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
    &= (1-2b\cdot x+b^2x^2)^{-2} 
    \\ &\quad \times [
        -\delta_{\mu}^{\nu}x^2
        (1 - 2b\cdot x + b^2 x^2)
        \\ &\qquad \quad
        - (x^{\nu} - b^{\nu} x^2)(
            - 2\delta_{\mu}^{\rho} x_{\rho}
            + g_{\rho \sigma} x^2 (
                \delta_{\mu}^{\rho}b^{\sigma}
                +b^{\rho} \delta_{\mu}^{\sigma}
            )
        )
    ]
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

The SCT generator by $K_{\mu}$ corresponding to $b^\mu$ is then

$$
\begin{aligned}
    i K_{\mu} \phi (x)
    &= \frac{\partial x'^{\nu}}{\partial b^{\mu}}(x,0) \,
    \partial_{\nu} \phi (x)
    \\
    &= (-\delta_{\mu}^{\nu}x^2+2x^{\nu}x_{\mu}) \,
    \partial_{\nu} \phi (x)
\end{aligned}
$$

Thus

$$
K_{\mu} 
= -i \,(2x_{\mu}x^{\nu} \partial_{\nu} - x^2 \partial_{\mu})
$$

