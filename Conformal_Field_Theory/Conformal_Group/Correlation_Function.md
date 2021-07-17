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

# Restriction on Correlation Function by Conformal Symmetry

The *global* conformal invariance already imposes strong restriction on the possible forms of the correlation functions of quasi-primary fields.

<div class="result">

**Two-point functions:**

- Chiral
    
    $$
    \langle \phi_1(z) \phi_2(w) \rangle
    = \frac{C_{12}}{(z-w)^{2h}}
    \quad \text{for} \quad
    h_1 = h_2 = h
    $$

- General

$$
\langle \phi_1(z, \bar{z}) \phi_2(w, \bar{w}) \rangle 
= \frac{C_{12}}{(z-w)^{2h} (\bar{z}-\bar{w})^{2\bar{h}}} 
\quad \text{for} \quad
\begin{cases}
    h_1 = h_2 = h \\
    \bar{h}_1 = \bar{h}_2 = \bar{h}
\end{cases}
$$

Otherwise the correlation function vanishes. 

</div><br>

<!-- <div class="remark">

*Remark*: In order that the correlation function is single-valued, $h$ for a chiral/anti-chiral quasi-primary field can only be an integer or half-integer.

</div><br> -->

Since the holomorphic (no-bar) and the anti-holomorphic (with-bar) parts decouples, once we have shown the holomorphic result, it is not difficult to write down the corresponding anti-holomorphic equations.

*Proof of the chiral case*: 

To save writing, let $G(z_1,z_2) = \expect{\phi_1(z_1) \phi_2(z_2)}$.

We apply infinitesimal conformal transformations $\epsilon(z_i)$ for each $i = 1,2$. The variation of the correlation function is

$$
\delta \expect{\phi_1 \phi_2}
= \expect{(\delta \phi_1) \phi_2}
+ \expect{\phi_1(\delta \phi_2)}
$$

However, we know that

$$
\expect{\phi_1(z') \phi_2(z')} 
= \expect{\phi'_1(z') \phi'_2(z')}
\, \Rightarrow \, \delta\expect{\phi_1 \phi_2} = 0
$$

and

$$
\delta \phi(z) = - (h \phi(z) \partial \epsilon(z)
+ \epsilon(z) \partial \phi(z))
$$

The path integral average only acts on $\phi$, so we obtain ($\partial_i \equiv \partial/\partial z_i$):

$$
\sum_{i=1}^2 [h_i \partial \epsilon(z_i) + \epsilon(z_i) \partial_i]
G(z_1,z_2) = 0
$$

Now we check the three special cases of global $\epsilon(z)$:

- Translation $l_{-1}: \epsilon(z) = \epsilon$. This is a constant transformation, so $\partial \epsilon(z) = 0$, and we are left with
    
    $$
    (\partial_1 + \partial_2) G(z_1, z_2) = 0
    $$

    This means that $G$ can only depend on the combination $x \equiv z_1 - z_2$:

    $$
    G(x) = G(z_1 - z_2)
    $$

- Scaling + rotation $l_0: \epsilon(z) = \epsilon z$. Then $\partial \epsilon(z) = \epsilon$, and we get
    
    $$
    (h_1 + h_2 + z_1 \partial_1 + z_2 \partial_2)G(z_1 - z_2) = 0
    $$

    We can write the derivative terms as

    $$
    \begin{align*}
        &(z_1 \partial_1 + z_2 \partial_2)G(z_1 - z_2) 
        \\
        &= (z_1 - z_2) \partial_x G(x) 
        = x\partial_x G(x)
    \end{align*}
    $$

    Then we have a differential equation of $G(x)$:

    $$
    (h_1 + h_2 + x\partial_x) G(x) = 0
    $$

    The general solution is ($C_{12}$ is a constant)

    $$
    G(x) = \frac{C_{12}}{x^{h_1 + h_2}}
    $$

- SCT $l_{-1}: \epsilon(z) = \epsilon z^2$. Then $\partial \epsilon(z) = 2 \epsilon z$, and
    
    $$
    (2h_1 z_1 + 2h_2 z_2 + z_1^2 \partial_1 + z_2^2 \partial_2)
    G(z_1 - z_2) = 0
    $$

    We simplify the derivative terms to

    $$
    \begin{align*}
        (z_1^2 \partial_1 + z_2^2 \partial_2) G(z_1 - z_2)
        &= (z_1^2 - z_2^2) \partial_x G(x)
        \\
        &= (z_1 + z_2) \, x \, \partial_x G(x)
        \\
        &= - (z_1 + z_2) (h_1 + h_2) G(x)
    \end{align*}
    $$

    Plug in the equation
    
    $$
    \begin{align*}
        (h_1 - h_2) (z_1 - z_2) G(x) = 0
    \end{align*}
    $$

    Since $z_1, z_2$ are arbitrary, we must have $h_1 = h_2$ for nonzero $G(x)$. $\blacksquare$

