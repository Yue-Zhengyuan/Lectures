# Conjugation and Norm of Grassmann Tensors

## Grassmann Conjugation

*Program implementation*: `GTensor.gconj`

The **Grassmann conjugation** of a Grassmann tensor 

$$
\mathbf{T}(\theta)_{i_1 i_2 ... i_r}^{n_1 n_2 ... n_r} 
= 
T_{i_1 i_2 ... i_r}^{n_1 n_2 ... n_r} 
\theta_1^{n_1} \theta_2^{n_2} ... \theta_r^{n_r}
$$

is defined to be

$$
\begin{aligned}
    \mathbf{T}^\dagger 
    (\bar{\theta})_{i_1 i_2 ... i_r}^{n_1 n_2 ... n_r} 
    \equiv
    (T_{i_r ... i_2 i_1}^{n_r ... n_2 n_1})^* 
    \bar{\theta}_1^{n_1} \bar{\theta}_2^{n_2} ... \bar{\theta}_r^{n_r}
    \\
    \equiv 
    (T^\dagger)_{i_1 i_2 ... i_r}^{n_1 n_2 ... n_r} 
    \bar{\theta}_1^{n_1} \bar{\theta}_2^{n_2} ... \bar{\theta}_r^{n_r}
\end{aligned}
$$

Here the star means ordinary complex conjugation. We should emphasize that $\bar{\theta}$'s are treated independently of $\theta$'s. Each component is *completely transposed* compared to $\mathbf{T}$. 

### Graphical Representation

```
         T†
    |---|---|---|
    3   2   1   0

    0   1   2   3
    |___|___|___|
          T
```

## Complex Conjugation

*Program implementation*: `GTensor.conj`

The *ordinary* **complex conjugation** of the Grassmann tensor $\mathbf{T}$ is defined as:

$$
\mathbf{T}^*(\theta)_{i_1 i_2 ... i_r}^{n_1 n_2 ... n_r} 
= 
(T_{i_1 i_2 ... i_r}^{n_1 n_2 ... n_r})^*
\theta_1^{n_1} \theta_2^{n_2} ... \theta_r^{n_r}
$$

This is seldom used. 

## Norm

*Program implementation*: `gtensor.norm` 

As usual, the **norm** of a Grassmann tensor is defined as

$$
(\text{norm }\mathbf{T})^2
= \sum_{n_1, ..., n_r} \sum_{i_1, ..., i_r} 
|T_{i_1 i_2 ... i_r}^{n_1 n_2 ... n_r}|^2
$$

This can be calculated by contracting the pairs of axes $(r,1), (r-1,2), ..., (1,r)$ in $\mathbf{T}^\dagger, \mathbf{T}$ with all Grassmann metrics all set to $+1$; recall that such a set of contraction pairs does not involve reordering of Grassmann variables):

$$
\begin{aligned}
    (\text{norm } \mathbf{T})^2
    &= [\mathbf{T}^\dagger(\bar{\theta}) \mathbf{T}(\theta)]
    \\
    &= \sum_{n_1, ..., n_r} \sum_{i_1, ..., i_r}
    g_{r,1}^{n_1} g_{r-1,2}^{n_2} \cdots g_{1,r}^{n_r}
    (T^\dagger)_{i_r ... i_1}^{n_r ... n_1} 
    T_{i_1 ... i_r}^{n_1 ... n_r} 
    \\
    &= \sum_{n_1, ..., n_r} \sum_{i_1, ..., i_r}
    (T^\dagger)_{i_r ... i_1}^{n_r ... n_1} 
    T_{i_1 ... i_r}^{n_1 ... n_r} 
    \quad \text{(setting all $g$ to 1)}
    \\ & =
    \sum_{n_1, ..., n_r} \sum_{i_1, ..., i_r} 
    |T_{i_1 i_2 ... i_r}^{n_1 n_2 ... n_r}|^2
\end{aligned}
$$

This is done by the following code:

```python
axes = tuple(range(a.ndim))
nrmsqr = gt.tensordot(a.gconj(), a, [axes[::-1], axes]).value()
```

*Remark*: 

- If $\mathbf{T}$ is of *even-parity*, it does not matter if we set all $g$ to $1$ or $-1$. Because the summand

    $$
    \begin{aligned}
        &g_{r,1}^{n_1} g_{r-1,2}^{n_2} \cdots g_{1,r}^{n_r}
        (T^\dagger)_{i_r ... i_1}^{n_r ... n_1} 
        T_{i_1 ... i_r}^{n_1 ... n_r} 
        \\ &\qquad
        \to
        (\pm 1)^{n_1 + \cdots + n_r}
        (T^\dagger)_{i_r ... i_1}^{n_r ... n_1} 
        T_{i_1 ... i_r}^{n_1 ... n_r} 
    \end{aligned}
    $$

    is nonzero only when

    $$
    n_1 + \cdots + n_r = P(T) \pmod{2}
    $$

    For the same reason, if $\mathbf{T}$ is of *odd-parity*, setting all $g$ to $-1$ will only produce an additional negative sign. 

- We can exchange of $\mathbf{T}, \mathbf{T}^\dagger$ in the calculation (the pairs of axes are certainly unchanged, thus we still need not to permute the Grassmann variables) :
    
    $$
    \begin{aligned}
        &(\text{norm } \mathbf{T})^2
        = [\mathbf{T}(\theta) \mathbf{T}^\dagger(\bar{\theta})]
        \\
        &= \sum_{n_1, ..., n_r} \sum_{i_1, ..., i_r}
        g_{r,1}^{n_1} g_{r-1,2}^{n_2} \cdots g_{1,r}^{n_r}
        T_{i_r ... i_1}^{n_r ... n_1} 
        (T^\dagger)_{i_1 ... i_r}^{n_1 ... n_r} 
        \\
        &= \sum_{n_1, ..., n_r} \sum_{i_1, ..., i_r}
        T_{i_r ... i_1}^{n_r ... n_1} 
        (T^\dagger)_{i_1 ... i_r}^{n_1 ... n_r} 
        \quad \text{(setting all $g$ to 1)}
        \\ & =
        \sum_{n_1, ..., n_r} \sum_{i_1, ..., i_r} 
        |T_{i_1 i_2 ... i_r}^{n_1 n_2 ... n_r}|^2
        \quad \text{(rename variables)}
    \end{aligned}
    $$
    
    This is done by the code

    ```python
    axes = tuple(range(a.ndim))
    nrmsqr = gt.tensordot(a, a.gconj(), [axes, axes[::-1]]).value()
    # or equivalently
    nrmsqr = gt.tensordot(a, a.gconj(), [axes[::-1], axes]).value()
    ```

### Graphical Representation

```
         T†
    |---|---|---|
    3   2   1   0
    ↓   ↓   ↓   ↓
    0   1   2   3
    |___|___|___|
          T
```