# Complex Klein-Gordon Field

The Lagrangian of the **complex scalar field** theory is

$$
\mathcal{L} = (\partial_\mu \phi^*)(\partial^\mu \phi)
- m^2 \phi^* \phi
$$

The complex fields $\phi, \phi^*$ are treated as *independent variables*. Usually we shall make a substitution

$$
\phi = \frac{1}{\sqrt{2}}(\phi_1 + i\phi_2), \quad
\phi^* = \frac{1}{\sqrt{2}}(\phi_1 - i\phi_2)
$$

so that the Lagrangian is converted to a free theory of *two real scalar fields* $\phi_1, \phi_2$:

$$
\mathcal{L} = \frac{1}{2}[
    (\partial \phi_1)^2 + (\partial \phi_2)^2
] - \frac{1}{2}m^2 (\phi_1^2 + \phi_2^2)
$$

## Mode Expansion

Similar to the real field theory, we can expand $\phi_1, \phi_2$ as

$$
\begin{aligned}
    \phi_1(x) 
    &= \int \frac{d^3 p}{(2\pi)^3} 
    \frac{1}{\sqrt{2 \omega_\mathbf{p}}} [
        a_{1\mathbf{p}} e^{-ipx} 
        + a^\dagger_{1\mathbf{p}} e^{ipx}
    ] \\
    \phi_2(x) 
    &= \int \frac{d^3 p}{(2\pi)^3} 
    \frac{1}{\sqrt{2 \omega_\mathbf{p}}} [
        a_{2\mathbf{p}} e^{-ipx} 
        + a^\dagger_{2\mathbf{p}} e^{ipx}
    ]
\end{aligned}
$$

Then we combine them to obtain the expansion for $\phi, \phi^*$: define

$$
\begin{aligned}
    a_\mathbf{p} &\equiv 
    \frac{1}{\sqrt{2}} (a_{1\mathbf{p}} + ia_{2\mathbf{p}}),
    &\quad
    b_\mathbf{p} \equiv 
    \frac{1}{\sqrt{2}} (a_{1\mathbf{p}} - ia_{2\mathbf{p}})
    \\
    a_\mathbf{p}^\dagger &\equiv 
    \frac{1}{\sqrt{2}} (a_{1\mathbf{p}}^\dagger - ia_{2\mathbf{p}}^\dagger),
    &\quad
    b_\mathbf{p}^\dagger \equiv 
    \frac{1}{\sqrt{2}} (a_{1\mathbf{p}}^\dagger + ia_{2\mathbf{p}}^\dagger)
\end{aligned}
$$

we have

$$
\begin{aligned}
    \phi(x) 
    &= \int \frac{d^3 p}{(2\pi)^3} 
    \frac{1}{\sqrt{2 \omega_\mathbf{p}}} [
        a_{\mathbf{p}} e^{-ipx} 
        + b^\dagger_{\mathbf{p}} e^{ipx}
    ] \\
    \phi^*(x) 
    &= \int \frac{d^3 p}{(2\pi)^3} 
    \frac{1}{\sqrt{2 \omega_\mathbf{p}}} [
        b_{\mathbf{p}} e^{-ipx} 
        + a^\dagger_{\mathbf{p}} e^{ipx}
    ]
\end{aligned}
$$

## Commutators

## Feynman Propagator and Wick's Theorem



## Causality and Anti-Particles