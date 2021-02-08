<style>
    .katex {
        font-size: 1.1em;
    }
    .remark {
        border-radius: 15px;
        padding: 20px;
        background-color: SeaGreen;
        color: White;
    }
    .result {
        border-radius: 15px;
        padding: 20px;
        background-color: DarkSlateBlue;
        color: White;
    }
</style>

# Descriptions of Time Evolution

*We choose $\hbar = 1$ to simplify the formulas.*

## Schrödinger Picture

Consider a system in state $\ket{\psi}$, with Hamiltonian $H(t)$ (which in general depends on time). In the **Schrödinger picture** (denoted by subscript $S$), the time evolution is entirely due to the evolution of the state, described by the **Schrödinger's equation**:

$$
\frac{\partial}{\partial t} \ket{\psi_S(t)}
= -i H(t) \ket{\psi_S(t)}
$$

To find a formal solution $\ket{\psi_S(t)}$, we introduce the **time evolution operator** $U(t,t_0)$ (with $t_0$ some reference instant providing the initial condition) so that

$$
\ket{\psi_S(t)} = U(t,t_0) \ket{\psi_S(t_0)}
$$

### Properties of Time Evolution Operator

- $U(t,t_0)$ is a *unitary* operator:
    
    $$
    U^\dagger(t,t_0) U(t,t_0) = 1
    $$

    *Proof*: This property follows from the requirement that the state norm is unchanged by time evolution.

    $$
    \begin{aligned}
        \braket{\psi_S(t_0)}{\psi_S(t_0)} 
        &= \braket{\psi_S(t)}{\psi_S(t)}
        \\
        &= \amp{\psi_S(t_0)}{U^\dagger(t,t_0) U(t,t_0)}{\psi_S(t_0)}
        \quad \blacksquare
    \end{aligned}
    $$

- Composition property:
    
    $$
    U(t_2,t_0) = U(t_2,t_1) U(t_1,t_0) \quad
    (t_2 > t_1 > t_0)
    $$

- Schrödinger equation for $U$:

    $$
    \frac{\partial}{\partial t} U(t, t_0)
    = -i H(t) U(t, t_0)
    $$

    *Proof*: This follows from the Schrödinger equation for the states due to the arbitrariness of the state. $\blacksquare$

- Infinitesimal time evolution
    
    $$
    U(t, t + \delta t) = 1 - i H(t) \, \delta t
    $$

    *Proof*: From the Schrödinger equation

    $$
    \begin{aligned}
        \delta \ket{\psi_S(t)} 
        &= - i \delta t \, H(t) \ket{\psi_S(t)} 
        \\
        &\overset{!}{=} \ket{\psi_S(t + \delta t)} 
        - \ket{\psi_S(t)} 
        \\
        &= (U(t,t+\delta t) - 1) \ket{\psi_S(t)} 
    \end{aligned}
    $$

    Due to the arbitrariness of $\ket{\psi_S(t)}$, we get the desired result. $\blacksquare$

### Finite Time Evolution

Let us now build the finite time evolution operator. We start from the Schrödinger equation for the time evolution operator:

$$
\frac{\partial}{\partial t} U(t, t_0)
= -i H(t) U(t, t_0)
$$

which can be integrated to (using the initial condition $U(t_0,t_0) = 1$)

