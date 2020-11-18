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

The new correlation is

$$
\begin{aligned}
    \left\langle X'\right\rangle 
    &= \frac{1}{Z} \int \left[d\phi' \right] 
    X'\exp\left(-S'\left[\phi' \right]\right)
    \\
    &= \frac{1}{Z} \int [d\phi] \,
    X'\exp\left(-S'\left[\phi
    '\right]\right)
    \\
    &= \frac{1}{Z} \int [d\phi]
    (X+\delta  X)
    \exp\left(
        -S[\phi]-\int d^dx \,
        \omega_a(x)\partial_{\mu}j_a^{\mu} 
    \right)
    \\
    &\simeq \frac{1}{Z} \int [d\phi](X+\delta  X)
    \exp(-S[\phi]) \left(
        1 - \int d^dx \,
        \omega_a(x)\partial_{\mu}j_a^{\mu} 
    \right)
    \\
    &\simeq \langle X \rangle 
    + \langle \delta X \rangle 
    \\ &\qquad
    - \frac{1}{Z} \int [d\phi] \, X 
    \exp(-S[\phi]) \left(
        \int d^dx \,
        \omega_a(x)\partial_{\mu}j_a^{\mu} 
    \right)
\end{aligned}
$$

Then, because $\left\langle X'\right\rangle =\langle X\rangle$

$$
\begin{aligned}
    \langle \delta  X\rangle 
    &=\frac{1}{Z} \int [d\phi] \,
    X \exp(-S[\phi]) \left(
        \int d^dx \, \omega_a(x)\partial_{\mu}j_a^{\mu}
    \right)
    \\
    &=\frac{1}{Z} \int d^dx \,
    \omega_a(x) \int [d\phi]\, X \partial_{\mu}j_a^{\mu} \exp(-S[\phi])
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

Meanwhile, we can directly write down the $\langle \delta  X\rangle$ using the generators

$$
\begin{aligned}
    &\delta  X
    =\sum_{k=1}^n \phi \left(x_1\right) \cdots  
    \left(-i G_a\omega_a\left(x_k\right)\phi \left(x_k\right)\right) 
    \cdots \phi \left(x_n\right)
    \\
    &= -i\int d^dx \, 
    \delta^{(d)} (x - x_k)\,
    \omega_a(x)
    \sum_{k=1}^n \left[\phi \left(x_1\right) \cdots  \left(G_a\phi \left(x_k\right)\right) \cdots  \phi \left(x_n\right)\right]
\end{aligned}
$$

Now we obtain the **Ward identity**

$$
\begin{aligned}
    &\partial_{\mu} \left\langle j_a^{\mu} \phi \left(x_1\right) \cdots  \phi \left(x_n\right)\right\rangle 
    \\
    &= -i\int d^dx \sum_{k=1}^n 
    \delta^{(d)} \left(x-x_k\right)\left\langle
    \phi \left(x_1\right) \cdots 
    \left(G_a\phi \left(x_k\right)\right) 
    \cdots \phi \left(x_n\right)\right\rangle
\end{aligned}
$$

## Ward Identity for Translation