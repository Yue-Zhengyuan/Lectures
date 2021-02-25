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

# Single Particle Green's Function

<div class="result">

**Single-particle Green's function (propagator):**

$$
i \hbar \, G_{\alpha \beta}(t,t')
= \amp{\Psi_0^N}{T[a_{\alpha H}(t) a^\dagger_{\beta H}(t')]}{\Psi_0^N}
$$

*Notation notes*:

- $\ket{\Psi_0^N}$: $N$-particle ground state
    
    For non-interacting systems (such as free boson), it is also denoted by $\ket{0}$.

- $a_{\alpha H}^{(\dagger)}$: Annihilation (creation) operator of state $\alpha$ in Heisenberg picture
    
    For non-interacting systems, this is the same as $a_{\alpha I}^{(\dagger)}$ in interaction picture.

- $T$: The time-ordering operator, defined as
    
    $$
    \begin{aligned}
        T[a_{\alpha H}(t) a^\dagger_{\beta H}(t')]
        &= a_{\alpha H}(t) a^\dagger_{\beta H}(t') \theta(t - t')
        \\ & \quad
        \pm a^\dagger_{\beta H}(t') a_{\alpha H}(t) \theta(t' - t)
    \end{aligned}
    $$

    with $+$ for bosons, and $-$ for fermions.

</div><br>

## Expectation Values

### One-body Operators

Construct the one-body density matrix

$$
\rho_{\alpha \beta}
\equiv \amp{\Psi_0}{c_\beta^\dagger c_\alpha}{\Psi_0}
= \pm i \lim_{t'\to t+} G_{\alpha \beta}(t,t')
\quad \left\{ \begin{aligned}
    + &: \, \text{boson} \\
    - &: \, \text{fermion}
\end{aligned} \right.
$$

Then the expectation values of the kinetic energy is

$$
\begin{aligned}
    \expect{\mathcal{T}} 
    &= \sum_{\alpha \beta} T_{\alpha \beta}
    \amp{\Psi_0}{c_\alpha^\dagger c_\beta}{\Psi_0}
    \\
    &= \pm i \lim_{t'\to t+} \sum_{\alpha \beta} T_{\alpha \beta}
    G_{\beta \alpha}(t,t')
    \\
    &= \pm i \lim_{t'\to t+} \operatorname{tr} [T G(t,t')]
\end{aligned}
$$