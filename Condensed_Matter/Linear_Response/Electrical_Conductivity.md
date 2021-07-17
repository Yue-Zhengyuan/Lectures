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

# Electrical Conductivity

*Note: In this section $c = \hbar = 1$*

*Reference: Bruus and Flensberg, Sections 1.4.3 and 6.2*

## Setting the Stage

### Particle Current Operator

The (particle number) current operator in the existence of electromagnetic field consists of two parts:

$$
\mathbf{J}_\sigma(\mathbf{x})
= \mathbf{J}_\sigma^\nabla + \mathbf{J}_\sigma^A
$$

<div class="result">

**Paramagnetic and diamagnetic currents:**

$$
\begin{align*}
    \text{Paramagnetic:} &\ &\mathbf{J}_\sigma^\nabla
    &= \frac{1}{2mi} \left[
        \psi^\dagger_\sigma(\mathbf{x})
        (\nabla \psi_\sigma(\mathbf{x}))
        - (\nabla \psi^\dagger_\sigma(\mathbf{x}))
        \psi_\sigma(\mathbf{x})
    \right]
    \\[1em]
    \text{Diamagnetic:} &\ &\mathbf{J}_\sigma^A
    &= - \frac{q}{m} \mathbf{A}(\mathbf{x}) 
    \psi^\dagger_\sigma(\mathbf{x}) \psi_\sigma(\mathbf{x})
    = -\frac{q}{m} \mathbf{A}(\mathbf{x}) \rho(\mathbf{x})
\end{align*}
$$

</div><br>

Here the paramagnetic current is the same as the usual probability current derived from Schrödinger equation.

### Perturbation Hamiltonian

Suppose that in addition to the equilibrium electromagnetic field, we add a perturbation

$$
\phi = \phi^0 + \phi^\text{ext}, \quad
\mathbf{A} = \mathbf{A}^0 + \mathbf{A}^\text{ext}
$$

The perturbation Hamiltonian is

$$
V = q \int d^3x \, \rho(\mathbf{x}) 
\phi^\text{ext}(\mathbf{x},t)
- q \int d^3x \,
\mathbf{J}(\mathbf{x}) \cdot \mathbf{A}^\text{ext}(\mathbf{x},t)
$$

Some simplifications follow: 

- Choose the gauge 

    $$\phi^\text{ext} = 0$$

- In the second term, keep first order term only:
    
    $$
    \begin{align*}
        &\mathbf{J}(\mathbf{x}) \cdot \mathbf{A}^\text{ext}(\mathbf{x},t)
        \\
        &= \left[
        \mathbf{J}^\nabla(\mathbf{x})
        -\frac{q}{m} (
            \mathbf{A}^0(\mathbf{x}) 
            + \mathbf{A}^\text{ext}
        )  \rho(\mathbf{x})
    \right] \cdot \mathbf{A}^\text{ext}(\mathbf{x},\omega)
    \\
    &\simeq \mathbf{j}(\mathbf{x}) 
    \cdot \mathbf{A}^\text{ext}(\mathbf{x},t)
    \end{align*}
    $$

    where we introduced

    $$
    \mathbf{j}(\mathbf{x}) 
    = \mathbf{J}^\nabla(\mathbf{x})
    -\frac{q}{m} \mathbf{A}^0(\mathbf{x}) 
    \rho(\mathbf{x})
    $$

Thus $V$ is reduced to

$$
V = - q \int d^3x \,
\mathbf{j}(\mathbf{x}) \cdot \mathbf{A}^\text{ext}(\mathbf{x},t)
$$

The linear response of the *electric* current $\mathbf{J}_e = q \mathbf{J}$ to the perturbation electric field $\mathbf{E}$ is described by

<div class="result">

**Electrical conductivity tensor:**

$$
J^e_\alpha(\mathbf{x},t)
= \int dt'\, d^3x' \, \sum_\beta 
\sigma_{\alpha \beta}(\mathbf{x},t; \mathbf{x}',t')
E_\beta(\mathbf{x}',t')
$$

Here $\alpha,\beta$ are vector component labels. 

</div><br>

## In the Frequency Domain

We Fourier transform the perturbation field

$$
A^\text{ext}(\mathbf{x},t) 
= \int \frac{d\omega}{2\pi} e^{-i\omega t}
A^\text{ext}(\mathbf{x},\omega)
$$

