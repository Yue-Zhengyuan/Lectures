# The Lorentz Group

## Classification of Lorentz Transformations

By definition, the spacetime interval is invariant under the Lorentz transformation $\Lambda_{\mu \nu}$:

$$
\begin{aligned}
    ds^2 &= \eta_{\mu \nu} dx^\mu dx^\nu
    \\
    &= \eta_{\rho \sigma} dx'^\rho dx'^\sigma
    \\
    &= \eta_{\rho \sigma} 
    ({\Lambda^\rho}_\mu dx^\mu)
    ({\Lambda^\sigma}_\nu dx^\nu)
\end{aligned}
$$

Here $\eta_{\mu \nu} = \operatorname{diag}(1,-1,-1,-1)$ is the flat spacetime metric, which happens to be equal to its inverse $\eta^{\mu \nu}$. Therefore, the matrix $\Lambda_{\mu \nu}$ should satisfy the constraint

$$
\eta_{\rho \sigma} {\Lambda^\rho}_\mu {\Lambda^\sigma}_\nu
= \eta_{\mu \nu}
$$

All transformations satisfying the above constraint form the **Lorentz group**. It turns out that

$$
\text{Lorentz group} = \text{Rotation} + \text{Boost} + T + P
$$

where $T$ is **time reversal** and $P$ is **parity**:

$$
{T^\mu}_\nu = \begin{bmatrix}
    -1 & 0 \\
    0 & \mathbf{1}
\end{bmatrix} \qquad
{P^\mu}_\nu = \begin{bmatrix}
    1 & 0 \\
    0 & -\mathbf{1}
\end{bmatrix} \qquad
$$

### Proper and Improper Transformations

Here we shall not deal with $L$ and $P$, i.e. restricting us to the **proper Lorentz group** $SO(1,3)$:

$$
SO(1,3) = \text{Rotation} + \text{Boost}
$$

Transformations in this sector of the full Lorentz group has *unit determinant*:

$$
\det \Lambda = 1
$$

### Orthochronous and Non-orthochronous Transformations



## Generator of Proper Lorentz Transformation 

Now consider a *proper* infinitesimal Lorentz transformation, which is **connected** to the identity. Its generator $L_{\mu \nu}$ (the factor $-i$ is somewhat artificial) is defined by:

$$
{\Lambda^\mu}_\nu = \delta^\mu_\nu - i {L^\mu}_\nu
$$

or using subscripts only

$$
\Lambda_{\mu \nu} = \eta_{\mu \nu} - i L_{\mu \nu}
$$

Here $L \ll 1$ is the parameters controlling the "amount" of the transformation. Plug it into the constraint above and keep only terms up to $O(L)$:

$$
\begin{aligned}
    \eta_{\mu \nu}
    &=\eta_{\rho \sigma} {\Lambda^\rho}_\mu {\Lambda^\sigma}_\nu
    \\
    &=\eta^{\rho \sigma} \Lambda_{\rho \mu} \Lambda_{\sigma \nu}
    \\
    &= \eta^{\rho \sigma} (
        \eta_{\rho \mu} 
        - i L_{\rho \mu}
    ) (
        \eta_{\sigma \nu} 
        - i L_{\sigma \nu}
    )
    \\
    &= \eta^{\rho \sigma} \eta_{\rho \mu} \eta_{\sigma \nu} 
    - i (
        \eta^{\rho \sigma} \eta_{\rho \mu} L_{\sigma \nu}
        + \eta^{\rho \sigma} \eta_{\sigma \nu} L_{\rho \mu}
    ) + O(L^2)
    \\
    &= \eta_{\mu \nu}
    - i (L_{\mu \nu} + L_{\nu \mu}) 
    + O(L^2)
\end{aligned}
$$

This indicates that $L_{\mu \nu}$ is an antisymmetric tensor:

$$
L_{\mu \nu} = - L_{\mu \nu}
$$

An arbitrary $4 \times 4$ antisymmetric matrix can be built from the "most basic" ones: let $\mathcal{L}^{\alpha \beta}$ be the "basic" antisymmetric matrix which has $1$ at the position $(\alpha, \beta)$ and $-1$ at the position $(\beta, \alpha)$, i.e.