$$
U(t, t_0) = 1 - i 
\int_{t_0}^{t} dt' \, H(t') U(t', t_0)
$$

An approximate solution can be obtained iteratively:

$$
\begin{aligned}
    U(t,t_0) &= 1 - i 
    \int_{t_0}^{t} dt_1 \, H(t_1) 
    \\ &\qquad \times\left[
        1 - i 
        \int_{t_0}^{t_1} dt_2 \, H(t_2) U(t_2, t_0)
    \right]
    \\
    &= \cdots
    \\
    &= 1 - i 
    \int_{t_0}^{t} dt_1 \, H(t_1) 
    + \left(- i\right)^2
    \int_{t_0}^t dt_1 \int_{t_0}^{t_1} dt_2
    \, H(t_1) H(t_2)
    \\ &\quad + \cdots 
    + \left(- i\right)^n
    \int_{t_0}^t dt_1 \int_{t_0}^{t_1} dt_2 \cdots
    \int_{t_0}^{t_{n-1}} dt_n 
    \, H(t_1) \cdots H(t_n)
    \\ &\quad + \cdots 
\end{aligned}
$$

This expansion is called the **Dyson series**. 

### Time-Ordered Exponential

To put the Dyson series into a nicer form, we introduce the **time-ordering operator** $T$:

$$
\begin{aligned}
    T[H(t_1) \cdots H(t_n)]
    &\equiv \sum_{\sigma \in S_n}
    H(t_{\sigma(1)}) \cdots H(t_{\sigma(n)}) 
    \\ &\qquad \quad \times
    \theta(t_{\sigma(1)} - t_{\sigma(2)}) \cdots
    \theta(t_{\sigma(n-1)} - t_{\sigma(n)})
\end{aligned}
$$

Only one term with $t_{\sigma(1)} > \cdots > t_{\sigma(n)}$ will survive. For example, when $n = 2$

$$
\begin{aligned}
    &T[H(t_1) H(t_2)]
    \\
    &= H(t_1) H(t_2) \theta(t_1 - t_2)
    + H(t_2) H(t_1) \theta(t_2 - t_1)
    \\
    &= \begin{cases}
        H(t_1) H(t_2), & t_1 > t_2 \\
        H(t_2) H(t_1), & t_2 > t_1
    \end{cases}
\end{aligned}
$$

For the $n$th-order ($n = 2,3,...$) term in the Dyson series (call it $D_n$), we can make the integration range of $t_1,...,t_n$ all equal to $[t_0,t]$ by introducing step functions:

$$
\begin{aligned}
    D_n &\equiv
    \int_{t_0}^t dt_1 \int_{t_0}^{t_1} dt_2 \cdots
    \int_{t_0}^{t_{n-1}} dt_n 
    \, H(t_1) \cdots H(t_n)
    \\
    &= \int_{t_0}^t dt_1 
    \int_{t_0}^t dt_2 \, \theta(t_1 - t_2) \cdots
    \\ &\qquad
    \int_{t_0}^t dt_n \, \theta(t_{n-1} - t_n)
    \, H(t_1) \cdots H(t_n)
\end{aligned}
$$

Then we can permute the names of the integration variables using permutations $\sigma \in S_n$, and sum all of them with equal weight $1/n!$ (since there are $n!$ permutations):

$$
\begin{aligned}
    D_n 
    &= \frac{1}{n!} \sum_{\sigma \in S_n}
    \int_{t_0}^t dt_{\sigma(1)}  
    \int_{t_0}^t dt_{\sigma(2)} \cdots
    \int_{t_0}^t dt_{\sigma(n)} \, \\ &\qquad
    \theta(t_{\sigma(1)} - t_{\sigma(2)}) \cdots
    \theta(t_{\sigma(n-1)} - t_{\sigma(n)})
    \, H(t_{\sigma(1)}) \cdots H(t_{\sigma(n)})
\end{aligned}
$$

But we recognize the integrand as the time-ordered product of all the $H$'s. Therefore

$$
D_n = \frac{1}{n!} \int_{t_0}^t dt_1 \int_{t_0}^t dt_2 
\cdots \int_{t_0}^t dt_n \, T[H(t_1) \cdots H(t_n)]
$$

We can then write the Dyson series as a **time-ordered exponential**:

$$
\begin{aligned}
    U(t,t_0) &= T{\left[ \exp{
        \left(
            -i \int_{t_0}^t dt' H(t')
        \right)
    } \right]}
    \\ &\equiv
    \sum_{n=0}^\infty \frac{(-i)^n}{n!} 
    \int_{t_0}^t dt_1 \cdots 
    \int_{t_0}^t dt_n \,
    T[H(t_1) \cdots H(t_n)]
\end{aligned}
$$

Below we consider two special cases:

- *Case 1*: $H(t)$ at different time commutes with each other

- *Case 2*: $H$ is independent of time

    Then the time ordering becomes useless, and the result simply reduces to

    $$
    U(t, t_0) = e^{-i H (t - t_0)}
    $$

### Time Ordering as Path Ordering


## Heisenberg Picture

There is another description of time evolution which gives the same result for the expectation value of any physical observables $O$, which is 

$$
\begin{aligned}
    \expect{O}(t) &= \amp{\psi_S(t)}{O_S}{\psi_S(t)}
    \\
    &= \amp{\psi_S(t_0)}{U^\dagger(t,t_0) O_S U(t,t_0)}{\psi_S(t_0)}
\end{aligned}
$$

The reference time is usually chosen to be the infinite past $t_0 = -\infty$ or $t = 0$. In the **Heisenberg picture**, the time evolution is fully absorbed into the observable operators by defining

$$
\begin{aligned}
    O_H(t) &= U^\dagger(t,t_0) O_S U(t,t_0) 
    \\[0.5em]
    \ket{\psi_H} &= \ket{\psi_S(t_0)}
\end{aligned}
$$

In particular, when $H$ is time-independent:

$$
O_H(t) = e^{iH(t-t_0)} O_S e^{-iH(t-t_0)}
$$

Then the expectation value can be written as

$$
\expect{O}(t) = \amp{\psi_H}{O_H(t)}{\psi_H}
$$

### Heisenberg Equation of Motion

Let us write down the differential equation determining the time evolution of $O_H$. By direct calculation (using the Schrödinger equation for $U(t,t_0)$)

$$
\begin{aligned}
    \frac{\partial O_H}{\partial t}
    &= \frac{\partial U^\dagger}{\partial t} O_S U
    + U^\dagger O_S \frac{\partial U}{\partial t}
    \\
    &= +i (H U)^\dagger O_S U + U^\dagger O_S (-i H U)
    \\
    &= i ( 
        U^\dagger H (U U^\dagger) O_S U
        - U^\dagger O_S (U U^\dagger) H U
    ) \\
    &= -i [O_H, U^\dagger H U]
