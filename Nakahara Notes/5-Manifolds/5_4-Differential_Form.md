## Differential Forms

*Definition*:

- **Differential form of order $r$ ($r$-form)**: a *totally anti-symmetric* tensor of type $(0,r)$ (sending $r$ (tangent) vectors to a number)

    *General expression of $r$-forms*:

    A general $(0,r)$-tensor $\omega$ has the local coordinate expression

    $$
    \omega^{(r)} = \omega_{\mu_1 ... \mu_r}
    dx^{\mu_1} \cdots dx^{\mu_r} 
    $$

    By *totally anti-symmetric*, we mean that for *any* two indices $\mu, \nu$ of $\omega$

    $$
    \omega_{... \mu ... \nu ...}
    = - \omega_{... \nu ... \mu ...}
    $$

    This requirement can be reformulated in more general language: let $P$ be a permutation of the $r$ indices of $\omega$, i.e. an element of the **symmetric group $S_r$**, then

    $$
    \omega_{\mu_{P(1)} ... \mu_{P(r)}} 
    = \text{sgn}(P) \, \omega_{\mu_1 ... \mu_r}
    $$

    It follows that the indices of *non-vanishing* components of $\omega$ must take values *different* from each other.

    Collecting all terms in $\omega$ which are obtained from a permutation of index order, the anti-symmetry of $\omega$ allows us to rewrite these terms as

    $$
    \begin{aligned}
        &\sum_{P \in S_r} \omega_{\mu_{P(1)} ... \mu_{P(r)}} 
        dx^{\mu_{P(1)}} \cdots dx^{\mu_{P(r)}}
        \\ &=
        \omega_{\mu_1 ... \mu_r} 
        \sum_{P \in S_r} \text{sgn}(P) \, 
        dx^{\mu_{P(1)}} \cdots dx^{\mu_{P(r)}}
    \end{aligned}
    $$
    
    *Examples of different order*:
    
    - **0-Form**: formally *defined* as **functions** in $\mathcal{F}(M)$

        $$ \omega^{(0)} = f \in \mathcal{F}(M) $$

    - **1-form**: general expression
        
        $$
        \omega^{(1)} = \omega_\mu dx^\mu
        $$

        including $dx^\mu$ and the ordinary differential of functions $df$. There is no concept of "anti-symmetric" for 1-forms.
    

- **Wedge (exterior) product of differential forms (generalized)**: let $\omega \in \Omega^r_p(M), \xi \in \Omega^s_p(M)$be two differential forms; the wedge product of them (denoted by $\omega \wedge \xi$) is defined as an element in $\Omega^{r+s}_p(M)$, which acts on vectors $V_i \in T_p M$ in the following way:

    $$
    \begin{aligned}
        &(\omega \wedge \xi)(V_1, ..., V_{r+s})
        \\ & \quad =
        \frac{1}{q! r!}\sum_{P \in S_{q+r}} \text{sgn}(P) \,
        \omega(V_{P(1)}, ..., V_{P(r)})
        \xi(V_{P(r+1)}, ..., V_{P(r+s)})
    \end{aligned}
    $$

*Remark*: 

- The wedge product of $r$ 1-forms is an $r$-form.

- All $r$-forms of the above form at point $p \in M$ form a basis of the vector space of $r$-forms (denoted by $\Omega^r_p(M)$)

    $$
    dx^{\mu_1} \wedge \cdots \wedge dx^{\mu_r}
    \equiv \sum_{P \in S_r} \text{sgn}(P) \,
    dx^{\mu_{P(1)}} \cdots dx^{\mu_{P(r)}}
    $$

- If $\dim{M} = m$, we can easily obtain

    $$
    \dim{\Omega^r_p(M)} =
    \begin{pmatrix}
        m \\ r
    \end{pmatrix}
    \equiv \frac{m!}{r!(m-r)!}
    $$

    since we are *selecting* $r$ 1-forms from the $m$ dual bases from $T_p^* M$.

*General expression of $r$-forms*:

$$
\omega = \frac{1}{r!} \omega_{\mu_1 ... \mu_r}
dx^{\mu_1} \wedge \cdots \wedge dx^{\mu_r}
$$

where $\omega_{\mu_1 ... \mu_r}$ is also *totally anti-symmetric* to keep LHS invariant.

#### Properties of Wedge Product

Let $\omega \in \Omega^q_p(M), \xi \in \Omega^r_p(M), \eta \in \Omega^s_p(M), \, \dim{M} = m$. Then

- $\omega \wedge \xi = (-1)^{qr} \xi \wedge \omega$

    - In particular, if $q$ is odd, then $\omega \wedge \omega = 0$

- (Associativity) $(\omega \wedge \xi) \wedge \eta = \omega \wedge (\xi \wedge \eta)$

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
    d \omega \equiv \frac{\partial}{\partial x^\mu}
    \left( 
        \frac{1}{r!} \omega_{\mu_1 ... \mu_r}
    \right) dx^\mu \wedge dx^{\mu_1} \wedge \cdots \wedge dx^{\mu_r}
    $$

#### Coordinate-free Expression

