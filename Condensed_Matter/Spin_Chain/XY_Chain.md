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

# XY Spin Chain

## Hamiltonian in Momentum Space

To see the energy levels more clearly, we shall go to the momentum space (reciprocal lattice)

$$
c_j = \frac{1}{\sqrt{N}} \sum_p c_p e^{ipx_j}, \quad
x_j = ja
$$

We transform the Hamiltonian term by term:

- Tight-binding term

    $$
    \begin{align*}
        &(-t) \sum_j (c_j^\dagger c_{j+1} + h.c.)
        \\
        &= -\frac{t}{N} \sum_j 
        \sum_{k,p} (
            c_k^\dagger e^{-ikja} c_p e^{ip(j+1)a}
            + h.c.
        )
        \\
        &= -\frac{t}{N} \sum_{k,p} \bigg[
            c_k^\dagger c_p e^{ipa} 
            \overbrace{\sum_{j} e^{i(p-k)ja}}^{= N \delta_{kp}}
            + h.c.
        \bigg]
        \\
        &= -t \sum_k c_k^\dagger c_k
        (e^{ika} + e^{-ika})
        = -2t \sum_k c_k^\dagger c_k \cos(ka)
    \end{align*}
    $$

- $p$-Wave potential term

    $$
    \begin{align*}
        &(-\Delta) \sum_j (c_j^\dagger c_{j+1}^\dagger + h.c.) 
        \\
        &= -\frac{\Delta}{N} \sum_j 
        \sum_{k,p} (
            c_k^\dagger e^{-ikja} c_p^\dagger e^{-ip(j+1)a}
            + h.c.
        )
        \\
        &= -\frac{\Delta}{N} \sum_{k,p} \bigg[
            c_k^\dagger c_p^\dagger e^{-ipa} 
            \overbrace{\sum_{j} e^{i(p+k)ja}}^{= N \delta_{k,-p}}
            + h.c.
        \bigg]
        \\
        &= -\Delta \sum_k (
            c_k^\dagger c_{-k}^\dagger e^{ika}
            + c_{-k} c_k e^{-ika}
        )
        \\
        &= -\Delta \sum_k e^{ika} (
            c_k^\dagger c_{-k}^\dagger + c_{k} c_{-k} 
        )
    \end{align*}
    $$

- Chemical potential term (omitting the constants)

    $$
    \begin{align*}
        &(-h) \sum_j n_j
        = (-h) \sum_j c_j^\dagger c_j
        \\
        &= -\frac{h}{N} \sum_j \sum_{k,p}
        c_k^\dagger e^{-ikja} c_p e^{ipja}
        = -h \sum_k c_k^\dagger c_k 
    \end{align*}
    $$

Thus

$$
H = - \sum_k \left[
    (h + 2t \cos ka) c_k^\dagger c_k
    + \Delta e^{ika}(
        c_k^\dagger c_{-k}^\dagger + c_k c_{-k}
    )
\right]
$$

We can restrict $k$ to positive values in $[0, \pi/a]$: 

$$
\begin{align*}
    H &= - \sum_{k\ge 0} \Big[
        (h + 2t \cos ka) (c_k^\dagger c_k + c_{-k}^\dagger c_{-k})
        \\ &\qquad \qquad
        + \Delta e^{ika}(
            c_k^\dagger c_{-k}^\dagger + c_k c_{-k}
        ) + \Delta e^{-ika} \underbrace{(
            c_{-k}^\dagger c_{k}^\dagger + c_{-k} c_{k}
        )}_{= -c_k^\dagger c_{-k}^\dagger - c_k c_{-k}}
    \Big]
    \\
    &= - \sum_{k\ge 0} \Big[
        (h + 2t \cos ka) (c_k^\dagger c_k + c_{-k}^\dagger c_{-k})
        \\ &\qquad \qquad
        + (2i \Delta \sin ka) (
            c_k^\dagger c_{-k}^\dagger + c_k c_{-k}
        )
    \Big]
\end{align*}
$$

## Diagonalization: Bogoliubov Transformation

To put this into diagonal form, we further apply the **Bogoliubov transformation**, i.e. make a linear combination of $k$ and $-k$ operators:

$$
\begin{align*}
    \eta_k &= A_k c_k + B_k c_{-k}^\dagger
    \\
    \eta_{-k} &= C_k c_{-k} + D_k c_k^\dagger
\end{align*} \qquad
A_k,B_k,C_k,D_k \in \mathbb{C}
$$

which can be more neatly written as

$$
\begin{bmatrix}
    \eta_k \\[0.5em] \eta_{-k}^\dagger
\end{bmatrix} = \begin{bmatrix}
    A_k & B_k \\[0.5em]
    D_k^* & C_k^*
\end{bmatrix} \begin{bmatrix}
    c_k \\[0.5em] c_{-k}^\dagger
\end{bmatrix}
$$

Then the inverse transformation can be more easily seen:

$$
\begin{bmatrix}
    c_k \\[0.5em] c_{-k}^\dagger
\end{bmatrix} 
= \frac{1}{A_k C_k^* - B_k D_k^*}\begin{bmatrix}
    C_k^* & B_k \\[0.5em]
    D_k^* & A_k
\end{bmatrix} \begin{bmatrix}
    \eta_k \\[0.5em] \eta_{-k}^\dagger
\end{bmatrix}
$$

We require that $\eta_k^{(\dagger)}$ still satisfies the fermion anti-commutators: when $k\ne 0$, we should obtain

$$
\begin{align*}
    \{\eta_k, \eta_k\} &= \{\eta_k^\dagger, \eta_k^\dagger\} = 0
    \\
    \{\eta_{-k}, \eta_{-k}\} &= \{\eta_{-k}^\dagger, \eta_{-k}^\dagger\} = 0
    \\
    \{\eta_k, \eta_{-k}^\dagger\} &= \{\eta_{-k}, \eta_k^\dagger\} = 0
    \\
    \{\eta_k, \eta_{k}^\dagger\} &= \{\eta_{-k}, \eta_{-k}^\dagger\} = 1
    \\
    \{\eta_{k}, \eta_{-k}\} &= \{\eta_{k}^\dagger, \eta_{-k}^\dagger\} = 0
\end{align*}
$$

The first three equations are automatically satisfied; the last two equations give us, respectively

$$
\begin{align*}
    |A_k|^2 + |B_k|^2 &= 1 \\
    |C_k|^2 + |D_k|^2 &= 1
\end{align*} 
\quad \text{and} \quad
A_k D_k + B_k C_k = 0
$$

We now determine the coefficients $A_k, ..., D_k$ so that the Hamiltonian is in diagonal form with the $\eta_k^{(\dagger)}$ operators. 

$$

$$

Finally

$$
H = \sum_{k \ge 0} \left[
    \Lambda_{1k} \eta_k^\dagger \eta_k
    + \Lambda_{2k} \eta_{-k}^\dagger \eta_{-k}
    + S^x_k
\right]
$$

