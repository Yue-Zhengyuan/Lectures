# Real Scalar Field Theory

The Lagrangian of the **real scalar (Klein-Gordon) field theory** is

$$
\begin{align*}
    \mathcal{L} 
    &= \frac{1}{2} [(\partial \phi)^2 
    -  m^2 \phi^2]
    \\
    &= \frac{1}{2} (
        \dot{\phi}^2 - (\nabla \phi)^2 - m^2 \phi^2
    )
\end{align*}
$$

where $\phi$ is a *real-valued* field. The equation of motion is found to be (called the **Klein-Gordon equation**)

$$
(\partial^2 + m^2) \phi = 0
$$

The momentum conjugate to $\phi$ is

$$
\pi(x) = \frac{\partial \mathcal{L}}{\partial \dot{\phi}}
= \dot{\phi}(x)
$$

which lead to the Hamiltonian

$$
\begin{align*}
    \mathcal{H} 
    &= \pi \dot{\phi} - \mathcal{L}
    \\
    &= \frac{1}{2} (
        \pi^2 + (\nabla \phi)^2 + m^2 \phi^2
    )
\end{align*}
$$

## Discretized Quantization

To illustrate the ideas on canonical quantization, we shall limit to (1 + 1)D spacetime for clarity. 

The conceptual difficulties associated with the *continuous* degrees of freedom may be lifted by replacing space with a discrete lattice of $N$ points at positions 

$$
x_n = n a, \quad (n = 0,1,...,N-1)
$$

where $a$ is the lattice spacing. We also assume that the fields $\phi_n \equiv \phi(x_n)$ defined on it obey the periodic boundary condition:

$$
\phi_{n} = \phi_{n+N}
$$

The Lagrangian now takes the discrete form

$$
\begin{align*}
    L &= \int dx \, \frac{1}{2} (
        \dot{\phi}^2 - (\nabla \phi)^2 - m^2 \phi^2
    ) \\
    &\to \sum_{n=0}^{N-1} \frac{a}{2} \left[
        \dot{\phi}_n^2 
        - \left(
            \frac{\phi_{n+1} - \phi_n}{a}
        \right)^2
        - m^2 \phi_n^2 
    \right]
\end{align*}
$$

The momentum operators conjugate to $\phi_n$ are

$$
\pi_n 
= \frac{\partial L}{\partial \dot{\phi}_n} 
= a \dot{\phi}_n
$$

Thus the Hamiltonian is

$$
\begin{align*}
    H &= \sum_n \pi_n \dot{\phi}_n - L
    \\
    &= \frac{1}{2a} \sum_{n=0}^{N-1} \left[
        \pi_n^2 + (\phi_{n+1}-\phi_n)^2 - a^2 m^2 \phi_n^2
    \right]
\end{align*}
$$

The **canonical quantization** means that we *impose* the following **equal-time commutation relations (ETC)**:

$$
\begin{align*}
    [\phi_n, \pi_m] &= i \delta_{nm}
    \\
    [\phi_n, \phi_m] &= [\pi_n, \pi_m] = 0
\end{align*} \quad
(x_n^0 = x_m^0)
$$

