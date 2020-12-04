<style>
    .remark {
        border-radius: 15px;
        padding: 20px;
        background-color: SeaGreen;
        color: White;
    }
</style>

# Spinor Representation

## The Weyl Spinor

The **Weyl Spinors** are 2-component basis objects of the $(\frac{1}{2},0)$ and $(0, \frac{1}{2})$ irreps of the Lorentz group. Recall that the 2-dimensional irrep of $SU(2)$ are generated by the spin operators $S^a = \sigma^a / 2$; therefore, for these two representations of the Lorentz group, the generators $J_+, J_-$ are represented by

$$
\begin{aligned}
    \left(\frac{1}{2}, 0\right): &\quad
    J^a_+ = \frac{1}{2} \sigma^a , \quad
    J^a_- = 0
    \\[1em]
    \left(0, \frac{1}{2}\right): &\quad
    J^a_+ = 0 , \quad
    J^a_- = \frac{1}{2} \sigma^a
\end{aligned} \quad
(a = 1,2,3)
$$

Here $\sigma^a$ are the Pauli matrices. Recall that

$$
J^a_\pm = \frac{1}{2}(J^a \pm iK^a)
\, \Rightarrow \, \left\{
\begin{aligned}
    J^a &= J^a_+ + J^a_-
    \\
    K^a &= -i(J^a_+ - J^a_-)
\end{aligned} \right.
$$

Then the rotation and boost generators are

$$
\begin{aligned}
    \left(\frac{1}{2}, 0\right): &\quad
    J^a = \frac{1}{2} \sigma^a , \quad
    K^a = -\frac{i}{2} \sigma^a
    \\[1em]
    \left(0, \frac{1}{2}\right): &\quad
    J^a = \frac{1}{2} \sigma^a , \quad
    K^a = \frac{i}{2} \sigma^a
\end{aligned}
$$

The 2 spinors corresponding to these two representations are called the **left/right-handed** Weyl spinors, denoted by $\psi_L, \psi_R$. Their transformations under finite rotation $\theta^a$ and boost $\beta^a$ are

$$
\begin{aligned}
    \psi_L &\to \exp(- i \theta^a J^a - i \beta^a K^a) \psi_L
    \\ &= \underbrace{\exp \left(
        - \frac{i}{2} \theta^a \sigma^a 
        - \frac{1}{2} \beta^a \sigma^a
    \right)}_{\equiv U_L} \psi_L
    \\[3em]
    \psi_R &\to \exp(- i \theta^a J^a - i \beta^a K^a) \psi_R
    \\ &= \underbrace{\exp \left(
        - \frac{i}{2} \theta^a \sigma^a 
        + \frac{1}{2} \beta^a \sigma^a
    \right)}_{\equiv U_R} \psi_R    
\end{aligned}
$$

The infinitesimal versions are

$$
\begin{aligned}
    \delta \psi_L 
    &= - \frac{i \theta^a + \beta^a}{2}
    \sigma^a \psi_L
    \\[1em]
    \delta \psi_R 
    &= - \frac{i \theta^a - \beta^a}{2}
    \sigma^a \psi_R
\end{aligned}
$$

with the Hermitian conjugate

$$
\begin{aligned}
    \delta \psi_L^\dagger 
    &= - \frac{-i \theta^a + \beta^a}{2}
    \sigma^a \psi_L^\dagger
    \\[1em]
    \delta \psi_R^\dagger 
    &= - \frac{- i \theta^a - \beta^a}{2}
    \sigma^a \psi_R^\dagger
\end{aligned}
$$

<div class="remark">

*Remark*: the transformation operators $U_L, U_R$ are *not unitary*, since the boost generators $K^a$ are not Hermitian:

$$
U_L^\dagger = \exp \left(
    + \frac{i}{2} \theta^a \sigma^a 
    - \frac{1}{2} \beta^a \sigma^a
\right) = U_R^{-1}
\\
U_R^\dagger = \exp \left(
    + \frac{i}{2} \theta^a \sigma^a 
    + \frac{1}{2} \beta^a \sigma^a
\right) = U_L^{-1}
$$

</div><br>

## The Dirac Lagrangian

The field theory of spinor fields should involve Lorentz-invariant Lagrangian. The simplest choice with dynamics is the **Dirac Lagrangian**:

$$
\mathcal{L} = i (
    \psi_R^\dagger \sigma^\mu \partial_\mu \psi_R
    + \psi_L^\dagger \bar{\sigma}^\mu \partial_\mu \psi_L
) - m(
    \psi_R^\dagger \psi_L
    + \psi_L^\dagger \psi_R
)
$$

The parameter $m$ is called the **Dirac mass**. Here we have defined

$$
\sigma^\mu \equiv (1, \boldsymbol{\sigma}) \qquad
\bar{\sigma}^\mu \equiv (1, -\boldsymbol{\sigma})
$$

We now verify that each term in the Lagrangian is indeed a Lorentz scalar.

----

*Proof*:


----

## $(\frac{1}{2},\frac{1}{2})$ Representation of Lorentz Group