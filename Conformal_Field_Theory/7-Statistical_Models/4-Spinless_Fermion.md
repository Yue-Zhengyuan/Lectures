# Spinless Fermion

$$
H = -t \sum_{\langle i,j \rangle} 
(c_i^\dagger c_j + h.c.)
+ V \sum_{\langle i,j \rangle} n_i n_j
$$

## Free Fermion $(V = 0)$

### Fourier Transform of the Fermion Operators

To see the energy levels more clearly, we shall go to the momentum space (reciprocal lattice). Let the number of sites be $N$; the $i$th site at the $i$th is at the lattice position $\bold{r}_i$.

Discrete Fourier transform and its inverse ($a$ is again the lattice spacing):

$$
\begin{aligned}
    c_\bold{k} &= \sum_n 
    c_n e^{-i \bold{k}\cdot \bold{r}_n} \\
    c_\bold{k}^\dagger &=  \sum_n 
    c_n^\dagger e^{+i \bold{k}\cdot \bold{r}_n}
\end{aligned}
\, \Longleftrightarrow \,
\begin{aligned}
    c_i &= \frac{1}{N} \sum_\bold{k} c_\bold{k} 
    e^{+i \bold{k}\cdot \bold{r}_i} 
    \\
    c_i^\dagger &= \frac{1}{N} \sum_\bold{k}
    c_\bold{k}^\dagger 
    e^{-i \bold{k}\cdot \bold{r}_i}
\end{aligned}
$$

where $n$ sums over the lattice sites, and $k$ sums over the reciprocal lattice in the 1st Brillouin zone (BZ). This transform is based on the following orthogonal and completeness relations:

$$
\begin{aligned}
    \sum_n e^{i (\bold{k} - \bold{k}') \cdot \bold{r}_n} 
    &= N \delta_{\bold{k}, \bold{k}'}
    \\
    \sum_\bold{k} e^{i \bold{k} \cdot (\bold{r}_m - \bold{r}_n)} 
    &= N \delta_{m,n}
\end{aligned}
$$

Boundary condition will alow different values of the momentum $k$. We explain this in one dimension:

- PBC: $c_{i+N} = c_i$

    $$
    e^{-ikNa} = 1
    \, \Rightarrow \, 
    kNa = 2\pi m \quad (m \in \mathbb{Z})
    $$

    Restricting the value of $k$ in 1st Brillouin zone, we have

    $$
    k = \frac{2\pi m}{Na} \qquad
    m \in \mathbb{Z} \cap 
    \left[-\frac{N}{2}, \frac{N}{2}\right]
    $$

- Anti-PBC: $c_{i+N} = -c_i$
    
    $$
    e^{-ikNa} = -1
    \, \Rightarrow \, 
    kNa = 2\pi \left(m + \frac{1}{2}\right) 
    \quad (m \in \mathbb{Z})
    $$

    Restricting the value of $k$ in 1st Brillouin zone, we have

    $$
    k = \frac{2\pi}{Na}
    \left(m + \frac{1}{2} \right) \qquad
    m \in \mathbb{Z} \cap 
    \left[-\frac{N}{2}, \frac{N}{2}\right]
    $$