<div class="result">

**Three-Point functions:**

- Chiral

    $$
    \expect{\phi_1(z_1) \phi_2(z_2) \phi_3(z_3)}
    = \frac{C_{123}}{
        z_{12}^{h_1 + h_2 - h_3}
        z_{23}^{h_2 + h_3 - h_1}
        z_{13}^{h_1 + h_3 - h_2}
    }
    $$

- General

    $$
    \begin{align*}
        &\expect{\phi_1(z_1, \bar{z}_1) \phi_2(z_2, \bar{z}_2) \phi_3(z_3, \bar{z}_3)}
        \\
        &= C_{123} \times
        \frac{1}{
            z_{12}^{h_1 + h_2 - h_3}
            z_{23}^{h_2 + h_3 - h_1}
            z_{13}^{h_1 + h_3 - h_2}
        }
        \\
        & \qquad \times
        \frac{1}{
            \bar{z}_{12}^{\bar{h}_1 + \bar{h}_2 - \bar{h}_3}
            \bar{z}_{23}^{\bar{h}_2 + \bar{h}_3 - \bar{h}_1}
            \bar{z}_{13}^{\bar{h}_1 + \bar{h}_3 - \bar{h}_2}
        }
    \end{align*}
    \quad \text{with} \quad 
    \begin{align*}
        z_{ij} &\equiv z_i - z_j 
        \\
        \bar{z}_{ij} &\equiv \bar{z}_i - \bar{z}_j
    \end{align*}
    $$

</div><br>

*Proof of the chiral case*: If we stick to the differential equation method, we shall get into some complicated mathematical identities. So another hand-waving proof is presented. 

From translation invariance, we immediately write down that

$$
\expect{\phi_1(z_1) \phi_2(z_2) \phi_3(z_3)}
= f(z_{12}, z_{23}, z_{13})
$$

Strictly speaking, $z_{13}$ is not an independent variable because $z_{13} = z_{12} + z_{23}$, but we shall ignore this issue.

- Apply scaling/rotation invariance
    
    $$
    \begin{align*}
        z & \to z' = \lambda z
        \\
        \phi(z) & \to \phi'(z') = \lambda^{-h} \phi(z)
    \end{align*}
    $$

    The correlation function transforms as

    $$
    \begin{align*}
        \expect{\phi_1(z'_1) \phi_2(z'_2) \phi_3(z'_3)}
        &= \expect{\phi'_1(z'_1) \phi'_2(z'_2) \phi'_3(z'_3)}
        \\ &\Downarrow \\
        \expect{\phi_1(\lambda z_1) \phi_2(\lambda z_2) \phi_3(\lambda z_3)}
        &= \lambda^{-(h_1+h_2+h_3)}
        \expect{\phi_1(z_1) \phi_2(z_2) \phi_3(z_3)}
        \\ &\Downarrow \\
        f(\lambda z_{12}, \lambda z_{23}, \lambda z_{13})
        &= \lambda^{-(h_1+h_2+h_3)} f(z_{12}, z_{23}, z_{13})
    \end{align*}
    $$

    Thus

    $$
    f(z_{12}, z_{23}, z_{13}) = \frac{C_{123}}{z_{12}^a z_{23}^b z_{13}^c}, \quad
    a + b + c = h_1 + h_2 + h_3
    $$

- Apply SCT. We choose a special one
    
    $$
    \begin{align*}
        z &\to z' = -1/z
        \\
        \phi(z) & \to \phi'(z') 
        = z^{2h} \phi(z)
    \end{align*}
    $$

    The correlation function transforms as

    $$
    \begin{align*}
        \expect{\phi_1(z'_1) \phi_2(z'_2) \phi_3(z'_3)}
        &= \expect{\phi'_1(z'_1) \phi'_2(z'_2) \phi'_3(z'_3)}
        \\ &\Downarrow \\
        \expect{\phi_1(-z_1^{-1}) \phi_2(-z_2^{-1}) \phi_3(-z_3^{-1})}
        &= z_1^{2h_1} z_2^{2h_2} z_3^{2h_3}
        \expect{\phi_1(z_1) \phi_2(z_2) \phi_3(z_3)}
    \end{align*}
    $$

    By direct calculation, one sees that

    $$
    \begin{align*}
        a &= h_1 + h_2 - h_3 \\
        b &= h_2 + h_3 - h_1 \\
        c &= h_1 + h_3 - h_2 \qquad \blacksquare
    \end{align*}
    $$
