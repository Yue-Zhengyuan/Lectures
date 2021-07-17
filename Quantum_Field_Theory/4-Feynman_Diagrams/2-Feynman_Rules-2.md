# Feynman Rules from Lagrangian

*Note: In this section we restore $\hbar$ to see where quantum effect comes in.*

The position space Feynman rules can be derived via another approach, using the **Schwinger-Dyson equation**. 

Recall that for the interacting theory

$$
\mathcal{L} = \mathcal{L}_0 + \mathcal{L}_\text{int}[\phi], 
\quad
\mathcal{L}_0 = \frac{1}{2}[(\partial \phi)^2 - m^2 \phi^2]
$$

Its equation of motion is

$$
(\partial^2 + m^2)\phi 
- \frac{\partial \mathcal{L}_\text{int}[\phi]}{\partial \phi}
= 0
$$

For example, if $\mathcal{L}_\text{int}[\phi] = (\lambda/4!)\phi^4$, then

$$
\frac{\partial \mathcal{L}_\text{int}[\phi]}{\partial \phi}
= \frac{\lambda}{3!} \phi
$$

For this particular type of theory, the Schwinger-Dyson equation states that

$$
\begin{align*}
    &(\partial_x^2 + m^2) 
    \langle \phi_x \phi_1 ... \phi_n \rangle
    \\
    &= \left\langle 
        \frac{\partial \mathcal{L}_\text{int}[\phi_x]}{\partial \phi_x}
        \phi_1 ... \phi_n
    \right\rangle
    - i \hbar \sum_{j=1}^n \delta^4(x-x_j)
    \langle \phi_1 ... \cancel{\phi_j} ... \phi_n \rangle
    \\[1em]
    &\text{with} \quad
    \phi_x \equiv \phi(x), \quad
    \phi_j \equiv \phi(x_j), \quad
    \partial_x^2 = (\partial/\partial x)^2
\end{align*}
$$

## Perturbation Expansion of Correlation Functions
