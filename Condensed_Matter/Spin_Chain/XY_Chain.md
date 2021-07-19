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

<div class="result">

**XY spin chain:**

- Local Hamiltonian and $\mathbb{Z}_2$ generator

    $$
    \begin{gather*}
        H_j = J_x S^x_j S^x_{j+1} + J_y S^y_j S^y_{j+1} - h S^z_j, \quad
        Z = \textstyle{\prod_{j=1}^N} Z_j
    \end{gather*}
    $$

    Sometimes people fix the scale of $H$ by setting

    $$
    J_x \equiv 1+\gamma, \quad
    J_y \equiv 1-\gamma
    $$

- APBC boundary term

    $$
    \begin{align*}
        H^A_N &= Z_1 H_N Z_1 
        = Z_1 (J_x S^x_N S^x_1 + J_y S^y_N S^y_1 - h S^z_N) Z_1 \\
        &= - J_x S^x_N S^x_1 - J_y S^y_N S^y_1 - h S^z_N
    \end{align*}
    $$

</div><br>

It is convenient to express $H_j$ in terms of $S^\pm$: 

$$
S_j^{\pm} = S_j^x \pm i S_j^y 
\, \Rightarrow \, \left\{
\begin{align*}
    S_j^x &= \frac{1}{2}(S_j^- + S_j^+)
    \\
    S_j^y &= \frac{i}{2}(S_j^- - S_j^+)
\end{align*}
\right.
$$

$$
\begin{align*}
    H_j
    &= \frac{J_x}{4} (S_j^- + S_j^+)(S_{j+1}^- + S_{j+1}^+)
    - \frac{J_y}{4}(S_j^- - S_j^+)(S_{j+1}^- - S_{j+1}^+) - h S_j^z
    \\
    &= t(S_j^+ S_{j+1}^- + S_j^- S_{j+1}^+)
    + \Delta (S_j^+ S_{j+1}^+ + S_j^- S_{j+1}^-) - h S_j^z
    \\
    &\boxed{
        = t(S_j^+ S_{j+1}^- + h.c.)
        + \Delta (S_j^+ S_{j+1}^+ + h.c.) - h S_j^z
    }
\end{align*}
$$

where we defined

$$
t \equiv \frac{J_x + J_y}{4} \qquad
\Delta \equiv \frac{J_x - J_y}{4}
$$

In terms of $\gamma$, we simply obtain $t = 1/2, \Delta = \gamma/2$. 

## Mapping to Fermion Model

Below we shall use Jordan-Wigner transformation to map the spin Hamiltonian to fermion Hamiltonian. 

### Non-Boundary Terms

For non-boundary terms $H_j \ (j = 1,...,N-1)$, the Jordan-Wigner transformation can be applied without subtleties. In the following we shall use the identity

$$
F_j F_{j+1} 
= \prod_{l=1}^{j-1} (-1)^{n_l} \prod_{l'=1}^{j} (-1)^{n_{l'}}
= (-1)^{n_j}
$$

- **"Spin Hopping" Terms**

    $$
    \begin{align*}
        S_j^+ S_{j+1}^-
        &= c_j^\dagger F_j c_{j+1} F_{j+1}
        = c_j^\dagger c_{j+1} F_j F_{j+1}
        \\
        &= c_j^\dagger c_{j+1} (-1)^{n_j} = c_j^\dagger c_{j+1}
    \end{align*}
    $$

    The last equality used the fact that this term is nonzero only when $n_j = 0$, cancelling the $(-1)^{n_j}$ factor. Combining with the h.c. term, we arrive at:

    $$
    S_j^+ S_{j+1}^- + h.c. = c_j^\dagger c_{j+1} + h.c.
    $$

- **"Spin Pair" Terms**

    $$
    \begin{align*}
        S_j^+ S_{j+1}^+
        &= c_j^\dagger F_j c_{j+1}^\dagger F_{j+1}
        = c_j^\dagger c_{j+1}^\dagger F_j F_{j+1}
        \\
        &= c_j^\dagger c_{j+1}^\dagger (-1)^{n_j} 
        = c_j^\dagger c_{j+1}^\dagger
    \end{align*}
    $$

    The last equality follows from the same argument as for the previous term. Therefore (this term is related to the **$p$-wave superconductivity**)

    $$
    S_j^+ S_{j+1}^+ + h.c. = c_j^\dagger c_{j+1}^\dagger + h.c.
    $$

- **Magnetic Field Terms**
    
    $$
    S_j^z = n_j - \frac{1}{2}
    $$

<div class="result">

**Local non-boundary term of fermion theory:**

$$
\begin{align*}
    (H_F)_j &= t(c_j^\dagger c_{j+1} + h.c.)
    \\ &\quad
    + \Delta (c_j^\dagger c_{j+1}^\dagger + h.c.) 
    - h \left(n_j - \tfrac{1}{2} \right)
\end{align*} \quad (j = 1,...,N-1)
$$

</div><br>

### The Boundary Term $H_N$

Since XY chain contains only nearest neighbor interaction, the only boundary term is $H_N$, which must be transformed carefully:

$$
\begin{align*}
    H^P_N &= + t(S_N^+ S_1^- + h.c.)
    + \Delta (S_N^+ S_1^+ + h.c.) - h S_N^z
    \\
    H^A_N &= - t(S_N^+ S_1^- + h.c.)
    - \Delta (S_N^+ S_1^+ + h.c.) - h S_N^z
\end{align*}
$$

We focus on the term:

$$
S_N^+ S_1^{(\pm)} = c_N^\dagger F_N c_1^{(\dagger)} \cancel{F_1}
$$

Introduce the the **fermion number parity** operator

$$
P \equiv (-1)^{n_\text{tot}} = \exp(i\pi n_\text{tot})
\quad \bigg( n_\text{tot} \equiv \sum_{l=1}^N n_l \bigg)
$$

Then we express $F_N$ in terms of $P$:

$$
\begin{align*}
    F_N &= F_N (-1)^{2n_N} = P (-1)^{n_N} \\ \Rightarrow
    S_N^+ S_1^{(\pm)} &= c_N^\dagger P (-1)^{n_N} c_1^{(\dagger)}
    \\
    &= c_N^\dagger P c_1^{(\dagger)} \quad 
    (\text{RHS is nonzero only when $n_N = 0$})
    \\
    &= P c_N^\dagger c_1^{(\dagger)} \quad
    
\end{align*}
$$

Obviously $P^2 = 1$, so its eigenvalues are $\pm 1$ ($n_\text{tot}$ is even or odd). In the spin representation, $n_\text{tot} = S^z_\text{tot}$ and one can verify that $[H^{A/P}, P] = 0$ (i.e. the parity is conserved). Thus the Hilbert space of the spin chain is separated into two parts $(P = \pm 1)$. To summarize:

<div class="result">

**Boundary condition of fermion theory:**

**Exact correspondence between spin Hamiltonian and fermion Hamiltonian:**

</div><br>

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

