## Differential Forms

### Permutation

*Definition*:

- **Symmetrizer $\mathcal{S}$**
- **Anti-Symmetrizer $\mathcal{A}$**

### Differential Forms

*Definition*:

- **Differential form of order $r$ ($r$-form)**: a *totally anti-symmetric* tensor of type $(0,r)$ (sending $r$ (tangent) vectors to a number)
    
    *Special case*: We already know what is 1-form; they are of the form
        
    $$
    \omega = \omega_\mu dx^\mu
    $$

    In particular, the differentials $dx^\mu$ themselves are 1-forms. 

    - **0-form**: we formally define functions in $\mathcal{F}(M)$ as 0-forms

- **Wedge product of 1-forms**: *totally anti-symmetric* tensor product of the involved 1-forms

    $$
    dx^{\mu_1} \wedge \cdots \wedge dx^{\mu_r}
    \equiv \sum_{P \in S_r} \text{sgn}(P) \,
    dx^{\mu_{P(1)}} \otimes \cdots \otimes dx^{\mu_{P(r)}}
    $$

    *Remark*: 
    - The wedge product of $r$ 1-forms is an $r$-form.
    
    - All $r$-forms of the above form at point $p \in M$ form a basis of the vector space of $r$-forms (denoted by $\Omega^r_p(M)$)
    
    - If $\dim{M} = m$, we can easily obtain

        $$
        \dim{\Omega^r_p(M)} =
        \begin{pmatrix}
            m \\ r
        \end{pmatrix}
        \equiv \frac{m!}{r!(m-r)!}
        $$

        since we are *selecting* $r$ 1-forms from the $m$ dual bases from $T_p^* M$.
    
    - An arbitrary $r$-form $\omega \in \Omega^r_p(M)$ can be written as linear superposition of the basis $r$-forms:

        $$
        \omega = \frac{1}{r!} \omega_{\mu_1 ... \mu_r}
        dx^{\mu_1} \wedge \cdots \wedge dx^{\mu_r}
        $$

        where $\omega_{\mu_1 ... \mu_r}$ is also *totally anti-symmetric* to keep LHS invariant.

    *Properties of wedge product*:

- **Exterior product of two differential forms**: let $\omega \in \Omega^r_p(M), \xi \in \Omega^s_p(M)$be two differential forms; the wedge product of them (denoted by $\omega \wedge \xi$) is defined as an element in $\Omega^{r+s}_p(M)$, which acts on vectors $V_i \in T_p M$ in the following way:

    $$
    \begin{aligned}
        &(\omega \wedge \xi)(V_1, ..., V_{r+s})
        \\ & \quad =
        \frac{1}{q! r!}\sum_{P \in S_{q+r}} \text{sgn}(P) \,
        \omega(V_{P(1)}, ..., V_{P(r)})
        \xi(V_{P(r+1)}, ..., V_{P(r+s)})
    \end{aligned}
    $$

    *Properties*:

    Let $\omega \in \Omega^q_p(M), \xi \in \Omega^r_p(M), \eta \in \Omega^s_p(M)$. Then

    - $\omega \wedge \xi = (-1)^{qr} \xi \wedge \omega$

        - In particular, if $q$ is odd, then $\omega \wedge \omega = 0$

    - (Associativity) $(\omega \wedge \xi) \wedge \eta = \omega \wedge (\xi \wedge \eta)$

    *Remark*:

    - The wedge product between 1-forms can be regarded as a special case of the exterior product.

    - If $q + r > m$, $\omega \wedge \xi$ *vanishes identically*.
    
    - The space of differential forms of *all order*

        $$
        \Omega^*_p(M) \equiv \bigoplus_{i=1}^m \Omega^i_p(M)
        $$

        is *closed* under the exterior product.

### Exterior Derivatives

*Definition*:

