# Spinor Representation

## The Weyl Spinor

The **Weyl Spinors** are 2-component basis objects of the $(\frac{1}{2},0)$ and $(0, \frac{1}{2})$ irreps of the Lorentz group. For these two representations, the generators $J^+, J^-$ are represented by

$$
\begin{aligned}
    \left(\frac{1}{2}, 0\right): &\quad
    J_a^+ = \frac{1}{2} \sigma_a , \quad
    J_a^- = 0
    \\[1em]
    \left(0, \frac{1}{2}\right): &\quad
    J_a^+ = 0 , \quad
    J_a^- = \frac{1}{2} \sigma_a
\end{aligned} \quad
(a = 1,2,3)
$$

Here $\sigma_a$ are the Pauli matrices. Recall that

$$
J_a^\pm = \frac{1}{2}(J_a \pm iK_a)
\, \Rightarrow \, \left\{
\begin{aligned}
    J_a &= J_a^+ + J_a^-
    \\
    K_a &= -i(J_a^+ - J_a^-)
\end{aligned} \right.
$$

Then the rotation and boost generators are

$$
\begin{aligned}
    \left(\frac{1}{2}, 0\right): &\quad
    J_a = \frac{1}{2} \sigma_a , \quad
    K_a = -\frac{i}{2} \sigma_a
    \\[1em]
    \left(0, \frac{1}{2}\right): &\quad
    J_a = \frac{1}{2} \sigma_a , \quad
    K_a = \frac{i}{2} \sigma_a
\end{aligned}
$$

The 2 spinors corresponding to these two representations are called the **left/right-handed** Weyl spinors, denoted by $\psi_L, \psi_R$. Their transformations under finite rotation $\theta_a$ and boost $\beta_a$ are

$$
\begin{aligned}
    \psi_L &\to \exp(- i \theta_a J_a - i \beta_a K_a) \psi_L
    \\ &= \exp \left(
        - \frac{i}{2} \theta_a \sigma_a 
        - \frac{1}{2} \beta_a \sigma_a
    \right) \psi_L
    \\[1em]
    \psi_R &\to \exp(- i \theta_a J_a - i \beta_a K_a) \psi_R
    \\ &= \exp \left(
        - \frac{i}{2} \theta_a \sigma_a 
        + \frac{1}{2} \beta_a \sigma_a
    \right) \psi_R    
\end{aligned}
$$

The infinitesimal versions are

$$
\begin{aligned}
    \delta \psi_L &= - \frac{1}{2} (
        i \theta_a + \beta_a 
    ) \sigma_a \psi_L
    \\[1em]
    \delta \psi_R &= - \frac{1}{2} (
        i \theta_a - \beta_a 
    ) \sigma_a \psi_R
\end{aligned}
$$

with the Hermitian conjugate

$$
\begin{aligned}
    \delta \psi_L^\dagger &= - \frac{1}{2} (
        -i \theta_a + \beta_a 
    ) \sigma_a \psi_L^\dagger
    \\[1em]
    \delta \psi_R^\dagger &= - \frac{1}{2} (
        - i \theta_a - \beta_a 
    ) \sigma_a \psi_R^\dagger
\end{aligned}
$$

## Dirac Spinor

The two spinors are sometimes packed together as the **Dirac spinor**, which is then a 4-component object :

$$
\psi \equiv \begin{bmatrix}
    \psi_L \\ \psi_R
\end{bmatrix}, \quad
\bar{\psi} \equiv \begin{bmatrix}
    \psi_L^\dagger & \psi_R^\dagger
\end{bmatrix}
$$

We can then build a (though reducible) $4 \times 4$ matrix representation of the Lorentz group: 
