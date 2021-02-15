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

# The Gell-Mann and Low Theorem

*Reference: arXiv math-ph/0612030*

Consider a time-independent Hamiltonian that can be split into a free (solvable) part and an interaction part

$$
H = H_0 + gV
$$

where $g$ is some coupling constant separated from $V$ for later convenience. One can add an auxiliary time dependence to the interaction $V$ to slowly (**adiabatically**) turn it on or off off:

$$
H_\epsilon(t) = H_0 + V_\epsilon(t), \quad 
V_\epsilon(t) = e^{-\epsilon|t|} g V
\quad (0 < \epsilon \ll 1)
$$

In this construction, 

$$
H_\epsilon(\pm \infty) = H_0, \quad
H_\epsilon(0) = H
$$

The introduction of the auxiliary time independence is to slowly evolve one eigenstate of $H_\epsilon(-\infty) = H_0$, in the hope that it will become a eigenstate of the *full Hamiltonian* $H = H_\epsilon(0)$, at least in the $\epsilon \to 0_+$ limit. Luckily this is confirmed by the **Gell-Mann and Low theorem**.

## A Lemma

Before proceed to the main theorem, one lemma is needed:

<div class="result">

**Lemma:** Let $U_\epsilon(t,s) \ (t \ge s)$ be the Schrödinger picture (full) evolution operator. Then for *all* $\epsilon > 0$ (not limited to infinitesimal ones)

$$
i\epsilon g \partial_g U_\epsilon(t,s)
= \begin{cases}
    + H_\epsilon(t) U_\epsilon(t,s) - U_\epsilon(t,s) H_\epsilon(s),
    & 0 \ge t \ge s \\
    - H_\epsilon(t) U_\epsilon(t,s) + U_\epsilon(t,s) H_\epsilon(s),
    & t \ge s \ge 0
\end{cases}
$$

</div><br>

*Proof*: Let us absorb $g$ into the exponential factor by defining $g = e^{\epsilon \theta}$; then

$$
H_\epsilon(t) = H_0 + e^{\epsilon(\theta - |t|)} gV
$$

Recall that we have the following integral equation derived from the Schrödinger equation