$$
\mathcal{L}^{\alpha \beta}_{\mu \nu} 
= \delta^\alpha_\mu \delta^\beta_\nu 
- \delta^\alpha_\nu \delta^\beta_\mu
\qquad
\alpha,\beta = 0,1,2,3
$$

But since Lorentz transformation matrices are real, and we picked out a factor of $i$, the generators $L$ should be purely imaginary. This means that $L$ is in fact *Hermitian*. Then we modify the construction of basic antisymmetric matrices a little bit to obtain the generators of the Lorentz transformation:

$$
L^{\alpha \beta}_{\mu \nu} 
= i (
    \delta^\alpha_\mu \delta^\beta_\nu 
    - \delta^\alpha_\nu \delta^\beta_\mu
)
$$

which has $i$ at the position $(\alpha, \beta)$ and $-i$ at the position $(\beta, \alpha)$

With this construction, we notice that

$$
L^{\alpha \beta} = - L^{\beta \alpha}
$$

Thus there are in fact only 

$$
\frac{n (n-1)}{2} \quad 
(n = \text{spacetime dimension})
$$

linearly independent such basic generators, as can be seen by requiring $\alpha < \beta$. Thus a general infinitesimal Lorentz transformation can be represented as

$$
L_{\mu \nu} 
= \sum_{\alpha < \beta} 
\omega_{\alpha \beta} L^{\alpha \beta}_{\mu \nu}
= \frac{1}{2} \omega_{\alpha \beta} L^{\alpha \beta}_{\mu \nu}
$$

where we have shown explicitly the infinitesimal parameters $\omega_{\alpha \beta} \ll 1$. In the last line we release the constraint $\alpha < \beta$ by setting $\omega_{\alpha \beta}$ to be also an antisymmetric matrix, and introducing the factor $1/2$ to cancel the repeated counting. 

Finally, a general infinitesimal Lorentz transformation (or more rigorously, a *proper* Lorentz transformation **connected with identity**) can be written as

$$
\Lambda_{\mu \nu} 
= \eta_{\mu \nu} 
- \frac{1}{2} i \omega_{\alpha \beta} L^{\alpha \beta}_{\mu \nu}
$$

## The Lorentz Algebra

The commutation relation between the generators $L^{\alpha \beta}$ is

$$
[L^{\mu \nu}, L^{\rho \sigma}]
= i (
    \eta^{\nu \rho} L^{\mu \sigma}
    + \eta^{\mu \sigma} L^{\nu \rho}
    - \eta^{\mu \rho} L^{\nu \sigma}
    - \eta^{\nu \sigma} L^{\mu \rho}
)
$$

This is called the **Lorentz algebra** $so(1,3)$. Although this algebra is derived using the matrix representation with the 4-vectors as the basis objects, it is an *inherent* property of the Lorentz transformations, independent of the representation. 

----

*Proof*:

