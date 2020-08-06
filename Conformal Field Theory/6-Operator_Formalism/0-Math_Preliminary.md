## Math Preliminary: Complex Analysis 

### Cauchy Integral Formula

For any function defined in a region on the complex plane, we have the expansion around the point $z_0$ in that region:

$$
f(z)=\sum_{n=-\infty}^{+\infty} a_n
(z - z_0)^n
$$

The $n<0$ part is called the **pricipal part**, and the normal $n\ge 0$ part is the **analytic part**.
The coefficients can be found by the **Cauchy integral formula**:

$$
a_n = \frac{1}{2\pi i}
\oint_C dz \,
\frac{f(z)}{(z - z_0)^{n+1}}
$$

valid for both positive and negative $n$. The integration path $C$ must
enclose the point $z_0$.

Compare the analytic part with the Taylor series, we find:

1. for $n\ge 0$

    $$
    f^{(n)}(z_0)
    = \frac{n!}{2\pi i}
    \oint_C dz \frac{f(z)}{(z-z_0)^n}
    $$

2. for $n=0$

    $$
    f(z_0)
    = \frac{1}{2\pi i}
    \oint_C dz \, \frac{f(z)}{z-z_0}
    $$

*Explanation of the Cauchy Integral Formula:*

Since the complex integration is *independent of the shape* of the closed path $C$, we can take $C$ to be a circle of radius $R$ around the point $z_0$. Then $C$ can be parametrized as

$$
C = \{ z \mid z_0+R e^{i \theta}, \,
\theta \in [0,2\pi) \}
$$

The complex integral is then reduced to the real integral over

$$
\oint_C dz 
= i R\int_0^{2\pi} e^{i \theta} d\theta
$$

Substituting the Laurent expansion in the RHS of the Cauchy formula:

$$
\begin{aligned}
    &\frac{1}{2 \pi i}
    \oint_C dz \frac{f(z)}{(z-z_0)^{n+1}}
    \\
    &=\frac{1}{2\pi i}
    \sum_{m=-\infty}^{\infty} 
    \oint_C dz \, a_m(z - z_0)^{m-(n+1)}
    \\
    &= \frac{1}{2 \pi i} \sum_{m=-\infty}^{\infty} i R a_m\int_0^{2\pi}d\theta  e^{i \theta} (R e^{i \theta})^{m-(n+1)}
    \\
    &= \frac{1}{2\pi} \sum_{m=-\infty}^{\infty} R^{m-n}a_m\int_0^{2\pi}d\theta  e^{i(m-n)\theta}
    \\
    &= \sum_{m=-\infty}^{\infty} R^{m-n}a_m \delta_{m n}
    = a_n
\end{aligned}
$$

### The Residue Theorem

Suppose that

$$
f(z) = \sum_{n=-m}^{+\infty} a_n (z - z_0)^n
\quad (m\in \mathbb{N})
$$

and let $C$ be a closed path enclosing $z=z_0$ but no other singular points of $f(z)$. Then the **residue theorem** states that

$$
\oint_Cdz f(z)=2 \pi i a_{-1}
$$

This is just the Cauchy Integral Formula for $n=-1$.