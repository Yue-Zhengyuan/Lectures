# Axis Merging and Split of Grassmann Tensors

*Program implementation*: 
- Merging: `gtensor.merge_axes`
- Split: `gtensor.split_axes`

Suppose we merge the axes of a Grassmann tensor $\mathbf{T}(\eta)$ into several groups, each containing $r,s,...$ consecutive axes. The reshaped tensor elements $\mathbf{T}^\prime$ is related to the old elements $\mathbf{T}$ by

$$
(\mathbf{T}^\prime)_{I J...}^{M N...}
= \mathbf{T}_{(i_1 ... i_r)(j_1 ... j_s)...}^{(m_1 ... m_r)(n_1 ... n_s)...}
$$

where $I,J,...$ and $M,N,...$ are the normal and the Grassmann indices of the merged axes. The inverse operation is just the splitting of axes. 

## Rule of Merging Axes

The conversion rule from $(m_1, ..., m_r), (i_1, ..., i_r)$ to $M,I$ is as follows: 

- **New Grassmann Index $M$**

    The rule to determine $M$ is very simple:

    - $m_1 + \cdots + m_r = 0 \pmod{2} \Rightarrow M = 0$
    - $m_1 + \cdots + m_r = 1 \pmod{2} \Rightarrow M = 1$

- **New Normal Index $I$**

    Let us assign a number to order all indices $(m_1, ..., m_r)(i_1, ..., i_r)$ of the even-parity or odd-parity part (depending on whether we are treating the $M = 0$ or $M = 1$ part) in (conventionally) ascending order. *This new label will be the new normal index*.

    The dimension of the new normal index is

    $$
    \dim{I[M]} = 
    \sum_{\sum m = M}
    \left(
        \prod_{k=1}^r \dim{i_k[m_k]}
    \right)
    $$

    Here we omitted $\text{mod } 2$ in $\sum m = M$. 

----

**Example:** For $\mathbf{T}_{(i_1 i_2)}^{(n_1 n_2)} \rightarrow \mathbf{T}_I^N$ with shape

$$
\dim{i_1} = 
\begin{cases}
    2, & n_1 = 0 \\
    1, & n_1 = 1
\end{cases}
, \quad
\dim{i_2} = 
\begin{cases}
    2, & n_2 = 0 \\
    1, & n_2 = 1
\end{cases}
$$

Then the old indices are merged to 

<center>

<table>
    <thead>
        <th><i>N <th>{<i>n</i>} <th>{<i>i</i>} <th><i>I
    </thead>
    <tbody>
        <tr><td rowspan=5>0 <td rowspan=4><code>(0,0) <td><code>(0,0) <td>0
        <tr><td><code>(0,1) <td>1
        <tr><td><code>(1,0) <td>2
        <tr><td><code>(1,1) <td>3
        <tr><td><code>(1,1) <td><code>(0,0) <td>4
        <tr><td rowspan=4>1 <td rowspan=2><code>(0,1) <td><code>(0,0) <td>0
        <tr><td><code>(0,1) <td>1
        <tr><td rowspan=2><code>(1,0) <td><code>(0,0) <td>2
        <tr><td><code>(1,0) <td>3
    </tbody>
</table>

</center>

The dimension of the new normal index $I$ is therefore

$$
\dim{I} = 
\begin{cases}
    5, &N = 0 \\
    4, &N = 1
\end{cases}
$$

----

### Interpretation of the Rule

In the following axis merging

$$
\mathbf{T}_{(i_1 ... i_r)(j_1 ... j_s)...}^{(m_1 ... m_r)(n_1 ... n_s)...}
\xrightarrow{\text{merge}} 
\mathbf{T}_{I J...}^{M N...}
$$

For a given new block $T^{M N ...}$, the corresponding (of correct parity) old Grassmann indices $(m_1 ... m_r)(n_1 ... n_s)...$ divide this new block into 

$$
\left( \frac{1}{2} \prod_{a=1}^{r} \dim{m_a} \right)
\times
\left( \frac{1}{2} \prod_{a=1}^{s} \dim{n_a} \right)
\times \cdots
= 2^{r-1} \times 2^{s-1} \times \cdots
$$

*sub*-blocks. 

Now we arrange the allowed old Grassmann indices in ascending order. Suppose that the index $(m_1 ... m_r)(n_1 ... n_s)...$ corresponding to the label $(I_m, I_n, ...)$, then the sub-block at the position $(I_m, I_n, ...)$ is just the old block $T^{(m_1 ... m_r)(n_1 ... n_s)...}$ reshaped to the new shape

