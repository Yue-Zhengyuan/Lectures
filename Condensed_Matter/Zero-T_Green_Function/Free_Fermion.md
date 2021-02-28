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

# Example of Free Green's Function: <br>Free Fermion

For free fermion, the interaction picture coincides with the Heisenberg picture. We shall then omit the picture label $I$ or $H$ for the fields. The Hamiltonian is given by

$$
H = \sum_{\mathbf{k}, \alpha} \omega_\mathbf{k}
c_{\mathbf{k}\alpha}^\dagger c_{\mathbf{k} \alpha}
$$

At the ground state, the electrons fill the momentum states up to some **Fermi surface** (maximum momentum) $k_F$. Therefore, electrons can only be created with $k > k_F$, and annihilated with $k < k_F$ (this is also interpreted as the creation of **holes**). Based on this observation, we define

$$
c_{\mathbf{k}\alpha} = \begin{cases}
    a_{\mathbf{k} \alpha}, & k > k_F \quad(\text{particle}) \\
    b_{-\mathbf{k} \alpha}, & k < k_F \quad(\text{hole})
\end{cases}
$$

Note that the hole has opposite momentum to the annihilated fermion. 

## In Position / Momentum Space

The Fourier expansion of the fermion field $\phi_\alpha(\mathbf{x},t)$ ($\alpha$ is the spin index) is 

$$
\begin{aligned}
    \phi_\alpha(\mathbf{x},t)
    &= \int \frac{d^3k}{(2\pi)^3} c_{\mathbf{k}\alpha}
    e^{i(-\omega t + \mathbf{k}\cdot\mathbf{x})}
    \\
    &= \int \frac{d^3k}{(2\pi)^3} \bigg[
        a_{\mathbf{k}\alpha} 
        \theta(k - k_F)
        + b_{-\mathbf{k}\alpha}^\dagger
        \theta(k_F - k)
    \bigg] e^{i(-\omega_k t + \mathbf{k}\cdot\mathbf{x})}
\end{aligned}
$$

The particle and the hole operators inherit the following properties from $c_{\mathbf{k}\alpha}$:

