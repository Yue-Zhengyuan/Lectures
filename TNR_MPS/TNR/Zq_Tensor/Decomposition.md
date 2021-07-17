# Decomposition of $Z_q$ Tensors

Since at least half of the elements in $T$ are zero, there will be many zeros in the decomposition results. However, if we perform ordinary decomposition without some **gauge fixing** (matrix decomposition results are *not unique*), *those elements that can be made be zero may not be zero*, increasing numerical error in the physical applications. 

Luckily, since $Z_2$ tensors can be put into the form of a Grassmann tensor of even parity (with commuting axes, instead of anti-commuting), we can also apply Grassmann tensor decomposition with some modifications.  

Let us decompose a rank-$r$ $Z_2$ tensor $T$ at the $q$th axis. First, we convert it to the Grassmann form, and reshape it to

$$
T_{(j_1 ... j_q) (j_{q+1} ... j_r)}^{(n_1 ... n_q) (n_{q+1} ... n_r)}
\rightarrow T_{J K}^{M N}
$$

where

$$
\begin{align*}
    \dim J = \frac{1}{2} \prod_{a=1}^q \dim{n_a} \dim{j_a} 
    &= 2^{q-1} \prod_{a=1}^q \dim{j_a} 
    \\
    \dim K = \frac{1}{2} \prod_{a=q+1}^r \dim{n_a} \dim{j_a}
    &= 2^{r-q-1} \prod_{a=q+1}^r \dim{j_a}
\end{align*}
$$

Since $T$ is of even parity, the nonzero components are $T^{0 0}, T^{1 1}$ (I call them the **even block** and the **odd block**, respectively). Now we perform the corresponding matrix decomposition on the four $T^{MN}$:

$$
T_{J K}^{M N} = A_{J j}^{M N} B_{j K}^{M N} 
\xrightarrow{\text{nonzero}}
\begin{cases}
    T_{J K}^{0 0} = A_{J j}^{0 0} B_{j K}^{0 0} \\
    T_{J K}^{1 1} = A_{J j}^{1 1} B_{j K}^{1 1}
\end{cases}
$$

From the properties of the matrix decomposition, the new normal index $j$ will have dimension

$$
\begin{align*}
    \dim j &= \min{(\dim{J}, \dim{K})} \\
    &= \min{\left(
        \frac{1}{2} \prod_{a=1}^q \dim{n_a} \dim{j_a}, \quad 
        \frac{1}{2} \prod_{a=q+1}^r \dim{n_a} \dim{j_a}
        \right)}
\end{align*}
$$

Since $A^{0 1}, A^{1 0}, B^{0 1}, B^{1 0}$ are all zero, this enables us to rewrite the decomposition as

$$
\left.
\begin{align*}
    T_{J K}^{0 0} &= A_{J j}^{0 0} B_{j K}^{0 0} +  A_{J j}^{0 1} B_{j K}^{1 0} \\
    T_{J K}^{0 1} &= A_{J j}^{0 0} B_{j K}^{0 1} +  A_{J j}^{0 1} B_{j K}^{1 1} \\
    T_{J K}^{1 0} &= A_{J j}^{1 0} B_{j K}^{0 0} +  A_{J j}^{1 1} B_{j K}^{1 0} \\
    T_{J K}^{1 1} &= A_{J j}^{1 0} B_{j K}^{0 1} +  A_{J j}^{1 1} B_{j K}^{1 1} \\
\end{align*}
\right\} \Longrightarrow
T_{J K}^{M N} = \sum_{n,j} A_{J j}^{M n} B_{j K}^{n N}
$$

Now we can split the merged indices to recover the tensor shape, obtaining the formula:

$$
T_{j_1 ... j_q,  j_{q+1} ... j_r}^{n_1 ... n_q,  n_{q+1} ... n_r}
= A_{j_1 ... j_q, j}^{n_1 ... n_q, n} B_{j, j_{q+1} ... j_r}^{n, n_{q+1} ... n_r} 
$$

Here summation over $n,j$ is implied. By construction, the decomposition result $A, B$ are both of *even* parity, i.e. have $Z_2$ symmetry.