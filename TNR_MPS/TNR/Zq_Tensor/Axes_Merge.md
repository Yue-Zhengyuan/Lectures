# Merging and Splitting Axes of $Z_n$ Tensors

For ordinary tensor contraction, it is valid to first merge the axes to be contracted, then contract over this merged axis. Mathematically:

$$
\sum_{i_1, ..., i_r} A_{... (i_1 ... i_r) ...} B_{... (i_1 ... i_r) ...}
\xrightarrow{\text{merge axes}}
\sum_I A_{... I ...} B_{... I ...}
$$

where $I$ is constructed as (using the "row-major" rule, as in Python and C, and define $\prod_{b=r}^r \dim{i_b} \equiv 1$)

$$
I(i_1, ..., i_r)
= \sum_{a=1}^r \left( {i_a \prod_{b=a}^r \dim{i_b}} \right), \quad
0 \le i_a < \dim{i_a}
$$

However, the ordinary axes merging rule *cannot preserve the $Z_2$ symmetry* of the tensor. It turns out that we borrow our knowledge of *Grassmann tensors* to construct *symmetry-preserving* axes merging (or splitting) rules. 

Suppose we want to merge $r$ axes of a $Z_2$ tensor $T$ such that

$$
T_{... (i_1 ... i_r) ...} \rightarrow T_{... I ...}
$$

First, let us put $T$ into the "Grassmann form": we split each index $i_a$ into two parts $(j_a, n_a)$:

$$
i_a \equiv 2 j_a + n_a, \quad
0 \le j_a < \frac{1}{2} \dim{i_a}, \quad n_a = 0, 1
$$

which is equivalent to a *ordinary reshaping* of $T$:

$$
T_{... i_1 i_2 ... i_r ...} \rightarrow
T_{... (j_1 n_1) (j_2 n_2) ... (j_r n_r) ...} \equiv
T_{... j_1 j_2 ... j_r ...}^{... n_1 n_2 ... n_r ...}
$$

Note here we put the $n$'s to the superscript, which is not very conventional, but makes the notation more similar to that of Grassmann tensors. The nonzero elements obviously satisfy

$$\sum \dim{\text{(original axis)}} = 0 \Longrightarrow 
\sum \dim{\text{(} n \text{-part of axis)}} = 0\pmod{2}$$

thus $T_{... j_1 j_2 ... j_r ...}^{... n_1 n_2 ... n_r ...}$ is similar to Grassmann tensors of *even parity*. But it does not have a series of Grassmann variables following, so we do not need to worry about minus signs when permuting the axes of $Z_2$ tensors. 

After the splitting of $i_a$ to $(n_a, j_a)$, we make the conversion

$$
T_{... (j_1 j_2 ... j_r) ...}^{... (n_1 n_2 ... n_r) ...}
\rightarrow T_{... J ...}^{... N ...}
$$

using the parity-preserving rule for the Grassmann tensors. We repeat it below:

----------
Case 1:
- $n_1 + \cdots + n_r = 0 \pmod{2}$
- $(n_1, ..., n_r)$ is the $J_g^0$th *even*-parity Grassmann index of length $r$
- $(j_1, ..., j_r)$ is the $J_n$th normal index of length $r$

$$ \Rightarrow N = 0, \quad J = J_g^0 \prod_{a=1}^r \dim{j_a} + j_n $$

Case 2:
- $n_1 + \cdots + n_r = 1 \pmod{2}$
- $(n_1, ..., n_r)$ is the $J_g^1$th *odd*-parity Grassmann index of length $r$
- $(j_1, ..., j_r)$ is the $J_n$th normal index of length $r$

$$ \Rightarrow N = 1, \quad J = J_g^1 \prod_{a=1}^r \dim{j_a} + J_n $$

The numbers $J_g^{(0,1)}, J_n$ can all be counted using a for-loop in computer programs; their ranges are

$$
0 \le J_g^{(0,1)} < 2^{r-1} \equiv \dim{J_g^{(0,1)}}, \quad
0 \le J_n < \prod_{a=1}^r \dim{j_a} \equiv \dim{J_n}
$$

Dimension check: 

$$
\dim J = \dim J_g^{(0,1)} \dim J_n 
= \frac{1}{2} \prod_{a=1}^r \dim{n_a} \dim{j_a}
= \frac{1}{2} \prod_{a=1}^r \dim{i_a}
$$

$$
\dim{N} \dim{J} = 2 \dim{J} = \prod_{a=1}^r \dim{i_a}
$$

----------

Finally, we combine $(J,N)$ back to $I$:

$$
I = 2J + N
$$

thus finishing the axis merging, without affecting the $Z_2$ symmetry of the tensor $T$. 
