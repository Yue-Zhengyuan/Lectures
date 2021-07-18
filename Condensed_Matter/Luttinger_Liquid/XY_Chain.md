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

# The XY Spin Chain

*References*:

- [Strongly Correlated Systems
in Solid State Physics](http://www.thp.uni-koeln.de/~as/Mypage/PSfiles/Korrel/korrel.pdf)
- [PhD Thesis of Zou Yijian](https://uwspace.uwaterloo.ca/handle/10012/16049)

*Notes on notations*:

Sometimes we also express the Pauli matrices as $(X_i, Y_i, Z_i) \equiv (\sigma_i^x, \sigma_i^y, \sigma_i^z)$.

## XY Chain with Different Boundary Conditions

**Periodic boundary condition (PBC)** can intuitively be applied to any spin chain by imposing on the spin operators the requirement

$$
\sigma_{j+N}^a = \sigma_j^a 
$$

However, the **anti-periodic boundary condition (APBC)** can only be imposed on spin chains with $\mathbb{Z}_2$ symmetry (symmetry with respect to the flip of all spins). 

Assume that both the PBC Hamiltonian and the $\mathbb{Z}_2$ symmetry generator are combinations of local term:

$$
H^P = \sum_{j=1}^N H_j, \quad
\mathcal{Z} \equiv \prod_{j=1}^N \mathcal{Z}_j
$$

which is indeed the case for many physically relevant models. For XY chain

<div class="result">

**XY spin chain:**

$$
\begin{align*}
    H_j &= - \left[
        \frac{1+\gamma}{2} \sigma_j^x \sigma_{j+1}^x 
        + \frac{1-\gamma}{2} \sigma_j^y \sigma_{j+1}^y 
        + h \sigma_j^z
    \right]
    \\
    \mathcal{Z}_i &= Z_i
\end{align*} \quad (j = 1,...,N)
$$

</div><br>

----

*Verify the claimed $\mathcal{Z}_i$*: Using the fact that

- The Pauli matrices are both Hermitian and unitary
- The Pauli matrices square to identity
- The commutators $[\sigma^a_m, \sigma^b_n] = \delta_{mn} \times 2i \epsilon^{abc} \sigma^c_m$

Then

$$
\begin{align*}
    \mathcal{Z} X_j X_{j+1} \mathcal{Z}^\dagger
    &= \bigg[ \prod_{m=1}^N Z_m \bigg]
    X_j X_{j+1}
    \bigg[ \prod_{n=1}^N Z_n \bigg]^\dagger
    \\
    &= Z_j Z_{j+1} X_j X_{j+1} Z_{j+1} Z_j
    \\
    &= Z_j X_j Z_j Z_{j+1} X_{j+1} Z_{j+1} 
    \\
    &= (-X_j) (-X_{j+1}) = X_j X_{j+1}
    \\
    \text{Similarly} \quad&
    \\
    \mathcal{Z} Y_j Y_{j+1} \mathcal{Z}^\dagger
    &= Z_j Y_j Z_j Z_{j+1} Y_{j+1} Z_{j+1} 
    \\
    &= (-Y_j) (-Y_{j+1}) = Y_j Y_{j+1}
    \\
    \text{And obviously} &
    \\
    \mathcal{Z} Z_j \mathcal{Z}^\dagger &= Z_j
\end{align*}
$$

Thus the local Hamiltonian of XY chain is invariant under the $\mathbb{Z}_2$ transformation:

$$
\mathcal{Z} H_j \mathcal{Z}^\dagger = H_j \qquad \blacksquare
$$

----

Then we introduce the lattice translation operator $\mathcal{T}$ and its **twisted** counterpart $\tilde{\mathcal{T}} \equiv \mathcal{Z}_1 \mathcal{T}$. The action of $\mathcal{T}$ on the local $H_j$ is defined as

$$
\mathcal{T}
$$

For the XY chain, the Hamiltonian can be written as the sum of the following local Hamiltonian



For convenience we write $H$ in terms of the pauli matrices $\sigma^a$ instead of the spin 1/2 operators $S^a = \sigma^a/2$. 

More formally, let $\mathcal{T}$ be the (unitary) lattice translation operator (by one site), whose action on the local Hamiltonian is

$$
\mathcal{T} H_j \mathcal{T}^\dagger = H_{j+1} \quad
(j = 1, ... N)
$$

We then *define* 

<div class="result">

**PBC/APBC Hamiltonian:**

$$
H^P = \sum_{j=1}^N \mathcal{T}^{j-1} H_1 (\mathcal{T}^\dagger)^{j-1}
$$

</div><br>

Then the PBC Hamiltonian will be invariant under lattice translation:

$$
\mathcal{T} H \mathcal{T}^\dagger
= \sum_{j=1}^N \mathcal{T} H_j \mathcal{T}^\dagger
= \sum_{j=2}^{N+1} \mathcal{T} H_j \mathcal{T}^\dagger
= H
$$

An alternative expression for the PBC Hamiltonian is then



### Anti-Periodic Boundary Condition

The anti-periodic boundary condition (APBC) can only be applied to spin chains with $\mathbb{Z}_2$ symmetry . The XY chain is such a model, with the $\mathbb{Z}_2$ generator

$$
\mathcal{Z} = \prod_{j=1}^N Z_j
$$

and the local Hamiltonian 

$$
H_j = -\left[
    \frac{1+\gamma}{2} X_j X_{j+1}
    + \frac{1-\gamma}{2} Y_j Y_{j+1} + h Z_j
\right]
$$



The we can define the **twisted** lattice translation operator

$$
\tilde{\mathcal{T}} \equiv Z_1 \mathcal{T}
$$

The Hamiltonian of XY chain with APBC or PBC can

## Mapping to Fermion Model

Below we shall use Jordan-Wigner transformation to map the spin Hamiltonian to fermion Hamiltonian. The boundary terms should be treated very carefully. 

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

