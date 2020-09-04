# Conformal Invariance

*By definition*, a **conformal transformation** of the coordinates is an *invertible* mapping $x\to x'$ which *leaves the metric invariant up to a scale*:

$$
g_{\mu \nu}^{\prime}\left(x'\right)
= \Lambda(x) g_{\mu \nu}(x)
$$

## Requirement on Infinitesimal Transformations

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
