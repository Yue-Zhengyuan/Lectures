# Matsubara Frequencies

The "energy formulation" in imaginary time leads to the **Matsubara frequencies**. 

## (Anti-)Periodicity of $\mathcal{G}$

The imaginary time Green's function has periodicity for boson, and anti-periodicity for fermion. To be specific:

<div class="result">

**(Anti-)Periodicity of imaginary time Green's function:**

$$
\mathcal{G}_{\rho \sigma}(\tau + \beta)
= \pm \mathcal{G}_{\rho \sigma}(\tau) \qquad
-\beta < \tau < 0
$$

</div><br>

----

*Proof*:

----

<div class="remark">

*Remark*: This periodicity of the function $\mathcal{G}_{\rho \sigma}$ in the range $\tau \in [-\beta,\beta]$ can in fact be extended to $(-\infty,\infty)$. But outside the original range, $\mathcal{G}_{\mu\nu}(\tau)$ is no longer defined by $\expect{c_\mu(\tau) c_\nu^\dagger(0)}$.

</div><br>

## Matsubara Frequencies

The (anti-)periodicity of $\mathcal{G}$ allows up to expand it as a Fourier series (instead of the continuous Fourier transform):

$$
\begin{align*}
    \mathcal{G}_{\rho \sigma}(\tau)
    &= \beta^{-1} \sum_n e^{-i\omega_n \tau} 
    \mathcal{G}_{\rho \sigma}(i\omega_n)
    \\ &\Updownarrow \\
    \mathcal{G}_{\rho \sigma}(i\omega_n)
    &= \int_0^\beta d\tau \, e^{+i\omega_n \tau} 
    \mathcal{G}_{\rho \sigma}(\tau)
\end{align*}
$$

The factor $i$ is included into the argument $\mathcal{G}_{\rho \sigma}(i\omega_n)$ for later convenience. The requirement $\mathcal{G}_{\rho \sigma}(\tau + \beta) = \pm \mathcal{G}_{\rho \sigma}(\tau)$ restricts the allowed values of $\omega_n$:

<div class="result">

**Matsubara frequencies:**

$$
e^{-i\omega_n \beta} = \pm 1 
\ \Rightarrow \ \omega_n = 
\left\{ \begin{align*}
    &2n \pi \beta^{-1}, &\, &
    \text{boson} \\
    &(2n+1)\pi \beta^{-1}, &\, &
    \text{fermion}
\end{align*}\right.
$$

</div><br>

Thus for bosons the Fourier series only contains *even* frequencies, and for fermions there are only *odd* ones. 

## The Summation Technique

Reference: [Wikipedia](https://en.wikipedia.org/wiki/Matsubara_frequency#Summation_formalism)

In the perturbative expansion of Green's function, one will encounter the summation over the Matsubara frequencies, i.e, evaluate the expression

$$
I \equiv \sum_{\omega_n} F(i \omega_n)
$$

Usually the function $F$ is the free boson/fermion propagator (ignoring the spin here)

$$
\mathcal{G}_\alpha(i\omega_n)
= \frac{1}
{i\omega_n - \epsilon_\alpha}
$$

The trick is to convert the summation to a contour integral

$$
\sum_{\omega_n} F(i \omega_n)
= \oint_C \frac{dz}{2\pi i} F(z) f(z)
$$

The auxiliary function $f(z)$ should have the following properties:

- It has poles at $z = i\omega_n \, (n \in \Z)$
- The residue at $z = i\omega_n$ is just equal to $F(i\omega_n)$

For boson/fermion, this function $f(z)$ can be chosen as the distribution function

$$
f(z) = \frac{1}{e^{\beta z} \mp 1}
$$

The contour $C$ is then chosen to enclose the imaginary axis, picking up the residues at all poles of $f(z)$. 