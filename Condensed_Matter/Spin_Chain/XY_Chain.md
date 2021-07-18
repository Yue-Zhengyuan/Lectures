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

*References*:

- [Strongly Correlated Systems
in Solid State Physics](http://www.thp.uni-koeln.de/~as/Mypage/PSfiles/Korrel/korrel.pdf)
- [PhD Thesis of Zou Yijian](https://uwspace.uwaterloo.ca/handle/10012/16049)

*Notes on notations*: The Pauli matrices will be alternatively denoted by $(X_i, Y_i, Z_i)$ or $(\sigma_i^x, \sigma_i^y, \sigma_i^z)$.

## Periodic/Anti-Periodic Boundary Conditions

**Periodic boundary condition (PBC)** can intuitively be applied to any spin chain. However, the **anti-periodic boundary condition (APBC)** can only be imposed on spin chains with $\mathbb{Z}_2$ symmetry (symmetry with respect to the flip of all spins). 

In the following discussion, the chain sites will be labelled periodically for both boundary conditions, i.e.

$$
\sigma_{j+N}^a = \sigma_j^a \qquad j = 1,...,N
$$

For the XY chain, the PBC Hamiltonian $H^P$ and the $\mathbb{Z}_2$ symmetry generator $Z$ are combinations of local term (for convenience we use Pauli matrices instead of spin-1/2 operators $S^a = \sigma^a/2$):

<div class="result">

**XY spin chain:**

$$
\begin{align*}
    H^P &= \sum_{j=1}^N H_j, \quad
    Z = \prod_{j=1}^N Z_j
    \\
    H_j &= - [J_x X_j X_{j+1} + J_y Y_j Y_{j+1} + h Z_j]
    \\[0.7em]
    J_x &\equiv \frac{1+\gamma}{2}, \quad
    J_y \equiv \frac{1-\gamma}{2}
\end{align*}
$$

</div><br>

The system in invariant under the $\mathbb{Z}_2$ transformation in the sense that *each local Hamiltonian*, and therefore the full $H$ is invariant:

$$
Z^\dagger H_j Z = H_j
\ \Rightarrow \ 
Z^\dagger H Z = H
$$

----

*Verify the claimed $Z$*: Using the fact that

- The Pauli matrices are both Hermitian and unitary (and therefore square to identity)
- The commutators $[\sigma^a_m, \sigma^b_n] = \delta_{mn} \times 2i \epsilon^{abc} \sigma^c_m$

Then for each term in $H_j$

$$
\begin{align*}
    Z^\dagger X_j X_{j+1} Z
    &= \bigg[ \prod_{m=1}^N Z_m \bigg]^\dagger
    X_j X_{j+1}
    \bigg[ \prod_{n=1}^N Z_n \bigg]
    \\
    &= Z_{j+1} Z_j X_j X_{j+1} Z_j Z_{j+1}
    \\
    &= Z_j X_j Z_j Z_{j+1} X_{j+1} Z_{j+1} 
    \\
    &= (-X_j) (-X_{j+1}) = X_j X_{j+1}
\end{align*}
$$

Similarly

$$
\begin{align*}
    Z^\dagger Y_j Y_{j+1} Z
    &= Z_j Y_j Z_j Z_{j+1} Y_{j+1} Z_{j+1} 
    \\
    &= (-Y_j) (-Y_{j+1}) = Y_j Y_{j+1}
\end{align*}
$$

And obviously $Z^\dagger Z_j Z = Z_j$. Thus we have proved that $Z^\dagger H_j Z = H_j$. $\blacksquare$

----

Then we introduce the lattice translation operator $T$ and its **twisted** counterpart $\tilde{T} \equiv Z_1 T$. The action of $T$ on any local spin operators $O_j$ is defined as

$$
T^\dagger O_j T = O_{j+1}
$$

We can then define the PBC *and* the APBC Hamiltonians as

<div class="result">

**PBC/APBC Hamiltonian:**

$$
\begin{align*}
    H^P &= \sum_{j=1}^N H^P_j, &\quad
    H^P_j &\equiv (T^\dagger)^{j-1} 
    H_1 T^{j-1} (= H_j)
    \\
    H^A &= \sum_{j=1}^N H^A_j, &\quad
    H^A_j &\equiv (\tilde{T}^\dagger)^{j-1} 
    H_1 \tilde{T}^{j-1}
\end{align*}
$$

</div><br>

The APBC Hamiltonian will include some non-trivial boundary terms. Let us determine the APBC local Hamiltonian: starting with $H^A_2$, we have

$$
\begin{align*}
    H^A_2 &= \tilde{T}^\dagger H_1 \tilde{T}
    \\
    &= - T^\dagger Z_1^\dagger 
    [J_x X_1 X_2 + J_y Y_1 Y_2 + h Z_1] Z_1 T
    \\
    &= - T^\dagger [
        J_x Z_1 X_1 Z_1 X_2 + J_y Z_1 Y_1 Z_1 Y_2 + h Z_1^3
    ] T
    \\
    &= 
\end{align*}
$$

## Mapping to Fermion Model

Below we shall use Jordan-Wigner transformation to map the spin Hamiltonian to fermion Hamiltonian. The boundary terms should be treated very carefully. 

### Periodic Boundary Condition

We first express $S_j^x, S_j^y$ using the raising and lowering operators $S_j^\pm$:

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

Then

$$
\begin{align*}
    &J_x S_j^x S_{j+1}^x 
    + J_y S_j^y S_{j+1}^y 
    \\
    &= \frac{J_x}{4} (S_j^- + S_j^+)(S_{j+1}^- + S_{j+1}^+)
    - \frac{J_y}{4}(S_j^- - S_j^+)(S_{j+1}^- - S_{j+1}^+)
    \\
    &= t(S_j^- S_{j+1}^+ + \underbrace{S_j^+ S_{j+1}^-}_\text{commute})
    + \Delta (S_j^+ S_{j+1}^+ + \underbrace{S_j^- S_{j+1}^-}_\text{commute})
    \\
    &= t(S_j^+ S_{j+1}^- + h.c.)
     + \Delta (S_j^+ S_{j+1}^+ + h.c.)
\end{align*}
$$

where we defined

$$
t \equiv \frac{J_x + J_y}{4} \qquad
\Delta \equiv \frac{J_x - J_y}{4}
$$

Therefore

$$
H_{xy} = - \sum_{j=0}^{N-1} \left[
    t(S_j^+ S_{j+1}^- + h.c.)
    + \Delta (S_j^+ S_{j+1}^+ + h.c.) 
\right] - h \sum_{j=0}^{N-1} S_j^z
$$

Let us now apply Jordan-Wigner transformation to fermionize the model.

- **"Spin Hopping" Terms**

    $$
    \begin{align*}
        \sum_j S_j^+ S_{j+1}^-
        &= \sum_j c_j^\dagger e^{i \phi_j} 
        \underbrace{c_{j+1} e^{-i \phi_{j+1}}}_\text{commute}
        \\
        &= \sum_j c_j^\dagger e^{i (\phi_{j} - \phi_{j+1})} c_{j+1} 
        \\
        &= \sum_j c_j^\dagger e^{-i \pi n_j} c_{j+1} 
    \end{align*}
    $$

    Each term will give nonzero outcome only when $n_j = 0$, but this behavior is the same if the $e^{-i\pi n_j}$ is absent. So we obtain the first conversion (**nearest neighbor (tight-binding) hopping**)

    $$
    \sum_j (S_j^+ S_{j+1}^- + h.c.) 
    = \sum_j (c_j^\dagger c_{j+1} + h.c.)
    $$

- **"Spin Pair" Terms**

    $$
    \begin{align*}
        \sum_j S_j^+ S_{j+1}^+
        &= \sum_j c_j^\dagger e^{i \phi_j} 
        \underbrace{c_{j+1}^\dagger e^{i \phi_{j+1}}}_\text{commute}
        \\
        &= \sum_j c_j^\dagger e^{i (2\phi_j + \pi n_j)} c_{j+1}^\dagger
    \end{align*}
    $$

    But $e^{2 i \phi_j} = \exp(2\pi i \textstyle{\sum_{j < j} n_j}) = 1$, and the extra $e^{i\pi n_j}$ has no effect again. Therefore (such term is related to the **$p$-wave superconductivity**)

    $$
    \sum_j (S_j^+ S_{j+1}^+ + h.c.) 
    = \sum_j (c_j^\dagger c_{j+1}^\dagger + h.c.)
    $$

- **Magnetic Field Terms**
    
    This simply corresponds to the replacement

    $$
    S_j^z = n_j - \frac{1}{2}
    $$

Finally, we obtain the fermion theory

<div class="result">

**Fermionized XY Chain:**

$$
H_F = - \sum_{j=0}^{N-1} \left[
    t(c_j^\dagger c_{j+1} + h.c.)
    + \Delta (c_j^\dagger c_{j+1}^\dagger + h.c.) 
\right] - h \sum_{j=0}^{N-1} \bigg(n_j - \frac{1}{2} \bigg)
$$

</div><br>

We see that the magnetic field $h$ now plays the role of the *chemical potential* $\mu$. 

## Hamiltonian in Momentum Space

To see the energy levels more clearly, we shall go to the momentum space (reciprocal lattice). We transform the Hamiltonian term by term:

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
        \\
        &= -2t \sum_k c_k^\dagger c_k \cos(ka)
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
        \\
        &= -h \sum_k c_k^\dagger c_k 
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
    + X_k
\right]
$$

