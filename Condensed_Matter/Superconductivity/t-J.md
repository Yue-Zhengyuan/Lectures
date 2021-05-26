# *t*-*J* Model

The ***t*-*J* Model** is derived from the Hubbard model by taking the strong coupling limit ($U / t \gg 1$). The Hamiltonian is

$$
\begin{aligned}
    H &= t\sum_{\langle i,j \rangle \sigma} 
    (\tilde{c}_{i,\sigma}^\dagger \tilde{c}_{j,\sigma} + h.c.)
    \\ &\quad 
    + J \sum_{\langle i,j \rangle} \left(
        S_i \cdot S_j - \frac{1}{4} n_i n_j
    \right)
    - \mu \sum_i n_i
\end{aligned}
$$

The model is defined *together with* the **non-double-occupancy constraint**: each site can have up to one electron. $\tilde{c}_{i,\sigma}$ is the fermion operator in the **no-double-occupancy** subspace:

$$
\tilde{c}_{i,\sigma}  = c_{i,\sigma} (1 - n_{i, -\sigma})
$$

and $n_i$ is the total number operator of the electron:

$$
n_i = \sum_\sigma n_{i,\sigma}
= \sum_\sigma c_{i,\sigma}^\dagger c_{i,\sigma}
$$

## The Hole Representation

