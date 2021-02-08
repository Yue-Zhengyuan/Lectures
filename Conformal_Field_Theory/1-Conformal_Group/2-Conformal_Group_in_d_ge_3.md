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

# Conformal Group in $d \ge 3$

Corollary 3 (which states that $\partial^2 f = 0$) imposes the restriction that $\partial \cdot \epsilon$ is at most *linear* in $x$. Thus $\epsilon$ itself is at most quadratic in $x$:

$$
\epsilon_\mu = a_\mu + b_{\mu \nu} x^\nu
+ c_{\mu \nu \rho} x^\nu x^\rho 
\quad (c_{\mu \nu \rho} = c_{\mu \rho \nu})
$$

We now discuss all possible situations allowed by the general requirement.

## Conformal Transformations in $d \ge 3$

1. $b, c = 0$ 
    
    $$
    \epsilon_\mu = a_\mu 
    \, \Rightarrow \,
    x'^\mu = x^\mu + a^\mu
    $$
    
    This trivially satisfies the general requirement, corresponding to uniform **translations**.

2. $a, c = 0$
    
    Plug into the general requirement:
    
    $$
    b_{\mu \nu} + b_{\nu \mu} 
    = \frac{2}{d} (\eta^{\rho \sigma} b_{\sigma \rho})
    \eta_{\mu \nu}
    = \frac{2}{d} b^\rho_{\phantom{\rho} \rho}
    \eta_{\mu \nu}
    $$

    We know that any matrix can be separated into a symmetric part and an anti-symmetric part. Let us do this for $b_{\mu \nu}$:
    
    $$
    \left.
    \begin{aligned}
        \text{Sym:} \quad s_{\mu \nu} 
        &= \frac{1}{2}(b_{\mu \nu} + b_{\nu \mu})
        \\
        \text{Anti-sym:} \quad r_{\mu \nu} 
        &= \frac{1}{2}(b_{\mu \nu} - b_{\nu \mu})
    \end{aligned}
    \right \} \Rightarrow
    b_{\mu \nu} = s_{\mu \nu} + r_{\mu \nu}
    $$
    
    But we can say more about $s$: plug $s$ and $r$ into the general requirement, we obtain

    $$
    s_{\mu \nu} = \frac{1}{d} b^\rho_{\phantom{\rho} \rho}
    \eta_{\mu \nu} 
    \equiv \alpha \eta_{\mu \nu} 
    $$

    i.e. $s$ is proportional to $\eta_{\mu \nu}$. Now we recognize that:

    - The symmetric part describes **scaling (dilation)**:

        $$
        \epsilon_\mu = \alpha \eta_{\mu \nu} x^\nu
        = \alpha x_\mu
        \, \Rightarrow \,
        x'^\mu = (1 + \alpha) x^\mu
        $$

    - The anti-symmetric part describes **rotation**:

        $$
        \epsilon_\mu = r_{\mu \nu} x^\nu
        \, \Rightarrow \,
        x'^\mu = (\delta_\nu^\mu + {r^\mu}_{\nu}) x^\nu
        $$

