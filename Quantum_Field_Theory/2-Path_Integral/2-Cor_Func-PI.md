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
= \lim_{T \to \infty(1-i\epsilon)} \frac{
    \int [d\phi] \, \phi(x_1) \cdots \phi(x_n)
    e^{i S[\phi(x)]}
}{
    \int [d\phi] \, e^{i S[\phi(x)]}
}
$$

where $T$ appears in the action:

$$
\begin{aligned}
    S &\equiv \int_{-T}^T dx^4 \, \mathcal{L}[\phi(x)]
    \\
    &= \int_{-T}^T dx^0 \int dx^3 \, \mathcal{L}[\phi(x)]
\end{aligned}
$$

*Proof*: 

Consider time-independent $H$ for simplicity, so that the time evolution operator is simply $e^{iHt}$. In the Heisenberg picture, 

$$
\phi(t,\mathbf{x}) = e^{iHt} \phi(0, \mathbf{x}) e^{-iHt}
$$

----

