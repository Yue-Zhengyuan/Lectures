<style>
    .katex {
        font-size: 1.1em;
    }
    .remark {
        border-radius: 15px;
        padding: 20px;
        background-color: SeaGreen;
        color: White;
    }
    .result {
        border-radius: 15px;
        padding: 20px;
        background-color: DarkSlateBlue;
        color: White;
    }
</style>

# Example of Free Green's Function: <br>1D Phonon Modes

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
\begin{aligned}
    H &= \sum_{j=1}^N \pi_j \dot{\phi}_j - L
    \\
    &= \sum_{j=1}^N \left[
        \frac{1}{2m} \pi_j^2
        + \frac{1}{2} m \omega^2 (\phi_{j+1} - \phi_j)^2
    \right]
\end{aligned}
$$

## Fourier Expansion

Since the system has translational symmetry, i.e. the Hamiltonian is invariant under

$$
\phi_j \to \phi_{j+1}, \quad
\pi_j \to \pi_{j+1}
$$

we can write $\phi_j, \pi_j$ as Fourier series ($a$ is the separation of the atoms when in equilibrium):

$$
\begin{aligned}
    \phi_j &= \frac{1}{\sqrt{N}} 
    \sum_q e^{iq R_j} \phi_q
    \\
    \pi_j &= \frac{1}{\sqrt{N}} 
    \sum_q e^{iq R_j} \pi_q
\end{aligned} \qquad
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
\begin{aligned}
    \phi_j &= \phi_j^\dagger \\
    \pi_j &= \pi_j^\dagger
\end{aligned} \quad \Rightarrow \quad
\begin{aligned}
    \phi_q^\dagger &= \phi_{-q} \\
    \pi_q^\dagger &= \pi_{-q}
\end{aligned}
$$

The nonzero commutation rules for the Fourier modes are

$$
\begin{aligned}
    [\phi_q, \pi_{-q}]
\end{aligned}
$$

Using the orthogonality condition

