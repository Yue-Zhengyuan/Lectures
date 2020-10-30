# Conserved Current

We first calculate the variation of the action under a symmetry operation. The new action is

$$
S' = \int d^d x' \, \mathcal{L}(
    \phi'(x'), \partial' \phi'(x')
)
$$

Recall that for infinitesimal transformations depending on a set of parameters $\omega_a$, the coordinates and the field itself transform according to:

$$
\begin{aligned}
    x'^{\mu}(x,\omega)
    & =x^{\mu}
    + \omega_a \frac{\partial x'^{\mu}}{\partial \omega_a}
    \\
    \phi' (x')
    &= \phi (x)+\omega_a\frac{\partial F}{\partial \omega_a}
\end{aligned}
$$

from which we obtain the Jacobi matrices for coordinate transformation (up to $O(\omega)$ terms)

$$
\begin{aligned}
    \frac{\partial x'^\nu}{\partial x^\mu}
    &= \delta_\mu^\nu + \partial_\mu \left(
        \omega_a \frac{\partial x'^{\mu}}{\partial \omega_a}
    \right)
    \\
    \frac{\partial x^\nu}{\partial x'^\mu}
    &= \delta_\mu^\nu - \partial_\mu \left(
        \omega_a \frac{\partial x'^{\nu}}{\partial \omega_a}
    \right)
\end{aligned}
$$

Then

$$
\begin{aligned}
    d^d x' 
    &= d^d x \det \frac{\partial x'^\nu}{\partial x^\mu}
    \\
    &= d^d x \left(
        1 + \partial_\mu \left(
            \omega_a \frac{\partial x'^{\mu}}{\partial \omega_a}
        \right)
    \right)
    \\
    \\
    \partial'_\mu \phi'(x')
    &= \frac{\partial x^\nu}{\partial x'^\mu} \partial_\nu
    \left(
        \phi (x)+\omega_a\frac{\partial F}{\partial \omega_a}
    \right)
    \\
    &= \left(
        \delta_\mu^\nu - \partial_\mu \left(
            \omega_a \frac{\partial x'^{\nu}}{\partial \omega_a}
        \right)
    \right) \partial_\nu
    \left(
        \phi (x)+\omega_a\frac{\partial F}{\partial \omega_a}
    \right)
    \\
    &= \partial_\mu \left(
        \phi (x)+\omega_a\frac{\partial F}{\partial \omega_a}
    \right)
    - \partial_\mu \left(
        \omega_a \frac{\partial x'^{\nu}}{\partial \omega_a}
    \right) \partial_\nu \phi(x) 
    + O(\omega^2)
\end{aligned}
$$

Up to $O(\omega)$ terms, the new action is

$$
\begin{aligned}
    S' 
    &= \int d^d x \left[
        1 + \partial_\mu \left(
            \omega_a \frac{\partial x'^{\mu}}{\partial \omega_a}
        \right)
    \right]
    \\ &\qquad \times
    \mathcal{L} \left[
        \phi + \omega_a\frac{\partial F}{\partial \omega_a}
        , \,
        \partial_\mu \left(
            \phi + \omega_a\frac{\partial F}{\partial \omega_a}
        \right)
        - \partial_\mu \left(
            \omega_a \frac{\partial x'^{\nu}}{\partial \omega_a}
        \right) \partial_\nu \phi
    \right]
    \\
    &= \int d^d x \left[
        1 + \partial_\mu \left(
            \omega_a \frac{\partial x'^{\mu}}{\partial \omega_a}
        \right)
    \right]
    \\ &\qquad \times
    \left\{
        \mathcal{L}(\phi,\partial_\mu \phi)
        + \omega_a \frac{\partial F}{\partial \omega_a}
        \frac{\partial \mathcal{L}}{\partial \phi}
        \right.
        \\ & \qquad \qquad
        \left.
        + \left[
            \partial_\mu \left(
                \omega_a\frac{\partial F}{\partial \omega_a}
            \right)
            - \partial_\mu \left(
                \omega_a \frac{\partial x'^{\nu}}{\partial \omega_a}
            \right) \partial_\nu \phi
        \right]
        \frac{\partial \mathcal{L}}{\partial (\partial_\mu \phi)}
    \right\}
    \\
    &= \underbrace{
        \int d^d x \, 
        \mathcal{L}(\phi(x), \partial_\mu \phi(x))
    }_S 
    + \int d^dx \, \omega_a f_a 
    - \underbrace{
        \int d^dx \, (\partial_\mu \omega_a) j_a^\mu
    }_{\text{integrate by parts}}
    \\
    &= S + \int d^d x \,
    \omega_a (f_a + \partial_\mu j_a^\mu)
\end{aligned}
$$

where we introduced two new quantities

$$
\begin{aligned}
    f_a &\equiv
    \mathcal{L} \, \partial_\mu 
    \frac{\partial x'^\mu}{\partial \omega_a}
    + \frac{\partial F}{\partial \omega_a}
    \frac{\partial \mathcal{L}}{\partial \phi}
    \\ &\quad
    + 
    \frac{\partial \mathcal{L}}{\partial (\partial_\mu \phi)} 
    \left[
        \partial_\mu \frac{\partial F}{\partial \omega_a}
        - (\partial_\nu \phi) \, 
        \partial_\mu 
        \frac{\partial x'^{\nu}}{\partial \omega_a}
    \right]
    \\ \\
    j_a^\mu &\equiv
    \frac{\partial \mathcal{L}}{\partial (\partial_\mu \phi)} 
    \frac{\partial x'^\nu}{\partial \omega_a} 
    \partial_\nu \phi
    - \frac{\partial x'^\mu}{\partial \omega_a} \mathcal{L}
    - \frac{\partial \mathcal{L}}{\partial (\partial_\mu \phi)}
    \frac{\partial F}{\partial \omega_a}
    \\
    &=
    \left\{
        \frac{\partial \mathcal{L}}{\partial (\partial_\mu \phi)} 
        \partial_\nu \phi
        - \delta_\nu^\mu \mathcal{L}
    \right\}
    \frac{\partial x'^\nu}{\partial \omega_a} 
    - \frac{\partial \mathcal{L}}{\partial (\partial_\mu \phi)}
    \frac{\partial F}{\partial \omega_a}
\end{aligned}
$$

The quantity $j_a^\mu$ goes by a special name, called the **current** associated with the infinitesimal transformation.

*Example*:

- **Scaling**

    $$
    x' = (1 + \omega) x
    \qquad
    \phi'(x') = \phi(x) = F(\phi(x),\omega)
    $$

    Obviously

    $$
    \frac{\partial x'^\nu}{\partial \omega} = x^\nu
    \qquad
    \frac{\partial F}{\partial \omega} = 0 
    $$

    Then

    $$
    \begin{aligned}
        f_a &\equiv
        \mathcal{L} \, \partial_\mu x^\mu
        + 
        \frac{\partial \mathcal{L}}{\partial (\partial_\mu \phi)} 
        \left[
            - (\partial_\nu \phi) \, 
            \partial_\mu x^\nu
        \right]
        \\
        &= \mathcal{L} \times d
        - \frac{\partial \mathcal{L}}{\partial (\partial_\mu \phi)} \partial_\mu \phi
    \end{aligned}
    $$

