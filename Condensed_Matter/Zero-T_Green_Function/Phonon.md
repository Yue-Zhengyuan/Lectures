# Example of Free Green's Function: <br>1D Phonon Modes

Recall that Hamiltonian of 1D phonon modes is

$$
H = \frac{1}{2m} \pi_0^2 + \sum_{q \ne 0} 
\omega_q \left(
    a_q^\dagger a_q
    + \frac{1}{2}
\right), \quad
\omega_q \equiv 2\omega \left|\sin \frac{qa}{2}\right|
$$

with the nonzero commutation rules

$$
[a_q, a^\dagger_{q'}] = \delta_{q q'}
$$

The phonon Green's function $G$ (in momentum space) is (recall that $\phi_q^\dagger = \phi_{-q}$ due to reality condition)

$$
\begin{align*}
    i G(q, t-t') 
    &\equiv \amp{0}{T[\phi_q(t) \phi_q^\dagger(t')]}{0}
    \\
    &= \amp{0}{\phi_q(t) \phi_{-q}(t')}{0} \theta(t - t')
    \\ &\quad
    + \amp{0}{\phi_{-q}(t') \phi_q(t)}{0} \theta(t' - t)
\end{align*}
$$

Recall that

$$
\begin{align*}
    \phi_q(t) &= \frac{1}{\sqrt{2m\omega_q}} 
    (a_q(t) + a_{-q}^\dagger(t))
    \\
    &= \frac{1}{\sqrt{2m\omega_q}} 
    (a_q e^{-i\omega_q t} + a_{-q}^\dagger e^{i\omega_q t})
\end{align*}
$$

Then

$$
\begin{align*}
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
\end{align*}
$$

Similarly, by exchanging $-q \leftrightarrow q$ and $t \leftrightarrow t'$, we get

$$
\amp{0}{\phi_{-q}(t') \phi_{q}(t)}{0}
= \frac{1}{2m\omega_q} e^{+i\omega_q(t-t')}
$$

Therefore

$$
\begin{align*}
    iG(q,t-t')
    &= \frac{1}{2m\omega_q} [
        e^{-i\omega_q(t-t')} \theta(t-t')
        + e^{i\omega_q(t-t')} \theta(t'-t)
    ] \\ \Rightarrow
    iG(q, t)
    &= \frac{1}{2m\omega_q} [
        e^{-i\omega_q t} \theta(t)
        + e^{i\omega_q t} \theta(-t)
    ]
\end{align*}
$$

## Energy Formulation

Now we Fourier transform the time to obtain Green's function in energy (or frequency) formulation using the result (set $t - t' \to t$)

$$
e^{-i \omega_q t} \theta(t)
= - \lim_{\epsilon \to 0+} \int_{-\infty}^{\infty} 
\frac{d\omega}{2\pi i} 
\frac{e^{-i\omega t}}{\omega - (\omega_q - i\epsilon)}
$$

----

*Proof*: We extend this to a contour integral by adding integration along a big semi-circle at infinity (which will give 0) of either the upper-half or lower-half plane, depending on the value of $t$.

- When $t > 0$, the semi-circle is at lower-half plane so that 
    
    $$
    e^{-i\omega t} \to 0 \qquad \omega \to -i\infty
    $$

    The contour will then enclose the pole $\omega_q - i\epsilon$ in clockwise direction. The residue theorem then implies

    $$
    \text{RHS} = - (-e^{- i\omega_q t}) = e^{i\omega_q t}
    \quad t > 0
    $$

- When $t < 0$, the semi-circle is at upper-half plane so that

    $$
    e^{-i\omega t} \to 0 \qquad \omega \to +i\infty
    $$

    The contour then encloses no pole, so

    $$
    \text{RHS} = 0 \quad t < 0
    \tag*{$\blacksquare$}
    $$

----

Similarly,

$$
e^{i\omega_q t} \theta(-t)
= \lim_{\epsilon \to 0+} \int_{-\infty}^{\infty} 
\frac{d\omega}{2\pi}
\frac{e^{-i\omega t}}{\omega - (-\omega_q + i\epsilon)}
$$

----

*Proof*: Again, we extend this to a contour integral by adding integration along a big semi-circle at infinity of either the upper-half or lower-half plane.

- When $t > 0$, the semi-circle is at lower-half plane. The contour will then enclose no pole. Then

    $$
    \text{RHS} = 0 \quad t > 0
    $$

- When $t < 0$, the semi-circle is at upper-half plane, enclosing the pole $-\omega_q + i\epsilon$ in counter-clockwise direction. Then

    $$
    \text{RHS} = e^{-i(-\omega_q) t}
    = e^{i\omega_q t} \quad t < 0
    \tag*{$\blacksquare$}
    $$

----

Then 

$$
\begin{align*}
    iG(q, t)
    &= \frac{1}{2m\omega_q} \int_{-\infty}^{\infty} 
    \frac{d\omega}{2\pi i} \left[
        - \frac{1}{\omega - (\omega_q - i\epsilon)}
        + \frac{1}{\omega - (-\omega_q + i\epsilon)}
    \right] e^{-i\omega t}
    \\
    &= \frac{1}{2m\omega_q} (-2\omega_q)
    \int_{-\infty}^{\infty} \frac{d\omega}{2\pi i} 
    \frac{e^{-i\omega t}}{\omega^2 - \omega_q^2 + i\epsilon}
    \\
    &= \frac{i}{m} \int_{-\infty}^{\infty} 
    \frac{d\omega}{2\pi} \,
    \frac{e^{-i\omega t}}{\omega^2 - \omega_q^2 + i\epsilon}
\end{align*}
$$

Here we used the common notation (since $\omega_q$ is finite)

$$
\omega^2 - \omega_q^2 + i\epsilon
\simeq \omega^2 - (\omega_q - i\epsilon)^2
\qquad (\epsilon \to 0^+)
$$

We recognize the Fourier mode as

$$
G(q,\omega) 
= \frac{1}{m (\omega^2 - \omega_q^2 + i\epsilon) }
$$
