# Restriction on Correlation Function by Conformal Symmetry

The (global) conformal invariance imposes strong restriction on the possible forms of the correlation functions of quasi-primary fields.

## Two-Point Functions

For general quasi-primary fields that contain both holomorphic and anti-holomorphic parts:

$$
\langle \phi_a(z, \bar{z}) \phi_b(w, \bar{w}) \rangle 
= \frac{C_{a b}}{(z-w)^{2h} (\bar{z}-\bar{w})^{2\bar{h}}} 
\quad \text{if }
\begin{cases}
    h_a = h_b = h \\
    \bar{h}_a = \bar{h}_b = \bar{h}
\end{cases}
$$

Otherwise the correlation function vanishes.

When the fields are all chiral, the result can be simplified to 

$$
\langle \phi_a(z) \phi_b(w) \rangle
= \frac{C_{ab}}{(z-w)^{2h}}
\quad \text{if }
h_a = h_b = h
$$

Otherwise the correlation function vanishes. 

*Proof of the general case*: 

Suppose

$$
\langle \phi_a(z, \bar{z}) \phi_b(w, \bar{w}) \rangle 
= g(z,w;\bar{z},\bar{w})
$$

- Impose invariance under *translation* 
    
    $$
    z \to z + a
    $$

    Then obviously, we should have

    $$
    g(z,w;\bar{z},\bar{w}) = g(z-w, \bar{z}-\bar{w})
    $$

- Impose invariance under *scaling*
  
    $$
    z \to \lambda z, \quad
    \bar{z} \to \bar{\lambda} \bar{z}
    $$
    
    For quasi-primary field, we have

    $$
    \phi_a (z, \bar{z}) 
    \to 
    \phi'_a (\lambda z, \bar{\lambda} \bar{z})
    = \lambda^{-h_a} {\bar{\lambda}}^{-\bar{h}_a}
    \phi(z, \bar{z})
    $$

    Then the correlation function transforms to

    $$
    \begin{aligned}
        &\langle \phi_a(z, \bar{z}) \phi_b(w, \bar{w}) \rangle 
        \\
        &= \lambda^{(h_a + h_b)}
        \bar{\lambda}^{(\bar{h}_a + \bar{h}_b)}
        \langle 
            \phi'_a (\lambda z, \bar{\lambda} \bar{z})
            \phi'_b (\lambda w, \bar{\lambda} \bar{w})
        \rangle 
    \end{aligned}
    $$

    Thus we should require

    $$
    g(z-w, \bar{z}-\bar{w})
    = \lambda^{(h_a + h_b)}
    \bar{\lambda}^{(\bar{h}_a + \bar{h}_b)}
    g( \lambda(z-w), \bar{\lambda}(\bar{z}-\bar{w}))
    $$

    Therefore

    $$
    g(z-w,\bar{z}-\bar{w}) = 
    \frac{C_{ab}}{
        (z-w)^{h_a + h_b} 
        (\bar{z}-\bar{w})^{\bar{h}_a + \bar{h}_b}
    }
    $$

- Impose invariance under *SCT*
    
    $$
    z \to -1/z
    $$

    Using $d(-z^{-1})/dz = z^{-2}$, for quasi-primary field, we obtain

    $$
    \phi_a(z,\bar{z}) \to
    \phi'_a \left(
        -\frac{1}{z}, -\frac{1}{\bar{z}}
    \right)
    = z^{2h_a}
    \bar{z}^{2\bar{h}_a}
    \phi_a(z,\bar{z})
    $$

    The correlation function transforms to 

    $$
    \begin{aligned}
        &\langle \phi_a(z, \bar{z}) \phi_b(w, \bar{w}) \rangle 
        \\
        &= z^{-2h_a} w^{-2h_a}
        \bar{z}^{-2\bar{h}_a} \bar{w}^{-2\bar{h}_a}
        \phi'_a \left(
            -\frac{1}{z}, -\frac{1}{\bar{z}}
        \right)
        \phi'_b \left(
            -\frac{1}{w}, -\frac{1}{\bar{w}}
        \right)
    \end{aligned}
    $$

    Thus we should have

    $$
    h_a = h_b = h, \quad 
    \bar{h}_a = \bar{h}_b = \bar{h}
    \qquad \blacksquare
    $$

## Three-Point Functions

The general case:

$$
\begin{aligned}
    &\langle \phi_1(z_1) \phi_2(z_2) \phi_3(z_3) \rangle
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
\end{aligned}
$$

When the fields are all chiral:

$$
\langle \phi_1(z_1) \phi_2(z_2) \phi_3(z_3) \rangle
= \frac{C_{123}}{
    z_{12}^{h_1 + h_2 - h_3}
    z_{23}^{h_2 + h_3 - h_1}
    z_{13}^{h_1 + h_3 - h_2}
}
$$

where $z_{ij} \equiv z_i - z_j, \bar{z}_{ij} \equiv \bar{z}_i - \bar{z}_j$.

For simplicity, we shall give the proof when the fields are all chiral.

*Proof of the chiral case*:



