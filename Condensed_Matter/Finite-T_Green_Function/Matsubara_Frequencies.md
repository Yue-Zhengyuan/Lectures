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

The (anti-)periodicity of $\mathcal{G}$ allows up to expand it as a Fourier series:

$$
\begin{aligned}
    \mathcal{G}_{\rho \sigma}(\tau)
    &= \beta^{-1} \sum_n e^{-i\omega_n \tau} 
    \mathcal{G}_{\rho \sigma}(i\omega_n)
    \\ &\Updownarrow \\
    \mathcal{G}_{\rho \sigma}(i\omega_n)
    &= \int_0^\beta d\tau \, e^{+i\omega_n \tau} 
    \mathcal{G}_{\rho \sigma}(\tau)
\end{aligned}
$$

The factor $i$ is included into the argument $\mathcal{G}_{\rho \sigma}(i\omega_n)$ for later convenience. The requirement $\mathcal{G}_{\rho \sigma}(\tau + \beta) = \pm \mathcal{G}_{\rho \sigma}(\tau)$ restricts the allowed values of $\omega_n$:

$$
e^{-i\omega_n \beta} = \pm 1 
\ \Rightarrow \ \omega_n = 
\left\{ \begin{aligned}
    &2n \pi \beta^{-1}, &\, &
    \text{boson} \\
    &(2n+1)\pi \beta^{-1}, &\, &
    \text{fermion}
\end{aligned}\right.
$$
