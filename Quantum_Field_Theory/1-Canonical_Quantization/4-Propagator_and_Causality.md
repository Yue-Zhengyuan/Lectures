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

## The Retarded Green's Function

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

It is called a "Green's function" because when plugging it into the Klein-Gordon EOM, we obtain

$$
(\partial^2 + m^2) D_R(x-y)
= -i \delta^4 (x-y)
$$

## Feynman Propagator 

### Momentum Representation

$$
\begin{aligned}
    D_F(x - y)
    &= \langle 0 | T[\phi(x) \phi(y)] |0 \rangle
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

*Proof*:

### Position Representation

$$
\begin{aligned}
    D_F(x - y)
    &\equiv \langle 0 | T[\phi(x) \phi(y)] |0 \rangle
    \\
    &= - \lim_{\epsilon \to 0+}
    \frac{1}{4\pi^2}
    \frac{
        1
    }{
        (x - y)^2 - i \epsilon
    }
\end{aligned}
$$

*Proof*: