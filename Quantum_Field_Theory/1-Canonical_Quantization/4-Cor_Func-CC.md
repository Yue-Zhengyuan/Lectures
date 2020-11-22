# Correlation Function (Canonical Quantization)

The **$n$-point (correlation) function** is defined as

$$
\langle \phi(x_1) \cdots \phi(x_n) \rangle
= \langle \Omega| T [\phi(x_1) \cdots \phi(x_n)] |\Omega \rangle
$$

where $T$ is the **time ordering operator**, and $|\Omega\rangle$ is the ground state of the interacting theory. Its calculation is of importance because its relation to the scattering amplitude, and significance in statistical physics.  

## Two-Point Correlation Function

### Correlation Function for Free Theory

The two-point correlation function in the free (Klein-Gordon) theory is just the Feynman propagator:

$$
\begin{aligned}
    \langle 0 | T[\phi(x) \phi(y)] | 0\rangle_\text{free}
    &= D_F(x - y)
    \\
    &= \int \frac{d^4 p}{(2\pi)^4}
    \frac{i e^{i p(x-y)}}{p^2 - m^2 + i\epsilon}
\end{aligned}
$$

### The Interaction Picture of Field

To obtain the two-point function for interacting theory, we need to use the **interaction picture** of the fields. 

We separate the Hamiltonian into two parts: the free part and the interaction

$$
H = H_0 + H_\text{int}
$$

Here we assume that the (Schrödinger picture) Hamiltonian is independent of time, so that the time evolution operator is simply $e^{-iH \Delta t}$. The field $\phi(x)$ evolves with time according to (from some given time $t_0$ to $t$)

$$
\phi(\mathbf{x},t)
= e^{iH(t-t_0)} \phi(\mathbf{x},t_0) e^{-iH(t-t_0)}
$$

We expand $\phi(\mathbf{x},t_0)$ ($t_0$ is some reference time) using the ladder operators

$$
\phi(\mathbf{x},t_0)
= \int \frac{d^3p}{(2\pi)^3} \frac{1}{\sqrt{2E_\mathbf{p}}} (
    a_\mathbf{p} e^{i \mathbf{p} \cdot \mathbf{x}}
    + a_\mathbf{p}^\dagger e^{-i \mathbf{p} \cdot \mathbf{x}}
)
$$

Then we define the **interaction picture field** at $t$ as the field obtained by time evolving $\phi(\mathbf{x},t_0)$ using the free Hamiltonian $H_0$:

$$
\phi_I(\mathbf{x},t)
= \int \frac{d^3p}{(2\pi)^3} \frac{1}{\sqrt{2E_\mathbf{p}}} 
\left. \left(
    a_\mathbf{p} e^{ipx}
    + a_\mathbf{p}^\dagger e^{-ipx}
\right) \right|_{x^0 = t - t_0}
$$

$$
\text{evolution: } \quad
\phi_I(\mathbf{x},t) 
= e^{i H_0(t-t_0)} \phi(\mathbf{x},t_0) e^{-i H_0(t-t_0)}
$$

Then we can express the evolution of $\phi$ itself as

$$
\begin{aligned}
    \phi(\mathbf{x},t)
    &= e^{iH(t-t_0)} \phi(\mathbf{x},t_0) e^{-iH(t-t_0)}
    \\
    &= e^{iH(t-t_0)} 
    e^{-i H_0(t-t_0)} \phi_I(\mathbf{x},t) e^{i H_0(t-t_0)}
    e^{-iH(t-t_0)}
    \\
    &= U^\dagger(t,t_0) \phi_I(\mathbf{x},t) U(t,t_0)
\end{aligned}
$$

where we defined the **time-evolution operator in interaction picture** from $t_0$ to $t$

$$
U(t,t_0) = e^{i H_0(t-t_0)}
e^{-iH(t-t_0)} \qquad
(t \ge t_0)
$$

### An Differential Equation for $U(t,t_0)$

We can verify that

$$
i \frac{\partial}{\partial t} U(t,t_0)
= H_I(t) U(t,t_0)
$$