The periodic boundary conditions and the translational invariance of $H$ motivate the use of [**discrete Fourier transforms**](https://en.wikipedia.org/wiki/Discrete_Fourier_transform#Definition):

$$
\begin{align*}
    \phi_k &= \frac{1}{\sqrt{N}} \sum_{n=0}^{N-1} \phi_n e^{-2\pi ikn/N}
    \\
    \pi_k &= \frac{1}{\sqrt{N}} \sum_{n=0}^{N-1} \pi_n e^{-2\pi ikn/N}
\end{align*} \quad
(k = 0, 1, ..., N-1)
$$

Since $\phi_n, \pi_n$ are *real* fields, we have

$$
\phi_k^\dagger = \phi_{-k}, \quad
\pi_k^\dagger = \pi_{-k}
$$

We can show that the Fourier modes $\phi_k, \pi_q$ obey the following ETC (note the dagger on $\pi_q$):

$$
[\phi_k, \pi^\dagger_q] = i \delta_{kq}
$$

Using these Fourier modes, the Hamiltonian becomes

$$
\begin{align*}
    H &= \frac{1}{2a} \sum_{k=0}^{N-1} \left[
        \pi_k \pi_k^\dagger 
        + a^2 \omega_k^2 \phi_k \phi_k^\dagger
    \right]
    \\
    \text{with} \quad \omega_k^2
    &= m^2 + \frac{2}{a^2} 
    (1 - \cos p_k a), \quad
    p_k = \frac{2\pi k}{N a}
\end{align*}
$$

We see that *each mode labelled by $k$ is an harmonic oscillator*. Following the usual methods, we define the **raising and lowering operators**:

$$
\begin{align*}
    a_k &= \frac{1}{\sqrt{2 a \omega_k}} 
    (a \omega_k \phi_k + i \pi_k)
    \\
    a_k^\dagger &= \frac{1}{\sqrt{2 a \omega_k}} 
    (a \omega_k \phi_k^\dagger - i \pi_k^\dagger)
\end{align*}
\, \Leftrightarrow \,
\begin{align*}
    \phi_k &= 
    \\
    \pi_k &= 
\end{align*}
$$

which can be verified to obey the commutation rules

$$
[a_k, a_q^\dagger] = \delta_{kq}
$$

Then the Hamiltonian becomes

$$
\begin{align*}
    H &= \frac{1}{2} \sum_{k=0}^{N-1} 
    (a_k^\dagger a_k + a_k a_k^\dagger) \omega_k
    \\
    &= \sum_{k=0}^{N-1} \left(
        a_k^\dagger a_k + \frac{1}{2}
    \right) \omega_k
\end{align*}
$$

The time evolution of $a_k$ (in Heisenberg picture) is determined by

$$
\partial_t a_k = i[J, a_k] = -i \omega_k a_k
$$

which means

$$
a_k(t) = a_k(0) e^{-i\omega_k t}
$$

Thus, performing the inverse Fourier transform, the complete time-dependent field $\phi_n(t)$ is

$$
\begin{align*}
    \phi_n(t) 
    &= \frac{1}{\sqrt{N}} \sum_{k=0}^{N-1} \phi_k(t) e^{+2\pi ikn/N}
    \\
    &= \sum_{k=0}^{N-1} \frac{2}{\sqrt{N a \omega_k}} \left[
        a_k(0) e^{i(- \omega_k t + 2\pi kn/N)}
        + a_k^\dagger(0) e^{i(\omega_k t -2\pi kn/N)}
    \right]
    \\
    &= \sum_{k=0}^{N-1} \frac{2}{\sqrt{N a \omega_k}} \left[
        a_k(0) e^{i(- \omega_k t + p_k x_n)}
        + a_k^\dagger(0) e^{i(\omega_k t -p_k x_n)}
    \right]
\end{align*}
$$

## Continuum Limit

The continuum limit is obtained by

$$
Na = \text{const} \quad \text{and} \quad
a \to 0
$$

For fields (the $1/a$ factor before $\pi_n$ is because $\pi(x)$ is the momentum *density*)

$$
\phi_n \to \phi(x), \quad
\frac{1}{a} \pi_n \to \pi(x) = \dot{\phi}(x) \qquad 
(x = na)
$$

The summation over sites is changed to integration over real space

$$
a \sum_{n=0}^{N-1} \to \int dx \qquad
\delta_{n n'} \to a \delta(x - x')
$$

Thus the commutation relations become

$$
[\phi(x), \pi(x')] = i \delta(x - x')
$$

Summation over the Fourier index $k$ is changed to integration over the momentum space ($V$ is the system volume)

$$
\frac{1}{V}\sum_{k=0}^{N-1} \to \frac{d^{d-1} p}{(2\pi)^{d-1}}
\qquad
\delta_{k k'} \to \frac{(2\pi)^{d-1}}{V} \delta(\mathbf{p} - \mathbf{p}')
$$

The frequency takes the limit

$$
\begin{align*}
    \omega_\mathbf{p}
    &= m^2 + \frac{2}{a^2} (1 - \cos \mathbf{p} a)
    \\
    &= m^2 + \frac{2}{a^2} \left[
        \frac{1}{2} (\mathbf{p}a)^2 + O(a^2)
    \right]
    \\
    &\sim m^2 + \mathbf{p}^2
\end{align*}
$$

The commutation relations between the ladder operators are

$$
a_\mathbf{p} = \sqrt{V} a_k \, \Rightarrow \,
[a_\mathbf{p}, a_{\mathbf{p}'}^\dagger] 
= (2\pi)^{d-1} \delta^{d-1}(\mathbf{p}-\mathbf{p}')
$$

where $d$ is the spacetime dimension. Finally, the field $\phi(x)$ can be expanded as

$$
\begin{align*}
    \phi(x) 
    &= \int \frac{d^{d-1} p}{(2\pi)^{d-1}} 
    \frac{1}{\sqrt{2 \omega_\mathbf{p}}} [
        a_\mathbf{p} e^{i (- \omega t + \mathbf{p}\cdot\mathbf{x})} 
        + a^\dagger_\mathbf{p} e^{i (\omega t - \mathbf{p}\cdot\mathbf{x})}
    ] \\
    &= \int \frac{d^{d-1} p}{(2\pi)^{d-1}} 
    \frac{1}{\sqrt{2 \omega_\mathbf{p}}} (
        a_\mathbf{p} e^{-ipx} 
        + a^\dagger_\mathbf{p} e^{ipx}
    )
\end{align*}
$$

where $p^0 = \omega_\mathbf{p} = \sqrt{m^2 + \mathbf{p}^2}$. 

We also obtain the expansion of the momentum $\pi(x)$:

$$
\pi(x) = \partial_t \phi(x)
= \int \frac{d^{d-1} p}{(2\pi)^{d-1}} 
\sqrt{\frac{\omega_\mathbf{p}}{2}} (
    a_\mathbf{p} e^{-ipx} 
    + a^\dagger_\mathbf{p} e^{ipx}
)
$$

## Heisenberg Equation for the Fields

$$
i \frac{\partial}{\partial t} \phi(x) = [\phi, H]
$$

## Normalization of Momentum Eigenstates

The Lorentz invariant definition of the one-particle momentum eigenstate is

$$
|\mathbf{p}\rangle 
= \sqrt{2E_\mathbf{p}} a_\mathbf{p}^\dagger |0\rangle
$$

Therefore, the orthogonality relation is

$$
\begin{align*}
    \langle \mathbf{p}|\mathbf{q} \rangle
    &= 2 \sqrt{E_\mathbf{p} E_\mathbf{q}}
    \langle 0 |a_\mathbf{p} a_\mathbf{q}^\dagger| 0\rangle
    \\
    &= 2 \sqrt{E_\mathbf{p} E_\mathbf{q}}
    \langle 0 | 
    \cancel{a_\mathbf{q}^\dagger a_\mathbf{p}}
    + [a_\mathbf{p}, a_\mathbf{q}^\dagger] 
    |0\rangle
    \\
    &= 2 E_\mathbf{p} (2\pi)^3
    \delta^3(\mathbf{p} - \mathbf{q})
\end{align*}
$$

and the completeness relation is

$$
(1)_\text{1-particle}
= \int \frac{d^3p}{(2\pi)^3} \frac{1}{2E_\mathbf{p}}
|\mathbf{p}\rangle \langle \mathbf{p}|
$$

## Action of the $\phi(\mathbf{x})$ Operator

Let us calculate the action of the field operator $\phi(\mathbf{x})$ on the vacuum $|0\rangle$:

$$
\phi(\mathbf{x}) | 0 \rangle
= e^{-i \mathbf{p}\cdot \mathbf{x}}
$$

Thus **$\phi(\mathbf{x})$ creates a particle at position $\mathbf{x}$**