# Schwinger-Dyson Equation

To begin with, we consider a general interacting Lagrangian and calculate the 2-point function

$$
\begin{aligned}
    &\langle \Omega|T[\phi(x_1) \phi(x_2)] |\Omega \rangle
    \\
    &= \frac{1}{Z} \int [d\phi] \,\phi(x_1) \phi(x_2) 
    e^{i \int d^4 x \, \mathcal{L}[\phi]}
\end{aligned}
$$

where $Z$ is the "vacuum" functional

$$
Z = \int [d\phi] \exp\left(
    i \int d^4x \, \mathcal{L}[\phi]
\right)
$$

Now we make a variation of the fields, which can be regarded as a change of variables

$$
\phi(x) \to \phi'(x) = \phi(x) + \epsilon(x)
$$

A change of variable should not affect the value of the correlation function (and $Z$ itself). Besides, the change is a shift, which does not affect the integration measure. Therefore, we expect

$$
\begin{aligned}
    &\int [d\phi] \,\phi(x_1) \phi(x_2)
    e^{i \int d^4 x \, \mathcal{L}[\phi]}
    \\
    &= \int [d\phi] \,\phi'(x_1) \phi'(x_2)
    e^{i \int d^4 x \, \mathcal{L}[\phi']}
\end{aligned}
$$

Let us calculate the right-hand side up to $O(\epsilon)$ terms. For convenience, we write $\phi(x_i) = \phi_i, \, \epsilon(x_i) = \epsilon_i$:

$$
\begin{aligned}
    \text{RHS}
    &= \int [d\phi]
    (\phi_1 + \epsilon_1)
    (\phi_2 + \epsilon_2)
    e^{i \int d^4 x \, (\mathcal{L}[\phi] + \delta \mathcal{L})}
    \\
    &\simeq \int [d\phi] \left[
        \phi_1 \phi_2 
        e^{i \int d^4 x \, (\mathcal{L}[\phi] + \delta \mathcal{L})}
        + (\epsilon_1 \phi_2 + \phi_1 \epsilon_2)
        e^{i \int d^4 x \, \mathcal{L}[\phi]}
    \right]
\end{aligned}
$$

The exponential function in the first term can be expanded as

$$
\begin{aligned}
    e^{i \int d^4 x \, (\mathcal{L}[\phi] + \delta \mathcal{L})}
    &= e^{i \int d^4 x \, \mathcal{L}[\phi]}
    \times e^{i \int d^4 x \, \delta \mathcal{L}}
    \\
    &\simeq e^{i \int d^4 x \, \mathcal{L}[\phi]}
    \times \left(
        1 + i \int d^4 x \, \delta \mathcal{L}
    \right)
\end{aligned}
$$

The variation of action can be written in terms of functional derivative:

$$
\int d^4 x \, \delta \mathcal{L}
= \delta \int d^4 x \, \mathcal{L}
\simeq \epsilon(x) \frac{\delta}{\delta \phi} \left[
    \int d^4 x' \, \mathcal{L}
\right]
$$

Equating the $O(\epsilon)$ terms on both LHS and RHS, we obtain

$$
\begin{aligned}
    0 &= \int [d\phi] e^{i \int d^4 x \, \mathcal{L}[\phi]}
    \bigg[
        (\epsilon_1 \phi_2 + \phi_1 \epsilon_2)
        \\ &\qquad \quad
        + \phi_1 \phi_2 \, i \int d^4x \,
        \epsilon(x) \frac{\delta}{\delta \phi}
        \int d^4x' \mathcal{L}
    \bigg]
    \\
    &= \int [d\phi] e^{i \int d^4 x \, \mathcal{L}[\phi]}
    \bigg\{
        i \int d^4x \, \epsilon(x) \bigg[
            \delta(x-x_1) \phi_2
            \\ &\qquad
            + \phi_1 \delta(x-x_2)
            + \frac{\delta}{\delta \phi} \left(
                \int d^4x' \mathcal{L}
            \right) \phi_1 \phi_2
        \bigg]
    \bigg\}
\end{aligned}
$$

Thus we conclude that the thing in the square bracket must be zero (under time ordering):

$$
\begin{aligned}
    &\left\langle
        \left(
            \frac{\delta}{\delta \phi}
            \int d^4x' \mathcal{L}
        \right) \phi_1 \phi_2
    \right\rangle
    \\[1em] &\qquad
    = i\delta(x-x_1) \langle \phi_2 \rangle
    + i\delta(x-x_2) \langle \phi_1 \rangle
\end{aligned}
$$

The generalization to $n$-point function is straightforward (here we put the $\hbar$ back into the equation):

$$
\begin{aligned}
    &\left\langle
        \left(
            \frac{\delta}{\delta \phi}
            \int d^4x' \mathcal{L}
        \right) \phi_1 \cdots \phi_n
    \right\rangle
    \\[1em] &\qquad
    = i \hbar \sum_{j=1}^n \delta(x-x_j) 
    \langle \phi_1 \cdots \cancel{\phi_j}
    \cdots \phi_n \rangle
\end{aligned}
$$

This is called the **Dyson-Schwinger equation**. 

## Special Cases

For the interacting theory based on real scalar fields

$$
\mathcal{L} = \mathcal{L}_0 + \mathcal{L}_\text{int}[\phi], 
\quad
\mathcal{L}_0 = \frac{1}{2}[(\partial \phi)^2 - m^2 \phi^2]
$$

Its equation of motion is

$$
- (\partial^2 + m^2)\phi 
+ \frac{\delta \mathcal{L}_\text{int}[\phi]}{\delta \phi}
= 0
$$


The Schwinger-Dyson equation then states that

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
