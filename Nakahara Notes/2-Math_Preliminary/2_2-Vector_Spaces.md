## Vector Spaces

### Vectors and Vector Spaces

### Linear Maps, Images and Kernels

*Definition*: Let $V, W$ be two vector spaces over the field $K$ (such as $\mathbb{C}, \mathbb{R}$).

- **Linear maps**: a map $f: V \rightarrow W$ satisfying

    $$
    f(a_1 v_1 + a_2 v_2) = a_1 f(v_1) + a_2 f(v_2)
    \quad \forall a_1, a_2 \in K, v_1 v_2 \in V
    $$

    which is a *homomorphism* preserving the algebraic structure (vector addition and scalar multiplication) of the vector space $V$.

- **Image and kernel of the map $f$**
- **Linear functions**
- **Isomorphic vector spaces**

*Theorem*: (**Relation between $\ker{f}$ and $\text{im }f$**)

Let $f: V \rightarrow W$ be a linear map. Then

$$
\dim{V} = \dim{\ker{f}}  + \dim{\text{im }f}
$$

### Dual Vector Space

### Inner Product and Adjoint

*Definition*:

- **Inner product**
- **Adjoint of linear maps**

*Theorem*: (**Dimension of $\tilde{f}$**)

$$
\dim{\text{im }f} = \dim{\text{im }\tilde{f}}
$$

*Theorem*: (**Toy index theorem**)

Let $V, W$ be *finite*-dimensional vector spaces, and $f: V\rightarrow W$. Then

$$
\dim{\ker{f}} - \dim{\ker{\tilde{f}}} = \dim{V} - \dim{W}
$$

### Tensors

*Definition*: 

- **Tensor**: a (real-valued) tensor $T$ of *type (p,q)* is a multi-linear map from $p$ dual vectors (in $V^*$) and $q$ vectors (in V) to $\mathbb{R}$, i.e.
    
    $$
    T: \bigotimes^p V^* \bigotimes V \rightarrow \mathbb{R}
    $$

    *Example*:

    - Dual vectors (from vector to $\mathbb{R}$):   
        tensor of type $(0,1)$

    - Vectors (from dual vectors (linear functions) to $\mathbb{R}$):   
        tensor of type $(1,0)$

- **Tensor space**
- **Tensor product**
- **Tensor contraction**
