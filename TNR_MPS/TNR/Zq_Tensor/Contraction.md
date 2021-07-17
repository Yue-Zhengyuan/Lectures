# Contraction of $Z_q$ Tensors

A tensor $T_{\alpha_1 \alpha_2 ... \alpha_r}$ is said to have **$Z_q$ symmetry** (or called a **$Z_q$ tensor**, $q \ge 2 \in \mathbb{N}$) if the dimension of *all* axes are *integer multiples* of $q$, and all nonzero elements satisfy 

$$
\alpha_1 + \cdots + \alpha_r = 0 \pmod{q}
\quad p \in \{0, 1, ..., q-1\}
$$

## $Z_q$ Index

We can separate the original index $\alpha_a \, (a = 1,2,...,r)$ into two parts:

$$
\alpha_a = q j_a + n_a
$$

where $j_a, n_a$ are the integer part and the remainder of $\alpha_a / q$:

$$
\begin{align*}
    j_a &\equiv \text{floor}\left( \frac{\alpha_a}{q} \right)
    &\quad \dim{j_a} &= \frac{\dim{\alpha_a}}{q}
    \\
    n_a &\equiv \alpha_a \text{ mod } q
    &\quad \dim{n_a} &= q
\end{align*}
$$

Now we understand why we require that $\dim{\alpha_a}$ must be an integer multiple of $q$. 

The new indices $n_a$ are called the **$Z_q$ indices**. Then obviously

$$
n_1 + \cdots + n_r = 0 \pmod{q}
$$

i.e. the $Z_q$ indices can determine whether the symmetry exists. 

With these new notation, we rewrite the $Z_q$ tensor $T$ in the so-called **$Z_q$ form**

$$
\text{traditional form: } T_{\alpha_1 ... \alpha_r} \to 
\text{$Z_q$ form: } T_{j_1 ... j_r}^{n_1 ... n_r}
$$

## Contraction in $Z_q$ Form

The **contraction** of two $Z_q$ tensors in the traditional form is no different from the contraction of ordinary tensors: the result of contraction of the $a$th axis of $A$ and the $b$th tensor of $B$ is ($r, s$ are the number of axes of $A, B$, respectively)

$$
(AB)_{\alpha_1 ... \cancel{\alpha_a} ... \alpha_r \beta_1 ... \cancel{\beta_b} ... \beta_s} \equiv
\sum_{\alpha_a,\beta_b} \delta_{\alpha_a,\beta_b} A_{\alpha_1 ... \alpha_r} B_{\beta_1 ... \beta_s}
$$

If we use the $Z_q$ form of the two tensors $A, B$, the right-hand side becomes 

$$
\sum_{i_a,j_b} \sum_{m_a,n_b} 
\delta_{q i_a + m_a, q j_b + n_b}
A_{i_1 ... i_r}^{m_1 ... m_r} 
B_{j_1 ... j_s}^{n_1 ... n_s} 
$$

But if $\alpha_a = \beta_b$, the integer part and the remainder of $\alpha_a / q, \, \beta_b / q$ must be the same individually. Thus we can write

$$
\delta_{q i_a + m_a, q j_b + n_b} 
= \delta_{m_a, n_b} \delta_{i_a, j_b}
$$

Thus we obtain the formula for contraction in $Z_q$ form:

$$
(AB)_{i_1 ... \cancel{i_a} ... i_r j_1 ... \cancel{j_b} ... j_s}^{m_1 ... \cancel{m_a} ... m_r n_1 ... \cancel{n_b} ... n_s}
= 
\sum_{i_a,j_b} \sum_{m_a,n_b} 
\delta_{m_a, n_b} \delta_{i_a, j_b} 
A_{i_1 ... i_r}^{m_1 ... m_r} 
B_{j_1 ... j_s}^{n_1 ... n_s} 
$$

which is the same as *ordinary* contraction over *two* pairs of indices $(i_a, j_b)$ and $(m_a, n_b)$. The generalization to contraction of multiple pairs of indices is straightforward: contracting axes $a,c,...$ of $A$ with axes $b,d,...$ of $B$, we obtain

$$
\begin{align*}
    &(AB)_{i_1 ... \cancel{i_a} ... \cancel{i_c} ... i_r, j_1... \cancel{j_b} ... \cancel{j_d} ... j_s}^{m_1 ... \cancel{m_a} ... \cancel{m_c} ... m_r, n_1 ... \cancel{n_b} ... \cancel{n_d} ... n_s}
    \\
    &= \sum_{m_a,n_b} \sum_{m_c,n_d} \cdots \sum_{i_a,j_b} \sum_{i_c,j_d} \cdots
    \\ &\qquad
    \delta_{m_a n_b} \delta_{m_c n_d} \cdots
    \delta_{i_a j_b} \delta_{i_c j_d} \cdots
    A_{i_1 ... i_r}^{m_1 ... m_r} 
    B_{j_1 ... j_s}^{n_1 ... n_s}
\end{align*}
$$

### Verification of $Z_q$ Symmetry of Contraction Result

$$
\begin{align*} 
    &\sum_{k \ne a,c,...} m_k + \sum_{l \ne b,d,...} n_l
    \pmod{q}
    \\
    &= 
    p_A + p_B - (m_a+n_b) - (m_c+n_d) - \cdots \pmod{q}
\end{align*}
$$

where $p_A, p_B = 0$. Thus the result **does not have definite (even) parity (??????)**