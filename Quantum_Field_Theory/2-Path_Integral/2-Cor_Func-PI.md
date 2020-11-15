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

