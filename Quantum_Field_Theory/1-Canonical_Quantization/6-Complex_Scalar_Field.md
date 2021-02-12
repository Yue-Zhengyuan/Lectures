# Complex Klein-Gordon Field

The Lagrangian of the **complex scalar field** theory is

$$
\mathcal{L} = (\partial_\mu \phi^\dagger)(\partial^\mu \phi)
- m^2 \phi^\dagger \phi
$$

The complex fields $\phi, \phi^\dagger$ are treated as *independent variables*. Usually we shall make a substitution

$$
\phi = \frac{1}{\sqrt{2}}(\phi_1 + i\phi_2), \quad
\phi^\dagger = \frac{1}{\sqrt{2}}(\phi_1 - i\phi_2)
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
    \frac{1}{\sqrt{2 E_\mathbf{p}}} [
        a_{1\mathbf{p}} e^{-ipx} 
        + a^\dagger_{1\mathbf{p}} e^{ipx}
    ] \\
    \phi_2(x) 
    &= \int \frac{d^3 p}{(2\pi)^3} 
    \frac{1}{\sqrt{2 E_\mathbf{p}}} [
        a_{2\mathbf{p}} e^{-ipx} 
        + a^\dagger_{2\mathbf{p}} e^{ipx}
    ]
\end{aligned}
$$

where $p^0 = E_\mathbf{p} = \sqrt{m^2 + \mathbf{p}^2}$. Define

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

we combine the two fields $\phi_1, \phi_2$: 

$$
\begin{aligned}
    \phi(x) 
    &= \int \frac{d^3 p}{(2\pi)^3} 
    \frac{1}{\sqrt{2 E_\mathbf{p}}} [
        a_{\mathbf{p}} e^{-ipx} 
        + b^\dagger_{\mathbf{p}} e^{ipx}
    ] \\
    \phi^\dagger(x) 
    &= \int \frac{d^3 p}{(2\pi)^3} 
    \frac{1}{\sqrt{2 E_\mathbf{p}}} [
        b_{\mathbf{p}} e^{-ipx} 
        + a^\dagger_{\mathbf{p}} e^{ipx}
    ]
\end{aligned}
$$

## Commutators

## Anti-Particles

The complex scalar field theory has a global $U(1)$ symmetry: the Lagrangian is invariant under a change of phase angle

$$
\phi(x) \to e^{i\alpha} \phi(x), \quad
\phi^\dagger(x) \to e^{-i\alpha} \phi^\dagger(x)
$$

This symmetry does not involve coordinate transformation, thus the current associated with this symmetry is

$$
\begin{aligned}
    j^\mu &= \left[
        - \frac{\partial \mathcal{L}}{\partial (\partial_\mu \phi)}
        \frac{\partial F[\phi(x)]}{\partial \alpha}
        - \frac{\partial \mathcal{L}}{\partial (\partial_\mu \phi^\dagger)}
        \frac{\partial F^*[\phi^\dagger(x)]}{\partial \alpha}
    \right]_{\alpha = 0}
    \\
    &= \left[
        -\partial^\mu \phi^\dagger \times ie^{i\alpha} \phi
        - \partial^\mu \phi (-ie^{-i\alpha} \phi^\dagger)
    \right]_{\alpha = 0}
    \\
    &= i (\phi^\dagger \partial^\mu \phi - \phi \partial^\mu \phi^\dagger)
\end{aligned}
$$

----

