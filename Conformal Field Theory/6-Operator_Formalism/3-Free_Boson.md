## Example: Free Boson

Here $L$ is the circumference of the cylinder. This means that the space is *compactified* with the length $L$, and we take the periodic boundary condition:

$$
\phi(t,x+L) = \phi(t,x)
$$

### Hamiltonian

Due to the periodicity in space, we expand the field as a Fourier series:

$$
\begin{aligned}
    \phi(t,x) 
    &= \sum_n \exp \left(\frac{2\pi i n}{L}x\right)
    \phi_n(t)
    \\
    \phi_n(t) &= \frac{1}{L} 
    \int dx \exp \left(-\frac{2\pi i n}{L}x\right)
    \phi(t,x)
\end{aligned}
$$

Since the field is real, we get

$$ 
\phi_{-n}=\phi_n^\dagger
$$

Now we recast the Lagrangian using the Fourier modes (in the process of canonical quantization, we always use the Minkowski space)

$$
\begin{aligned}
    \mathcal{L}
    &=\frac{1}{2}h\int dx \left[\left(\partial_t\phi \right)^2-\left(\partial_x\phi \right)^2\right]
    \\
    &= \frac{1}{2}h\int dx \left[
        \sum_{n,m}  
        \exp \left(i\frac{2\pi  n}{L}x\right)
        \exp \left(i\frac{2\pi  m}{L}x\right)
        \dot{\phi}_n(t) \dot{\phi}_m(t)
        \right.
        \\ &\qquad
        \left.
        -\left(\frac{2\pi i}{L} \right)^2
        \sum_{n,m}  n m 
        \exp \left(i\frac{2\pi  n}{L}x\right)
        \exp \left(i\frac{2\pi  m}{L}x\right)
        \phi_n(t) \phi_m(t)
    \right]
\end{aligned}
$$

First, we integrate over $x$ and make use of the completeness relation

$$
\int_0^Ldx 
\exp \left(\frac{2\pi i}{L} (n-m)x\right)
=L \delta_{n m}
$$

Then

$$
\mathcal{L}
= \frac{1}{2} h L
\sum_n \left[
    \dot{\phi}_n \dot{\phi}_{-n}
    - \left( \frac{2\pi n}{L} \right)^2 \phi_n \phi_{-n}
\right]
$$

We can now construct the Hamiltonian: the momentum conjugate to $\phi_n$ is

$$
\pi_n
= \frac{\partial \mathcal{L}}{\partial \dot{\phi}_n}
= h L \dot{\phi}_{-n}
$$

(the sum over all $n$ contributes a factor of 2) and we impose the commutation relation $\left[\phi_n,\pi_m\right]=i \delta_{n m}$.

Because $\phi_{-n}=\phi_n^\dagger$, we have for the momentum

$$
\pi_{-n}=\pi_n^\dagger
$$

Then

$$
\begin{aligned}
    H &=\sum_n  \pi_n\dot{\phi}_n-\mathcal{L} 
    \\
    &= \sum_n  \pi_n \frac{\pi_{-n}}{h L}
    - \frac{1}{2} h L \sum_n \frac{\pi_{-n}}{h L} \frac{\pi_n}{h L}
    + \frac{1}{2} h L \sum_n  \left(\frac{2\pi  n}{L} \right)^2 \phi_n \phi_{-n} 
    \\
    &=\frac{1}{2 h L} \sum_n  \left[
        \pi_n\pi_{-n}
        + (2\pi n h)^2 \phi_n \phi_{-n} 
    \right]
\end{aligned}
$$

Now we change $n\to -n$:

$$
\begin{aligned}
    H 
    &=\frac{1}{2 h L} \sum_n \left[
        \pi_{-n} \pi_n
        + (2\pi  n h)^2\phi_{-n} \phi_n
    \right]
    \\
    &=\sum_n \left[
        \frac{1}{2h L} \pi_n^\dagger \pi_n
        + \frac{1}{2} h L \left(\frac{2\pi n}{L} \right)^2 \phi_n^\dagger \phi_n
    \right]
\end{aligned}
$$

This represents a sum of *decoupled harmonic oscillators* of frequencies

$$
\omega_n=\frac{2\pi  |n|}{L} \quad
\left(
    \text{comparing with } 
    \frac{p^2}{2m}+\frac{1}{2}m \omega^2x^2, 
    \text{with } m=h L
\right)
$$

However, *the* $n=0$ *mode vanishes*: it is a consequence of the absence of a mass term, which, with the boundary conditions chosen, is the same as conformal invariance.

### Creation and Annihilation Operators

For each mode $n$, we can define the creation and annihilation operators in a way analogous to the simple harmonic oscillator:

SHO:

$$
H=\frac{1}{2}m \omega^2x^2+\frac{1}{2m}p^2 
\Rightarrow
a=\sqrt{\frac{m \omega}{2}} \left(x+\frac{i}{m \omega}p\right)
$$

Free boson CFT:

$$
\begin{aligned}
    a_n 
    &=\sqrt{\frac{1}{2}h L \frac{2\pi  |n|}{L}} \left(\phi_n+\frac{i}{2\pi h L |n|/L} \pi_n\right)
    \\
    &=\sqrt{\pi h |n|} \left(
        \phi_n + \frac{i}{2\pi  |n| h} \pi_n
    \right)
    \\
    &=\frac{1}{\sqrt{4\pi |n| h}} (
        2\pi |n| h \phi_n+i \pi_n
    )
\end{aligned}
$$

We now have

$$
\left[a_n,a_m\right]=0, \left[a_n,a_m^\dagger \right]=\delta_{n m}
$$

But this definition does not apply to the $n=0$ mode.