where $H_I$ is the interaction Hamiltonian evolved (in the Heisenberg sense) using the free Hamiltonian $H_0$:

$$
H_I(t) \equiv
e^{i H_0(t-t_0)} H_\text{int} e^{-i H_0(t-t_0)}
$$

Solving this equation of $U(t,t_0)$, we obtain an alternative form of the time-evolution operator

$$
\begin{aligned}
    U(t,t_0) &= T\left[
        \exp \left(
            -i \int_{t_0}^t dt' H_I(t')
        \right)
    \right]
    \\
    &\equiv 1
    + (-i) \int_{t_0}^t dt' H_I(t')
    \\ &\quad
    + \frac{(-i)^2}{2!} \int_{t_0}^t dt_1 \int_{t_0}^t dt_2
    \, T[H_I(t_1) H_I(t_2)] + \cdots
\end{aligned}
$$

where

$$
\begin{aligned}
    &\frac{1}{n!} \int_{t_0}^t dt_1 \cdots \int_{t_0}^t dt_n
    \, T[H_I(t_1) \cdots H_I(t_n)]
    \\
    &= \int_{t_0}^t dt_1 \int_{t_0}^{t_1} dt_2 \cdots
    \int_{t_0}^{t_{n-1}} dt_n \, H_I(t_1) \cdots H_I(t_n)
\end{aligned}
$$

### Properties of the Time-Evolution Operator

The general time-evolution operator from $t'$ (no longer constrained to start from the reference time $t_0$) to $t$ as