$$
\sum_{j=1}^N e^{i(q + q') R_j} = N \delta_{q+q',0}
$$

we obtain the inverse transformation

$$
\begin{aligned}
    \phi_q &= \frac{1}{\sqrt{N}} 
    \sum_j e^{-iq R_j} \phi_j
    \\
    \pi_q &= \frac{1}{\sqrt{N}} 
    \sum_j e^{-iq R_j} \pi_j
\end{aligned}
$$

and the nonzero commutation rules 

$$
\begin{aligned}
    [\phi_q, \pi_{q'}]
    &= \frac{1}{N} \sum_{j,j'} 
    e^{-iq R_j} e^{-iq' R_{j'}} [\phi_j, \pi_{j'}]
    \\
    &= \frac{i}{N} \sum_j e^{-iq R_j} e^{-iq' R_j}
    \\
    &= i \delta_{q+q',0}
\end{aligned}
$$

The Hamiltonian can be expressed in terms of the Fourier modes:

- The kinetic energy term

    $$
    \begin{aligned}
        \sum_{j=1}^N \pi_j^2
        &= \frac{1}{N} \sum_{j=1}^N 
        \sum_{q,q'} e^{iq R_j} \pi_q
        e^{iq' R_j} \pi_{q'}
        \\
        &= \sum_{q,q'} \pi_q \pi_{q'} \delta_{q+q',0}
        \\
        &= \sum_q \pi_q \pi_{-q}
    \end{aligned}
    $$

- The potential energy term

    $$
    \begin{aligned}
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
    \end{aligned}
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
\begin{aligned}
    a_q &= \sqrt{\frac{m \omega_q}{2}}
    \left( \phi_q + \frac{i}{m\omega_q} \pi_q \right)
    \\
    a_q^\dagger &= \sqrt{\frac{m \omega_q}{2}}
    \left( \phi_q^\dagger - \frac{i}{m\omega_q} \pi_q^\dagger \right)
    = \sqrt{\frac{m \omega_q}{2}}
    \left( \phi_{-q} - \frac{i}{m\omega_q} \pi_{-q} \right)
\end{aligned}
$$

The nonzero commutation rules are

$$
\begin{aligned}
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
\end{aligned}
$$

We can express $H$ in terms of $a_q, a_{q'}$: first, 

$$
\begin{aligned}
    \phi_q &= \frac{1}{\sqrt{2m\omega_q}} (a_q + a_{-q}^\dagger)
    \\
    \pi_q &= -i \sqrt{\frac{m \omega_q}{2}}(a_q - a_{-q}^\dagger)
\end{aligned}
$$

It follows that (no commutation rules are used here)

$$
\begin{aligned}
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
\end{aligned}
$$

Then the Hamiltonian can be written as

$$
\begin{aligned}
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
\end{aligned}
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
    \begin{aligned}
        \frac{\partial a_q}{\partial t}
        &= i \omega_q [a_q^\dagger a_q, a_q]
        \\
        &= i \omega_q [a_q^\dagger, a_q] a_q
        \\
        &= -i \omega_q a_q
    \end{aligned} \qquad
    \begin{aligned}
        \frac{\partial a_q^\dagger}{\partial t}
        &= i \omega_q [a_q^\dagger a_q, a_q^\dagger]
        \\
        &= i \omega_q a_q^\dagger [a_q, a_q^\dagger]
        \\
        &= i \omega_q a_q^\dagger
    \end{aligned}
    $$

    Therefore

    $$
    a_q(t) = a_q e^{-i\omega_q t}, \quad
    a_q^\dagger(t) = a_q^\dagger e^{i\omega_q t}
    $$

## Phonon Green's Function

The phonon Green's function $G^0$ (in momentum space) is defined to be

$$
\begin{aligned}
    i G^0(q, t-t') 
    &\equiv \amp{0}{T[\phi_q(t) \phi_{-q}(t')]}{0}
    \\
    &= \amp{0}{\phi_q(t) \phi_{-q}(t')}{0} \theta(t - t')
    \\ &\quad
    + \amp{0}{\phi_{-q}(t') \phi_q(t)}{0} \theta(t' - t)
\end{aligned}
$$

where $\ket{0}$ is the "vacuum state" satisfying

$$
a_q \ket{0} = 0, \quad \braket{0}{0} = 1
$$

Recall that

$$
\begin{aligned}
    \phi_q(t) &= \frac{1}{\sqrt{2m\omega_q}} 
    (a_q(t) + a_{-q}^\dagger(t))
    \\
    &= \frac{1}{\sqrt{2m\omega_q}} 
    (a_q e^{-i\omega_q t} + a_{-q}^\dagger e^{i\omega_q t})
\end{aligned}
$$

Then

$$
\begin{aligned}
    &\amp{0}{\phi_q(t) \phi_{-q}(t')}{0}
    \\
    &= \frac{1}{2m\omega_q} \amp{0}{
        (a_q e^{-i\omega_q t} + a_{-q}^\dagger e^{i\omega_q t})
        (a_{-q} e^{-i\omega_q t'} + a_{q}^\dagger e^{i\omega_q t'})
    }{0}
    \\
    &= \frac{1}{2m \omega_q} \amp{0}{
        a_q e^{-i\omega_q t} a_{q}^\dagger e^{i\omega_q t'}
    }{0}
    \\
    &= \frac{1}{2m \omega_q} e^{-i\omega_q(t-t')}
    \amp{0}{[a_q,a_q^\dagger] + a_q^\dagger a_q}{0}
    \\
    &= \frac{1}{2m\omega_q} e^{-i\omega_q(t-t')}
\end{aligned}
$$

Similarly, by exchanging $-q \leftrightarrow q$ and $t \leftrightarrow t'$, we get

$$
\amp{0}{\phi_{-q}(t') \phi_{q}(t)}{0}
= \frac{1}{2m\omega_q} e^{+i\omega_q(t-t')}
$$

Therefore ($\tau \equiv t - t'$)

$$
\begin{aligned}
    iG^0(q,t-t')
    &= \frac{1}{2m\omega_q} [
        e^{-i\omega_q(t-t')} \theta(t-t')
        + e^{i\omega_q(t-t')} \theta(t'-t)
    ] \\ \Rightarrow
    iG^0(q, \tau)
    &= \frac{1}{2m\omega_q} [
        e^{-i\omega_q \tau} \theta(\tau)
        + e^{i\omega_q \tau} \theta(-\tau)
    ]
\end{aligned}
$$

To Fourier transform the time, we use the result ($\tau \equiv t - t'$)

$$
e^{-i \omega_q \tau} \theta(\tau)
= - \lim_{\epsilon \to 0+} \int_{-\infty}^{\infty} 
\frac{d\omega}{2\pi i} 
\frac{e^{-i\omega \tau}}{\omega - (\omega_q - i\epsilon)}
$$

----

*Proof*: We extend this to a contour integral by adding integration along a big semi-circle at infinity (which will give 0) of either the upper-half or lower-half plane, depending on the value of $\tau$.

- When $\tau > 0$, the semi-circle is at lower-half plane so that 
    
    $$
    e^{-i\omega \tau} \to 0 \qquad \omega \to -i\infty
    $$

    The contour will then enclose the pole $\omega_q - i\epsilon$ in clockwise direction. The residue theorem then implies

    $$
    \text{RHS} = - (-e^{- i\omega_q \tau}) = e^{i\omega_q \tau}
    \quad \tau > 0
    $$

- When $\tau < 0$, the semi-circle is at upper-half plane so that

    $$
    e^{-i\omega \tau} \to 0 \qquad \omega \to +i\infty
    $$

    The contour then encloses no pole, so

    $$
    \text{RHS} = 0 \quad \tau < 0
    \tag*{$\blacksquare$}
    $$

----

Similarly,

$$
e^{i\omega_q \tau} \theta(-\tau)
= \lim_{\epsilon \to 0+} \int_{-\infty}^{\infty} 
\frac{d\omega}{2\pi}
\frac{e^{-i\omega \tau}}{\omega - (-\omega_q + i\epsilon)}
$$

----

*Proof*: Again, we extend this to a contour integral by adding integration along a big semi-circle at infinity of either the upper-half or lower-half plane.

- When $\tau > 0$, the semi-circle is at lower-half plane. The contour will then enclose no pole. Then

    $$
    \text{RHS} = 0 \quad \tau > 0
    $$

- When $\tau < 0$, the semi-circle is at upper-half plane, enclosing the pole $-\omega_q + i\epsilon$ in counter-clockwise direction. Then

    $$
    \text{RHS} = e^{-i(-\omega_q) \tau}
    = e^{i\omega_q \tau} \quad \tau < 0
    \tag*{$\blacksquare$}
    $$

----

Then 

$$
\begin{aligned}
    iG^0(q, \tau)
    &= \frac{1}{2m\omega_q} \int_{-\infty}^{\infty} 
    \frac{d\omega}{2\pi i} \left[
        - \frac{1}{\omega - (\omega_q - i\epsilon)}
        + \frac{1}{\omega - (-\omega_q + i\epsilon)}
    \right] e^{-i\omega \tau}
    \\
    &= \frac{1}{2m\omega_q} (-2\omega_q)
    \int_{-\infty}^{\infty} \frac{d\omega}{2\pi i} 
    \frac{e^{-i\omega \tau}}{\omega^2 - \omega_q^2 + i\epsilon}
    \\
    &= \frac{i}{m} \int_{-\infty}^{\infty} 
    \frac{d\omega}{2\pi} \,
    \frac{e^{-i\omega \tau}}{\omega^2 - \omega_q^2 + i\epsilon}
\end{aligned}
$$

Here we used the common notation (since $\omega_q$ is finite)

$$
\omega^2 - \omega_q^2 + i\epsilon
\simeq \omega^2 - (\omega_q - i\epsilon)^2
\qquad (\epsilon \to 0^+)
$$

We recognize the Fourier mode as

$$
G^0(q,\omega) 
= \frac{1}{m (\omega^2 - \omega_q^2 + i\epsilon) }
$$
