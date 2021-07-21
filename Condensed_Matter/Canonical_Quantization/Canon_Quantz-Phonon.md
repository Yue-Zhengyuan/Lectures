# Canonical Quantization: <br>1D Phonon Modes

Consider a system of $N$ atoms (with mass $m$) along a one-dimensional chain, connected by springs of stiffness $m \omega^2$. The Lagrangian is 

$$
L = \sum_{j=1}^N \left[
    \frac{1}{2} m \dot{\phi}_j^2 
    - \frac{1}{2} m \omega^2 (\phi_{j+1} - \phi_j)^2
\right]
$$

where $\phi_j$ is the displacement of the $j$th atom from the equilibrium position. The periodic boundary condition $\phi_{j+N} = \phi_j$ is used. 

## Canonical Quantization

The momentum conjugate to $\phi_j$ is

$$
\pi_j = \frac{\partial L}{\partial \dot{\phi}_j}
= m \dot{\phi}_j
$$

We then impose the commutation rule

$$
[\phi_i, \pi_j] = i \delta_{i,j}
$$

The Hamiltonian is

$$
\begin{align*}
    H &= \sum_{j=1}^N \pi_j \dot{\phi}_j - L
    \\
    &= \sum_{j=1}^N \left[
        \frac{1}{2m} \pi_j^2
        + \frac{1}{2} m \omega^2 (\phi_{j+1} - \phi_j)^2
    \right]
\end{align*}
$$

## Fourier Expansion

Since the system has translational symmetry, i.e. the Hamiltonian is invariant under

$$
\phi_j \to \phi_{j+1}, \quad
\pi_j \to \pi_{j+1}
$$

we can write $\phi_j, \pi_j$ as Fourier series ($a$ is the separation of the atoms when in equilibrium):

$$
\begin{align*}
    \phi_j &= \frac{1}{\sqrt{N}} 
    \sum_q e^{iq R_j} \phi_q
    \\
    \pi_j &= \frac{1}{\sqrt{N}} 
    \sum_q e^{iq R_j} \pi_q
\end{align*} \qquad
(R_j = j a)
$$

The PBC imposes the constraint on $q$ that

$$
\phi_{j+N} = e^{iqNa} \phi_j = \phi_j
\, \Rightarrow \,
q = \frac{2\pi n}{N a}, \,
n \in \Z
$$

But we only need $q \in [-\pi/a, \pi/a]$ (in the first Brillouin zone) in the Fourier series. In addition, the reality condition on $\phi_j$ and $\pi_j$ require

$$
\begin{align*}
    \phi_j &= \phi_j^\dagger \\
    \pi_j &= \pi_j^\dagger
\end{align*} \quad \Rightarrow \quad
\begin{align*}
    \phi_q^\dagger &= \phi_{-q} \\
    \pi_q^\dagger &= \pi_{-q}
\end{align*}
$$

The nonzero commutation rules for the Fourier modes are

$$
\begin{align*}
    [\phi_q, \pi_{-q}]
\end{align*}
$$

Using the orthogonality condition

