# Schwinger-Dyson Equation

*Note: In this section we restore $\hbar$ to see where quantum effect comes in.*

Let $|\Omega\rangle$ be the ground state of the *interacting theory* based on the Klein-Gordon theory:

$$
\begin{aligned}
    \text{Lagrangian:} &\quad
    \mathcal{L} = \frac{1}{2} (\partial \phi)^2 
    - \frac{1}{2} m^2 \phi^2
    + \mathcal{L}_\text{int}[\phi]
    \\[1em]
    \text{EOM:} &\quad 
    (\partial^2 + m^2)\phi 
    - \frac{\delta \mathcal{L}_\text{int}[\phi]}{\delta \phi}
    = 0
\end{aligned}
$$

## Lemma 1

$$
\begin{aligned}
    (\partial_x^2 + m^2) 
    &\langle \phi_x \phi_y \rangle
    = \langle (\partial_x^2 + m^2) \phi_x \phi_y \rangle
    - i \hbar \delta^4(x - y)
    \\[0.5em]
    \text{with} \quad
    \phi_x &\equiv \phi(x), \quad
    \phi_y \equiv \phi(y), \quad
    \partial_x^2 = (\partial/\partial x)^2
\end{aligned}
$$

*Remark*: For the free Klein-Gordon field

$$
\langle \phi_x \phi_y \rangle =  D_F(x - y), \quad
(\partial_x^2 + m^2) \phi_x = 0
$$

so we are left with

$$
(\partial_x^2 + m^2) D_F(x - y)
= - i \hbar \delta^4(x - y)
$$

agrees with the fact that $D_F$ is a Green's function of the Klein-Gordon EOM. 

## Lemma 2

$$
\begin{aligned}
    &(\partial_x^2 + m^2) 
    \langle \phi_x \phi_1 ... \phi_n \rangle
    \\
    &= \left\langle 
        (\partial_x^2 + m^2)
        \phi_1 ... \phi_n
    \right\rangle
    
    - i \hbar \sum_{j=1}^n \delta^4(x-x_j)
    \langle \phi_1 ... \cancel{\phi_j} ... \phi_n \rangle
    \\[1em]
    &\text{with} \quad
    \phi_x \equiv \phi(x), \quad
    \phi_j \equiv \phi(x_j), \quad
    \partial_x^2 = (\partial/\partial x)^2
\end{aligned}
$$

## Schwinger-Dyson Equation

$$
\begin{aligned}
    &(\partial_x^2 + m^2) 
    \langle \phi_x \phi_1 ... \phi_n \rangle
    \\
    &= \left\langle 
        \frac{\delta \mathcal{L}_\text{int}[\phi_x]}{\delta \phi_x}
        \phi_1 ... \phi_n
    \right\rangle
    
    - i \hbar \sum_{j=1}^n \delta^4(x-x_j)
    \langle \phi_1 ... \cancel{\phi_j} ... \phi_n \rangle
    \\[1em]
    &\text{with} \quad
    \phi_x \equiv \phi(x), \quad
    \phi_j \equiv \phi(x_j), \quad
    \partial_x^2 = (\partial/\partial x)^2
\end{aligned}
$$

