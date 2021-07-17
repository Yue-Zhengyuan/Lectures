# Photon Propagator

We start from the Lagrangian of scalar QED:

$$
\begin{align*}
    \mathcal{L} 
    &= -\frac{1}{4} F_{\mu \nu} F^{\mu \nu}
    + (D_\mu \phi^*)(D^\mu \phi) - m^2 \phi^* \phi
    \\[1em]
    &= -\frac{1}{4} F_{\mu \nu} F^{\mu \nu}
    + (\partial_\mu \phi^*)(\partial^\mu \phi)
    - m^2 \phi^* \phi
    \\ &\qquad
    + ieA_\mu (\phi^* \partial^\mu \phi - \phi \partial^\mu \phi^*)
    + e^2 A_\mu A^\mu \phi^* \phi
    \\[1em]
    &\text{with} \qquad
    \begin{align*}
        D_\mu &= \partial_\mu + ieA_\mu
        \\
        F_{\mu\nu} &= \partial_\mu A_\nu - \partial_\nu A_\mu
        \\
        &= D_\mu A_\nu - D_\nu A_\mu
    \end{align*}
\end{align*}
$$

$D_\mu$ is called the **gauge-covariant derivative**.

This theory is invariant under the following gauge transformation

$$
\begin{align*}
    \phi &\to &\phi' &= e^{i\alpha(x)} \phi
    \\
    eA_\mu &\to &eA'_\mu &= eA_\mu - \partial_\mu \alpha(x)
\end{align*}
$$

----

*Verify*: For the second term in $\mathcal{L}$: 

$$
\begin{align*}
    D'^\mu \phi'
    &= (\partial_\mu + ieA'_\mu) \phi'
    \\
    &= (\partial_\mu + ieA_\mu - i\partial_\mu\alpha)
    e^{i\alpha} \phi
    \\
    &= (\partial_\mu + ieA_\mu) \phi
    \\
    &= D^\mu \phi
\end{align*}
$$

and similarly $D'_\mu \phi'^* = D_\mu \phi^*$. 

----

Recall that the current in the complex scalar field theory is

$$
j^\mu = i (\phi^* \partial^\mu \phi - \phi \partial^\mu \phi^*)
$$

It can be directly generalized to a gauge-invariant one by using the covariant derivative

$$
\begin{align*}
    J^\mu &= i (\phi^* D^\mu \phi - \phi D^\mu \phi^*)
    \\
    &= i (\phi^* \partial^\mu \phi - \phi \partial^\mu \phi^*)
    - 2e A^\mu \phi^* \phi
\end{align*}
$$

----

*Verify*:

----

With this current, the scalar QED Lagrangian can be written as

$$
\mathcal{L} = -\frac{1}{4} F_{\mu \nu}^2 - A_\mu J^\mu
$$

## Propagator of the Scalar Particles

The propagator of the scalar particles is calculated from

$$
\begin{align*}
    \langle 0 |T[\phi^*(x) \phi(y)] | 0\rangle
\end{align*}
$$

Since the terms in $\mathcal{L}$ containing only $\phi, \phi^*$ are the same as the scalar field theory, we use the same mode expansion to obtain the same propagator:

$$
\begin{align*}
    \langle 0 |T[\phi^*(x) \phi(y)] | 0\rangle
    = \int \frac{d^4 p}{(2\pi)^4}
    \frac{
        i e^{i p(x - y)}
    }{
        p^2 - m^2 + i \epsilon
    }
\end{align*}
$$

## Propagator of the Photons

The vector field $A_\mu$ represents the **photon**. Its propagator $\Pi_{\mu\nu}$ is calculated from the Fourier transform:

$$
\langle 0 |T[A_\mu(x) A_\nu(y)] | 0\rangle
= \int \frac{d^4 p}{(2\pi)^4}
i e^{i p(x - y)}
\Pi_{\mu\nu}(p)
$$

The propagator should be a Green's function to the equation of motion for $A_\mu$, which is

$$
\partial^\mu F_{\mu \nu} = J_\nu
$$

Transforming into the momentum space $(\partial_\mu \to i p_\mu)$