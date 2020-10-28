# Causality in Klein-Gordon Theory

## The Propagator

The **propagator** $D(x-y)$ is defined as the amplitude for a particle to propagate from $y$ to $x$ (in spacetime):

$$
\begin{aligned}
    D(x-y) &\equiv 
    \langle \bold{x}|e^{-i H(x^0 - y^0)}|\bold{y} \rangle
    \\
    &= \langle 0 | \phi(x) \phi(y) | 0 \rangle
\end{aligned}
$$

Using the expansion

$$
\begin{aligned}
    \phi(x) 
    &= \int \frac{d^{d-1} p}{(2\pi)^{d-1}} 
    \frac{1}{\sqrt{2 E_\bold{p}}} [
        a_\bold{p} e^{ipx} 
        + a^\dagger_\bold{p} e^{-ipx}
    ]
    \\[1em] \text{with} \quad
    p^0 &= \sqrt{m^2 + \bold{p}^2} = E_\bold{p}
\end{aligned}
$$

and noting that only the terms $\langle 0 | a_\bold{p} a_\bold{q}^\dagger |0\rangle = (2\pi)^3 \delta^3 (\bold{p-q})$ survives, we are left with

$$
\begin{aligned}
    D(x-y) &= \langle 0 | \phi(x) \phi(y) | 0 \rangle
    \\
    &= \int \frac{d^3 p}{(2\pi)^3} \frac{1}{2E_\bold{p}}
    e^{-ip(x-y)}
\end{aligned}
$$

## Measuring the Field at Two Places

We calculate 

$$
\begin{aligned}
    [\phi(x), \phi(y)]
    &= \int \frac{d^3p}{(2\pi)^3} \frac{d^3 q}{(2\pi)^3}
    \frac{1}{\sqrt{2E_\bold{p} \cdot 2 E_\bold{q}}}
    \\ &\qquad \times
    [
        a_\bold{p} e^{ipx} 
        + a^\dagger_\bold{p} e^{-ipx}, 
        a_\bold{q} e^{iqx} 
        + a^\dagger_\bold{q} e^{-iqx}
    ]
\end{aligned}
$$

Using the commutators

$$
\begin{aligned}
    [a_\bold{p}, a^\dagger_{\bold{p}'}]
    &= (2\pi)^3 \delta^3(\bold{p} - \bold{p}')
    \\
    [a_\bold{p}, a_{\bold{p}'}]
    &= [a^\dagger_\bold{p}, a^\dagger_{\bold{p}'}]
    = 0
\end{aligned}
$$

we obtain

$$
\begin{aligned}
    [\phi(x), \phi(y)]
    &= \int \frac{d^3p}{(2\pi)^3} \frac{1}{2E_\bold{q}}
    (e^{-ip(x-y)} - e^{ip(x-y)})
    \\
    &= D(x - y) - D(y - x)
\end{aligned}
$$

## The Klein-Gordon Propagators

### The Retarded Green's Function

The commutator $[\phi(x), \phi(y)]$ is a *c*-number, so it is equal to $\langle 0 | [\phi(x),\phi(y)] | 0 \rangle$. Assume that $x^0 > y^0$, we obtain

$$
\begin{aligned}
    &\langle 0 | [\phi(x),\phi(y)] | 0 \rangle
    \\
    &= \int \frac{d^3p}{(2\pi)^3} \frac{1}{2E_\bold{p}}
    \left. [e^{-ip(x-y)} - e^{ip(x-y)}]
    \right|_{p^0 = E_\bold{p}}
    \\
    &= \int \frac{d^3p}{(2\pi)^3} \left[
        \left. \frac{e^{-ip(x-y)}}{2E_\bold{p}}
        \right|_{p^0 = E_\bold{p}}
        - \left. \frac{e^{-ip(x-y)}}{2E_\bold{p}} 
        \right|_{p^0 = -E_\bold{p}}
    \right]
\end{aligned}
$$

In the second term, we have make the change of variable $p \to -p$, which does not cause additional minus signs since the the integration range is even.

The two terms in the square bracket can be regarded as *the residue of the complex contour integration over $p^0$*, of the following integrand with poles at $p^0 = \pm E_\bold{p}$: (the spatial part $e^{-i \bold{p} \cdot \bold{x-y}}$ is just a irrelevant constant factor in this integration)

$$
\begin{aligned}
    &\int \frac{dp^0}{2\pi i}
    \frac{e^{-ip(x-y)}}{p^2 - m^2}
    \qquad \left( \,
        p^2 - m^2 = (p^0)^2 - E_\bold{p}^2
    \, \right)
    \\[1.2em]
    &= \int \frac{dp^0}{2\pi i}
    \frac{e^{-ip(x-y)}}{2 E_\bold{p}} \left(
        \frac{1}{p^0 - E_\bold{p}} 
        - \frac{1}{p^0 + E_\bold{p}}
    \right)
\end{aligned}
$$

However, how the contour passes by the poles should be carefully chosen. First, the factor $e^{-ip^0(x^0-y^0)}$ will determine how the contour closes:

- When $x^0 - y^0 < 0$ (so that when $p^0 \to i\infty$ the factor vanishes), the contour closes in the **upper** half plane
- When $x^0 - y^0 > 0$, the contour closes in the **lower** half plane

Now that we assumed that $x^0 - y^0 > 0$. In order for the contour to enclose both poles, we make the shift

<center>

![](p0-int-DR.png)

</center>

$$
E_\bold{p} \to E_\bold{p} - i \epsilon, \quad
-E_\bold{p} \to -E_\bold{p} - i \epsilon, \quad
$$

Therefore

$$
\begin{aligned}
    D_R(x - y) 
    &= \theta(x^0 - y^0)
    \langle 0 | [\phi(x), \phi(y)] | 0 \rangle
    \\
    &= \int \frac{d^4 p}{(2\pi)^4}
    \frac{
        i e^{-i p(x - y)}
    }{
        p^2 - m^2
    }
\end{aligned}
$$

It is a Green's function of the Klein-Gordon EOM:

$$
(\partial^2 + m^2) D_R(x-y)
= -i \delta^4 (x-y)
$$

### Feynman Propagator

<center>

![](p0-int-DR.png)

</center>

$$
E_\bold{p} \to E_\bold{p} - i \epsilon, \quad
-E_\bold{p} \to -E_\bold{p} - i \epsilon, \quad
$$

$$
\begin{aligned}
    D_F(x - y)
    &\equiv \langle 0 | T[\phi(x) \phi(y)] |0 \rangle
    \\
    &= \lim_{\epsilon \to 0+}
    \int \frac{d^4 p}{(2\pi)^4}
    \frac{
        i e^{-i p(x - y)}
    }{
        p^2 - m^2 + i \epsilon
    }
\end{aligned}
$$

This is sometimes simply denoted by $D_{xy}$. We can verify that it is also a Green's function of the Klein-Gordon EOM:

$$
(\partial^2 + m^2) D_F(x-y)
= -i \delta^4 (x-y)
$$
