# Schwinger-Dyson Equation

To begin with, we consider a general interacting Lagrangian and calculate the 2-point function

$$
\begin{align*}
    &\langle \Omega|T[\phi(x_1) \phi(x_2)] |\Omega \rangle
    \\
    &= \frac{1}{Z} \int [d\phi] \,\phi(x_1) \phi(x_2) 
    e^{i \int d^4 x \, \mathcal{L}[\phi]}
\end{align*}
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

A change of variable should not affect the value of the correlation function (and $Z$ itself). Besides, the change is a shift, which should not affect the integration measure. Therefore, we expect

$$
\begin{align*}
    &\int [d\phi] \,\phi(x_1) \phi(x_2)
    e^{i \int d^4 x \, \mathcal{L}[\phi]}
    \\
    &= \int [d\phi] \,\phi'(x_1) \phi'(x_2)
    e^{i \int d^4 x \, \mathcal{L}[\phi']}
\end{align*}
$$

Let us calculate the right-hand side (new correlation function) up to $O(\epsilon)$ terms. For convenience, we write $\phi(x_i) = \phi_i, \, \epsilon(x_i) = \epsilon_i$:

$$
\begin{align*}
    \text{RHS}
    &= \int [d\phi]
    (\phi_1 + \epsilon_1)
    (\phi_2 + \epsilon_2)
    e^{i \int d^4 x \, \mathcal{L}[\phi'(x)]}
    \\
    &\simeq \int [d\phi] \left[
        (\epsilon_1 \phi_2 + \phi_1 \epsilon_2)
        e^{i \int d^4 x \, \mathcal{L}[\phi(x)]}
        + \phi_1 \phi_2 
        e^{i \int d^4 x \, \mathcal{L}[\phi'(x)]}
    \right]
\end{align*}
$$

The exponential function in the last term can be expanded to $O(\epsilon)$ as

$$
\begin{align*}
    e^{i \int d^4 y \, \mathcal{L}[\phi'(y)]}
    &= e^{i \int d^4 y \, \mathcal{L}[\phi(y)]}
    + \int d^4x \, \epsilon(x)
    \frac{\delta}{\delta \phi(x)}
    e^{i \int d^4 y \, \mathcal{L}[\phi(y)]}
    \\
    &= e^{i \int d^4 y \, \mathcal{L}[\phi(y)]}
    + \int d^4x \, i \epsilon(x) 
    \frac{\delta}{\delta \phi(x)}
    \int d^4 y \, \mathcal{L}[\phi(y)]
\end{align*}
$$

We note that this functional derivative is exactly the one that produces the equation of motion:

$$
\begin{align*}
    \frac{\delta S}{\delta \phi(x)}
    &= \frac{\delta}{\delta \phi(x)}
    \int d^4 y \, \mathcal{L}[\phi(y)]
\end{align*}
$$

Equating the $O(\epsilon)$ terms of both the new and the old correlation functions, we obtain

$$
\begin{align*}
    0 &= \int [d\phi] e^{i \int d^4 x \, \mathcal{L}[\phi]}
    \bigg[
        (\epsilon_1 \phi_2 + \phi_1 \epsilon_2)
        \\ &\qquad \quad
        + i \phi_1 \phi_2 \int d^4x \,
        \epsilon(x) \frac{\delta}{\delta \phi(x)}
        \int d^4y \, \mathcal{L[\phi(y)]}
    \bigg]
    \\
    &= \int [d\phi] e^{i \int d^4 x \, \mathcal{L}[\phi]}
    \bigg\{
        \int d^4x \, \epsilon(x) \bigg[
            \delta(x-x_1) \phi_2
            \\ &\qquad
            + \phi_1 \delta(x-x_2)
            + i \phi_1 \phi_2
            \frac{\delta}{\delta \phi(x)} 
            \int d^4y \, \mathcal{L[\phi(y)]}
        \bigg]
    \bigg\}
\end{align*}
$$

Thus we conclude that the thing in the square bracket must be zero (under time ordering):

$$
\begin{align*}
    &\left\langle
        \left(
            \frac{\delta}{\delta \phi(x)}
            \int d^4y \, \mathcal{L[\phi(y)]}
        \right) \phi_1 \phi_2
    \right\rangle
    \\[1em] &\qquad
    = i\delta(x-x_1) \langle \phi_2 \rangle
    + i\delta(x-x_2) \langle \phi_1 \rangle
\end{align*}
$$

The generalization to $n$-point function is straightforward (here we put the $\hbar$ back into the equation):

$$
\begin{align*}
    &\left\langle
        \left(
            \frac{\delta}{\delta \phi(x)}
            \int d^4y \, \mathcal{L[\phi(y)]}
        \right) \phi_1 \cdots \phi_n
    \right\rangle
    \\[1em] &\qquad
    = i \hbar \sum_{j=1}^n \delta(x-x_j) 
    \langle \phi_1 \cdots \cancel{\phi_j}
    \cdots \phi_n \rangle
\end{align*}
$$

This is called the **Dyson-Schwinger equation**. 