- **Exterior derivative on differential forms**: for a general $r$-form
    
    $$
    \omega = \frac{1}{r!} \omega_{\mu_1 ... \mu_r}
        dx^{\mu_1} \wedge \cdots \wedge dx^{\mu_r}
    $$

    the exterior derivative $d_r: \Omega^r(M) \rightarrow \Omega^{r+1}(M)$ (or simply denoted by $d$) acts on $\omega$ as follows:

    $$
    d_r \omega \equiv \frac{1}{r!} \left( 
        \frac{\partial}{\partial x^\nu}
        \omega_{\mu_1 ... \mu_r}
    \right) dx^\nu \wedge dx^{\mu_1} \wedge \cdots \wedge dx^{\mu_r}
    $$

#### Relation to Usual Vector Calculus

- 0-forms: **Gradient**
    
    $$
    \begin{aligned}
        \omega_0 &= f(\mathbf{r}) \\ \Rightarrow
        d \omega_0 &=
        \partial_x f \, dx
        + \partial_y f \, dy
        + \partial_z f \, dz
        \equiv \nabla f \cdot d \mathbf{r}
    \end{aligned}
    $$

    This reduce to the usual differential of a function, corresponding to **gradient** $\nabla f(\mathbf{r})$. 

- 1-forms: **Curl**

    $$
    \begin{aligned}
        \omega_1 &= \omega_x(\mathbf{r}) dx + \omega_y(\mathbf{r}) dy + \omega_z(\mathbf{r}) dz
        \\ \Rightarrow
        d\omega_1 &= (
            \partial_y \omega_x dy \wedge dx 
            + \partial_z \omega_x dz \wedge dx
        ) \\ &\quad + (
            \partial_x \omega_y dx \wedge dy
            + \partial_z \omega_y dz \wedge dy
        ) \\ &\quad + (
            \partial_x \omega_z dx \wedge dz
            + \partial_y \omega_z dy \wedge dz
        ) \\
        &= (\partial_y \omega_z - \partial_z \omega_y) dy \wedge dz
        \\ &\quad + 
        (\partial_z \omega_x - \partial_x \omega_z) dz \wedge dx +
        (\partial_x \omega_y - \partial_y \omega_x) dx \wedge dy
    \end{aligned}
    $$

    The three components correspond to the **curl** $\nabla \times \mathbf{\omega}$ of a usual vector field $\omega \equiv (\omega_x, \omega_y, \omega_z)$.

- 2-forms: **Divergence**

    $$
    \begin{aligned}
        \omega_2 &= 
        \omega_{xy}(\mathbf{r}) \, dx \wedge dy 
        + \omega_{yz}(\mathbf{r}) \, dy \wedge dz
        + \omega_{zx}(\mathbf{r}) \, dz \wedge dx
        \\ \Rightarrow
        d\omega_2 &= 
        \partial_z \omega_{xy} \, dz \wedge dy \wedge dx 
        \\ &\quad + 
        \partial_x \omega_{yz} \, dx \wedge dy \wedge dz
        +
        \partial_y \omega_{zx} \,dy \wedge dz \wedge dx
        \\
        &= (\partial_x \omega_{yz} + \partial_y \omega_{zx} + \partial_z \omega_{xy}) \, dx \wedge dy \wedge dz
    \end{aligned}
    $$

    The coefficient corresponds to the **divergence** $\nabla \cdot \omega$ of a usual vector field $\omega \equiv (\omega_{yz}, \omega_{zx}, \omega_{xy})$.

- 3-forms: Related to [**Gauss' theorem** and **Stokes' theorem**](../6-de_Rham/6_1-Stokes_Theorem.md)

    $$
    \omega_3 = 
    \omega_{xyz}(\mathbf{r}) \, dx \wedge dy \wedge dz
    \, \Rightarrow \,
    d\omega_3 = 0
    $$

#### Properties of Exterior Derivative

- If $\xi \in \Omega^q(M), \omega \in \Omega^r(M)$, then
    
    $$ d(\xi \wedge \omega) = d\xi \wedge \omega + (-1)^q \xi \wedge d\omega$$

- $d^2 \equiv d_{r+1} \circ d_r = 0$

### Interior Product and Lie Derivative of Forms

*Definition*:

- **Interior product**