$$
\begin{aligned}
    U_\epsilon(t, s) &= 1 - i \int_{s}^{t} dt' \, 
    H_\epsilon(t') U_\epsilon(t', s)
    \\
    &= 1 - i \int_{s}^{t} dt' \, 
    (H_0 + e^{\epsilon(\theta - |t'|)} V) U_\epsilon(t', s)
\end{aligned}
$$

We also construct two further Hamiltonians with the following artificial time dependence

$$
H_\pm(t) = H_0 + e^{\pm \epsilon t}
$$

and let the corresponding full evolution operators be $U_\pm(t,s)$, satisfying the integral equations

$$
\begin{aligned}
    U_\pm(t, s) &= 1 - i \int_{s}^{t} dt' \, 
    H_\pm(t') U_\pm(t', s)
    \\
    &= 1 - i \int_{s}^{t} dt' \, 
    (H_0 + e^{\pm \epsilon t'}V) U_\epsilon(t', s)
\end{aligned}
$$

However, we shall see that with proper shift of arguments, $U_\pm$ will yield the same integral equation as $U_\epsilon$, so they are closely related. 

- For $0 \ge t \ge s$:
    
    $$
    \begin{aligned}
        U_\epsilon(t, s) &= 1 - i \int_{s}^{t} dt' \, 
        (H_0 + e^{\epsilon(\theta + t')} V) U_\epsilon(t', s)
        \\
        U_+(t+\theta, s+\theta) 
        &= 1 - i \int_{s+\theta}^{t+\theta} dt' \, 
        (H_0 + e^{\epsilon t'}V) U_\epsilon(t', s+\theta)
        \\
        &= 1 - i \int_{s}^{t} dt' \, 
        (H_0 + e^{\epsilon (\theta+t')}V) U_\epsilon(t', s+\theta)
    \end{aligned}
    $$

    The uniqueness of the solution implies that

    $$
    U_\epsilon(t, s) = U_+(t+\theta, s+\theta) 
    \qquad (0 \ge t \ge s)
    $$

- For $t \ge s \ge 0$,

    $$
    \begin{aligned}
        U_\epsilon(t, s) &= 1 - i \int_{s}^{t} dt' \, 
        (H_0 + e^{\epsilon(\theta - t')} V) U_\epsilon(t', s)
        \\
        U_-(t-\theta, s-\theta) 
        &= 1 - i \int_{s-\theta}^{t-\theta} dt' \, 
        (H_0 + e^{-\epsilon t'}V) U_\epsilon(t', s-\theta)
        \\
        &= 1 - i \int_{s}^{t} dt' \, 
        (H_0 + e^{-\epsilon (t'-\theta)}V) U_\epsilon(t', s-\theta)
    \end{aligned}
    $$

    This implies

    $$
    U_\epsilon(t, s) = U_-(t-\theta, s-\theta) 
    \qquad (t \ge s \ge 0)
    $$

These relations make the $\theta$ (or $g$) dependence of $U_\epsilon$ very simple. Then we can apply the chain rule to obtain ($\partial_i$ means the derivative in the $i$th slot)

$$
\begin{aligned}
    \partial_\theta U_\epsilon(t,s)
    &= \partial_1 U_\pm(t \pm \theta, s \pm \theta) 
    + \partial_2 U_\pm(t \pm \theta, s \pm \theta)
    \\
    &= \pm (\partial_1 U_\epsilon(t,s) + \partial_2 U_\epsilon(t,s))
    \\
    &= -i (\pm H_\epsilon(t) U_\epsilon(t,s)
    \mp U_\epsilon(t,s) H_\epsilon(s))
\end{aligned}
$$

In the last line we used the Schrödinger equations

$$
\begin{aligned}
    \partial_1 U_\epsilon(t,s) 
    &= - i H_\epsilon(t) U_\epsilon(t,s) \\
    \partial_2 U_\epsilon(t,s)
    &= + i U_\epsilon(t,s) H_\epsilon(s)
\end{aligned}
$$

But do not forget that $\theta$ is related to $g$, then

$$
\partial_\theta
= (\partial_\theta g) \partial_g
= \epsilon g \partial_g
$$

Finally we get the desired result. $\blacksquare$

## The Gell-Mann and Low Theorem

We now state and prove the main theorem. 

<div class="result">

**The Gell-Mann and Low theorem:** 

Suppose the full Hamiltonian can be separated into $H = H_0 + gV$. Let:

- $\ket{\Phi_0}$ be an eigenstate of $H_0$ (in the free Heisenberg picture);
- $U_{\epsilon I}(t, s)$ be the time evolution operator in the interaction picture with the auxiliary Hamiltonian
    
    $$
    H_\epsilon(t) = H_0 + e^{-\epsilon|t|} g V
    $$

Define the state 

$$
\begin{aligned}
    \ket{\Psi_\epsilon} 
    &\equiv \frac{U_{\epsilon I}(0, -\infty) \ket{\Phi_0}}
    {\amp{\Phi_0}{U_{\epsilon I}(0, -\infty)}{\Phi_0}}
\end{aligned}
$$

Then the following limit (if it exists) is still an eigenstate of the full Hamiltonian $H$:

$$
\ket{\Psi_0} \equiv \lim_{\epsilon \to 0_+} 
\ket{\Psi_\epsilon}
$$

</div><br>

*Proof*: Since in the proof of the lemma we only used the Schrödinger equations, we can directly replace $U_\epsilon, H_\epsilon$ there by the corresponding operators in the interaction picture, we obtain for *all* $\epsilon > 0$ 

$$
\begin{aligned}
    i\epsilon g \partial_g U_{\epsilon I}(t,s)
    &= \begin{cases}
        + H_{\epsilon I}(t) U_{\epsilon I}(t,s) - U_{\epsilon I}(t,s) H_{\epsilon I}(s),
        & 0 \ge t \ge s \\
        - H_{\epsilon I}(t) U_{\epsilon I}(t,s) + U_{\epsilon I}(t,s) H_{\epsilon I}(s),
        & t \ge s \ge 0
    \end{cases}
    \\[1.5em]
    H_{\epsilon I}(t) 
    &= e^{iH_0(t-t_0)} H_\epsilon(t) e^{-iH_0(t-t_0)}
\end{aligned}
$$

Now let us apply this to the Heisenberg picture eigenstate $\ket{\Phi_0}$ (time-independent) of $H_0$. Note that this state can be interpreted as

Then we choose

$$
t = 0, \quad s = t_0 = -\infty
$$

then

$$
\begin{aligned}
    \text{LHS} \ket{\Phi_0(-\infty)}
    &= i\epsilon g \partial_g 
    U_{\epsilon I}(0,-\infty) \ket{\Phi_\epsilon(-\infty)}
    \\
    &= i\epsilon g \partial_g \ket{\Phi_\epsilon(0)}
    
    \\[1em]

    \text{RHS} \ket{\Phi_0(-\infty)}
    &= H_{\epsilon I}(0) U_{\epsilon I}(0,-\infty) 
    \ket{\Phi_\epsilon(-\infty)}
    \\ &\quad
    - U_{\epsilon I}(0,-\infty) \underbrace{
        H_{\epsilon I}(-\infty) \ket{\Phi_0(-\infty)}
    }_{E_0 \ket{\Phi_0(-\infty)}}
    \\
    &= (H_{\epsilon I}(0) - E_0) \ket{\Phi_\epsilon(0)}
\end{aligned}
$$

However, this $H_{\epsilon I}(0)$ is just the original full Hamiltonian $H$ in its own interaction picture

$$
H_{\epsilon I}(0) = e^{iH_0(0-t_0)} 
\underbrace{H_\epsilon(0)}_{= H} e^{-iH_0(0-t_0)}
= H_I(0)
$$

Thus we obtain (by further dividing both sides by the factor $\braket{\Phi_\epsilon(-\infty)}{\Phi_\epsilon(0)}$)

$$
(H - E_0) \ket{\Psi_\epsilon}
= i\epsilon g \partial_g \ket{\Psi_\epsilon}
$$
