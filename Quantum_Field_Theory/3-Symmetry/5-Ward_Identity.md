# Ward Identity

The **correlation function** is defined by the "mean value" of a product of the field at different places

$$
\langle 
    \phi \left(x_1\right) \cdots  \phi \left(x_n\right)
\rangle 
=\frac{1}{Z} \int [d\phi] \,
\phi(x_1) \cdots \phi(x_n)
\exp(-S[\phi])
$$

Here $Z$ is the "vacuum" functional

$$
Z=\int [d\phi] \exp(-S[\phi])
$$

If the system is symmetric under some transformation, *the correlation function at the same place should be invariant*:

$$
\langle
    \phi(x_1) \cdots \phi(x_n)
\rangle 
= \langle 
    \phi'(x_1) \cdots \phi'(x_n)
\rangle 
$$

To save writing, define $X \equiv \phi(x_1) \cdots  \phi(x_n)$. Then

$$
\langle X' \rangle =\langle X \rangle
$$

We also *assume* that the *integration measure* is invariant under the transformation:

$$
[d\phi'] = [d\phi]
$$

The new correlation is (up to first order terms)

$$
\begin{aligned}
    \left\langle X'\right\rangle 
    &= \frac{1}{Z} \int \left[d\phi' \right] 
    X' e^{-S'[\phi']}
    = \frac{1}{Z} \int [d\phi] \,
    X' e^{-S'[\phi']}
    \\
    &= \frac{1}{Z} \int [d\phi]
    (X + \delta X) e^{-S[\phi]}
    e^{-\delta S}
    \\
    &\simeq \frac{1}{Z} \int [d\phi](X + \delta X)
    e^{-S[\phi]} (1 - \delta S)
    \\
    &\simeq \langle X \rangle 
    + \langle \delta X \rangle 
    - \frac{1}{Z} \int [d\phi] \, X 
    e^{-S[\phi]} \delta S
\end{aligned}
$$

Then, because $\left\langle X'\right\rangle =\langle X\rangle$

$$
\begin{aligned}
    \langle \delta X\rangle 
    &= \frac{1}{Z} \int [d\phi] \, X 
    e^{-S[\phi]} \delta S
    \\
    &= \frac{1}{Z} \int [d\phi] \,
    X e^{-S[\phi]}
    \int d^dx \, \omega_a(x)\partial_{\mu}j_a^{\mu}
    \\
    &=\int d^dx \, \omega_a(x) \,
    \partial_{\mu} \left(
        \frac{1}{Z} \int [d\phi] \, X j_a^{\mu} \exp(-S[\phi])
    \right)
    \\
    &=\int d^dx \, \omega_a(x) \, 
    \partial_{\mu} \langle X j_a^{\mu} \rangle
\end{aligned}
$$

Meanwhile, we can directly write down $\delta X$ using the generators

$$
\begin{aligned}
    &\delta X
    =\sum_{k=1}^n \phi (x_1) \cdots  
    \left(-i G_a\omega_a(x_k)\phi (x_k)\right) 
    \cdots \phi (x_n)
    \\
    &= -i\int d^dx \, 
    \delta^{(d)} (x - x_k)\,
    \omega_a(x)
    \sum_{k=1}^n \left[\phi (x_1) \cdots  \left(G_a\phi (x_k)\right) \cdots  \phi (x_n)\right]
\end{aligned}
$$

Now we obtain the **Ward identity**

$$
\begin{aligned}
    &\partial_{\mu} \left\langle 
    j_a^{\mu} \phi (x_1) \cdots \phi (x_n)
    \right\rangle 
    \\
    &= -i \sum_{k=1}^n 
    \delta^{(d)} (x-x_k)\left\langle
    \phi (x_1) \cdots 
    \left(G_a\phi (x_k)\right) 
    \cdots \phi (x_n)\right\rangle
\end{aligned}
$$

## Ward Identity for Translation