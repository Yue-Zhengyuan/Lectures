# Conserved Current

We first calculate the variation of the action under a symmetry operation. The new action is

$$
S' = \int d^d x' \, \mathcal{L}(
    \phi'(x'), \partial' \phi'(x')
)
$$

Recall that for infinitesimal transformations depending on a set of parameters $\omega_a$, the coordinates and the field itself transform according to:

$$
\begin{align*}
    x'^{\mu}(x,\omega)
    & =x^{\mu}
    + \omega_a \frac{\partial x'^{\mu}}{\partial \omega_a}
    \\
    \phi' (x')
    &= \phi (x)+\omega_a\frac{\partial F}{\partial \omega_a}
\end{align*}
$$

from which we obtain the Jacobi matrices for coordinate transformation (up to $O(\omega)$ terms)

$$
\begin{align*}
    \frac{\partial x'^\nu}{\partial x^\mu}
    &= \delta_\mu^\nu + \partial_\mu \left(
        \omega_a \frac{\partial x'^{\mu}}{\partial \omega_a}
    \right)
    \\
    \frac{\partial x^\nu}{\partial x'^\mu}
    &= \delta_\mu^\nu - \partial_\mu \left(
        \omega_a \frac{\partial x'^{\nu}}{\partial \omega_a}
    \right)
\end{align*}
$$

Then

$$
\begin{align*}
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
\end{align*}
$$

Up to $O(\omega)$ terms, the new action is

$$
\begin{align*}
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
    - \int d^dx \, (\partial_\mu \omega_a) j_a^\mu
\end{align*}
$$

where we introduced two new quantities

$$
\begin{align*}
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
    \\[2em]
    j_a^\mu &\equiv
    \frac{\partial \mathcal{L}}{\partial (\partial_\mu \phi)} 
    \frac{\partial x'^\nu}{\partial \omega_a} 
    \partial_\nu \phi
    - \frac{\partial x'^\mu}{\partial \omega_a} \mathcal{L}
    - \frac{\partial \mathcal{L}}{\partial (\partial_\mu \phi)}
    \frac{\partial F}{\partial \omega_a}
    \\
    &=
    \left[
        \frac{\partial \mathcal{L}}{\partial (\partial_\mu \phi)} 
        \partial_\nu \phi
        - \delta_\nu^\mu \mathcal{L}
    \right]
    \frac{\partial x'^\nu}{\partial \omega_a} 
    - \frac{\partial \mathcal{L}}{\partial (\partial_\mu \phi)}
    \frac{\partial F}{\partial \omega_a}
\end{align*}
$$

The quantity $j_a^\mu$ goes by a special name, called the **current** associated with the infinitesimal transformation. 

Any physical theory should be symmetric under **rigid transformations**, i.e. those with parameters $\omega_a$ *independent on $x$*. In this case

$$
\delta S = \int d^dx \, \omega_a f_a 
$$

and we conclude that **$f_a$ must be zero identically**. This is true even for $x$-dependent $\omega_a$. 

With $f_a = 0$, we are left with

$$
\delta S = - \int d^dx \, (\partial_\mu \omega_a) j_a^\mu
$$

which can be integrated by parts to yield

$$
\delta S = \int d^dx \, \omega_a (\partial_\mu j_a^\mu)
$$

## Conservation of Current

Requiring $\delta S = 0$ (which is equivalent to applying the equation of motion), and because of the arbitrariness of $\omega_a$, we obtain the **conservation of current**:

$$
\partial_\mu j_a^\mu = 0
$$

*Remark*: The expression of the current can be easily generalized to theories with more than one field:

$$
j_a^\mu
= \sum_i \left[
    \frac{\partial \mathcal{L}}{\partial (\partial_\mu \phi_i)} 
    \partial_\nu \phi_i
    - \delta_\nu^\mu \mathcal{L}
\right]
\frac{\partial x'^\nu}{\partial \omega_a} 
- \frac{\partial \mathcal{L}}{\partial (\partial_\mu \phi_i)}
\frac{\partial F_i}{\partial \omega_a}
$$

where $F_i$ is the map from $\phi_i(x)$ to $\phi'_i(x')$. Note that all the $\omega_a$ derivatives are evaluated at $\omega_a = 0$.