- Action on 1-forms

    $$
    (d\omega)(X,Y) = X[\omega(Y)] - Y[\omega(X)] - \omega([X,Y])
    $$

    *Proof*: Using the coordinate expression

    $$
    X = X^\mu \partial_\mu, \quad
    Y = Y^\mu \partial_\mu, \quad
    \omega = \omega_\mu dx^\mu
    $$

    we obtain

    $$
    \begin{aligned}
        \text{LHS}
        &= \partial_\mu \omega_{\nu}
        (dx^\mu \wedge dx^{\nu})(X, Y)
        \\
        &= \partial_\mu \omega_{\nu} (
            X^\mu Y^\nu - Y^\mu X^\nu
        )
        \\
        \text{RHS} 
        &= X^\mu \partial_\mu (\omega_\nu Y^\nu)
        - Y^\mu \partial_\mu (\omega_\nu X^\nu)
        \\ &\quad
        - \omega_\nu (
            X^\mu \partial_\mu Y^\nu 
            - Y^\mu \partial_\mu X^\nu
        )
        \\
        &= \partial_\mu \omega_\nu (X^\mu Y^\nu - X^\nu Y^\mu) = \text{LHS} \qquad \blacksquare
    \end{aligned}
    $$

- General formula for $r$-forms
    
    $$
    \begin{aligned}
        &(d\omega)(X_1, ..., X_r, X_{r+1}) \\
        &= \sum_{i=1}^r (-1)^{i+1} X_i[\omega(X_1, ..., \cancel{X_i}, ..., X_{r+1})]
        \\ &\quad
        + \sum_{i<j} (-1)^{i+j} 
        \omega([X_i,X_j], X_1, ..., \cancel{X_i}, ..., \cancel{X_j}, ..., X_{r+1})
    \end{aligned}
    $$


#### Properties of Exterior Derivative

- Exterior derivative is *nilpotent*:
    
    $$
    d^2 \equiv d_{r+1} \circ d_r = 0
    $$

- Exterior derivative with exterior product

    Let $\xi \in \Omega^q(M), \omega \in \Omega^r(M)$.
    
    $$
    d(\xi \wedge \omega) = d\xi \wedge \omega + (-1)^q \xi \wedge d\omega
    $$

- Exterior derivative *commutes* with pullback
    
    Let $\omega \in \Omega^r(N), \, f: M \rightarrow N$

    $$
    d(f^* \omega) = f^*(d \omega)
    $$
    
    *Proof*: Let the coordinates used in $M, N$ be $x, y$ respectively. Using the coordinate expression, we obtain

    $$
    \begin{aligned}
        d (f^*\omega) 
        &= \frac{1}{r!} 
        \partial_\mu (f^* \omega)_{\mu_1 ... \mu_r}
        dx^\mu \wedge dx^{\mu_1} \wedge \cdots \wedge dx^{\mu_r}
        \\
        &= \frac{1}{r!} 
        \partial_\mu \left(
            \omega_{\nu_1 ... \nu_s}
            \frac{\partial y^{\nu_1}}{\partial x^{\mu_1}} \cdots
            \frac{\partial y^{\nu_s}}{\partial x^{\mu_s}}
        \right)
        dx^\mu \wedge dx^{\mu_1} \wedge \cdots \wedge dx^{\mu_r}
    \end{aligned}
    $$

    We note that $x^\mu$ is a *new variable*

    On the other hand,

    $$
    \begin{aligned}
        f^* (d\omega)
        &= (d\omega)_{\nu \nu_1 ... \nu_r}
        \frac{\partial y^{\nu}}{\partial x^{\mu}}
        \frac{\partial y^{\nu_1}}{\partial x^{\mu_1}} \cdots
        \frac{\partial y^{\nu_s}}{\partial x^{\mu_s}}
        dx^\mu dx^{\mu_1} \cdots dx^{\mu_r}
        \\
        &= \frac{\partial \omega_{\nu_1 ... \nu_s}}{\partial y^\nu}
        \frac{\partial y^{\nu}}{\partial x^{\mu}}
        \frac{\partial y^{\nu_1}}{\partial x^{\mu_1}} \cdots
        \frac{\partial y^{\nu_s}}{\partial x^{\mu_s}}
        dx^\mu dx^{\mu_1} \cdots dx^{\mu_r}
        \\
        &= (\partial_\mu \omega_{\nu_1 ... \nu_s})
        \frac{\partial y^{\nu_1}}{\partial x^{\mu_1}} \cdots
        \frac{\partial y^{\nu_s}}{\partial x^{\mu_s}}
        dx^\mu dx^{\mu_1} \cdots dx^{\mu_r}
        \\
        &= \frac{1}{r!} 
        \partial_\mu \left(
            \omega_{\nu_1 ... \nu_s}
            \frac{\partial y^{\nu_1}}{\partial x^{\mu_1}} \cdots
            \frac{\partial y^{\nu_s}}{\partial x^{\mu_s}}
        \right)
        dx^\mu \wedge dx^{\mu_1} \wedge \cdots \wedge dx^{\mu_r}
    \end{aligned}
    $$

    Thus the two sides are equal. $\blacksquare$

- Pullback is *distributive* over exterior product:
    
    Let $\xi, \omega$ be differential forms defined in $N$, and $f: M \rightarrow N$

    $$
    f^*(\xi \wedge \omega) = (f^* \xi) \wedge (f^* \omega)
    $$

### Interior Product and Lie Derivative of Forms

*Definition*:

- **Interior product**

### Application to Classical Mechanics