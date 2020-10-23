# Feynman Propagator

For the *free* field

$$
\phi(x) = \int \frac{d^3 k}{(2\pi)^3}
\frac{1}{\sqrt{2\omega_k}}
(a_k e^{-ikx} + a_k^\dagger e^{ikx})
$$

where $\omega_k = \sqrt{m^2 + \boldsymbol{k}^2}$, the time-ordered amplitude

$$
\begin{aligned}
    D_F(x_1, x_2)
    &= \langle 0 | T[\phi(x_1) \phi(x_2)] |0 \rangle
    \\
    &= \int \frac{d^4 k}{(2\pi)^4}
    \frac{
        i e^{i k(x_1  - x_2)}
    }{
        k^2 - m^2 + i \epsilon
    }
\end{aligned}
$$

is called the **Feynman propagator**.