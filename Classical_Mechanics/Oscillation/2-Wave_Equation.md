# Fourier Series and Wave Equation 

## Continuum Limit of 1D Chain Oscillation

Let us play a trick that we used when learning the Principle of Least
Action: taking the **continuum limit** of the lattice in Problem 1. We
fix the three quantities $L,\ c$ and $M$ defined by

$$L = Na,\ \ c = \Omega a,\ \ M = Nm$$

And introduce a two-variable function $u\left( x,\ t \right)$:

$$u\left( x_{n},\ t \right) = u_{n}\left( t \right),\ \ x_{n} = na$$

Now we take the limit
$a \rightarrow 0\ \left( N \rightarrow \infty \right)$.

1)  \* Show that the equation of motion (eq. 1) becomes

$$\frac{\partial^{2}u}{\partial x^{2}}\left( x,\ t \right) = \frac{1}{c^{2}}\frac{\partial^{2}u}{\partial t^{2}}\left( x,\ t \right)$$

This is the well-known **wave equation**. (How does it get its name?
See the following question.)

2)  Verify that the familiar sine and cosine waves

$$u\left( x,\ t \right) = \sin\left( kx - \omega t + \varphi \right)\ \text{or\ }\cos\left( kx - \omega t + \varphi \right)\text{\ \ \ \ }\left( \omega = ck,\ \ k 0 \right)$$

are solutions of the wave equation. (What is the physical meaning of
$c$?)

3)  Can you derive $\omega = ck$ directly from
    $\omega = 2\Omega\left| \sin\left( \frac{\text{ka}}{2} \right) \right|$
    by taking the $a \rightarrow 0$ limit?

**Solution:**

1)  We rewrite the discrete equation of motion using the function
    $u\left( x,\ t \right)$:

$$m\frac{\partial^{2}u\left( x_{n},\ t \right)}{\partial t^{2}} = m\Omega^{2}\left\lbrack \left( u\left( x_{n + 1},\ t \right) - u\left( x_{n},\ t \right) \right) - \left( u\left( x_{n},\ t \right) - u\left( x_{n - 1},\ t \right) \right) \right\rbrack$$

The right-hand side (RHS) should remind you of the definition of
derivatives. In fact, as $a \rightarrow 0$

$$\begin{matrix}
RHS = m\Omega^{2}a\left( \frac{u\left( x_{n} + a,\ t \right) - u\left( x_{n},\ t \right)}{a} - \frac{u\left( x_{n},\ t \right) - u\left( x_{n} - a,\ t \right)}{a} \right) \\
 = m\Omega^{2}a\left( \frac{\partial u\left( x_{n},\ t \right)}{\partial x} - \frac{\partial u\left( x_{n} - a,\ t \right)}{\partial x} \right) = m\Omega^{2}a^{2} \cdot \frac{1}{a}\left( \frac{\partial u\left( x_{n},\ t \right)}{\partial x} - \frac{\partial u\left( x_{n} - a,\ t \right)}{\partial x} \right) \\
 = mc^{2}\frac{\partial^{2}u\left( x_{n} - a,\ t \right)}{\partial x^{2}} \rightarrow mc^{2}\frac{\partial^{2}u\left( x_{n},\ t \right)}{\partial x^{2}} \\
\end{matrix}$$

Therefore

$$\frac{\partial^{2}u}{\partial x^{2}} = \frac{1}{c^{2}}\frac{\partial^{2}u}{\partial t^{2}}$$

2)  For
    $u\left( x,\ t \right) = \sin\left( kx - \omega t + \varphi \right)$,
    straightforward calculation gives

$$\frac{\partial u}{\partial x} = k\cos\left( kx - \omega t + \varphi \right),\ \ \frac{\partial^{2}u}{\partial x^{2}} = - k^{2}\sin\left( kx - \omega t + \varphi \right)$$

$$\frac{\partial u}{\partial x} = - \omega\cos\left( kx - \omega t + \varphi \right),\ \ \frac{\partial^{2}u}{\partial x^{2}} = - \omega^{2}\sin\left( kx - \omega t + \varphi \right)$$

(Don't tell me you forget the chain rule) Since $\omega = ck$, the
wave equation is of course satisfied by the sine wave. Similarly, we
can show that the cosine wave is also a solution of the wave equation.

3)  For any finite $k$, since

$$\sin x \rightarrow x\ \ \ \ \ \ \text{as}\ \ \ \ \ \ x \rightarrow 0$$

We obtain

$$\omega = 2\Omega\sin\frac{\text{ka}}{2} \rightarrow 2\Omega\frac{\text{ka}}{2} = \Omega ka = ck$$