# Schwinger-Dyson Equation

Let $|\Omega\rangle$ be the ground state of the *interacting theory* based on the Klein-Gordon theory:

$$
\mathcal{L} = \frac{1}{2} (\partial \phi)^2 
- \frac{1}{2} m^2 \phi^2
+ \mathcal{L}_\text{int}[\phi]
$$

## Lemma

$$
(\partial^2 + m^2)
$$

## Schwinger-Dyson Equation

$$
\begin{aligned}
    (\partial^2 + m^2) 
    &\langle \phi_x \phi_1 \cdots \phi_2 \rangle
    \\
    &= \left\langle 
        \frac{\delta \mathcal{L}_\text{int}}{\delta \phi}[\phi_x]
        \phi_1 \cdots \phi_n
    \right\rangle
    \\ & \qquad
    - i \hbar \sum_{j=1}^n \delta^4(x-x_j)
    \langle \phi_1 \cdots \cancel{\phi_j} \cdots \phi_n \rangle
    \\[1em]
    \text{with} \quad
    \phi_x &\equiv \phi(x), \quad
    \phi_j \equiv \phi(x_j), \quad
    \partial^2 = (\partial/\partial x)^2
\end{aligned}
$$