When the original Hamiltonian $H_0$ is time-independent, $\sigma_{\alpha \beta}$ should depends on the combination $t - t'$, which allows a further Fourier transform:

$$
\begin{align*}
    &\int dt'\, d^3x' \, \sum_\beta 
    \int \frac{d\omega}{2\pi} e^{-i\omega(t - t')}
    \sigma_{\alpha \beta}(\mathbf{x},\mathbf{x}',\omega)
    \int \frac{d\omega'}{2\pi} e^{-i\omega't'} 
    E_\beta(\mathbf{x}',\omega')
    \\
    &= \int d^3x' \frac{d\omega}{2\pi}
    \frac{d\omega'}{2\pi} e^{-i\omega t}
    \delta(\omega - \omega') \sum_\beta 
    \sigma_{\alpha \beta}(\mathbf{x},\mathbf{x}',\omega)
    E_\beta(\mathbf{x}',\omega')
    \\
    &= \int d^3x' \frac{d\omega}{2\pi}
    e^{-i\omega t} \sum_\beta 
    \sigma_{\alpha \beta}(\mathbf{x},\mathbf{x}',\omega)
    E_\beta(\mathbf{x}',\omega)
\end{align*}
$$

from which we recognize the Fourier transform of the current

<div class="result">

**Electrical conductivity in frequency domain:**

$$
J^e_\alpha(\mathbf{x},\omega) 
= \int d^3x' \sum_\beta 
\sigma_{\alpha \beta}(\mathbf{x},\mathbf{x}',\omega)
E_\beta(\mathbf{x}',\omega)
$$

</div><br>


Working in the frequency domain has the advantage that the electric field is simply related to the vector potential:

$$
\begin{align*}
    \mathbf{E}(\mathbf{x},t) 
    &= -\nabla \phi^\text{ext}(\mathbf{x},t) 
    - \partial_t \mathbf{A}^\text{ext}(\mathbf{x},t)
    \\
    &\to - \partial_t \mathbf{A}^\text{ext}(\mathbf{x},t)
    \\ &\Downarrow \\
    \mathbf{E}(\mathbf{x},\omega) 
    &= i\omega \mathbf{A}^\text{ext}(\mathbf{x},\omega) 
\end{align*}
$$

To obtain the current under perturbation, we separate it into two parts:

$$
\mathbf{J}(\mathbf{x}, \omega)
= \mathbf{j}(\mathbf{x}, \omega)
- \frac{q}{m} \mathbf{A}^\text{ext}(\mathbf{x},\omega)
\rho(\mathbf{x})
$$

- For the $\mathbf{j}$ part, the Kubo formula can be applied, with the observation that $\expect{\mathbf{j}}_0 = 0$ (no current in equilibrium): 

    $$
    \begin{align*}
        \expect{j_\alpha(\omega)} 
        &= -q \sum_\beta \int d^3x' \,
        \Pi^R_{\alpha \beta}(\mathbf{x},\mathbf{x}', \omega)
        A_\beta^\text{ext}(\mathbf{x}',\omega)
        \\
        &= \frac{iq}{\omega} \sum_\beta \int d^3x' \,
        \Pi^R_{\alpha \beta}(\mathbf{x},\mathbf{x}', \omega)
        E_\beta(\mathbf{x}',\omega)
    \end{align*}
    $$

    where we introduced the 

    <div class="result">
    
    **Current-current correlation function:**

    $$
    \Pi^R_{\alpha \beta}(\mathbf{x},\mathbf{x}',t - t')
    \equiv -i \expect{[
        j_\alpha(\mathbf{x}, t), 
        j_\beta(\mathbf{x}', t')
    ]}_0 \theta(t - t')
    $$

    </div><br>

- For the second part, we make the first order approximation

    $$
    \begin{align*}
        \expect{
            - \frac{q}{m} A_\alpha^\text{ext}(\mathbf{x},\omega)
            \rho(\mathbf{x})
        } &\simeq - \frac{q}{m} 
        A_\alpha^\text{ext}(\mathbf{x},\omega)
        \expect{\rho(\mathbf{x})}_0
        \\
        &= \frac{iq}{m\omega} n(\mathbf{x})
        E_\alpha(\mathbf{x},\omega)
    \end{align*}
    $$

    where $n(\mathbf{x}) = \expect{\rho(\mathbf{x})}_0$ is the equilibrium particle number density.

Collecting these two terms:

$$
\begin{align*}
    \expect{J_\alpha(t)} 
    &= \frac{iq}{\omega} \sum_\beta \int d^3x' \,
    \Pi^R_{\alpha \beta}(\mathbf{x},\mathbf{x}', \omega)
    E_\beta(\mathbf{x}',\omega) 
    \\ & \quad
    + \frac{iq}{m\omega} n(\mathbf{x})
    E_\alpha(\mathbf{x},\omega)
    \\
    &= \int d^3x' \sum_\beta \frac{iq}{\omega} 
    \\ &\qquad \times \bigg[
        \Pi^R_{\alpha \beta}(\mathbf{x},\mathbf{x}', \omega)
        + \frac{1}{m} n(\mathbf{x}) \delta_{\alpha \beta}
        \delta^3(\mathbf{x} - \mathbf{x}')
    \bigg] E_\beta(\mathbf{x}',\omega) 
\end{align*}
$$

By comparison with the definition of $\sigma_{\alpha \beta}$, and noting that $J^e_\alpha = q J_\alpha$, we obtain

<div class="result">

**Electrical conductivity in frequency domain:**

$$
\sigma_{\alpha \beta}(\mathbf{x},\mathbf{x}',\omega)
= \frac{iq^2}{\omega} \bigg[
    \Pi^R_{\alpha \beta}(\mathbf{x},\mathbf{x}', \omega)
    + \frac{n(\mathbf{x})}{m} \delta_{\alpha \beta}
    \delta^3(\mathbf{x} - \mathbf{x}')
\bigg]
$$

</div><br>

## Translational Invariant Systems

For systems with translational symmetry, $\sigma_{\alpha \beta}$ only depends on the combination $\mathbf{x} - \mathbf{x}'$. Then it is convenient to also Fourier transform the space (setting $\mathbf{x}' = 0$):

$$
\begin{align*}
    \sigma_{\alpha \beta}(\mathbf{k},\omega)
    &= \int d^3x \, 
    e^{-i\mathbf{k}\cdot \mathbf{x}}
    \sigma_{\alpha \beta}(\mathbf{x},\omega)
    \\
    &= \int d^3x \, e^{-i\mathbf{k}\cdot \mathbf{x}}
    \frac{iq^2}{\omega} \bigg[
        \Pi^R_{\alpha \beta}(\mathbf{x}, \omega)
        + \frac{n(\mathbf{x})}{m} \delta_{\alpha \beta}
        \delta^3(\mathbf{x})
    \bigg]
    \\
    &= \frac{iq^2}{\omega} \bigg[
        \Pi^R_{\alpha \beta}(\mathbf{k}, \omega)
        + \frac{n_0}{m} \delta_{\alpha \beta}
    \bigg]
\end{align*}
$$

In the last step, we set $n_0 = n(\mathbf{x} = 0)$, and it is the uniform particle density due to translational invariance. 

Explicitly, the current-current correlation function in momentum-frequency space is

$$
\begin{align*}
    \Pi^R_{\alpha \beta}(\mathbf{k}, \omega)
    &= \int d^3x \, e^{-i\mathbf{k}\cdot \mathbf{x}}
    \Pi^R_{\alpha \beta}(\mathbf{x}, \omega)
    \\
    &=  -i \int d^3x \, e^{-i\mathbf{k}\cdot \mathbf{x}}
    \expect{[
        j_\alpha(\mathbf{x}, t), 
        j_\beta(0, t')
    ]}_0 \theta(t - t')
\end{align*}
$$

### Long-Wavelength Limit

In experiment one is interested in the $\mathbf{k} \to 0$ limit. In this limit we omit the $\mathbf{k}$ argument in the various quantities:

$$
\lim_{\mathbf{k}\to 0} \ \left\{
\begin{align*}
    \sigma_{\alpha \beta}(\mathbf{k},\omega)
    &= \sigma_{\alpha \beta}(\omega)
    \\
    \Pi_{\alpha \beta}(\mathbf{k},\omega)
    &= \Pi_{\alpha \beta}(\omega)
    \\
    & \ \ \vdots
\end{align*}
\right.
$$
