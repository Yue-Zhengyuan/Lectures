## The Conformal Group

*By definition*, a **conformal transformation** of the coordinates is an *invertible* mapping $x\to x'$ which *leaves the metric invariant up to a scale*:

$$
g_{\mu \nu}^{\prime}\left(x'\right)
= \Lambda(x) g_{\mu \nu}(x)
$$

### Requirement on Infinitesimal Transformations

Consider the infinitesimal transformation

$$
x^{\mu}\to x'^{\mu}=x^{\mu}+\epsilon^{\mu}(x)
$$

The metric transforms according to the law

$$
g_{\mu \nu}^{\prime}\left(x'\right)
= 
\frac{\partial x^{\rho}}{\partial x'^{\mu}}
\frac{\partial x^{\sigma}}{\partial x'^{\nu}}
g_{\rho \sigma}(x)
$$

Here the partial derivatives are

$$
\frac{\partial x^{\rho}}{\partial x'^{\mu}}
= \frac{\partial}{\partial x'^{\mu}}[
    x'^{\rho} 
    - \epsilon^{\rho}(x(x'))
]
= 
\delta_{\mu}^{\rho}
- \frac{\partial x^{\alpha}}{\partial x'^{\mu}}
\frac{\partial \epsilon^{\rho}}{\partial x^{\alpha}}
$$

But we know that $\partial x^{\alpha}/\partial x'^{\mu} = \delta_{\mu}^{\alpha} + O(\epsilon)$, then up to first order in $\epsilon$

$$
\frac{\partial x^{\rho}}{\partial x'^{\mu}}
= \delta_{\mu}^{\rho}
- \frac{\partial \epsilon^{\rho}(x)}{\partial x^{\mu}}
+ O(\epsilon^2)
$$

Then

$$
\begin{aligned}
    g_{\mu \nu}^{\prime}\left(x'\right)
    &\simeq \left(
        \delta_{\mu}^{\rho}
        - \frac{\partial \epsilon^{\rho}(x)}{\partial x^{\mu}}
    \right) \left(
        \delta_{\nu}^{\sigma}
        - \frac{\partial \epsilon^{\sigma}(x)}{\partial x^{\nu}}
    \right) g_{\rho \sigma}(x)
    \\
    &\simeq (
        \delta_{\mu}^{\rho}\delta_{\nu}^{\sigma}
        - \delta_{\mu}^{\rho} \partial_{\nu} \epsilon^{\sigma}(x)
        - \delta_{\nu}^{\sigma} \partial_{\mu} \epsilon^{\rho}(x)
    ) g_{\rho \sigma}(x)
    \\
    &= g_{\mu \nu}(x)
    - g_{\mu \sigma}(x) \partial_{\nu} \epsilon^{\sigma}(x)
    - g_{\rho \nu}(x) \partial_{\mu} \epsilon^{\rho}(x)
\end{aligned}
$$

For current purposes, we always assume that we are originally in *flat* (Euclidean) spacetime, i.e.

$$
g_{\mu \nu}(x) = \eta_{\mu \nu}
= \text{diag}(1,...,1)
$$

Then

$$
g_{\mu \nu}^{\prime}\left(x'\right)
= \eta_{\mu \nu}
- \partial_{\nu}\epsilon_{\mu}(x)
- \partial_{\mu}\epsilon_{\nu}(x)
$$

Then we get the requirement on the transformation

$$
\partial_{\mu} \epsilon_{\nu}(x)
+ \partial_{\nu} \epsilon_{\mu}(x)
= f(x) \eta_{\mu \nu}
$$

By taking trace of both sides, we can determine the factor $f(x)$:

$$
f(x) = \frac{2}{d} \partial_{\rho} \epsilon^{\rho}(x)
$$

### 2. Finite Conformal Transformations

$$
\begin{aligned}
    \text{Translation} &: 
    x'^{\mu} = x^{\mu}+a^{\mu}
    \\
    \text{Dilation} &: 
    x'^{\mu} = \alpha x^{\mu}
    \\
    \text{Rigid rotation} &: 
    x'^{\mu} = {M^{\mu}}_{\nu}x^{\nu}
    \\
    \text{Special conformal trans.} &: 
    x'^{\mu} =
    \frac{x^{\mu} - b^{\mu}x^2}
    {1 - 2b^{\rho} x_{\rho} + b^2x^2}
\end{aligned}
$$

The corresponding generators for *scalar fields* (for which
$\mathcal{F}(\phi)=\phi$) are

$$
\begin{aligned}
    \text{Translation}&: 
    P_{\mu} = -i \partial_{\mu}
    \\
    \text{Dilation} &:
    D = -i x^{\mu}\partial_{\mu}
    \\
    \text{Rigid rotation} &: 
    L_{\mu \nu} = i (
        x_{\mu} \partial_{\nu}
        - x_{\nu} \partial_{\mu}
    )
    \\
    \text{SCT} &:
    K_{\mu} = -i (
        2x_{\mu}x^{\nu}\partial_{\nu}
        - x^2\partial_{\mu}
    )
\end{aligned}
$$

If we define

$$
\begin{aligned}
    J_{\mu \nu} &= L_{\mu \nu}
    \\
    J_{-1,0} &= D
    \\
    J_{0 \mu} &= \frac{1}{2} (P_{\mu} + K_{\mu})
    \\
    J_{-1, \mu} &= \frac{1}{2} (P_{\mu} - K_{\mu})
\end{aligned}
$$

so that $J_{a b} = -J_{b a}$ for $a, b \in \{-1,0,1, ...,d\}$, then we have the algebra

$$
[J_{a b},J_{c d}]
= i (
    \eta_{a d} J_{b c} + \eta_{b c} J_{a d}
    - \eta_{a c} J_{b d} - \eta_{b d} J_{a c}
)
$$

with the metric (in Euclidean space)
$\eta_{a b}=\text{diag}(-1,1,1,...,1)$. This is the *same* as the $SO(d+1,1)$ algebra. Thus the conformal group in $d$ dimensions is *isomorphic* to the group $SO(d+1,1)$.

### Representations of the Conformal Group

More interesting representations of the conformal group can be obtained from the transformation of multi-component fields. Recall that

$$
\phi '(x)
= (1 - i \omega_a G_a ) \phi (x)
$$