Again, we verify that the rigid part $f$ is zero (omitting terms with derivatives of $x'$; $c.c.$ is for complex conjugate):

$$
\begin{aligned}
    f &= \left[
        \frac{\partial F}{\partial \alpha}
        \frac{\partial \mathcal{L}}{\partial \phi}
        + 
        \frac{\partial \mathcal{L}}{\partial (\partial_\mu \phi)} 
        \left(
            \partial_\mu \frac{\partial F}{\partial \alpha}
        \right) + c.c.
    \right]_{\alpha = 0}
    \\
    &= \left[
        i e^{i\alpha} \phi \times (-m^2 \phi^\dagger)
        + \partial^\mu \phi^\dagger\times \partial_\mu(i e^{i\alpha} \phi)
        + c.c.
    \right]_{\alpha = 0}
    \\
    &= -im^2 \phi \phi^\dagger + i (\partial^\mu \phi^\dagger)(\partial_\mu\phi)
    + c.c
    \\
    &= 0
\end{aligned}
$$

----

This leads to the conserved charge (it does not matter whether we use $j^0$ or $j_0$, since they are the same in flat spacetime)

$$
\begin{aligned}
    Q &= \int d^3x \, j_0
    \\
    &= i \int d^3x (\phi^\dagger \partial_0 \phi - \phi \partial_0 \phi^\dagger)
\end{aligned}
$$

Plugging in the mode expansion:

$$
\begin{aligned}
    \partial_0 \phi
    &= i \int \frac{d^3 p}{(2\pi)^3} 
    \sqrt{\frac{E_\mathbf{p}}{2}} [
        - a_{\mathbf{p}} e^{-ipx} 
        + b^\dagger_{\mathbf{p}} e^{ipx}
    ] \\
    \partial_0 \phi^\dagger
    &= i \int \frac{d^3 p}{(2\pi)^3}
    \sqrt{\frac{E_\mathbf{p}}{2}} [
        - b_{\mathbf{p}} e^{-ipx} 
        + a^\dagger_{\mathbf{p}} e^{ipx}
    ]
\end{aligned}
$$

Then

$$
\begin{aligned}
    Q
    &= \int d^3x \frac{d^3 p}{(2\pi)^3} \frac{d^3 q}{(2\pi)^3} 
    \sqrt{\frac{E_\mathbf{q}}{4 E_\mathbf{p}}}
    \\ & \qquad \quad \Big\{ 
        [
            b_{\mathbf{p}} e^{-ipx} 
            + a^\dagger_{\mathbf{p}} e^{ipx}
        ] [
            a_{\mathbf{q}} e^{-iqx} 
            - b^\dagger_{\mathbf{q}} e^{iqx}
        ] \\ &\qquad \qquad -
        [
            a_{\mathbf{p}} e^{-ipx} 
            + b^\dagger_{\mathbf{p}} e^{ipx}
        ] [
            b_{\mathbf{q}} e^{-iqx} 
            - a^\dagger_{\mathbf{q}} e^{iqx}
        ]
    \Big\}
    \\
    &= \int d^3x \frac{d^3 p}{(2\pi)^3} \frac{d^3 q}{(2\pi)^3} 
    \sqrt{\frac{E_\mathbf{q}}{4 E_\mathbf{p}}}
    \\ & \qquad \quad \Big\{
        (b_\mathbf{p}a_\mathbf{q} - a_\mathbf{p} b_\mathbf{q}) e^{-i(p+q)x} 
        + (b_\mathbf{p}^\dagger a_\mathbf{q}^\dagger - a_\mathbf{p}^\dagger b_\mathbf{q}^\dagger) e^{+i(p+q)x} 
        \\ &\qquad \qquad
        + (a_\mathbf{p}^\dagger a_\mathbf{q} - b_\mathbf{p}^\dagger b_\mathbf{q}) e^{i(p-q)x}
        + (a_\mathbf{p} a_\mathbf{q}^\dagger - b_\mathbf{p} b_\mathbf{q}^\dagger) e^{i(-p+q)x}
    \Big\}
\end{aligned}
$$

Integration over $x$ will give some delta functions, allowing us to remove integration over $\mathbf{q}$ and the $E_\mathbf{p}$ factors:

$$
\begin{aligned}
    Q &= \frac{1}{2}
    \int \frac{d^3p}{(2\pi)^3} \Big\{
        (b_\mathbf{p}a_\mathbf{-p} - a_\mathbf{p} b_\mathbf{-p}) 
        + (b_\mathbf{p}^\dagger a_\mathbf{-p}^\dagger - a_\mathbf{p}^\dagger b_\mathbf{-p}^\dagger) 
        \\ &\qquad \qquad
        + (a_\mathbf{p}^\dagger a_\mathbf{p} - b_\mathbf{p}^\dagger b_\mathbf{p}) 
        + (a_\mathbf{p} a_\mathbf{p}^\dagger - b_\mathbf{p} b_\mathbf{p}^\dagger)
    \Big\}
\end{aligned}
$$

The first two brackets vanish, since (e.g. for the first one)

$$
\begin{aligned}
    &\int \frac{d^3p}{(2\pi)^3} 
    (b_\mathbf{p}a_\mathbf{-p} - a_\mathbf{p} b_\mathbf{-p}) 
    = \int \frac{d^3p}{(2\pi)^3} 
    (b_\mathbf{p}a_\mathbf{-p} - b_\mathbf{-p} a_\mathbf{p}) 
    \\
    &=\int \frac{d^3p}{(2\pi)^3} 
    (b_\mathbf{p}a_\mathbf{-p} - b_\mathbf{p} a_\mathbf{-p})
    = 0 
\end{aligned}
$$

The last two brackets are rearranged to

$$
\begin{aligned}
    Q &= \frac{1}{2}
    \int \frac{d^3p}{(2\pi)^3} \Big\{
        (
            2 a_\mathbf{p}^\dagger a_\mathbf{p} 
            + \underbrace{[a_\mathbf{p}, a_\mathbf{p}^\dagger]}_{(2\pi)^3 \delta^3(0)}
        ) - (
            2 b_\mathbf{p}^\dagger b_\mathbf{p} 
            + \underbrace{[b_\mathbf{p}, b_\mathbf{p}^\dagger]}_{(2\pi)^3 \delta^3(0)}
        )
    \Big\}
    \\
    &= \int \frac{d^3p}{(2\pi)^3} \Big(
        a_\mathbf{p}^\dagger a_\mathbf{p} 
        - b_\mathbf{p}^\dagger b_\mathbf{p} 
    \Big)
\end{aligned}
$$

Now we see that $a_\mathbf{p}^\dagger$ creates particles with positive charges, while $b_\mathbf{p}^\dagger$ creates particles with negative charges. They are interpreted as **anti-particles** of each other. The conserved charge then has the meaning

$$
Q = \text{Number of Particles} - \text{Number of Anti-Particles}
$$

## Feynman Propagator and Wick's Theorem

Since $\phi$ creates $b$ and annihilates $a$ only, we can easily see that

$$
\begin{aligned}
    \langle 0 | T[\phi(x) \phi(y)] | 0 \rangle &= 0
    \\[0.5em]
    \langle 0 | T[\phi^\dagger(x) \phi^\dagger(y)] | 0 \rangle &= 0
\end{aligned}
$$

Thus the only meaningful 2-point function is

$$
\langle 0 | T[\phi^\dagger(x) \phi(y)] | 0 \rangle
= \langle 0 | T[\phi(y) \phi^\dagger(x)] | 0 \rangle
$$

Let us evaluate this propagator explicitly:

$$
\begin{aligned}
    &\langle 0 | T[\phi^\dagger(x) \phi(y)] | 0 \rangle
    \\
    &= \langle 0 |\phi^\dagger(x) \phi(y)| 0 \rangle \theta(x^0 - y^0)
    + \langle 0 |\phi(y) \phi^\dagger(x)| 0 \rangle \theta(y^0 - x^0)
\end{aligned}
$$

Let us express $\phi^\dagger(x) \phi(y)$ using normal-ordered operators:

$$
\begin{aligned}
    \phi^\dagger(x) \phi(y)
    &= \int \frac{d^3 p}{(2\pi)^3} 
    \frac{1}{\sqrt{2 E_\mathbf{p}}} [
        b_{\mathbf{p}} e^{-ipx} 
        + a^\dagger_{\mathbf{p}} e^{ipx}
    ] \\ & \quad \times
    \int \frac{d^3 q}{(2\pi)^3} 
    \frac{1}{\sqrt{2 E_\mathbf{q}}} [
        a_{\mathbf{q}} e^{-iqy} 
        + b^\dagger_{\mathbf{q}} e^{iqy}
    ]
    \\
    &= \int \frac{d^3 p}{(2\pi)^3} 
    \frac{d^3 q}{(2\pi)^3} 
    \frac{1}{\sqrt{2 E_\mathbf{p} 2 E_\mathbf{q}}}
    [
        b_\mathbf{p} a_\mathbf{q} e^{i(-px-qy)}
        \\ & \qquad
        + b_\mathbf{p} b_\mathbf{q}^\dagger e^{i(-px+qy)}
        + a_\mathbf{p}^\dagger a_\mathbf{q} e^{i(px-qy)}
        + a_\mathbf{p}^\dagger b_\mathbf{q}^\dagger e^{i(px+qy)}
    ]
\end{aligned}
$$

The only term survives is

$$
\langle 0 | b_\mathbf{p} b_\mathbf{q}^\dagger |0\rangle = (2\pi)^3 \delta^3 (\mathbf{p-q})
$$

Similarly, for

$$
\begin{aligned}
    \phi(y) \phi^\dagger(x)
    &= \int \frac{d^3 q}{(2\pi)^3} 
    \frac{1}{\sqrt{2 E_\mathbf{q}}} [
        a_{\mathbf{q}} e^{-iqy} 
        + b^\dagger_{\mathbf{q}} e^{iqy}
    ] \\ & \quad \times
    \int \frac{d^3 p}{(2\pi)^3} 
    \frac{1}{\sqrt{2 E_\mathbf{p}}} [
        b_{\mathbf{p}} e^{-ipx} 
        + a^\dagger_{\mathbf{p}} e^{ipx}
    ]
\end{aligned}
$$

The only term survives is

$$
\langle 0 | a_\mathbf{q} a_\mathbf{p}^\dagger |0\rangle = (2\pi)^3 \delta^3 (\mathbf{p-q})
$$

Therefore 

$$
\begin{aligned}
    \langle 0 |\phi^\dagger(x) \phi(y)| 0 \rangle
    &= \int \frac{d^3 p}{(2\pi)^3} \left.
    \frac{1}{2E_\mathbf{p}} e^{-ip(x-y)}
    \right|_{p^0 = E_\mathbf{p}} 
    \\
    &= D(x - y)
    \\[1em]
    \langle 0 |\phi(y) \phi^\dagger(x)| 0 \rangle
    &= \int \frac{d^3 p}{(2\pi)^3} \left.
    \frac{1}{2E_\mathbf{p}} e^{-ip(y-x)}
    \right|_{p^0 = E_\mathbf{p}} 
    \\
    &= D(y - x)
    \\[1em]
    \langle 0 | T[\phi^\dagger(x) \phi(y)] | 0 \rangle
    &= D(x - y) \theta(x^0 - y^0)
    \\ &\quad
    + D(y - x) \theta(y^0 - x^0)
\end{aligned}
$$

We see that

- When $x^0 > y^0$, it is the $b$ particle that is propagating;
- When $x^0 < y^0$, it is the $a$ particle that is propagating.

These is the very similar to the results from real scalar field theory. Thus the Feynman propagator is

$$
\begin{aligned}
    D_F(x - y) 
    &= \langle 0 | T[\phi^\dagger(x) \phi(y)] | 0 \rangle
    \\[0.5em]
    &= \int \frac{d^4 p}{(2\pi)^4}
    \frac{
        i e^{\pm i p(x - y)}
    }{
        p^2 - m^2 + i \epsilon
    }
\end{aligned}
$$