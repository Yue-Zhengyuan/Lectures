<style>
    .remark {
        border-radius: 15px;
        padding: 20px;
        background-color: SeaGreen;
        color: White;
    }
</style>

# The Dirac Equation

## Dirac Spinor

The two spinors can be packed together as the **Dirac spinor**, a 4-component object:

$$
\psi \equiv \begin{bmatrix}
    \psi_L \\[0.5em] \psi_R
\end{bmatrix}, \quad
\bar{\psi} \equiv \begin{bmatrix}
    \psi_L^\dagger & \psi_R^\dagger
\end{bmatrix}
$$

We can then build a (though reducible) 4-dimensional matrix representation $(\frac{1}{2},0) \oplus (0,\frac{1}{2})$ of the Lorentz group. 

According to Dirac, we can generate a (possibly reducible) $n$-dimensional representation of the Lorentz algebra by finding a set of four $n \times n$ matrices $\gamma^\mu$ satisfying the **Dirac algebra**

$$
\{\gamma^\mu, \gamma^\nu\} 
= 2\eta^{\mu \nu} \times \mathbf{1}_{n\times n}
$$

The the Lorentz generators $L^{\mu \nu}$ can be expresses as (now we change the notation to $S^{\mu \nu}$ to remind us that we are dealing with the spinor representation)

$$
S^{\mu \nu} = \frac{i}{4} [\gamma^\mu, \gamma^\nu]
$$

Here we want $n = 4$ (which turns out to be the *minimum* value of $n$ for (3+1)-dimensional spacetime). One explicit choice (the **Weyl (chiral) representation**) corresponds to the combination of Weyl spinors:

$$
\gamma^\mu = \begin{bmatrix}
    0 & \sigma^\mu \\
    \bar{\sigma}^\mu & 0
\end{bmatrix} 
\quad \text{where} \quad
\begin{aligned}
    \sigma^\mu &= (1, \boldsymbol{\sigma}) \\
    \bar{\sigma}^\mu &= (1, -\boldsymbol{\sigma})
\end{aligned}
$$

Each entry is a $2 \times 2$ matrix. 

<div class="remark">

*Remark*: Another choice, which we shall not use here, is the **Majorana representation**

$$
\begin{aligned}
    \gamma^0 &= \begin{bmatrix}
        0 & \sigma^2 \\ \sigma^2 & 0
    \end{bmatrix} &\qquad
    \gamma^1 &= \begin{bmatrix}
        i\sigma^3 & 0 \\ 0 & i\sigma^3
    \end{bmatrix}
    \\
    \gamma^2 &= \begin{bmatrix}
        0 & -\sigma^2 \\ \sigma^2 & 0
    \end{bmatrix} &\qquad
    \gamma^3 &= \begin{bmatrix}
        -i\sigma^1 & 0 \\ 0 & -i\sigma^1
    \end{bmatrix}
\end{aligned}
$$

It is *unitarily equivalent* to the Weyl representation. 

</div><br>

In the Weyl representation:

- The rotation and boost generators are

    $$
    \begin{aligned}
        &\text{Rotation:} &\quad
        S^{ab} &= \frac{i}{4}[\gamma^a, \gamma^b]
        = \frac{1}{2} \epsilon^{abc} \begin{bmatrix}
            \sigma^c & 0 \\ 0 & \sigma^c
        \end{bmatrix}
        \\[1em]
        &\text{Boost:} &\quad
        S^{0a} &= \frac{i}{4}[\gamma^0, \gamma^a]
        = \frac{i}{2} \begin{bmatrix}
            -\sigma^a & 0 \\ 0 & \sigma^a
        \end{bmatrix}
    \end{aligned}
    $$

    This block-diagonal structure is quite expected: we are simply packing $\psi_L, \psi_R$ together, and we know that the rotation and the boost generators for the two Weyl spinors are exactly

    $$
    \begin{aligned}
        \psi_L: &\quad
        S^{ab} = \epsilon^{abc} J^c 
        = \frac{1}{2} \epsilon^{abc} \sigma^c , \quad
        K^a = -\frac{i}{2} \sigma^a
        \\[1em]
        \psi_R: &\quad
        S^{ab} = \epsilon^{abc} J^c 
        = \frac{1}{2} \epsilon^{abc} \sigma^c , \quad
        K^a = \frac{i}{2} \sigma^a
    \end{aligned}
    $$

    <div class="remark">

    *Remark*: By direct calculation

    $$
    (S^{ab})^\dagger = S^{ab} \qquad
    (S^{0a})^\dagger = -S^{0a}
    $$

    Again, the boost generators are not Hermitian. Then only rotations are unitary, while boosts are not. 

    </div><br>

- The Dirac Lagrangian can be written as
    
    $$
    \mathcal{L} = \bar{\psi} (i \gamma^\mu \partial_\mu - m) \psi
    $$

    The inner product of the form $\gamma^\mu \mathcal{O}_\mu$ will appear frequently, and people adopt the shorthand $\cancel{\mathcal{O}}$ (the **slash notation**). Then

    $$
    \mathcal{L} = \bar{\psi} (i \cancel{\partial} - m) \psi
    $$

## Dirac Field Bilinears

The infinitesimal transformations matrices in the 4-vector representation and the Weyl representation are

$$
\begin{aligned}
    &\text{Vector:} &\quad
    {\Lambda^\mu}_\nu 
    &= \big(
        1 - \frac{i}{2} \omega_{\alpha \beta} L^{\alpha \beta}
    {\big)^\mu}_\nu
    \\
    &\text{Weyl:} &\quad
    {(\Lambda_s)^\mu}_\nu 
    &= \big(
        1 - \frac{i}{2} \omega_{\alpha \beta} S^{\alpha \beta}
    {\big)^\mu}_\nu
\end{aligned}
$$

It can be verified that (the indices corresponding to matrix multiplication is omitted)

$$
\Lambda_s^{-1} \gamma^\mu \Lambda_s = {\Lambda^\mu}_\nu \gamma^\nu
$$


