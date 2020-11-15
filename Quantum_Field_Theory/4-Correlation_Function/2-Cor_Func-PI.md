# Correlation Function (Path Integral)

Here we use the path integral formalism to calculate the **$n$-point correlation function**

$$
\langle \phi(x_1) \cdots \phi(x_n) \rangle
= \langle \Omega| T [\phi(x_1) \cdots \phi(x_n)] |\Omega \rangle
$$

----

*Proposition*: (**Correlation function as path integral**)

$$
\langle \phi(x_1) \cdots \phi(x_n) \rangle
= \lim_{\epsilon \to 0} \frac{
    \int [dx] \, \phi(x_1) \cdots \phi(x_n)
    \exp(i S_\epsilon[\phi(x)])
}{
    \int [dx] \, \exp(i S_\epsilon[\phi(x)])
}
$$

where $S_\epsilon[\phi(t)]$ is the action obtained by replacing $t$ by $t(1-i\epsilon)$.

*Proof*: (Consider time-independent $H$ for simplicity)

In the Heisenberg picture, 

$$
\phi(t) = e^{iHt} \phi e^{-iHt}
$$

----

## Euclidean Formalism and Statistical Physics

In statistical physics, people usually define all correlation functions in *imaginary time*, and then perform the **Wick rotation**

$$
\tau = it \in \mathbb{R}
$$

We define the **Euclidean Lagrangian** as

$$
\begin{aligned}
    L_E \left(\phi, \frac{dx}{d\tau}, \tau\right)
    &= - \left.
    L \left(\phi, \frac{dx}{dt}, t \right)
    \right|_{t \to -i\tau}
    \\
    &= - L \left(\phi, i \, \frac{dx}{d\tau}, -i\tau \right)
\end{aligned}
$$

and the **Euclidean action** as

$$
S_E[\phi(\tau)] = \int d\tau \, L_E
$$

Then the usual action $S$ is related to $S_E$ by

$$
S = \int dt \, L
= -i \int d\tau \, (-L_E) = i S_E
$$

Therefore, the imaginary time correlation function is

$$
\langle \phi(\tau_1) \cdots \phi(\tau_n) \rangle
= \frac{
    \int [dx] \, \phi(\tau_1) \cdots \phi(\tau_n)
    \exp(- S_E[\phi(\tau)])
}{
    \int [dx] \, \exp(- S_E[\phi(\tau)])
}
$$