$$
\begin{aligned}
    \text{LHS}_{\alpha \beta}
    &= L^{\mu \nu}_{\alpha \gamma} L^{\rho \sigma}_{\gamma \beta}
    - L^{\rho \sigma}_{\alpha \gamma} L^{\mu \nu}_{\gamma \beta}
    \\
    &= - (
        \delta^\mu_\alpha \delta^\nu_\gamma 
        - \delta^\mu_\gamma \delta^\nu_\alpha
    ) (
        \delta^\rho_\gamma \delta^\sigma_\beta 
        - \delta^\rho_\beta \delta^\sigma_\gamma
    ) \\ &\quad + (
        \delta^\rho_\alpha \delta^\sigma_\gamma 
        - \delta^\rho_\gamma \delta^\sigma_\alpha
    ) (
        \delta^\mu_\gamma \delta^\nu_\beta 
        - \delta^\mu_\beta \delta^\nu_\gamma
    )
    \\
    &= - \delta^\mu_\alpha \delta^\nu_\gamma 
    \delta^\rho_\gamma \delta^\sigma_\beta 
    + \delta^\mu_\alpha \delta^\nu_\gamma 
    \delta^\rho_\beta \delta^\sigma_\gamma
    + \delta^\mu_\gamma \delta^\nu_\alpha
    \delta^\rho_\gamma \delta^\sigma_\beta 
    - \delta^\mu_\gamma \delta^\nu_\alpha
    \delta^\rho_\beta \delta^\sigma_\gamma
    \\ &\quad 
    + \delta^\rho_\alpha \delta^\sigma_\gamma 
    \delta^\mu_\gamma \delta^\nu_\beta 
    - \delta^\rho_\alpha \delta^\sigma_\gamma 
    \delta^\mu_\beta \delta^\nu_\gamma
    - \delta^\rho_\gamma \delta^\sigma_\alpha
    \delta^\mu_\gamma \delta^\nu_\beta 
    + \delta^\rho_\gamma \delta^\sigma_\alpha
    \delta^\mu_\beta \delta^\nu_\gamma
    \\
    &= \eta^{\nu \rho} (
        - \delta^\mu_\alpha \delta^\sigma_\beta 
        + \delta^\mu_\beta \delta^\sigma_\alpha
    ) + \eta^{\nu \sigma} (
        - \delta^\rho_\alpha \delta^\mu_\beta
        + \delta^\rho_\beta \delta^\mu_\alpha
    ) \\ &\quad + \eta^{\mu \rho} (
        - \delta^\sigma_\alpha \delta^\nu_\beta
        + \delta^\sigma_\beta \delta^\nu_\alpha
    )
    + \eta^{\mu \sigma} (
        - \delta^\nu_\alpha \delta^\rho_\beta
        + \delta^\nu_\beta \delta^\rho_\alpha
    )
    \\
    &= i (
        \eta^{\nu \rho} L^{\mu \sigma}_{\alpha\beta}
        + \eta^{\nu \sigma} L^{\rho \mu}_{\alpha\beta}
        + \eta^{\mu \rho} L^{\sigma \nu}_{\alpha\beta}
        + \eta^{\mu \sigma} L^{\nu \rho}_{\alpha\beta}
    )
    \\
    &= i (
        \eta^{\nu \rho} L^{\mu \sigma}_{\alpha\beta}
        + \eta^{\mu \sigma} L^{\nu \rho}_{\alpha\beta}
        - \eta^{\mu \rho} L^{\nu \sigma}_{\alpha\beta}
        - \eta^{\nu \sigma} L^{\mu \rho}_{\alpha\beta}
    ) 
    \\
    &= \text{RHS}_{\alpha \beta}
    \quad \blacksquare
\end{aligned}
$$

----

*Remark*: This algebra can also be verified using another representation of the generators

$$
L^{\rho \sigma}
= i \left(x^{\rho} \partial^{\sigma}-x^{\sigma} \partial^{\rho} \right)
$$

## Rotation and Boost Generators

In (3+1)D spacetime, there are 6 linearly independent Lorentz transformation generators:
    
$$
L^{\alpha \beta}_{\mu \nu} 
= i (
    \delta^\alpha_\mu \delta^\beta_\nu 
    - \delta^\alpha_\nu \delta^\beta_\mu
) \qquad
0 \le \alpha < \beta \le 3
$$

It turns out that these generators $L^{\alpha \beta}$ are no other than the 3 **rotation** generators $J_a$ and 3 **boost** generators $K_a$ ($a = 1,2,3$ or $x,y,z$). 

### Rotation

The 3D rotation matrices around $x, y, z$ axes are, respectively (promoted as $4 \times 4$ matrices)

$$
\begin{aligned}
    R_x(\alpha) 
    &= \begin{bmatrix}
        1 & 0 & 0 & 0 \\
        0 & 1 & 0 & 0 \\
        0 & 0 & \cos  \alpha  & -\sin  \alpha  \\
        0 & 0 & \sin  \alpha  & \cos  \alpha
    \end{bmatrix} \xrightarrow{\alpha \to 0}
    \begin{bmatrix}
        1 & 0 & 0 & 0 \\
        0 & 1 & 0 & 0 \\
        0 & 0 & 1  & -\alpha  \\
        0 & 0 & \alpha  & 1
    \end{bmatrix}
    \\[3em]
    R_y(\alpha)
    &= \begin{bmatrix}
        1 & 0 & 0 & 0 \\
        0 & \cos  \alpha  & 0 & \sin  \alpha  \\
        0 & 0 & 1 & 0 \\
        0 & -\sin  \alpha  & 0 & \cos  \alpha
    \end{bmatrix} \xrightarrow{\alpha \to 0}
    \begin{bmatrix}
        1 & 0 & 0 & 0 \\
        0 & 1  & 0 & \alpha  \\
        0 & 0 & 1 & 0 \\
        0 & -\alpha  & 0 & 1
    \end{bmatrix}
    \\[3em]
    R_z(\alpha)
    &= \begin{bmatrix}
        1 & 0 & 0 & 0 \\
        0 & \cos  \alpha  & -\sin  \alpha  & 0 \\
        0 & \sin  \alpha  & \cos  \alpha  & 0 \\
        0 & 0 & 0 & 1
    \end{bmatrix} \xrightarrow{\alpha \to 0}
    \begin{bmatrix}
        1 & 0 & 0 & 0 \\
        0 & 1  & -\alpha  & 0 \\
        0 & \alpha  & 1  & 0 \\
        0 & 0 & 0 & 1
    \end{bmatrix}
