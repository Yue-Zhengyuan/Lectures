## Conformal Group in $d \ge 3$

### The Special Conformal Field Transformation (SCT)

### Finite Conformal Transformations

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
    \text{SCT} &: 
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