$$
\left( \frac{1}{2} \prod_{a=1}^{r} \dim{i_a[m_a]} \right)
\times
\left( \frac{1}{2} \prod_{a=1}^{s} \dim{j_a[n_a]} \right)
\times \cdots
$$

*Remark*: 

The new Grassmann index $M$ indicate whether the whole group $\eta_1^{m_1}...\eta_r^{m_r}$ behaves like a fermion (i.e. is the product of an odd number of Grassmann numbers). The various combinations of $\{\eta\}$ is now regarded as "internal states" of this new fermion, labelled by the new normal index $I$. 

----

### Parity of the Reshaped Tensor

By construction

$$
M = \sum_{a=1}^r m_a, \quad N = \sum_{a=1}^s n_a, \quad \cdots \pmod 2
$$

Thus 

$$
M + N + \cdots = \sum_{a=1}^r m_a + \sum_{a=1}^s n_a + \cdots \pmod 2
$$

i.e. the reshaped tensor $T^\prime$ has the *same parity* as the original tensor $T$.

### The `order = -1` Option

Sometimes we may want to merge the axes in *reversed order*:

$$
\mathbf{T}_{i_1 ... i_r}^{n_1 ... n_r}
\xrightarrow{\text{transpose}}
{\mathbf{T}'}_{i_r ... i_1}^{n_r ... n_1}
\xrightarrow{\text{merge}}
\mathbf{T}_I^N
$$

The program will first reverse the order of axes to be merged, then merge the axes. Similar caution should also be raised when using the inverse operation to split an axis. 

This modified rule can be interpreted as follows: consider the following axis merging

$$
\mathbf{T}_{(i_1 ... i_r)(j_1 ... j_s)...}^{(m_1 ... m_r)(n_1 ... n_s)...}
\xrightarrow{\text{transpose}}
{\mathbf{T}^\prime}_{(i_1 ... i_r)(j_s ... j_1)...}^{(m_1 ... m_r)(n_s ... n_1)...}
\xrightarrow{\text{merge}}
\mathbf{T}_{I J...}^{M N...}
$$

(`order = -1` option is applied to the axis $(N,J), ...$)

For a given new block $T^{M N ...}$, the corresponding (of correct parity) old Grassmann indices $(m_1 ... m_r)(n_s ... n_1)...$ still divide this new block into 

$$
\left( \frac{1}{2} \prod_{a=1}^{r} \dim{m_a} \right)
\times
\left( \frac{1}{2} \prod_{a=1}^{s} \dim{n_a} \right)
\times \cdots
= 2^{r-1} \times 2^{s-1} \times \cdots
$$

*sub*-blocks. 

Now we arrange the allowed old Grassmann indices in ascending order. Suppose that the index $(m_1 ... m_r)(n_1 ... n_s)...$ (using the original order) corresponding to the label $(I_m, I_n, ...)$, then the sub-block at the position $(I_m, I_n, ...)$ is just the old block $(T^\prime)^{(m_1 ... m_r)(n_s ... n_1)...}$ *first ordinarily transposed to original order*, then *reshaped* to the new shape

$$
\left( \frac{1}{2} \prod_{a=1}^{r} \dim{i_a[m_a]} \right)
\times
\left( \frac{1}{2} \prod_{a=1}^{s} \dim{j_a[n_a]} \right)
\times \cdots
$$

## Transposition of Merged Axis

If transposition happened *after* axis merging, does the transposition affect the "internal structure" of the merged axes? 

As an example, suppose we perform

$$
\mathbf{T}_{i_1 (i_2 i_3 i_4) i_5}^{n_1 (n_2 n_3 n_4) n_5}
\xrightarrow{\text{merge}}
\mathbf{T}_{i_1 I i_5}^{n_1 N n_5}
\xrightarrow{\text{transpose}}
\mathbf{T}_{i_1 i_5 I}^{n_1 n_5 N}
$$

- Corresponding code:

    ```python
    a = a.merge_axes((1,3,1), (1,-1,1))
    a = a.transpose(0,2,1)
    ```

It turns out that this is equivalent to:

$$
T_{i_1 (i_2 i_3 i_4) i_5}^{n_1 (n_2 n_3 n_4) n_5}
\xrightarrow{\text{transpose}}
T_{i_1 i_5 (i_2 i_3 i_4)}^{n_1 n_5 (n_2 n_3 n_4)}
\xrightarrow{\text{merge}}
T_{i_1 I i_5}^{n_1 N n_5}
$$

- Corresponding code:

    ```python
    a = a.transpose(0,4,1,2,3)
    a = a.merge_axes((1,1,3), (1,1,-1))
    ```

In other words, transposition does *not* affect the order of the original axes contained in the merged axis. This is still true if the merging is performed with option `order = -1`. Such behaviors are the same as ordinary tensors. 