$$
\sum_{j=1}^N e^{i(q + q') R_j} = N \delta_{q+q',0}
$$

we obtain the inverse transformation

$$
\begin{align*}
    \phi_q &= \frac{1}{\sqrt{N}} 
    \sum_j e^{-iq R_j} \phi_j
    \\
    \pi_q &= \frac{1}{\sqrt{N}} 
    \sum_j e^{-iq R_j} \pi_j
\end{align*}
$$

and the nonzero commutation rules 

$$
\begin{align*}
    [\phi_q, \pi_{q'}]
    &= \frac{1}{N} \sum_{j,j'} 
    e^{-iq R_j} e^{-iq' R_{j'}} [\phi_j, \pi_{j'}]
    \\
    &= \frac{i}{N} \sum_j e^{-iq R_j} e^{-iq' R_j}
    \\
    &= i \delta_{q+q',0}
\end{align*}
$$

The Hamiltonian can be expressed in terms of the Fourier modes:

- The kinetic energy term

    $$
    \begin{align*}
        \sum_{j=1}^N \pi_j^2
        &= \frac{1}{N} \sum_{j=1}^N 
        \sum_{q,q'} e^{iq R_j} \pi_q
        e^{iq' R_j} \pi_{q'}
        \\
        &= \sum_{q,q'} \pi_q \pi_{q'} \delta_{q+q',0}
        \\
        &= \sum_q \pi_q \pi_{-q}
    \end{align*}
    $$

- The potential energy term

    $$
    \begin{align*}
        &\sum_{j=1}^N (\phi_{j+1} - \phi_j)^2
        \\
        &= \frac{1}{N} \sum_{j=1}^N 
        \sum_{q,q'} (e^{iq R_{j+1}} - e^{iq R_j}) \phi_q
        (e^{iq' R_{j+1}} - e^{iq' R_j}) \phi_{q'}
        \\
        &= \sum_{q,q'} \frac{1}{N} 
        (e^{iqa} - 1) (e^{iq'a} - 1)
        \sum_{j=1}^N e^{iq R_j} e^{iq' R_j} \phi_q \phi_{q'}
        \\
        &= \sum_{q} (e^{iqa} - 1)(e^{-iqa} - 1)
        \phi_q \phi_{-q}
        \\
        &= \sum_q 4 \sin^2(qa/2) \phi_q \phi_{-q}
    \end{align*}
    $$

Therefore, 

$$
H = \sum_q \left[
    \frac{1}{2m} \pi_q \pi_{-q}
    + \frac{1}{2} m \omega_q^2 \phi_q \phi_{-q}
\right], \quad
\omega_q \equiv 2\omega \left|\sin \frac{qa}{2}\right|
$$

which is a summation of decoupled harmonic oscillators. Note that $\omega_0 = 0$, thus we separate this "zero mode" out and write

$$
H = \frac{1}{2m} \pi_0^2
+ \sum_{q \ne 0} \left[
    \frac{1}{2m} \pi_q \pi_{-q}
    + \frac{1}{2} m \omega_q^2 \phi_q \phi_{-q}
\right]
$$

## Creation and Annihilation Operators

We then introduce the creation and annihilation operators for the $q \ne 0$ modes:

$$
\begin{align*}
    a_q &= \sqrt{\frac{m \omega_q}{2}}
    \left( \phi_q + \frac{i}{m\omega_q} \pi_q \right)
    \\
    a_q^\dagger &= \sqrt{\frac{m \omega_q}{2}}
    \left( \phi_q^\dagger - \frac{i}{m\omega_q} \pi_q^\dagger \right)
    = \sqrt{\frac{m \omega_q}{2}}
    \left( \phi_{-q} - \frac{i}{m\omega_q} \pi_{-q} \right)
\end{align*}
$$

The nonzero commutation rules are

$$
\begin{align*}
    [a_q, a_{q'}^\dagger]
    &= \frac{m \sqrt{\omega_q \omega_{q'}}}{2}
    \left[
        \phi_q + \frac{i}{m\omega_q} \pi_q,
        \phi_{-q'} - \frac{i}{m\omega_{q'}} \pi_{-q'}
    \right]
    \\
    &= \frac{m \sqrt{\omega_q \omega_{q'}}}{2}
    \left(
        -\frac{i}{m\omega_{q'}} [\phi_q, \pi_{-q'}]
        +\frac{i}{m\omega_{q}} [\pi_q, \phi_{-q'}]
    \right)
    \\
    &= \frac{\sqrt{\omega_q \omega_{q'}}}{2}
    \left(
        -\frac{i}{\omega_{q'}} i \delta_{q,q'}
        +\frac{i}{\omega_{q}} (-i \delta_{q,q'})
    \right)
    \\
    &= \delta_{q,q'}
\end{align*}
$$

We can express $H$ in terms of $a_q, a_{q'}$: first, 

$$
\begin{align*}
    \phi_q &= \frac{1}{\sqrt{2m\omega_q}} (a_q + a_{-q}^\dagger)
    \\
    \pi_q &= -i \sqrt{\frac{m \omega_q}{2}}(a_q - a_{-q}^\dagger)
\end{align*}
$$

It follows that (no commutation rules are used here)

$$
\begin{align*}
    \pi_q \pi_{-q}
    &= \frac{m \omega_q}{2} (
        a_{-q}^\dagger a_{-q}
        + a_q a_q^\dagger
        - a_{-q}^\dagger a_q^\dagger
        - a_q a_{-q}
    )
    \\[1em]
    \phi_q \phi_{-q} 
    &= \frac{1}{2m \omega_q} (
        a_{-q}^\dagger a_{-q}
        + a_q a_q^\dagger
        + a_{-q}^\dagger a_q^\dagger
        + a_q a_{-q}
    )
\end{align*}
$$

Then the Hamiltonian can be written as

$$
\begin{align*}
    H &= \frac{1}{2m} \pi_0^2 + \sum_{q \ne 0} 
    \frac{\omega_q}{4} \bigg[
        (
            a_{-q}^\dagger a_{-q}
            + a_q a_q^\dagger
            - a_{-q}^\dagger a_q^\dagger
            - a_q a_{-q}
        )
        \\ &\qquad \qquad \qquad + (
            a_{-q}^\dagger a_{-q}
            + a_q a_q^\dagger
            + a_{-q}^\dagger a_q^\dagger
            + a_q a_{-q}
        )
    \bigg]
    \\
    &= \frac{1}{2m} \pi_0^2 + \sum_{q \ne 0} 
    \frac{\omega_q}{2} (
        a_{-q}^\dagger a_{-q}
        + a_q a_q^\dagger
    )
    \\
    &= \frac{1}{2m} \pi_0^2 + \sum_{q \ne 0} 
    \frac{\omega_q}{2} (
        a_q^\dagger a_q
        + a_q a_q^\dagger
    )
    \\
    &= \frac{1}{2m} \pi_0^2 + \sum_{q \ne 0} 
    \omega_q \left(
        a_q^\dagger a_q
        + \frac{1}{2}
    \right)
\end{align*}
$$

## To the Heisenberg Picture

Let us find the time dependence of the $\pi_0, a_q, a^\dagger_q$ operators in the Heisenberg picture using the equation of motion

$$
\frac{\partial O}{\partial t} = i [H, O]
$$

- "Center-of-mass" momentum $\pi_0$

    Since $H$ does not contain $\phi_0$, obviously $[H, \pi_0] = 0$, and $\pi_0$ is a constant operator.

- Annihilation/Creation $a_q, a_q^\dagger$
    
    $$
    \begin{align*}
        \frac{\partial a_q}{\partial t}
        &= i \omega_q [a_q^\dagger a_q, a_q]
        \\
        &= i \omega_q [a_q^\dagger, a_q] a_q
        \\
        &= -i \omega_q a_q
    \end{align*} \qquad
    \begin{align*}
        \frac{\partial a_q^\dagger}{\partial t}
        &= i \omega_q [a_q^\dagger a_q, a_q^\dagger]
        \\
        &= i \omega_q a_q^\dagger [a_q, a_q^\dagger]
        \\
        &= i \omega_q a_q^\dagger
    \end{align*}
    $$

    Therefore

    $$
    a_q(t) = a_q e^{-i\omega_q t}, \quad
    a_q^\dagger(t) = a_q^\dagger e^{i\omega_q t}
    $$
