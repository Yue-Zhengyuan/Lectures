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

## Current Operator

The (particle number) current operator consists of two parts:

$$
\mathbf{J}_\sigma(\mathbf{x})
= \mathbf{J}_\sigma^\nabla + \mathbf{J}_\sigma^A
$$

<div class="result">

**Paramagnetic and diamagnetic currents:**

$$
\begin{aligned}
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
\end{aligned}
$$

</div><br>

Here the paramagnetic current is the same as the usual probability current derived from Schrödinger equation.

## Response to External Electric Field

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
    \begin{aligned}
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
    &\simeq \mathbf{J}^0(\mathbf{x}) 
    \cdot \mathbf{A}^\text{ext}(\mathbf{x},t)
    \end{aligned}
    $$

    where we introduced

    $$
    \mathbf{J}^0(\mathbf{x}) 
    = \mathbf{J}^\nabla(\mathbf{x})
    -\frac{q}{m} \mathbf{A}^0(\mathbf{x}) 
    \rho(\mathbf{x})
    $$

Thus $V$ is simplified to

$$
V = - q \int d^3x \,
\mathbf{J}^0(\mathbf{x}) \cdot \mathbf{A}^\text{ext}(\mathbf{x},t)
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

### Going to the Frequency Domain

We Fourier transform the perturbation field

$$
A^\text{ext}(\mathbf{x},t) 
= \int \frac{d\omega}{2\pi} e^{-i\omega t}
A^\text{ext}(\mathbf{x},\omega)
$$

When the original Hamiltonian $H_0$ is time-independent, $\sigma_{\alpha \beta}$ should depends on the combination $t - t'$, which allows a further Fourier transform:

$$
\begin{aligned}
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
\end{aligned}
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

### Response at a Single Frequency

Working in the frequency domain has the advantage that the electric field is simply related to the vector potential:

$$
\begin{aligned}
    \mathbf{E}(\mathbf{x},t) 
    &= -\nabla \phi^\text{ext}(\mathbf{x},t) 
    - \partial_t \mathbf{A}^\text{ext}(\mathbf{x},t)
    \\
    &\to - \partial_t \mathbf{A}^\text{ext}(\mathbf{x},t)
    \\ &\Downarrow \\
    \mathbf{E}(\mathbf{x},\omega) 
    &= i\omega \mathbf{A}^\text{ext}(\mathbf{x},\omega) 
\end{aligned}
$$

To obtain the current under perturbation, we separate it into two parts:

$$
\mathbf{J}(\mathbf{x}, \omega)
= \mathbf{J}^0(\mathbf{x}, \omega)
- \frac{q}{m} \mathbf{A}^\text{ext}(\mathbf{x},\omega)
\rho(\mathbf{x})
$$

- For the $\mathbf{J}^0$ part, the Kubo formula can be applied, with the observation that $\expect{\mathbf{J}^0}_0 = 0$ (no current in equilibrium): 
  
    $$
    \expect{J^0_\alpha(t)} 
    = \delta\expect{J^0_\alpha(t)} 
    = \int_{-\infty}^{\infty} dt' \, 
    \chi^R_{J^0_\alpha V}(t - t')
    $$

    The response function, before Fourier transformation, is explicitly

    $$
    \begin{aligned}
        &\chi_{J^0_\alpha V}^R(t - t')
        = - i \expect{[J^0_\alpha(\mathbf{x}, t), V_I(t')]}_0 
        \theta(t - t')
        \\
        &= -q \sum_\beta \int d^3x' \,
        (-i) \expect{[
            J^0_\alpha(\mathbf{x}, t), 
            J^0_\beta(\mathbf{x}', t')
        ]}_0 \theta(t - t')
        A_\beta^\text{ext}(\mathbf{x}',t')
        \\
        &= -q \sum_\beta \int d^3x' \,
        \Pi^R_{\alpha \beta}(\mathbf{x},\mathbf{x}',t - t')
        A_\beta^\text{ext}(\mathbf{x}',t')
    \end{aligned}
    $$

    where we introduced the 

    <div class="result">
    
    **Current-current correlation function:**

    $$
    \Pi^R_{\alpha \beta}(\mathbf{x},\mathbf{x}',t - t')
    \equiv -i \expect{[
        J^0_\alpha(\mathbf{x}, t), 
        J^0_\beta(\mathbf{x}', t')
    ]}_0 \theta(t - t')
    $$

    </div><br>

    Then we can perform Fourier transform to the frequency domain

    $$
    \begin{aligned}
        \expect{J^0_\alpha(\omega)} 
        &= \int dt \, dt' \, e^{i\omega t} 
        \chi^R_{J^0_\alpha V}(t - t')
        \\
        &= -q \sum_\beta \int dt \, dt' \, d^3x'
        e^{i\omega t} 
        \Pi^R_{\alpha \beta}(\mathbf{x},\mathbf{x}',t - t')
        A_\beta^\text{ext}(\mathbf{x}',t')
        \\
        &= -q \sum_\beta \int dt \, dt' \, d^3x'
        \frac{d\omega_1}{2\pi} \frac{d\omega_2}{2\pi}
        \\ &\qquad \quad \times e^{i\omega t} 
        e^{-i\omega_1(t - t')} e^{-i\omega_2 t'}
        \Pi^R_{\alpha \beta}(\mathbf{x},\mathbf{x}', \omega_1)
        A_\beta^\text{ext}(\mathbf{x}',\omega_2)
    \end{aligned}
    $$

    Note that the integration over $t$ and $t'$ gives $(2\pi) \delta(\omega - \omega_1)$ and $(2\pi) \delta(\omega_1 - \omega_2)$, respectively. Thus we finally have

    $$
    \begin{aligned}
        \expect{J^0_\alpha(\omega)} 
        &= -q \sum_\beta \int d^3x' \,
        \Pi^R_{\alpha \beta}(\mathbf{x},\mathbf{x}', \omega)
        A_\beta^\text{ext}(\mathbf{x}',\omega)
        \\
        &= \frac{iq}{\omega} \sum_\beta \int d^3x' \,
        \Pi^R_{\alpha \beta}(\mathbf{x},\mathbf{x}', \omega)
        E_\beta(\mathbf{x}',\omega)
    \end{aligned}
    $$

- For the second part, we make the first order approximation

    $$
    \begin{aligned}
        \expect{
            - \frac{q}{m} A_\alpha^\text{ext}(\mathbf{x},\omega)
            \rho(\mathbf{x})
        } &\simeq - \frac{q}{m} 
        A_\alpha^\text{ext}(\mathbf{x},\omega)
        \expect{\rho(\mathbf{x})}_0
        \\
        &= \frac{iq}{m\omega} n(\mathbf{x})
        E_\alpha(\mathbf{x},\omega)
    \end{aligned}
    $$

    where $n(\mathbf{x}) = \expect{\rho(\mathbf{x})}_0$ is the equilibrium particle number density.

Collecting these two terms:

$$
\begin{aligned}
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
\end{aligned}
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

### Translational Invariant Systems

For systems with translational symmetry, $\sigma_{\alpha \beta}$ only depends on the combination $\mathbf{x} - \mathbf{x}'$. Then it is convenient to also Fourier transform the space:



<div class="remark">

*Remark*: For *isotropic* media, we can make further simplifications.

- $\sigma_{\alpha \beta}$ will only have diagonal elements, and they are the same;

</div><br>