3. $c \ne 0$
    
    First evaluate $f$:

    $$
    \begin{aligned}
        f &= \frac{2}{d} 
        \eta^{\mu \nu} \partial_{\mu} \epsilon_{\nu}(x)
        \\
        &= \frac{2}{d} (
            {b^\mu}_\mu + 2{c^\mu}_{\mu \rho} x^\rho
        )
    \end{aligned}
    $$

    Plug into Corollary 1:

    $$
    \begin{aligned}
        \text{LHS}
        &= 2 \partial_\mu \partial_{\nu} \epsilon_{\rho}
        = 2 c_{\rho \mu \nu}
        \\
        \text{RHS}
        &= (
            \eta_{\rho \mu} \partial_\nu
            + \eta_{\nu \rho} \partial_\mu
            - \eta_{\mu \nu} \partial_\rho
        ) f
        \\
        &= \frac{2}{d} (
            \eta_{\rho \mu} {c^\alpha}_{\alpha \nu}
            + \eta_{\nu \rho} {c^\alpha}_{\alpha \mu}
            - \eta_{\mu \nu} {c^\alpha}_{\alpha \rho}
        )
    \end{aligned}
    $$

    Now we define (not to be confused with the $b_{\mu \nu}$ above)

    $$
    b_\mu \equiv \frac{1}{d} {c^\alpha}_{\alpha \mu}
    $$

    then we find the conditions that must be satisfied by $b_\mu$:

    $$
    c_{\rho \mu \nu}
    = \eta_{\rho \mu} b_\nu
    + \eta_{\nu \rho} b_\mu
    - \eta_{\mu \nu} b_\rho
    $$

    which is symmetric in $\mu, \nu$ as expected. 

    When $a_\mu, b_{\mu\nu} = 0$ (i.e. remove the contribution from translation, scaling and rotation):

    $$
    \begin{aligned}
        \epsilon_\mu &= c_{\mu \nu \rho} x^\nu x^\rho 
        \\
        &= (
            \eta_{\mu \nu} b_\rho
            + \eta_{\rho \mu} b_\nu
            - \eta_{\nu \rho} b_\mu
        ) x^\nu x^\rho 
        \\
        &= 2 (x \cdot b) x_\mu - x^2 b_\mu
    \end{aligned}
    $$

    This is called the **special conformal transformation (SCT)**. We give its finite form below without proof.

Any conformal transformation in $d \ge 3$ can be expressed as composition of the above four types (these four basic types also exist in $d = 2$, although there are more):

<div class="result">

**Conformal transformations in $d \ge 3$:**

$$
\def \arraystretch{1.5}
\begin{array}{r|l|l}
    \text{Type}& \text{Finite} & \text{Infinitesimal}
    \\ \hline
    \text{Translation} &
    x'^\mu = x^\mu + a^\mu &
    x'^\mu = x^\mu + \epsilon^\mu
    \\
    \text{Scaling} &
    x'^\mu = \alpha x^\mu &
    x'^\mu = (1 + \alpha) x^\mu &
    \\
    \text{Rotation} &
    x'^\mu = {R^\mu}_\nu x^\nu &
    x'^\mu = (\delta_\nu^\mu + r^\mu_{\phantom{\mu} \nu}) x^\nu
    \\
    \text{SCT} & 
    x'^{\mu} = 
    \frac{x^{\mu} - b^{\mu} x^2}{1 - 2b \cdot x + b^2 x^2} &
    \def \arraystretch{0.2}
    \begin{aligned}
        \\
        x'^\mu &= x^\mu + 2 (x \cdot b) x_\mu 
        \\ &\quad
        - x^2 b_\mu
    \end{aligned}
\end{array}
$$

</div><br>

## Transformation Generators

Now we derive the transformation **generators** corresponding to the conformal group in $d\ge 3$. Under an infinitesimal transformation, the coordinates and the field will change according to

<center>
<img src="Figures/field_trans.png" width="300pt">
</center>

$$
\begin{aligned}
    x &\mapsto x'(x)=x+\epsilon (x)
    \\
    \phi (x) &\mapsto \phi' \left(x'(x)\right)=F(\phi (x))
\end{aligned}
$$

Assume that the transformation depends on some set of parameters $\left\{\omega_a\right\}$, i.e.

$$
x^{\mu} \mapsto x'^{\mu}(x,\omega),
\quad
\phi (x) \mapsto \phi' \left(x'(x)\right)=F(\phi (x),\omega)
$$

with $\omega =0$ representing doing nothing:

$$
x'^{\mu}(x,0)=x^{\mu}, 
\quad
F(\phi (x),0)=\phi (x)
$$

The **generator** $G_a$ of the transformation is *defined* by the difference between the new and the old field *at the same position*:

$$
\phi' (x)-\phi (x)=-i \omega_aG_a\phi (x)
$$