$$
\begin{aligned}
    a_{\mathbf{k},\alpha} \ket{\Psi_0} &= 0 &\qquad
    \{a_{\mathbf{k}\alpha},a_{\mathbf{k}'\alpha'}\}
    &= (2\pi)^3 \delta^{3}(\mathbf{k} - \mathbf{k}')
    \delta_{\alpha \alpha'}
    \\
    b_{\mathbf{k},\alpha} \ket{\Psi_0} &= 0 &\qquad
    \{b_{\mathbf{k}\alpha},b_{\mathbf{k}'\alpha'}\}
    &= (2\pi)^3 \delta^{3}(\mathbf{k} - \mathbf{k}')
    \delta_{\alpha \alpha'}
\end{aligned}
$$

Let $\ket{\Psi_0}$ be the normalized ground state. We first calculate the common structures that occur in different kinds of Green's functions:

$$
\begin{aligned}
    A_1 &\equiv \amp{\Psi_0}{
        \phi_{\alpha}(\mathbf{x},t) 
        \phi^\dagger_{\beta}(\mathbf{x}', t')
    }{\Psi_0}
    \\
    &= \int \frac{d^3k}{(2\pi)^3} \frac{d^3k'}{(2\pi)^3}
    \Big \langle \Psi_0 \Big|
    (
        a_{\mathbf{k}\alpha} 
        \theta(k - k_F)
        + b_{-\mathbf{k}\alpha}^\dagger
        \theta(k_F - k)
    ) \\ &\qquad (
        a_{\mathbf{k}' \beta}^\dagger
        \theta(k' - k_F)
        + b_{-\mathbf{k}' \beta}
        \theta(k_F - k')
    ) \Big| \Psi_0 \Big \rangle
    e^{i(-\omega_k t + \mathbf{k}\cdot\mathbf{x})}
    e^{i(\omega_{k'} t' - \mathbf{k}'\cdot\mathbf{x}')}
    \\
    &= \int \frac{d^3k}{(2\pi)^3} \frac{d^3k'}{(2\pi)^3}
    \underbrace{
        \amp{\Psi_0}{
            a_{\mathbf{k}\alpha} 
            a_{\mathbf{k}' \beta}^\dagger
        }{\Psi_0}
    }_{
        = (2\pi)^3 \delta^{3}(\mathbf{k}-\mathbf{k}')
        \delta_{\alpha \beta}
    } \\ &\qquad \qquad \times
    \theta(k - k_F) \theta(k' - k_F)
    e^{i(-\omega_k t + \mathbf{k}\cdot\mathbf{x})}
    e^{i(\omega_{k'} t' - \mathbf{k}'\cdot\mathbf{x}')}
    \\
    &= \delta_{\alpha \beta}
    \int \frac{d^3k}{(2\pi)^3} \theta(k - k_F)
    e^{i \mathbf{k} \cdot (\mathbf{x - x'})}
    e^{-i \omega_k (t - t')} 

    \\[2em]
    
    A_2 &\equiv \amp{\Psi_0}{
        \phi^\dagger_{\beta}(\mathbf{x}', t')
        \phi_{\alpha}(\mathbf{x},t) 
    }{\Psi_0}
    \\
    &= \int \frac{d^3k'}{(2\pi)^3} \frac{d^3k}{(2\pi)^3}
    \Big \langle \Psi_0 \Big|
    (
        a_{\mathbf{k}' \beta}^\dagger
        \theta(k' - k_F)
        + b_{-\mathbf{k}' \beta}
        \theta(k_F - k')
    ) \\ &\qquad (
        a_{\mathbf{k}\alpha} 
        \theta(k - k_F)
        + b_{-\mathbf{k}\alpha}^\dagger
        \theta(k_F - k)
    ) \Big| \Psi_0 \Big \rangle
    e^{i(\omega_{k'} t' - \mathbf{k}'\cdot\mathbf{x}')}
    e^{i(-\omega_k t + \mathbf{k}\cdot\mathbf{x})}
    \\
    &= \int \frac{d^3k}{(2\pi)^3} \frac{d^3k'}{(2\pi)^3}
    \underbrace{
        \amp{\Psi_0}{
            b_{-\mathbf{k}' \beta}
            b_{-\mathbf{k}\alpha}^\dagger
        }{\Psi_0}
    }_{
        = (2\pi)^3 \delta^{3}(\mathbf{k}-\mathbf{k}')
        \delta_{\alpha \beta}
    } \\ &\qquad \qquad \times
    \theta(k_F - k') \theta(k_F - k)
    e^{i(-\omega_k t + \mathbf{k}\cdot\mathbf{x})}
    e^{i(\omega_{k'} t' - \mathbf{k}'\cdot\mathbf{x}')}
    \\
    &= \delta_{\alpha \beta}
    \int \frac{d^3k}{(2\pi)^3} \theta(k_F - k)
    e^{i \mathbf{k} \cdot (\mathbf{x - x'})}
    e^{-i \omega_k (t - t')} 
\end{aligned}
$$

These two structures contain a common factor $e^{-i \omega_k \tau} \ (\tau \equiv t - t')$. It will later be combined with $\theta(\pm \tau)$ to Fourier transform the time:

$$
\begin{aligned}
    e^{-i\omega_k \tau} \theta(\tau) 
    &= -\lim_{\epsilon \to 0+}
    \int_{-\infty}^{\infty} \frac{d\omega}{2\pi i} \,
    \frac{e^{-i\omega \tau}}{\omega - (\omega_k - i\epsilon)}
    &\qquad &\text{(1)}
    \\
    e^{-i\omega_k \tau} \theta(- \tau) 
    &= +\lim_{\epsilon \to 0+}
    \int_{-\infty}^{\infty} \frac{d\omega}{2\pi i} \,
    \frac{e^{-i\omega \tau}}{\omega - (\omega_k + i\epsilon)}
    &\qquad &\text{(2)}
\end{aligned}
$$

----

*Proof*: Use the contour integral trick.

- $\theta(\tau)$ means that semi-circle in the lower-half plane corresponds to nonzero integral. It encloses the pole $\omega_k - i\epsilon$ in clockwise direction. Then
    
    $$
    \text{RHS (1)} = -(-e^{-i\omega_k\tau}) = e^{-i\omega_k\tau}
    \qquad \tau > 0
    $$

- $\theta(\tau)$ means that semi-circle in the upper-half plane corresponds to nonzero integral. It encloses the pole $\omega_k + i\epsilon$ in counter-clockwise direction. Then
    
    $$
    \text{RHS (1)} = e^{-i\omega_k\tau}
    \qquad \tau < 0
    $$

----

### Time-Ordered Green's Function

$$
\begin{aligned}
    &iG^0_{\alpha \beta}(\mathbf{x},t;\mathbf{x}',t')
    \equiv \amp{\Psi_0}{
        T[\phi_{\alpha}(\mathbf{x},t) 
        \phi^\dagger_{\beta}(\mathbf{x}', t')]
    }{\Psi_0}
    \\
    &= A_1 \theta(t - t') - A_2 \theta(t' - t)
    \\
    &= \delta_{\alpha \beta} \int \frac{d^3k}{(2\pi)^3} 
    e^{i \mathbf{k} \cdot (\mathbf{x - x'})}
    \\ &\quad \times \Big[
        \theta(k - k_F)
        e^{-i \omega_k (t - t')} \theta(t - t')
        - \theta(k_F - k)
        e^{-i \omega_k (t - t')} \theta(t' - t)
    \Big]
    \\
    &= \delta_{\alpha \beta} \int \frac{d^3k}{(2\pi)^3} 
    e^{i \mathbf{k} \cdot (\mathbf{x - x'})}
    \\ &\qquad \times
    \int \frac{d\omega}{2\pi i}
    \left[
        - \frac{\theta(k - k_F)}
        {\omega - (\omega_k - i\epsilon)}
        - \frac{\theta(k_F - k)}
        {\omega - (\omega_k + i\epsilon)}
    \right] e^{-i\omega (t-t')}
    \\
    &= i \delta_{\alpha \beta} 
    \int \frac{d^3k}{(2\pi)^3} \frac{d\omega}{2\pi}
    e^{i \mathbf{k} \cdot (\mathbf{x - x'})}
    e^{-i\omega (t-t')} 
    \\ &\qquad \qquad \qquad \times
    \left[
        \frac{\theta(k - k_F)}
        {\omega - (\omega_k - i\epsilon)}
        + \frac{\theta(k_F - k)}
        {\omega - (\omega_k + i\epsilon)}
    \right]
\end{aligned}
$$

Then the Fourier component of the Green's function is

$$
G^R_{\alpha \beta}(\mathbf{k},\omega) 
= \delta_{\alpha \beta} \left[
    \frac{\theta(k - k_F)}
    {\omega - (\omega_k - i\epsilon)}
    + \frac{\theta(k_F - k)}
    {\omega - (\omega_k + i\epsilon)}
\right]
$$


### Retarded Green's Function

$$
\begin{aligned}
    &iG^R_{\alpha \beta}(\mathbf{x},t;\mathbf{x}',t')
    \equiv \amp{\Psi_0}{
        \{\phi_{\alpha}(\mathbf{x},t) 
        \phi^\dagger_{\beta}(\mathbf{x}', t')\}
    }{\Psi_0} \theta(t - t')
    \\
    &= (A_1 + A_2) \theta(t - t')
    \\
    &= \delta_{\alpha \beta} \int \frac{d^3k}{(2\pi)^3} 
    e^{i \mathbf{k} \cdot (\mathbf{x - x'})}
    \\ &\quad \times \Big[
        \theta(k - k_F)
        e^{-i \omega_k (t - t')} \theta(t - t')
        + \theta(k_F - k)
        e^{-i \omega_k (t - t')} \theta(t - t')
    \Big]
    \\
    &= \delta_{\alpha \beta} \int \frac{d^3k}{(2\pi)^3} 
    e^{i \mathbf{k} \cdot (\mathbf{x - x'})}
    \\ &\qquad \times
    \int \frac{d\omega}{2\pi i}
    \left[
        - \frac{\theta(k - k_F) + \theta(k_F - k)}
        {\omega - (\omega_k - i\epsilon)}
    \right] e^{-i\omega (t-t')}
    \\
    &= i \delta_{\alpha \beta} 
    \int \frac{d^3k}{(2\pi)^3} \frac{d\omega}{2\pi}
    e^{i \mathbf{k} \cdot (\mathbf{x - x'})}
    e^{-i\omega (t-t')} 
    \frac{1}{\omega - (\omega_k - i\epsilon)}
\end{aligned}
$$

In the last step the following relation is used:

$$
\theta(k - k_F) + \theta(k_F - k) = 1
$$

Then the Fourier component of the Green's function is

$$
G^R_{\alpha \beta}(\mathbf{k},\omega) 
= \frac{\delta_{\alpha \beta}}{\omega - (\omega_k - i\epsilon)}
$$

### Advanced Green's Function

$$
\begin{aligned}
    &iG^A_{\alpha \beta}(\mathbf{x},t;\mathbf{x}',t')
    \equiv - \amp{\Psi_0}{
        \{\phi_{\alpha}(\mathbf{x},t) 
        \phi^\dagger_{\beta}(\mathbf{x}', t')\}
    }{\Psi_0} \theta(t' - t)
    \\
    &= -(A_1 + A_2) \theta(t' - t)
    \\
    &= - \delta_{\alpha \beta} \int \frac{d^3k}{(2\pi)^3} 
    e^{i \mathbf{k} \cdot (\mathbf{x - x'})}
    \\ &\quad \times \Big[
        \theta(k - k_F)
        e^{-i \omega_k (t - t')} \theta(t' - t)
        + \theta(k_F - k)
        e^{-i \omega_k (t - t')} \theta(t' - t)
    \Big]
    \\
    &= -\delta_{\alpha \beta} \int \frac{d^3k}{(2\pi)^3} 
    e^{i \mathbf{k} \cdot (\mathbf{x - x'})}
    \\ &\qquad \times
    \int \frac{d\omega}{2\pi i}
    \left[
        \frac{\theta(k - k_F) + \theta(k_F - k)}
        {\omega - (\omega_k + i\epsilon)}
    \right] e^{-i\omega (t-t')}
    \\
    &= i \delta_{\alpha \beta} 
    \int \frac{d^3k}{(2\pi)^3} \frac{d\omega}{2\pi}
    e^{i \mathbf{k} \cdot (\mathbf{x - x'})}
    e^{-i\omega (t-t')} 
    \frac{1}{\omega - (\omega_k + i\epsilon)}
\end{aligned}
$$

Then the Fourier component of the Green's function is

$$
G^A_{\alpha \beta}(\mathbf{k},\omega) 
= \frac{\delta_{\alpha \beta}}{\omega - (\omega_k + i\epsilon)}
$$
