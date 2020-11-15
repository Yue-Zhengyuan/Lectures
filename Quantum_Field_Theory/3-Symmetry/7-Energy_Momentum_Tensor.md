# Energy-Momentum Tensor

Symmetry under *spacetime translation* leads to an important conserved current: the **energy-momentum tensor**.

$$
x'^\alpha = x^\alpha + \epsilon^\alpha(x), \quad
\phi'(x') = \phi(x)
$$

The parameters $\omega_a$ are the amount of translation $\epsilon^\alpha(x)$. Then

$$
\frac{\partial x'^\nu}{\partial \epsilon^\alpha} = \delta_\alpha^\nu,
\quad
\frac{\partial F}{\partial \epsilon^\alpha} = 0
$$

We can easily verify that $f_\alpha = 0$. The current ${j^\mu}_\alpha$ corresponding to $\epsilon^\alpha$ is

$$
\begin{aligned}
    {j^\mu}_\alpha &=
    \left[
        \frac{\partial \mathcal{L}}{\partial (\partial_\mu \phi)} 
        \partial_\nu \phi
        - \delta_\nu^\mu \mathcal{L}
    \right]
    \frac{\partial x'^\nu}{\partial \epsilon^\alpha} 
    - \frac{\partial \mathcal{L}}{\partial (\partial_\mu \phi)}
    \frac{\partial F}{\partial \epsilon^\alpha}
    \\
    &= \frac{\partial \mathcal{L}}{\partial (\partial_\mu \phi)} 
        \partial_\alpha \phi
        - \delta_\nu^\alpha \mathcal{L}
\end{aligned}
$$

The $\alpha$ labels the transformation, and $\mu$ refers to the components of the current $j_\alpha$. This conserved current is called the **(canonical) energy-momentum tensor**, denoted by ${(T_c)^\mu}_\alpha$. Using superscripts only, and rename $\alpha$ to $\nu$, we obtain

$$
T_c^{\mu \nu} = -g^{\mu \nu} \mathcal{L}
+ \frac{\partial \mathcal{L}}{\partial (\partial_\mu \phi)} 
\partial^\nu \phi
$$

The corresponding conserved *charge* is the **four-momentum**

$$
P^\nu = \int d^{d-1}x \, T_c^{0 \nu}
$$

*Remark*: The energy is then given by

$$
P^0 = \int d^{d-1}x \, T_c^{0 0}
= \int d^{d-1}x \, \left[
    \frac{\partial \mathcal{L}}{\partial \dot{\phi}} 
    \partial \dot{\phi}
    - \mathcal{L}
\right]
$$

The integrand is just the usual definition of Hamiltonian (density). 

## Conservation Law for $T^{\mu \nu}$

The conservation equation $\partial_\mu j^\mu = 0$ applied to the energy-momentum tensor takes the form

$$
\partial_\mu T^{\mu \nu} = 0
$$

*Proof*: To show the conservation law, the equation of motion must be used.

$$
\begin{aligned}
    \partial_\mu T^{\mu \nu}
    &= \partial_\mu \left[
        \frac{\partial \mathcal{L}}{\partial (\partial_\mu \phi)} \partial^\nu \phi
        - g^{\mu\nu} \mathcal{L}
    \right]
    \\
    &= \underbrace{\partial_\mu \left(
        \frac{\partial \mathcal{L}}{\partial (\partial_\mu \phi)}
    \right)}_\text{apply EOM} \partial^\nu \phi
    + \frac{\partial \mathcal{L}}{\partial (\partial_\mu \phi)} \partial_\mu \partial^\nu \phi
    - \partial^\nu \mathcal{L}
    \\
    &= \frac{\partial \mathcal{L}}{\partial \phi} 
    \partial^\nu \phi
    + \frac{\partial \mathcal{L}}{\partial (\partial_\mu \phi)} \partial_\mu \partial^\nu \phi
    - \partial^\nu \mathcal{L}
\end{aligned}
$$

Notice that $\mathcal{L} = \mathcal{L}(\phi(x), \partial_\mu \phi(x))$, we can expand $\partial^\nu \mathcal{L}$ to

$$
\partial^\nu \mathcal{L}
= \frac{\partial \mathcal{L}}{\partial \phi} 
\partial^\nu \phi
+ \frac{\partial \mathcal{L}}{\partial (\partial_\mu \phi)} 
\partial^\nu \partial_\mu \phi
$$

In flat space $\partial^\nu \partial_\mu = \partial_\mu \partial^\nu$. Thus all terms cancel out and we obtain $\partial_\mu T^{\mu \nu} = 0$. $\blacksquare$

## Belinfante Energy-Momentum Tensor

Since the variation of the action under spacetime translation (even if it is non-uniform, i.e. depend on the coordinates) is

$$
\delta S = -\int d^d x \, \partial_\mu T^{\mu \nu} \epsilon_\nu(x)
$$

we have the freedom to add a term to the energy-momentum tensor:

$$
T_B^{\mu \nu} = T_c^{\mu \nu} + \partial_\rho B^{\rho \mu \nu}, \quad
B^{\rho \mu \nu} = -B^{\mu \rho \mu}
$$

The tensor $B$ is *anti-symmetric* in the first two indices. This modification does not change the divergence of $T$:

$$
\partial_\mu T_B^{\mu \nu} = \partial_\mu T_c^{\mu \nu}
$$

It is possible to choose a special $B$ so that $T_B$ will become *symmetric*. Such a tensor $B$ is called the **Belinfante (energy-momentum) tensor**. 

