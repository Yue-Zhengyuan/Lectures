## Compactified Boson

Recall that a free boson field $\phi(z,\bar{z})$ compactified on a circle of radius $R$ is identified in the following way:

$$
\phi(z,\bar{z}) = \phi(z,\bar{z}) + 2\pi n R, \quad
n \in \mathbb{Z}
$$

i.e. $\phi$ is treated as an angular variable. 

*Remark*: We emphasize that the circle has no direct relation with the manifold described by the variables $z,\bar{z}$. The latter is the space the theory is defined on, which in our case is the Riemann sphere respectively a torus.

### Partition Function

The currents have the mode expansion

$$
\begin{aligned}
    j(z) &\equiv i \partial \phi 
    = \sum_{n \in \mathbb{Z}} j_n z^{-n-1}
    \\
    \bar{j}(\bar{z}) &\equiv i \bar{\partial} \phi 
    = \sum_{n \in \mathbb{Z}} \bar{j}_n \bar{z}^{-n-1}
\end{aligned}
$$

After integration over $z, \bar{z}$, we obtain

$$
\phi(z,\bar{z}) 
= x_0 - i (j_0 \ln z + \bar{j}_0 \ln \bar{z})
+ i \sum_{n \ne 0} \frac{1}{n} (
    j_n z^{-n} + \bar{j}_n \bar{z}^{-n}
)
$$

Now we require that the field is invariant under the $2\pi$ rotation $z \to e^{2\pi i} z$, but now up to the angular identification:

$$
\phi(e^{2\pi i} z, e^{-2\pi i} \bar{z})
= \phi(z, \bar{z}) + 2\pi n R,
\quad z \in \mathbb{Z}
$$

Using the expression of $\phi$ obtained above, we find

$$
j_0 - \bar{j}_0 = n R,
\quad z \in \mathbb{Z}
$$

Then we infer that

$$
j_0 | Q,n\rangle = Q |Q,n\rangle, \quad
\bar{j}_0 |Q, n \rangle = (Q - nR) |Q, n \rangle
$$

where $Q$ is the $j_0$ charge to be found later. 

The partition function of the compactified boson (denoted by $\text{cb.}$) is related to the free boson (denoted by $\text{fb.}$) by

$$
\begin{aligned}
    Z_{\text{cb.}} (\tau,\bar{\tau})
    &= Z_{\text{fb.}}(\tau, \bar{\tau}) 
    \sum_{Q, n} \langle Q,n | q^{j_0^2/2} \bar{q}^{\bar{j}_0^2/2} | Q,n \rangle
    \\
    &= \frac{1}{|\eta(\tau)|^2}
    \sum_{Q,n} q^{Q^2/2} \bar{q}^{(Q-nR)^2/2}
\end{aligned}
$$

The partition function should be invariant under modular transformations. We can use the *T*-transformation ($\tau \to \tau + 1$) only to determine the form of $Q$: recall that $q \equiv e^{2\pi i \tau}$, then

$$
Z_{\text{cb.}} (\tau+1, \bar{\tau}+1)
= \frac{1}{|\eta(\tau)|^2}
\sum_{Q, n} q^{Q^2/2} \bar{q}^{(Q-nR)^2/2}
e^{2\pi i n (QR - nR^2/2)}
$$

Thus we require

$$
QR - \frac{n R^2}{2} = m 
\, \Rightarrow \,
Q =  \frac{m}{R} + \frac{nR}{2},
\quad
m \in \mathbb{Z}
$$

Using this new notation, we write

$$
\begin{aligned}
    j_0 |m,n \rangle &= \left(
        \frac{m}{R} + \frac{nR}{2}
    \right) |m,n \rangle
    \\
    \bar{j}_0 |m,n \rangle &= \left(
        \frac{m}{R} - \frac{nR}{2}
    \right) |m,n \rangle
\end{aligned}
$$

and

$$
Z_{\text{cb.}}(\tau, \bar{\tau}) 
= \frac{1}{|\eta(\tau)|^2}
\sum_{m, n} q^{(m/R + nR/2)^2/2} 
\bar{q}^{(m/R - nR/2)^2/2}
$$

### Invariance of $Z_\text{cb.}$ under *S*-Transformations

To show the invariance of the partition function under the *S*-transformation ($\tau \to -1/\tau$)

$$
Z_\text{cb.} \left(
    -\frac{1}{\tau}, -\frac{1}{\bar{\tau}}
\right) = Z_{\text{cb.}}(\tau, \bar{\tau}) 
$$

we need to use the **Poisson Resummation Formula**

$$
\sum_{n \in \mathbb{Z}} \exp(-\pi a n^2 + b n)
= \frac{1}{\sqrt{a}} \sum_{k \in \mathbb{Z}}
\exp \left[
    -\frac{\pi}{a} \left(
        k + \frac{b}{2\pi i}
    \right)^2
\right]
$$

### Appendix: Proof of Poisson Resummation Formula