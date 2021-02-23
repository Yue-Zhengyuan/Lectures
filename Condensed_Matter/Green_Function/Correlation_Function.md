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

# Correlation Function

<div class="result">

**The $n$-point (correlation) function:**

$$
\expect{O_1(t_1) \cdots O_n(t_n)}
= \frac{\amp{\Psi_0}{T [O_{1H}(t_1) \cdots O_{nH}(t_n)]}{\Psi_0}}
{\braket{\Psi_0}{\Psi_0}}
$$

*Notation notes*:

- Operators and states on the RHS are in the Heisenberg picture
- $T$ is the time ordering operator
- $\ket{\Psi_0}$ is the ground state with interaction

</div><br>

## Ground State with Interaction

Let the full Hamiltonian (assumed to be time-independent) with interaction be 

$$
H = H_0 + V
$$

Now we need to find the state $\ket{\Psi_0}$ with interaction. One way to do so is to apply the Gell-Mann and Low theorem, but there is a more straightforward approach. 

We express the time evolution (in the Schrödinger picture) of the *free* ground state $\ket{0}$ as the superposition of the evolution of energy eigenstates $\ket{\Psi_n}$ (the ground state is $\ket{\Psi_0}$)

$$
e^{-iHT} \ket{0}
= e^{-iE_0 T} \ket{\Psi_0} \braket{\Psi_0}{0}
+ \sum_{n \ge 1} e^{-iE_n T} \ket{\Psi_n} \braket{\Psi_n}{0}
$$

Note that the Hamiltonian is time-independent, thus the time evolution operator takes the simple exponential form. Taking the limit $T \to \infty(1-i\epsilon)$, all the higher excited states will die out compared to the ground state; thus

$$
\ket{\Psi_0} = \lim_{T \to \infty(1-i\epsilon)}
\frac{e^{+i E_0 T}}{\braket{\Psi_0}{0}}
e^{-iHT} \ket{0}
$$

Since $T$ is now very large, we shift the time evolution by a small constant time $t_0$, which is the reference time in interaction picture:

$$
\ket{\Psi_0} = \lim_{T \to \infty(1-i\epsilon)}
\frac{e^{+i E_0 (t_0 + T)}}{\braket{\Psi_0}{0}}
e^{-iH(t_0 + T)} \ket{0}
$$

The time evolution duration $t_0 + T$ is interpreted as $t_0 - (-T)$, i.e. from infinitely past $-T$ to the reference time $t_0$. We try to put the time-evolution operator into the expression:

$$
\begin{aligned}
    S(t_0, -T) &= e^{iH_0(t_0-t_0)}
    e^{-iH(t_0 - (-T))} e^{-iH_0(-T-t_0)}
    \\
    &= e^{-iH(t_0 + T)} e^{-iH_0(-T-t_0)}
\end{aligned}
$$

We notice that $H_0\ket{0} = 0$ (i.e. the empty state is the ground state of the free $H_0$, whose energy is set to 0). Thus $e^{-iH_0(-T-t_0)} \ket{0} = e^0 \ket{0} = \ket{0}$, and

<div class="result">

**Relation between interacting and free ground states:**

$$
\ket{\Psi_0} = \lim_{T \to \infty(1-i\epsilon)}
\frac{e^{+i E_0 (t_0 + T)}}{\braket{\Psi_0}{0}}
S(t_0, -T) \ket{0}
$$

Similarly, one can show that

$$
\bra{\Psi_0}
= \lim_{T \to \infty(1-i\epsilon)} \bra{0}
S(T, t_0) \frac{e^{+iE_0 (T-t_0)}}{\braket{0}{\Psi_0}}
$$

</div><br>

## Evaluating the Correlation Function

