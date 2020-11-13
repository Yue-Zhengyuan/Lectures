# Operator Algebra

The information needed in order to write down all *correlation functions*, i.e. the complete OPE (*including all regular terms*) of all primary fields with each other, and hence solve the field theory, is called the **operator algebra**.

## Two-Point Function Coefficients $C_{a b}$

Recall that the two-point function of two primary fields (they must have the *same* conformal dimension, otherwise the correlation function vanishes) is

$$
\langle \phi_a(z,\bar{z}) \phi_b(w,\bar{w}) \rangle
= \frac{C_{ab}}{(z-w)^{2h} (\bar{z}-\bar{w})^{2\bar{h}}}
$$

Since $C_{ab}$ is symmetric and is just a normalization, we can simply choose

$$
C_{ab} = \delta_{ab}
$$

## OPE of Two Primary Fields

Invariance under scaling transformations requires the operator algebra to have the following general form

$$
\phi_1(z,\bar{z})\phi_2(0,0)
= \sum_p \sum_{k,\bar{k}}
C_{12}^{p k \bar{k}} 
z^{h_p - h_1 - h_2 + K}
\bar{z}^{h_p - h_1 - h_2 + K}
\phi_p^{(k,\bar{k})}(0,0)
$$

where:

- $p$ iterates over all fields
- $k$ (or $\bar{k}$) collectively represents $\{k_1, k_2, ...\}$ (or $\{\bar{k}_1, \bar{k}_2, ...\}$)
- $K \equiv \sum_{i} k_i, \, \bar{K} \equiv \sum_{i} \bar{k}_i$

## Constraint on the Coefficients $C_{12}^{p k \bar{k}}$

Introduce a third primary field $\phi_r(w,\bar{w})$, and calculate

$$
\begin{aligned}
    &\langle \phi_r | \phi_1(z,\bar{z}) | \phi_2\rangle
    \\
    &\equiv \lim_{w,\bar{w} \to \infty}
    w^{2h_r} \bar{w}^{2\bar{h}_r}
    \langle \phi_r(w,\bar{w}) \phi_1(z,\bar{z}) \phi_2(0,0)\rangle
\end{aligned}
$$

where $C_{r12}$ are coefficients of 3-point functions: recall that

$$
\begin{aligned}
    \langle \phi_1(x_1) \phi_2(x_2) \phi_3(x_3) \rangle
    &= C_{123} [
        z_{12}^{h_1+h_2-h_3}
        z_{23}^{h_2+h_3-h_1}
        z_{13}^{h_3+h_1-h_2}
    ]^{-1}
    \\ &\qquad \times
    [
        \bar{z}_{12}^{\bar{h}_1+\bar{h}_2-\bar{h}_3}
        \bar{z}_{23}^{\bar{h}_2+\bar{h}_3-\bar{h}_1}
        \bar{z}_{13}^{\bar{h}_3+\bar{h}_1-\bar{h}_2}
    ]^{-1}
\end{aligned}
$$

Therefore

$$
\begin{aligned}
    &\langle \phi_r | \phi_1(z,\bar{z}) | \phi_2\rangle
    \\
    &= \lim_{w,\bar{w} \to \infty}
    w^{2h_r} \bar{w}^{2\bar{h}_r}
    C_{r12} [
        (w-z)^{h_r+h_1-h_2}
        z^{h_1+h_2-h_r}
        w^{h_2+h_r-h_1}
    ]^{-1}
    \\ &\qquad \qquad \times
    [
        (\bar{w}-\bar{z})^{\bar{h}_r+\bar{h}_1-\bar{h}_2}
        \bar{z}^{\bar{h}_1+\bar{h}_2-\bar{h}_r}
        \bar{w}^{\bar{h}_2+\bar{h}_r-\bar{h}_1}
    ]^{-1}
    \\
    &= \lim_{w,\bar{w} \to \infty}
    w^{2h_r} \bar{w}^{2\bar{h}_r}
    C_{r12} [
        w^{2h_r} z^{h_1+h_2-h_r}
    ]^{-1}
    [
        \bar{w}^{2\bar{h}_r} 
        \bar{z}^{\bar{h}_1+\bar{h}_2-\bar{h}_r}
    ]^{-1}
    \\
    &= \frac{C_{r12}}{z^{h_1+h_2-h_r} \bar{z}^{\bar{h}_1+\bar{h}_2-\bar{h}_r}}
\end{aligned}
$$