\end{aligned}
$$

Using $R_a = 1 - i \alpha J_a \, (a = x,y,z)$, we obtain

$$
\begin{aligned}
    J_1 &= \begin{bmatrix}
        0 & 0 & 0 & 0 \\
        0 & 0 & 0 & 0 \\
        0 & 0 & 0 & -i \\
        0 & 0 & i & 0
    \end{bmatrix} = L^{32} = -L^{23}
    \\[3em]
    J_2 &= \begin{bmatrix}
        0 & 0 & 0 & 0 \\
        0 & 0 & 0 & i \\
        0 & 0 & 0 & 0 \\
        0 & -i & 0 & 0
    \end{bmatrix} = L^{13} = -L^{31}
    \\[3em]
    J_3 &= \begin{bmatrix}
        0 & 0 & 0 & 0 \\
        0 & 0 & -i & 0 \\
        0 & i & 0 & 0 \\
        0 & 0 & 0 & 0
    \end{bmatrix} = L^{21} = -L^{12}
\end{aligned}
$$

### Boost

The 3+1D boost matrices along $x, y, z$ axes are, respectively

$$
\begin{aligned}
    B_x(\beta) &= \begin{bmatrix}
        \cosh \beta & \sinh \beta & 0 & 0 \\
        \sinh \beta & \cosh \beta & 0 & 0 \\
        0 & 0 & 1 & 0 \\
        0 & 0 & 0 & 1
    \end{bmatrix} \xrightarrow{\beta \to 0}
    \begin{bmatrix}
        1 & \beta & 0 & 0 \\
        \beta & 1 & 0 & 0 \\
        0 & 0 & 1 & 0 \\
        0 & 0 & 0 & 1
    \end{bmatrix}
    \\[3em]
    B_y(\beta) &= \begin{bmatrix}
        \cosh \beta & 0 & \sinh \beta & 0 \\
        0 & 1 & 0 & 0 \\
        \sinh \beta & 0 & \cosh \beta & 0 \\
        0 & 0 & 0 & 1
    \end{bmatrix} \xrightarrow{\beta \to 0}
    \begin{bmatrix}
        1 & 0 & \beta & 0 \\
        0 & 1 & 0 & 0 \\
        \beta & 0 & 1 & 0 \\
        0 & 0 & 0 & 1
    \end{bmatrix}
    \\[3em]
    B_z(\beta) &= \begin{bmatrix}
        \cosh \beta & 0 & 0 & \sinh \beta \\
        0 & 1 & 0 & 0 \\
        0 & 0 & 1 & 0 \\
        \sinh \beta & 0 & 0 & \cosh \beta
    \end{bmatrix} \xrightarrow{\beta \to 0}
    \begin{bmatrix}
        1 & 0 & 0 & \beta \\
        0 & 1 & 0 & 0 \\
        0 & 0 & 1 & 0 \\
        \beta & 0 & 0 & 1
    \end{bmatrix}
\end{aligned}
$$

Using $B_a = 1 - i\beta K_a \, (a = x,y,z)$, we obtain

$$
K_1 = \begin{bmatrix}
    0 & i & 0 & 0 \\
    i & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0
\end{bmatrix}, 
K_2 = \begin{bmatrix}
    0 & 0 & i & 0 \\
    0 & 0 & 0 & 0 \\
    i & 0 & 0 & 0 \\
    0 & 0 & 0 & 0
