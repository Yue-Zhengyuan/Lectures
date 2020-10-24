# Correlation Function (Canonical Quantization)

The **$n$-point correlation function** is defined as

$$
\langle \phi(x_1) \cdots \phi(x_n) \rangle
= \langle \Omega| T [\phi(x_1) \cdots \phi(x_n)] |\Omega \rangle
$$

where $T$ is the **time ordering operator**, and $|\Omega\rangle$ is the ground state of the interacting theory.

## Two-Point Correlation Function

### Free Theory

The two-point correlation function in the free (Klein-Gordon) theory is just the Feynman propagator:

$$
\begin{aligned}
    \langle 0 | T[\phi(x) \phi(y)] | 0\rangle_\text{free}
    &= D_F(x - y)
    \\
    &= \int \frac{d^4 p}{(2\pi)^4}
    \frac{i e^{-i p(x-y)}}{p^2 - m^2 + i\epsilon}
\end{aligned}
$$

### The Interaction Picture

To obtain the two-point function for interacting theory, we need to use the **interaction picture** of the fields. 

### Interacting Theory

$$
\begin{aligned}
    &\langle \Omega | T[\phi(x) \phi(y)] | \Omega\rangle
    \\
    &= \lim_{T \to \infty(1-i\epsilon)}
    \frac{
        \left\langle 0 \left| T \left[
            \phi_I(x) \phi_I(y) \exp \left(
                -i \int_{-T}^{+T} dt H_I(t)
            \right)
        \right] \right| 0 \right\rangle
    }{
        \left\langle 0 \left| T \left[
            \exp \left(
                -i \int_{-T}^{+T} dt H_I(t)
            \right)
        \right] \right| 0 \right\rangle
    }
\end{aligned}
$$