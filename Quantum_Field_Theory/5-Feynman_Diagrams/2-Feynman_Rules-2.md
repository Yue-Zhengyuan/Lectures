# Feynman Rules from Lagrangian

*Note: In this section we restore $\hbar$ to see where quantum effect comes in.*

The position space Feynman rules can be derived via another approach, using the **Schwinger-Dyson equation**. 

## Schwinger-Dyson Equation

For the interacting theory

$$
\mathcal{L} = \mathcal{L}_0 + \mathcal{L}_\text{int}[\phi], 
\quad
\mathcal{L}_0 = \frac{1}{2}[(\partial \phi)^2 - m^2 \phi^2]
$$

The **Schwinger-Dyson equation** states that

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

## Perturbation Expansion of Correlation Functions