\end{bmatrix}, 
K_3 = \begin{bmatrix}
    0 & 0 & 0 & i \\
    0 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 \\
    i & 0 & 0 & 0
\end{bmatrix}
$$

At first sight, the $K_a$ matrices appear to be *symmetric*, which is troublesome. But in fact the matrices above refers to ${(K_a)^\mu}_\nu$ (one upper index and one lower index), while explicit anti-symmetry requires all lower index (or all upper index). Bringing down the first index using

$$
(K_a)_{\mu \nu} = \eta_{\mu \rho} {(K_a)^\rho}_\nu
$$

we see that

$$
\begin{aligned}
    K_1 &= \begin{bmatrix}
        0 & i & 0 & 0 \\
        -i & 0 & 0 & 0 \\
        0 & 0 & 0 & 0 \\
        0 & 0 & 0 & 0
    \end{bmatrix} = L^{01} = -L^{10}
    \\[3em]
    K_2 &= \begin{bmatrix}
        0 & 0 & i & 0 \\
        0 & 0 & 0 & 0 \\
        -i & 0 & 0 & 0 \\
        0 & 0 & 0 & 0
    \end{bmatrix} = L^{02} = -L^{20}
    \\[3em]
    K_3 &= \begin{bmatrix}
        0 & 0 & 0 & i \\
        0 & 0 & 0 & 0 \\
        0 & 0 & 0 & 0 \\
        -i & 0 & 0 & 0
    \end{bmatrix} = L^{03} = -L^{30}
\end{aligned}
$$

This problem does not exist for the rotation generators, since they do not involve the transformation of time. 

Now we can formally write $L^{\alpha \beta}$ as a $4\times 4$ matrix:

$$
L^{\alpha \beta} =\begin{bmatrix}
    0 & K_1 & K_2 & K_3 \\[0.3em]
    -K_1 & 0 & -J_3 & J_2 \\[0.3em]
    -K_2 & J_3 & 0 & -J_1 \\[0.3em]
    -K_3 & -J_2 & J_1 & 0
\end{bmatrix}
$$

### Finite Transformations

A general infinitesimal *proper* Lorentz transformation can be written using $J_a, K_a$ as (summation over $a$ is assumed)

$$
\begin{aligned}
    \Lambda_{\mu \nu} 
    &= \eta_{\mu \nu} 
    - i \theta_a J_a - i \beta_a K_a
    \\
    &= \eta_{\mu \nu} 
    - i \theta \cdot \mathbf{J} - i \beta \cdot \mathbf{K}
\end{aligned}
$$

The finite transformation is then obtained by exponentiation:

$$
\Lambda = \exp(- i \theta_a J_a - i \beta_a K_a)
$$

## Representations of the Lorentz Group

From direct calculation, the commutation relations of the six generators (the Lorentz algebra $so(1,3)$) can be simplified as follows: 

$$
\begin{aligned}
    [J_a, J_b] &= i \epsilon_{abc} J_c
    \\
    [K_a, K_b] &= -i \epsilon_{abc} K_c
    \\
    [J_a, K_b] &= i \epsilon_{abc} K_c
\end{aligned} \qquad
a,b,c = 1,2,3
$$

If we define

$$
J_a^\pm \equiv \frac{1}{2}(J_a \pm iK_a) \qquad
a = 1,2,3
$$

we can separate the Lorentz algebra into two commuting sub-algebras ("independent pieces")

$$
\begin{aligned}
    [J_a^+, J_b^+] &= i\epsilon_{abc} J_c^+
    \\
    [J_a^-, J_b^-] &= i\epsilon_{abc} J_c^-
    \\
    [J_a^+, J_b^-] &= 0
\end{aligned} \qquad
a,b,c = 1,2,3
$$

The sub-algebra is exactly the $su(2)$ (or $so(3)$) algebra. Therefore

$$
so(1,3) = su(2) \oplus su(2)
$$

It is known that irreducible representations (irreps) of $SU(2)$ is labeled by a half-integer $j$ (the corresponding matrix dimension if $2j+1$). Thus the irreps of the Lorentz group can be labeled by two half-integers $(j_+, j_-)$.