After some calculation (see the Yellow Book 2.4.2), one arrives at

<div class="result">

**Generator of an infinitesimal transformation:**

$$
i G_a\phi (x)
= \frac{\partial x'^{\mu}}{\partial \omega_a}(x,0)
\, \partial_{\mu} \phi (x)
- \frac{\partial F}{\partial \omega_a}(\phi(x),0)
$$

</div><br>

For *scalar* fields in particular, the functional $F$ depends on the parameters $\omega$ only through the coordinates $x$. Therefore

$$
\frac{\partial F}{\partial \omega_a} = 0
\, \Rightarrow \,
i G_a\phi (x)
= \frac{\partial x'^{\mu}}{\partial \omega_a}(x,0)
\, \partial_{\mu} \phi(x)
$$

For the four types of conformal transformations, we then obtain

<div class="result">

**Conformal transformation generators (scalar fields, $d\ge 3$)**

$$
\begin{aligned}
    \text{Translation}&: \quad
    P_{\mu} = -i \partial_{\mu}
    \\
    \text{Dilation} &: \quad
    D = -i x^{\mu}\partial_{\mu}
    \\
    \text{Rigid rotation} &: \quad
    L_{\mu \nu} = i (
        x_{\mu} \partial_{\nu}
        - x_{\nu} \partial_{\mu}
    )
    \\
    \text{SCT} &: \quad
    K_{\mu} = -i (
        2x_{\mu}x^{\nu}\partial_{\nu}
        - x^2\partial_{\mu}
    )
\end{aligned}
$$

</div><br>

## Algebra of the Generators

The nonzero commutators of the conformal generators (the **conformal algebra**) are found to be

$$
\begin{aligned}
[D, P_\mu] &= i P_\mu \\
[D, K_\mu] &= -i K_\mu \\
[K_\mu, P_\nu] &= 2i (\eta_{\mu\nu} D - L_{\mu\nu} ) \\
[K_\rho, L_{\mu\nu}] &= i (\eta_{\rho\mu} K_\nu - \eta_{\rho\nu} K_\mu) \\
[P_\rho, L_{\mu\nu}] &= i (\eta_{\rho\mu} P_\nu - \eta_{\rho\nu} P_\mu ) \\
[L_{\mu\nu}, L_{\rho\sigma}] &= i (\eta_{\nu\rho} L_{\mu\sigma} + \eta_{\mu\sigma} L_{\nu\rho} - \eta_{\mu\rho} L_{\nu\sigma} - \eta_{\nu\sigma} L_{\mu\rho} )
\end{aligned}
$$

Here $\eta_{\mu\nu}$ is the metric in $\R^{d,0}$. We note that the algebra of the rotation generators $L$ form a sub-algebra $SO(d)$. 

These commutation relations can be greatly simplified if we define

$$
\begin{aligned}
    J_{\mu \nu} &= L_{\mu \nu}
    \qquad &
    J_{-1,0} &= D
    \\
    J_{0 \mu} &= \frac{1}{2} (P_{\mu} + K_{\mu})
    \qquad &
    J_{-1, \mu} &= \frac{1}{2} (P_{\mu} - K_{\mu})
\end{aligned}
$$

so that $J_{a b} = -J_{b a}$ for $a, b \in \{-1,0,1, ...,d\}$, then we have the algebra

$$
[J_{a b},J_{c d}]
= i (
    \eta_{a d} J_{b c} + \eta_{b c} J_{a d}
    - \eta_{a c} J_{b d} - \eta_{b d} J_{a c}
)
$$

The new metric is in $\R^{d+1,1}$ if we start with the Euclidean metric. This is the *same* as the $SO(d+1, 1)$ algebra. In general, if we start from the Minkowski space $\R^{p,q}$, we will obtain:

<div class="result">
<center>

**The conformal group of $\R^{p,q}$ ($d \equiv p+q \ne 2$) <br> is isomorphic to the group $SO(p+1,q+1)$.**

</center>
</div><br>