$$
U(t,t') = T\left[
    \exp \left(
        -i \int_{t'}^t dt'' H_I(t'')
    \right)
\right] \qquad (t \ge t')
$$

which has the following properties:

- Differential equation
    
    $$
    i \frac{\partial}{\partial t} U(t,t')
    = H_I(t) U(t,t')
    $$

- Unitarity

    $$
    U(t,t') = e^{iH_0(t-t_0)}
    e^{-iH(t-t')} e^{-iH_0(t'-t_0)}
    $$

- Combination of time-evolution
    
    $$
    \begin{aligned}
        U(t_1, t_2) U(t_2, t_3) &= U(t_1, t_3)
        \\
        U(t_1, t_3) U^\dagger(t_2, t_3) &= U(t_1, t_2)
    \end{aligned} \qquad
    (t_1 \ge t_2 \ge t_3)
    $$

### Ground State with Interaction

We express the time evolution of the *no-particle state* $|0\rangle$ as the superposition of the evolution of energy eigenstates $|n\rangle$ (the ground state is denoted as $|\Omega\rangle$)

$$
e^{-iHT} |0\rangle
= e^{-iE_0 T} |\Omega\rangle \langle\Omega|0\rangle
+ \sum_{n \ge 1} e^{-iE_n T} |n \rangle \langle n|0 \rangle
$$

Taking the limit $T \to \infty(1-i\epsilon)$ (in a slightly negative imaginary direction), all the higher excited states will die out compared to the ground state; thus

$$
|\Omega\rangle = \lim_{T \to \infty(1-i\epsilon)}
\frac{e^{+i E_0 T}}{\langle \Omega |0 \rangle}
e^{-iHT} |0\rangle
$$

Since $T$ is now very large, we shift the time evolution by a small constant time $t_0$, which is our reference time:

$$
|\Omega\rangle = \lim_{T \to \infty(1-i\epsilon)}
\frac{e^{+i E_0 (t_0 + T)}}{\langle \Omega |0 \rangle}
e^{-iH(t_0 + T)} |0\rangle
$$

The time evolution duration $t_0 + T$ is interpreted as $t_0 - (-T)$, i.e. from infinitely past $-T$ to the reference time $t_0$. We try to put the time-evolution operator into the expression:

$$
\begin{aligned}
    U(t_0, -T) &= e^{iH_0(t_0-t_0)}
    e^{-iH(t_0 - (-T))} e^{-iH_0(-T-t_0)}
    \\
    &= e^{-iH(t_0 + T)} e^{-iH_0(-T-t_0)}
\end{aligned}
$$

We notice that $H_0|0\rangle = 0$ (i.e. the empty state is the ground state of the free $H_0$, whose energy is set to 0). Thus $e^{-iH_0(-T-t_0)} |0\rangle = e^0 |0\rangle = |0\rangle$, and

$$
|\Omega\rangle = \lim_{T \to \infty(1-i\epsilon)}
\frac{e^{+i E_0 (t_0 + T)}}{\langle \Omega |0 \rangle}
U(t_0, -T) |0\rangle
$$

This means that *the interacting ground state $|\Omega\rangle$ can be obtained by evolving $|0\rangle$ from infinite past $-T$ to $t_0$ with $U$*. Similarly, we can show that

$$
\langle \Omega |
= \lim_{T \to \infty(1-i\epsilon)} \langle 0|
U(T, t_0) \frac{e^{+iE_0 (T-t_0)}}{\langle 0|\Omega \rangle}
$$

### Two-Point Function with Interaction

Now we calculate the two-point function with interaction. Assuming $x^0 > y^0$, and expressing all things in interaction picture, we find

$$
\begin{aligned}
    &\langle\Omega |\phi(x)\phi(y)|\Omega\rangle
    \\
    &= \lim_{T \to \infty(1-i\epsilon)}
    \frac{e^{+iE_0 (T-t_0)}}{\langle 0|\Omega \rangle} 
    \frac{e^{+i E_0 (t_0 + T)}}{\langle \Omega |0 \rangle}
    \langle 0| 
    \underbrace{U(T, t_0) U^\dagger(x^0,t_0)}_{U(T,x^0)} 
    \phi_I(x) 
    \\ &\qquad \qquad
    \underbrace{U(x^0,t_0) U^\dagger(y^0,t_0)}_{
        U(x^0, y^0), \, x^0 > y^0
    } \phi_I(y) 
    \underbrace{U(y^0,t_0) U(t_0, -T)}_{U(y^0,-T)} 
    |0\rangle
    \\
    &= \lim_{T \to \infty(1-i\epsilon)}
    \frac{e^{i E_0 (2T)}}{|\langle 0 | \Omega\rangle|^2}
    \langle 0 | 
    U(T, x^0) \phi_I(x) U(x^0, y^0) \phi_I(y) U(y^0, -T) 
    |0 \rangle
    \\
    &= \lim_{T \to \infty(1-i\epsilon)}
    \frac{e^{i E_0 (2T)}}{|\langle 0 | \Omega\rangle|^2}
    \left\langle 0 \left| T[
        \phi_I(x) \phi_I(y) U(T, -T) 
    ]
    \right| 0 \right\rangle
\end{aligned}
$$

Using the normalization of $|\Omega\rangle$

$$
\begin{aligned}
    1 &= \langle \Omega | \Omega \rangle
    \\
    &= \lim_{T\to \infty(1-i\epsilon)}
    \langle 0|
    U(T, t_0) 
    \frac{e^{+iE_0 (T-t_0)}}{\langle 0|\Omega \rangle}
    \frac{e^{+i E_0 (t_0 + T)}}{\langle \Omega |0 \rangle}
    U(t_0, -T) |0\rangle
    \\[0.5em]
    &= \lim_{T\to \infty(1-i\epsilon)}
    \frac{e^{i E_0 (2T)}}{|\langle 0 | \Omega\rangle|^2}
    \langle 0| U(T, -T) |0\rangle
\end{aligned}
$$

we can eliminate the common factor in front (and write $\phi(x)\phi(y)$ as $T[\phi(x)\phi(y)]$ since we assumed $x^0 > y^0$):

$$
\begin{aligned}
    &\langle \Omega | T[\phi(x) \phi(y)] | \Omega\rangle
    \\
    
    &= \lim_{T \to \infty(1-i\epsilon)}
    \frac{
        \left\langle 0 \left| T[
            \phi_I(x) \phi_I(y) U(T, -T) 
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

If we assumed $x^0 < y^0$ instead, this result of time ordering still holds. 

## General $n$-Point Correlation Function

The general formula for $n$-point functions is very similar to the one for 2-point functions:

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
