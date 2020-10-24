# Description of Quantum Field Theory

## Lagrangian Field Theory

The Lagrangian description has the advantage that all expressions are explicitly *Lorentz invariant*. The theory is described by the action

$$
S = \int d^d x \, \mathcal{L}(\phi(x), \partial_\mu \phi(x))
$$

Varying the fields $\phi \to \delta \phi$ ($\delta \phi = 0$ at the boundary), the variation of action is

$$
\begin{aligned}
    \delta S 
    &= \int d^d x \, \left[
        \frac{\partial \mathcal{L}}{\partial \phi} \delta \phi
        + \frac{\partial \mathcal{L}}{\partial(\partial_\mu \phi)} \partial_\mu (\delta \phi)
    \right]
    \\
    &= \int d^d x \, \left[
        \frac{\partial \mathcal{L}}{\partial \phi} \delta \phi
        - \partial_\mu \left(
            \frac{\partial \mathcal{L}}{\partial(\partial_\mu \phi)}
        \right) \delta \phi
        + \partial_\mu \left(
            \frac{\partial \mathcal{L}}{\partial(\partial_\mu \phi)} \delta \phi
        \right)
    \right]
    \\
    &= \int d^d x \, \left[
        \frac{\partial \mathcal{L}}{\partial \phi}
        - \partial_\mu \left(
            \frac{\partial \mathcal{L}}{\partial(\partial_\mu \phi)}
        \right)
    \right] \delta \phi
\end{aligned}
$$

The last term in the second step can be converted (using Gauss' theorem) to an integration over the boundary, and hence vanishes. The **principle of least action** requires $\delta S = 0$. Due to the arbitrariness of $\delta \phi$, this means

$$
\partial_{\mu} \left(
    \frac{\partial \mathcal{L}}{\partial \left(\partial_{\mu} \phi \right)}
\right) 
- \frac{\partial \mathcal{L}}{\partial \phi}
= 0
$$

which is the **equation of motion (EOM)**. If there are multiple components of the field, the equation can be easily generalized to 

$$
\partial_{\mu} \left(
    \frac{\partial \mathcal{L}}{\partial \left(\partial_{\mu} \phi^\alpha \right)}
\right) 
- \frac{\partial \mathcal{L}}{\partial \phi^\alpha}
= 0
$$

### Ambiguity in Lagrangian

The equation of motion is unaffected if we add a *total derivative* term to $\mathcal{L}$:

$$
\mathcal{L} \to \mathcal{L} + \partial_\alpha X^\alpha(\phi, \partial_\mu \phi)
$$

since the variation of the additional total derivative term can be converted to integration over the boundary and vanishes.

## Hamiltonian Field Theory

Recall that for a discrete system, the Hamiltonian in classical mechanics is defined as

$$
H = \sum_a p_a \dot{q}_a - L, \quad
p_a = \frac{\partial L}{\partial \dot{q}_a}
$$

In field theory we deal with Lagrangian and Hamiltonian *densities*:

$$
L = \int d^3 x \, \mathcal{L}, 
\quad 
H = \int d^3 x \, \mathcal{H}
$$

In analogy, we define for QFT the **momentum density** conjugate to the field $\phi(\bold{x})$ as

$$
\pi(\bold{x}) \equiv
\frac{\partial \mathcal{L}}{\partial \dot{\phi}(\bold{x})}
,\quad
L = \int d^3 x \, \mathcal{L}
$$

and the relation between the Lagrangian density and the Hamiltonian density

$$
\mathcal{H} = \pi(\bold{x}) \dot{\phi}(\bold{x}) - \mathcal{L}
$$

