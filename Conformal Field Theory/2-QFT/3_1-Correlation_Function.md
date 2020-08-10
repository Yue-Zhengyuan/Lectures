## Correlation Function

For a *single* point particle, the **$n$-point correlation function** is defined as

$$
\langle x(t_1) \cdots x(t_n) \rangle
= \langle 0| \mathcal{T} (x(t_1) \cdots x(t_n)) |0 \rangle
$$

where $\mathcal{T}$ is the **time ordering operator**.

----

*Proposition*: (**Correlation function as path integral**)

$$
\langle x(t_1) \cdots x(t_n) \rangle
= \lim_{\epsilon \to 0} \frac{
    \int [dx] \, x(t_1) \cdots x(t_n)
    \exp(i S_\epsilon[x(t)])
}{
    \int [dx] \, \exp(i S_\epsilon[x(t)])
}
$$

where $S_\epsilon[x(t)]$ is the action obtained by replacing $t$ by $t(1-i\epsilon)$.

*Proof*: (Consider time-independent $H$ for simplicity)

In the Heisenberg picture, 

$$
x(t) = e^{iHt} x e^{-iHt}
$$

----

### Euclidean Formalism

In statistical physics, people usually define all correlation functions in *imaginary time*, and then perform the **Wick rotation**

$$
\tau = it \in \mathbb{R}
$$

We define the **Euclidean Lagrangian** as

$$
\begin{aligned}
    L_E \left(x, \frac{dx}{d\tau}, \tau\right)
    &= - \left.
    L \left(x, \frac{dx}{dt}, t \right)
    \right|_{t \to -i\tau}
    \\
    &= - L \left(x, i \, \frac{dx}{d\tau}, -i\tau \right)
\end{aligned}
$$

and the **Euclidean action** as

$$
S_E[x(\tau)] = \int d\tau \, L_E
$$

Then the usual action $S$ is related to $S_E$ by

$$
S = \int dt \, L
= -i \int d\tau \, (-L_E) = i S_E
$$

Therefore, the imaginary time correlation function is

$$
\langle x(\tau_1) \cdots x(\tau_n) \rangle
= \frac{
    \int [dx] \, x(\tau_1) \cdots x(\tau_n)
    \exp(- S_E[x(\tau)])
}{
    \int [dx] \, \exp(- S_E[x(\tau)])
}
$$