Now we calculate the two-point function (the Green's function) with interaction

$$
\amp{\Psi_0}{T[O_{1H}(t) O_{2H}(t')]}{\Psi_0}
$$

It is convenient to work with operators in the interaction picture using the relation

$$
O_H(t) = S^\dagger(t,t_0) O_I(t) S(t,t_0)
$$

When $t > t'$, we find

$$
\begin{aligned}
    &\amp{\Psi_0}{O_{1H}(t) O_{2H}(t')}{\Psi_0}
    \\
    &= \lim_{T \to \infty(1-i\epsilon)}
    \frac{e^{+iE_0 (T-t_0)}}{\braket{0}{\Psi_0}} 
    \frac{e^{+i E_0 (t_0 + T)}}{\braket{\Psi_0}{0}}
    \bra{0} 
    \underbrace{S(T, t_0) S^\dagger(t,t_0)}_{S(T,t)} 
    O_{1I}(t)
    \\ &\qquad \qquad
    \underbrace{S(t,t_0) S^\dagger(t',t_0)}_{
        S(t, t')
    } O_{2I}(t') 
    \underbrace{S(t',t_0) S(t_0, -T)}_{S(t',-T)} 
    \ket{0}
    \\
    &= \lim_{T \to \infty(1-i\epsilon)}
    \frac{e^{i E_0 (2T)}}{|\braket{0}{\Psi_0}|^2}
    \amp{0}{S(T, t) O_{1I}(t) S(t, t') O_{2I}(t') S(t', -T) }{0}
    \\
    &= \lim_{T \to \infty(1-i\epsilon)}
    \frac{e^{i E_0 (2T)}}{|\braket{0}{\Psi_0}|^2}
    \amp{0}{T[S(T, -T) \phi_I(x) \phi_I(y) ]}{0}
\end{aligned}
$$

Where we put $S(T,-T)$ in the time ordering does not matter, but conventionally it is put in front of the operators in the correlation function. Using the normalization of $\ket{\Psi_0}$

$$
\begin{aligned}
    1 &= \braket{\Psi_0}{\Psi_0}
    \\
    &= \lim_{T\to \infty(1-i\epsilon)}
    \bra{0} S(T, t_0) 
    \frac{e^{+iE_0 (T-t_0)}}{\braket{0}{\Psi_0}}
    \frac{e^{+i E_0 (t_0 + T)}}{\braket{\Psi_0}{0}}
    S(t_0, -T) \ket{0}
    \\[0.5em]
    &= \lim_{T\to \infty(1-i\epsilon)}
    \frac{e^{i E_0 (2T)}}{|\braket{0}{\Psi_0}|^2}
    \amp{0}{S(T, -T)}{0}
\end{aligned}
$$

we can eliminate the common factor in the front (and write $O_1(t) O_2(t')$ as $T[O_1(t) O_2(t')]$ since we assumed $t > t'$):

$$
\begin{aligned}
    &\frac{\amp{\Psi_0}{T [O_{1H}(t) O_{2H}(t')]}{\Psi_0}}
    {\braket{\Psi_0}{\Psi_0}}
    \\
    
    &= \lim_{T \to \infty(1-i\epsilon)}
    \frac{
        \amp{0}{T[S(T, -T) O_{1I}(t) O_{2I}(t')]}{0}
    }{
        \amp{0}{S(T, -T)}{0}
    }
\end{aligned}
$$

If we assumed $t < t'$ instead, one can verify that the time ordering still holds. One can generalize this result to:

<div class="result">

**The $n$-point correlation function:**

$$
\begin{aligned}
    &\frac{\amp{\Psi_0}{T [O_{1H}(t_1) \cdots O_{nH}(t_n)]}{\Psi_0}}
    {\braket{\Psi_0}{\Psi_0}}
    \\
    &= \lim_{T \to \infty(1-i\epsilon)}
    \frac{
        \amp{0}{T[O_{1}(t_1) \cdots O_{n}(t_n) S(T, -T)]}{0}
    }{
        \amp{0}{S(T, -T)}{0}
    }
\end{aligned}
$$

</div><br>

<div class="remark">

*Remark*: The interaction picture label $I$ for operators is usually omitted in free correlation functions (in free systems the interaction picture coincides with the Heisenberg picture).

</div><br>

## Perturbative Expansion

*In this section we restore $\hbar$.*

Recall that the time-evolution operator $S$ can be expanded as the Dyson series

$$
\begin{aligned}
    S(t,t_0) &= T{\left[ \exp{
        \left(
            \frac{-i}{\hbar} \int_{t_0}^t dt' \, V(t')
        \right)
    } \right]}
    \\ &\equiv
    \sum_{k=0}^\infty \frac{1}{k!} 
    \left(\frac{-i}{\hbar}\right)^k
    \int_{t_0}^t dt'_1 \cdots 
    \int_{t_0}^t dt'_k \,
    T[V(t'_1) \cdots V(t'_k)]
\end{aligned}
$$

we can then also expand the correlation function; the $k$th order term (of the numerator) is

$$
\begin{aligned}
    &\amp{0}{T[O_{1}(t_1) \cdots O_{n}(t_n) S^{(k)}(T, -T)]}{0}
    \\
    &= \frac{1}{k!} \left(\frac{-i}{\hbar}\right)^k
    \int_{-T}^T dt'_1 \cdots 
    \int_{-T}^T dt'_k \,
    \amp{0}{T[
        V(t'_1) \cdots V(t'_k)
        O_{1}(t_1) \cdots O_{n}(t_n)
    ]}{0}
\end{aligned}
$$

Note that inside the time-ordering, the $V$ always commutes with other operators, but the $O_I$ operators will anti-commute with other $O_I$ for a fermion system.

Then one can apply Wick's theorem to the amplitude

$$
\amp{0}{T[
    V(t'_1) \cdots V(t'_k)
    O_{1}(t_1) \cdots O_{n}(t_n)
]}{0}
$$

to convert it into products of free two-point functions (which are assumed to be known). Each term in the perturbative expansion can be converted to **Feynman diagrams** with specific rules (**Feynman rules**; the details will differ a little by models).
