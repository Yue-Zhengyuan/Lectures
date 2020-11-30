# The XY Spin Chain

## Model Hamiltonian

The Hamiltonian of the (1+1)D anisotropic **XY spin chain** under external transverse field $h$ is

$$
H = - \sum_{j=0}^{N-1} \left[
    J_x S_j^x S_{j+1}^x 
    + J_y S_j^y S_{j+1}^y 
\right] - h \sum_{j=0}^{N-1} S_j^z
$$

Here we assume periodic boundary condition (PBC):

$$
S_N^a = S_0^a \qquad a=x,y,z
$$

The coefficients $J_x, J_y$ will control whether we have ferromagnetic $(J > 0)$ or anti-ferromagnetic $(J < 0)$ interaction in the $xy$-plane. 

## Mapping to Fermion Model

We first express $S_j^x, S_j^y$ using the raising and lowering operators $S_j^\pm$:

$$
S_j^{\pm} = S_j^x \pm j S_j^y 
\, \Rightarrow \, \left\{
\begin{aligned}
    S_j^x &= \frac{1}{2}(S_j^- + S_j^+)
    \\
    S_j^y &= \frac{j}{2}(S_j^- - S_j^+)
\end{aligned}
\right.
$$

Then

$$
\begin{aligned}
    &J_x S_j^x S_{j+1}^x 
    + J_y S_j^y S_{j+1}^y 
    \\
    &= \frac{J_x}{4} (S_j^- + S_j^+)(S_{j+1}^- + S_{j+1}^+)
    \\ &\quad - \frac{J_y}{4}(S_j^- - S_j^+)(S_{j+1}^- - S_{j+1}^+)
    \\
    &= t(S_j^- S_{j+1}^+ + \underbrace{S_j^+ S_{j+1}^-}_\text{commute})
    + \Delta (S_j^+ S_{j+1}^+ + \underbrace{S_j^- S_{j+1}^-}_\text{commute})
    \\
    &= t(S_j^+ S_{j+1}^- + h.c.)
     + \Delta (S_j^+ S_{j+1}^+ + h.c.)
\end{aligned}
$$

where we defined

$$
t \equiv \frac{J_x + J_y}{4} \qquad
\Delta \equiv \frac{J_x - J_y}{4}
$$

Therefore

$$
H = - \sum_{j=0}^{N-1} \left[
    t(S_j^+ S_{j+1}^- + h.c.)
    + \Delta (S_j^+ S_{j+1}^+ + h.c.) 
\right] - h \sum_{j=0}^{N-1} S_j^z
$$

Let us now apply Jordan-Wigner transformation to fermionize the model.

$$
\begin{aligned}
    \sum_j S_j^+ S_{j+1}^-
    &= \sum_j c_j^\dagger e^{i \phi_j} 
    \underbrace{c_{j+1} e^{-i \phi_{j+1}}}_\text{commute}
    \\
    &= \sum_j c_j^\dagger e^{i (\phi_{j} - \phi_{j+1})} c_{j+1} 
    \\
    &= \sum_j c_j^\dagger e^{-i \pi n_j} c_{j+1} 
\end{aligned}
$$

Each term will give nonzero outcome only when $n_j = 0$, but this behavior is the same if the $e^{-i\pi n_j}$ is absent. So we obtain the first conversion (**nearest neighbor (tight-binding) hopping**)

$$
\sum_j (S_j^+ S_{j+1}^- + h.c.) 
= \sum_j (c_j^\dagger c_{j+1} + h.c.)
$$

Next,

$$
\begin{aligned}
    \sum_j S_j^+ S_{j+1}^+
    &= \sum_j c_j^\dagger e^{i \phi_j} 
    \underbrace{c_{j+1}^\dagger e^{i \phi_{j+1}}}_\text{commute}
    \\
    &= \sum_j c_j^\dagger e^{i (2\phi_j + \pi n_j)} c_{j+1}^\dagger
\end{aligned}
$$

But $e^{2 i \phi_j} = \exp(2\pi i \textstyle{\sum_{j < j} n_j}) = 1$, and the extra $e^{i\pi n_j}$ has no effect again. Therefore (such term is related to the **$p$-wave superconductivity**)

$$
\sum_j (S_j^+ S_{j+1}^+ + h.c.) 
= \sum_j (c_j^\dagger c_{j+1}^\dagger + h.c.)
$$

Finally, we obtain the fermion theory

$$
H = - \sum_{j=0}^{N-1} \left[
    t(c_j^\dagger c_{j+1} + h.c.)
    + \Delta (c_j^\dagger c_{j+1}^\dagger + h.c.) 
\right] - h \sum_{j=0}^{N-1} \bigg(n_j - \frac{1}{2} \bigg)
$$

We see that the magnetic field $h$ now plays the role of the *chemical potential* $\mu$. 

## Exact Solution

### Hamiltonian in Momentum Space

To see the energy levels more clearly, we shall go to the momentum space (reciprocal lattice). We transform the Hamiltonian term by term:

- Tight-binding term

    $$
    \begin{aligned}
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
    \end{aligned}
    $$

- $p$-Wave potential term

    $$
    \begin{aligned}
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
    \end{aligned}
    $$

- Chemical potential term (omitting the constants)

    $$
    \begin{aligned}
        &(-h) \sum_j n_j
        = (-h) \sum_j c_j^\dagger c_j
        \\
        &= -\frac{h}{N} \sum_j \sum_{k,p}
        c_k^\dagger e^{-ikja} c_p e^{ipja}
        \\
        &= -h \sum_k c_k^\dagger c_k 
    \end{aligned}
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
\begin{aligned}
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
\end{aligned}
$$

### Diagonalization: Bogoliubov Transformation

To put this into diagonal form, we further apply the **Bogoliubov transformation**, i.e. make a linear combination of $k$ and $-k$ operators:

$$
\begin{aligned}
    \eta_k &= A_k c_k + B_k c_{-k}^\dagger
    \\
    \eta_{-k} &= C_k c_{-k} + D_k c_k^\dagger
\end{aligned} \qquad
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
\begin{aligned}
    \{\eta_k, \eta_k\} &= \{\eta_k^\dagger, \eta_k^\dagger\} = 0
    \\
    \{\eta_{-k}, \eta_{-k}\} &= \{\eta_{-k}^\dagger, \eta_{-k}^\dagger\} = 0
    \\
    \{\eta_k, \eta_{-k}^\dagger\} &= \{\eta_{-k}, \eta_k^\dagger\} = 0
    \\
    \{\eta_k, \eta_{k}^\dagger\} &= \{\eta_{-k}, \eta_{-k}^\dagger\} = 1
    \\
    \{\eta_{k}, \eta_{-k}\} &= \{\eta_{k}^\dagger, \eta_{-k}^\dagger\} = 0
\end{aligned}
$$

The first three equations are automatically satisfied; the last two equations give us, respectively

$$
\begin{aligned}
    |A_k|^2 + |B_k|^2 &= 1 \\
    |C_k|^2 + |D_k|^2 &= 1
\end{aligned} 
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

