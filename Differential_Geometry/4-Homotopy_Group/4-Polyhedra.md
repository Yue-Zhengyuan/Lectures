## Fundamental Groups of Polyhedra

### Math Preparation: Free Groups and Relations

*Definition*:

- **Free set of generators of group $G$**: a *subset* $X = \{x_j\} \subset G$ which can be used to *uniquely* express *any* element $g \in G$ in the form
    
    $$
    g = x_1^{i_1} x_2^{i_2} \cdots x_n^{i_n} \qquad
    n \text{ finite}, \,
    i_k \in \mathbb{Z}, \,
    x_j \ne x_{j+1}
    $$

    We also adopt the following rules:
    
    > 1. If $i_j = 0$, then $x_j$ should not appear in the expression
    >
    > 2. If all $i$ are zero, we obtain the identity element.
    
    - **Letter**: an element in $X$ (generator)
    
    - **Word**: the product $w = x_1^{i_1} x_2^{i_2} \cdots x_n^{i_n}$, where we does *not* require that $x_j \ne x_{j+1}$ or $i_j \ne 0$
    
    - **Reduced word**: a word satisfying the constraint $x_j \ne x_{j+1}$ and $i_j \ne 0$
    
    - **Empty word**: a word with no letters, denoted by 1.

    - **Product of two words**: juxtaposition of two words (which may be further reduced if necessary)

- **Free group generated by $X$**: a group containing all reduced words generated by the set $X$ of letters, denoted by $F[X]$.
    
    **Group structure**:
        
    - **Multiplication**: product of words
    
    - **Identity**: the empty word 1
    
    - **Inverse**: 

        $$
        w = x_1^{i_1} x_2^{i_2} \cdots x_n^{i_n}
        \Rightarrow
        w^{-1} = x_n^{-i_n} \cdots x_2^{-i_2} x_1^{-i_1}
        $$

- **Relations**: constraints that prohibits some reduced words to appear in the group; general form

    $$
    r = x_1^{k_1} x_2^{k_2} \cdots x_n^{k_n} =  1
    $$

    *Example*:

    <center>

    |Group|Letters|Relation|
    |:-:|:-:|:-|
    |Cyclic group of order $n$|$\{x\}$|$x^n = 1$|

    </center>

### Relation between $H_1(K)$ and $\pi_1(|K|)$

*Definition*:

- **Commutator subgroup**

----

*Theorem*: 

Let $F$ be the commutator subgroup of $\pi_1(|K|)$, then

$$
H_1(K) \cong \pi_1(|K|) / F
$$

*Corollary*:

- Let $X$ be a connected topological space. Then $\pi_1(X) \cong H_1(X)$ *if and only if* $\pi_1(X)$ is *commutative*. 
    
    - If $\pi_1(X)$ is generated by one generator (which implies the commutativity), it is always isomorphic to $H_1(X)$

- If $X$ and $Y$ are of the same homotopy type, then $H_1(X) = H_1(Y)$ (*identical*, not only isomorphic).

----