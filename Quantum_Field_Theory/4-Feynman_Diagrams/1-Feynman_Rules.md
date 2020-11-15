# Feynman Rules for Real Scalar Field

## Perturbation Expansion of Correlation Function

Previously, we have shown that the correlation function of an interacting scalar field theory is given by

$$
\begin{aligned}
    &\langle \Omega | T[\phi(x_1) \cdots \phi(x_n)] | \Omega\rangle
    \\
    &= \lim_{T \to \infty(1-i\epsilon)}
    \frac{
        \left\langle 0 \left| T[
            \phi_I(x_1) \cdots \phi_I(x_n) U(T, -T) 
        ]
        \right| 0 \right\rangle
    }{
        \left\langle 0 \left| 
        U(T, -T)
        \right| 0 \right\rangle
    }
    \\[1em]
    &\text{with} \quad 
    U(T, -T) = T\left[
        \exp \left(
            -i \int_{-T}^{+T} dt \, H_I(t)
        \right)
    \right]
\end{aligned}
$$

The field $\phi_I(x)$ and the interaction Hamiltonian $H_I$ are time evolved by the free part of the Hamiltonian:

$$
\begin{aligned}
    \phi_I(\mathbf{x},t) 
    &= e^{i H_0(t-t_0)} \phi(\mathbf{x},t_0) e^{-i H_0(t-t_0)}
    \\
    H_I(t) 
    &= e^{i H_0(t-t_0)} H_\text{int} e^{-i H_0(t-t_0)}
\end{aligned}
$$

In practice, the interaction Lagrangian is given as a power series expansion controlled by some parameter, such as

$$
\mathcal{L}_\text{int}[\phi]
= \frac{g}{3!} \phi^3, \quad
\frac{\lambda}{4!} \phi^4, \quad \text{etc.}
$$

Thus the exponent in the time evolution operator can also be expressed as

$$
-i \int_{-T}^{+T} dt \, H_I(t)
= i \int d^4x \, \mathcal{L}_\text{int}[\phi_I]
$$

and the exponential function can be Taylor expanded for approximations. 

### Example: $\phi^4$ Theory

$$
\mathcal{L}_\text{int}[\phi] = \frac{\lambda}{4!} \phi^4
$$

Let us first focus on the nominator: we can perform perturbation expansion on $\lambda$ as follows (from now on we omit the subscript $I$ of the interacting picture fields):

$$
\begin{aligned}
    &\left\langle 0 \left| T[
        \phi(x_1) \cdots \phi(x_n) U(T, -T) 
    ]
    \right| 0 \right\rangle
    \\
    &= \bigg\langle 0 \bigg| \,
    T \bigg[
        \phi(x_1) \cdots \phi(x_n) 
        \exp \left(
            \frac{i \lambda}{4!} \int d^4x \, \phi^4(x)
        \right)
    \bigg]
    \bigg| 0 \bigg\rangle
    \\[1em]
    &= \left\langle 0 \left| T \left[
        \phi(x_1) \cdots \phi(x_n)
    \right] \right| 0 \right\rangle
    \\[0.5em] &\quad 
    + \frac{i \lambda}{4!} \int d^4x
    \left\langle 0 \left| T \left[
        \phi(x_1) \cdots \phi(x_n) \phi^4(x)
    \right] \right| 0 \right\rangle
    \\[0.5em] &\quad 
    + \frac{1}{2!} 
    \left(\frac{i \lambda}{4!}\right)^2
    \int d^4x \int d^4y
    \left\langle 0 \left| T \left[
        \phi(x_1) \cdots \phi(x_n) 
        \phi^4(x) \phi^4(y)
    \right] \right| 0 \right\rangle
    \\[1em] &\quad
    + O(\lambda^3)
\end{aligned}
$$

For the term at each order of expansion, we can apply Wick's theorem to compute the time-ordered product. Similar expansion holds for the denominator as well. 

## Feynman Diagram for Expansion Terms