\end{aligned}
$$

When the Hamiltonian $H$ is independent of time, it must commute with $U(t,t_0) = e^{-iH(t-t_0)}$. Then we have

$$
U^\dagger(t) H U(t) = H
$$

Thus

$$
\frac{\partial O_H}{\partial t} = -i [O_H, H]
$$

## Interaction Picture

Consider a special category of problems, in which the Hamiltonian can be separated into two parts:

$$
H(t) = H_0 + V(t)
$$

The first part $H_0$ is time-*independent*, usually the no-interaction (free) part of $H$. The second part $V(t)$ is usually the interaction terms, which can either be time dependent or not. A common practice is to add a time dependence in order to turn on or off these terms. Then we define the **interaction picture** state $\ket{\psi_I(t)}$ and observable $O_I$ as

$$
\begin{aligned}
    \ket{\psi_I(t)} &= e^{iH_0 (t-t_0)} \ket{\psi_S(t)}
    \\[0.5em]
    O_I(t) &= e^{iH_0(t-t_0)} O_S e^{-iH_0(t-t_0)}
\end{aligned}
$$

In other words, the interaction picture operators are evolved by the *free* Hamiltonian $H_0$, which immediately leads to the equation of motion

$$
\frac{\partial O_I}{\partial t} = -i [O_I, H_0]
$$

### Time Evolution Operator

Let us now determine the time evolution of $\ket{\psi_I}$, i.e. the time evolution operator $U_I$ appearing in

$$
\ket{\psi_I(t)} = U_I(t,t_0) \ket{\psi_I(t_0)}
$$

<div class="remark">

*Remark*: The time evolution operator in the interaction picture is sometimes denoted by $S(t,t_0)$ because its connection with the ***S*-matrix** in particle scattering theory.

</div><br>

We rewrite the definition of $\ket{\psi_I}$ as

$$
\begin{aligned}
    \ket{\psi_I(t)} &= e^{iH_0 (t-t_0)} \ket{\psi_S(t)}
    \\
    &= e^{iH_0 (t-t_0)} U(t, t_0) \ket{\psi_S(t_0)}
    \\
    &= e^{iH_0 (t-t_0)} U(t, t_0) \ket{\psi_I(t_0)}
\end{aligned}
$$

Thus

$$
U_I(t,t_0) = e^{iH_0 (t-t_0)} U(t, t_0)
$$

To determine the differential equation governing $U_I$, we calculate

$$
\begin{aligned}
    \frac{dU_I}{\partial t}
    &= \frac{\partial e^{iH_0 (t-t_0)}}{\partial t} U
    + e^{iH_0 (t-t_0)} \frac{\partial U}{\partial t}
    \\
    &= iH_0 e^{iH_0 (t-t_0)} U
    + e^{iH_0 (t-t_0)} (-i H U)
    \\
    &= i e^{iH_0 (t-t_0)} (H_0 - H) U
    \\
    &= -i e^{iH_0 (t-t_0)} V U
    \\
    &= -i \underbrace{
        e^{iH_0 (t-t_0)} V e^{-iH_0 (t-t_0)}
    }_{V_I(t)} \underbrace{
        e^{iH_0 (t-t_0)} U
    }_{U_I(t,t_0)}
\end{aligned}
$$

We get a Schrödinger-like equation, with $H$ replaced by $V_I$:

$$
\frac{\partial U_I}{\partial t} = -i V_I(t) U_I(t,t_0)
$$

For the state evolution, we have a similar result:

$$
\frac{\partial}{\partial t} \ket{\psi_I(t)}
= -i V_I(t) \ket{\psi_I(t)}
$$

These means that the interaction picture states are evolved by $V_I$. As a special case, when $H$ is independent of time, and $[H_0, V] = 0$, we obtain

$$
\begin{aligned}
    U_I(t,t_0) &= e^{iH_0 (t-t_0)} e^{-iH(t-t_0)}
    \\
    &= e^{-iV (t-t_0)}
\end{aligned}
$$

which is time evolution solely by $V_I = V$. 

## Summary

$$
\def \arraystretch{1.5}
\begin{array}{c|cc}
    \text{Representation} & \text{States} & \text{Operators}
    \\ \hline
    \text{Schrödinger} & 
    \partial_t \ket{\psi_S(t)} = -i H \ket{\psi_S(t)} & 
    \text{Constant}
    \\
    \text{Heisenberg} & 
    \text{Constant} &
    \partial_t O_H(t) = -i [O_H(t), H]
    \\
    \text{Interaction} &
    \partial_t \ket{\psi_I(t)} = -i V_I \ket{\psi_I(t)} &
    \partial_t O_I(t) = -i [O_I(t), H_0]
\end{array}
$$
