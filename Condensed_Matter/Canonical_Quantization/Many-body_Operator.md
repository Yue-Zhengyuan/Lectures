# Many-Body Operators after Second Quantization

## One-body Operators

The one-body term takes the general form

$$
T = \sum_{i} T(i)
$$

Here the summation is over the particle labels. 

<div class="result">

**Lemma for one-body operators:**

</div><br>

----

*Proof*:

<div align="right">QED.</div>

----

Let us calculate its action on the symmetrized states (using an orthonormal set of one-body basis states):

## Two-body Operators

The two-body interaction term takes the general form

$$
V = \sum_{i < j} V(i,j),
\qquad V(i,j) = V(j,i)
$$

Because of the symmetry property of each term, we can also write

$$
V = \frac{1}{2} \sum_{i \ne j} V(i,j)
$$

<div class="result">

**Lemma for two-body operators:**

$$
\begin{align*}
    &a_r^\dagger a_s^\dagger a_{s'} a_{r'}
    S_\pm(N) \ket{r_1,...,r_N}
    \\
    &= \sum_{i\ne j} \delta_{r',r_i} \delta_{s',r_j}
    S_\pm(N) \ket{...,r,...,s,...}
\end{align*}
$$

</div><br>

----

*Proof*: First, act $a_{r'}$ on the symmetrized state:

$$
\text{LHS}
= a_r^\dagger a_s^\dagger a_{s'} \frac{1}{\sqrt{N}}
\sum_{i=1}^N (\pm 1)^{i+1} \delta_{r',r_i}
S_\pm(N-1) \ket{r_1,...,\cancel{r_i},...,r_N}
$$

Next, for the action of $a_{s'}$, since we have already removed the $i$th particle, the particles $j$ removed by $a_{s'}$ must satisfy $j \ne i$. However, the parity factor is slightly different for $j < i$ and $j > i$:

$$
\begin{align*}
    \text{LHS}
    &= \frac{1}{\sqrt{N(N-1)}}
    a_r^\dagger a_s^\dagger \sum_{i=1}^N (\pm 1)^{i+1} 
    \\ &\qquad \times \bigg(
        \sum_{j<i} (\pm 1)^{j+1} 
        \delta_{s',r_j} \delta_{r',r_i}
        S_\pm(N-2) \ket{...,\cancel{r_j},...,\cancel{r_i},...}
        \\ &\qquad \qquad +
        \sum_{j>i} (\pm 1)^{j}
        \delta_{s',r_j} \delta_{r',r_i}
        S_\pm(N-2) \ket{...,\cancel{r_i},...,\cancel{r_j},...}
    \bigg)
\end{align*}
$$

Finally we put the two particle back using $a_r, a_s$:

$$
\begin{align*}
    \text{LHS} 
    &= \sum_{i=1}^N 
    \bigg(
        \sum_{j<i} (\pm 1)^{i+j} 
        \delta_{s',r_j} \delta_{r',r_i} S_\pm(N) 
        \ket{r,s,...,\cancel{r_j},...,\cancel{r_i},...}
        \\ &\quad \quad +
        \sum_{j>i} (\pm 1)^{i+j+1} 
        \delta_{s',r_j} \delta_{r',r_i} S_\pm(N) 
        \ket{r,s,...,\cancel{r_i},...,\cancel{r_j},...}
    \bigg)
\end{align*}
$$

To put $r,s$ back to the original place $r_i = r', r_j = s'$:

- When $j < i$:
    
    - Swap $s$ with $r_1,...,r_{j-1}$, contributing $(\pm 1)^{j-1}$;
    - Swap $r$ with $r_1, ...,r_j = s,..., r_{i-1}$, contributing $(\pm 1)^{i-1}$

    Thus the total parity factor is $(\pm 1)^{2(i+j)-2} = 1$.

- When $j > i$

    - Swap $s$ with $r_1,...,\cancel{r_i},...,r_{j-1}$, contributing $(\pm 1)^{j-2}$;
    - Swap $r$ with $r_1, ...,r_{i-1}$, contributing $(\pm 1)^{i-1}$

    Thus the total parity factor is still $(\pm 1)^{2(i+j) +1-3} = 1$.

Thus in both cases the parity factor are canceled, and we obtain the desired result

$$
\text{LHS} = \sum_{i\ne j} \delta_{r',r_i} \delta_{s',r_j}
S_\pm(N) \ket{...,r,...,s,...}
$$

<div align="right">QED.</div>

----

With this lemma, let us calculate the action of $V$ on the symmetrized states (using orthonormal one-body basis) is

$$
\begin{align*}
    &V S_\pm \ket{r_1,...,r_N}
    \\
    &= \frac{1}{2} S_\pm \sum_{i \ne j} 
    V(i,j) \ket{...,r_i,...,r_j,...}
    \\
    &= \frac{1}{2} S_\pm \sum_{i\ne j}
    \ket{...,\cancel{r_i},...,\cancel{r_j},...}
    \otimes V\ket{r_i,r_j}
    \\
    &= \frac{1}{2} S_\pm \sum_{i\ne j}
    \ket{...,\cancel{r_i},...,\cancel{r_j},...}
    \otimes \sum_{r,s} \ket{r,s} \amp{r,s}{V}{r_i,r_j}
    \\
    &= \frac{1}{2} \sum_{r,s} \amp{r,s}{V}{r_i,r_j}
    \sum_{i\ne j} S_\pm \ket{...,r,...,s,...}
    \\
    &= \frac{1}{2} \sum_{r,s}
    \sum_{r',s'} \bra{r,s} V 
    \ket{r',s'} \braket{r',s'}{r_i,r_j}
    \sum_{i\ne j} S_\pm \ket{...,r,...,s,...}
    \\
    &= \frac{1}{2} \sum_{r,s}
    \sum_{r',s'} \bra{r,s} V 
    \ket{r',s'} \delta_{r',r_i} \delta_{s',r_j}
    \sum_{i\ne j} S_\pm \ket{...,r,...,s,...}
\end{align*}
$$

By comparison with the lemma, we finally have

<div class="result">

**Two-body interaction after second quantization:**

$$
V = \frac{1}{2} \sum_{r,s} \sum_{r',s'} 
a_r^\dagger a_s^\dagger
\amp{r,s}{V}{r',s'} a_{s'} a_{r'}
$$

The summation is over the one-body orthonormal basis states. 

</div><br>

### Using Field Operators

If we use the position eigenstates $\ket{x}$ as the one-body basis, we immediately obtain

$$
V = \frac{1}{2} \int dx \, dy \, dx' \, dy' \,
\phi^\dagger(x) \phi^\dagger(y) \amp{x,y}{V}{x',y'}
\phi(y') \phi(x')
$$

When $V(i,j)$ is a function of $x_i, x_j$, the amplitude can be expressed as

$$
\begin{align*}
    \amp{x,y}{V}{x',y'}
    &= V(x',y') \braket{x,y}{x',y'}
    \\
    &= V(x',y') \delta(x-x') \delta(y-y')
\end{align*}
$$

Then we can remove the integration over $x', y'$ and write

<div class="result">

**Two-body interaction in terms of field operators:**

$$
V = \frac{1}{2} \int dx \, dy \, 
\phi^\dagger(x) \phi^\dagger(y) V(x,y)
\phi(y) \phi(x)
$$

</div><br>
