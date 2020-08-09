## Conserved Charge

The **conserved charge** associated with the current $j_a$ is defined as

$$
Q_a=\int d^{d-1}x \, j_a^0
$$

The integration is carried in the spatial part only. We verify that its time ($x^0$) derivative indeed vanishes:

$$
\frac{dQ_a}{dx^0}
= \int d^{d-1}x \, (\partial_0 j_a^0)
=-\int d^{d-1}x \, (\partial_i j_a^i)
$$

In the second equality we used $\partial_{\mu}j_a^{\mu}=0$. 

Gauss' Theorem then converts the integral to a surface integral at infinity, which gives zero provided that the current vanished sufficiently rapidly as $x\to \infty$.

### Conserved Charge as Transformation Generators

Recall the definition of the conserved charge associated with
$\omega_a$

$$
Q_a(x^0)=\int d^{d-1}x \, j_a^0
$$

Let 

$$
Y=\phi \left(x_2\right) \cdots  \phi \left(x_n\right)
$$ 

Note that it does not include the field at $x_1$, distinguishing it from the quantity $X$. 

Then we integrate both sides of the Ward identity with
respect to $x_1$, in a volume bounded by two surfaces $x_1^0=t_{\pm}$:

$$
\text{LHS}=\int_{t_-}^{t_+}dx_1^0\int d^{d-1}x_1\partial_{\mu} \left\langle j_a^{\mu} \phi \left(x_1\right)Y\right\rangle
$$

This can be converted (by Gauss' Theorem) to an integral on the two boundary surfaces :

$$
\text{LHS}=\left\langle Q_a\left(t_+\right)\phi \left(x_1\right)Y\right\rangle -\left\langle Q_a\left(t_-\right)\phi \left(x_1\right)Y\right\rangle
$$