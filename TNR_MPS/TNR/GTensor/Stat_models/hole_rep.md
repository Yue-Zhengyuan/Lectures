# Trotter Gate: <br>Hole Representation

## Spinon and Hole

In the **hole representation**, the fermion annihilation operator $c_{i,\sigma}$ is decomposed to

$$
c_{i,\sigma} = h_i^\dagger b_{i,\sigma}
$$

i.e. annihilate the **spinon** (*boson*) and then create a **hole** (*fermion*). 

The commutation rules for holes and spinons are:

- Hole (fermion anti-commutation rules)

$$
\{h_i,h_j\} = 0, \quad
\{h_i^\dagger, h_j^\dagger\} = 0, \quad
\{h_i, h_j^\dagger\} = \delta_{i j}
$$

- Spinon (boson commutation rules)

$$
[b_{i,\sigma}, b_{j, \sigma^\prime}] = 0, \quad 
[b_{i,\sigma}^\dagger, b_{j, \sigma^\prime}^\dagger] = 0, \quad
[b_{i,\sigma}, b_{j, \sigma^\prime}^\dagger] = \delta_{i j} \delta_{\sigma \sigma^\prime}
$$

- Holes *commute* with spinons

## Other Operators in Hole Representation

### Fermion creation operator $c_{i,\sigma}^\dagger$

$$
c_{i,\sigma}^\dagger = b_{i,\sigma}^\dagger h_i
$$

i.e. annihilate the hole and create a spinon.

### Fermion number operator $n_{i,\sigma} \equiv c_{i,\sigma}^\dagger c_{i,\sigma}$:

In the hole representation, the number of fermions is the same as the number of spinons. Therefore

$$
n_{i,\sigma} = n_{i,\sigma}^b
$$

where $n_i^h, n_{i,\sigma}^b$ are hole and spinon number operators, respectively. 

### Spin operators (Pauli matrix)

In the $| \uparrow (\downarrow) \rangle$ basis, the Pauli matrices are

$$
\tau^1 = 
\begin{pmatrix}
    0 & 1 \\ 1 & 0
\end{pmatrix}
, \quad
\tau^2 = 
\begin{pmatrix}
    0 & -i \\ i & 0
\end{pmatrix}
, \quad
\tau^3 = 
\begin{pmatrix}
    1 & 0 \\ 0 & -1
\end{pmatrix}
$$

Then

$$
S_i^\alpha = \sum_{\sigma,\sigma^\prime} 
b_{i,\sigma}^\dagger \tau_{\sigma,\sigma^\prime}^\alpha
b_{i,\sigma^\prime}
$$

## No-Double-Occupancy Constraint

The hole representation is applicable only when there can be *no more than one* particle on each site, i.e. either one particle or one hole. This is stated by the **no-double-occupancy** constraint:

$$
\sum_{\sigma} b_{i,\sigma}^\dagger b_{i,\sigma}
+ h_i^\dagger h_i 
= \sum_{\sigma} n_{i,\sigma}^b + n_i^h
= 1
$$

This constraint reveals itself in the tensor by forcing the elements breaking the rule to vanish. For models which does not obey this constraint, we need to use the method described [here](spin_fermion.md) to construct the Trotter gate. 

## Basis States

We have the following set of basis for each site:

- Spin-up/down states: 
    $$
    |\sigma_i \rangle \equiv b_{i,\sigma}^\dagger |0 \rangle, \quad
    \sigma \in \{\uparrow,\downarrow\}
    $$
- Hole (empty) state: 
    $$
    |h_i \rangle \equiv h_i^\dagger |0 \rangle
    $$

Under the no-double-occupancy constraint, this set of basis is *complete*:

$$
|\uparrow_i \rangle \langle \uparrow_i |
+ |\downarrow_i \rangle \langle \downarrow_i |
+ |h_i \rangle \langle h_i | = 1_i
$$

We can also use the fermion coherent state for the holes:

$$
| \eta_i \rangle \equiv (1 - \eta_i h_i^\dagger) |0\rangle
= |0\rangle - \eta_i |h_i\rangle
$$

with its "conjugate":

$$
\langle \eta_i | = \langle 0 | (1 - h_i \bar{\eta}_i)
= \langle 0 | - \langle h_i| \bar{\eta}_i
$$

Then we can verify that

$$
\begin{align*}
    \int g_{\bar{\eta}_i \eta_i}
    |\eta_i\rangle \langle \eta_i |
    &=
    \int d \bar{\eta}_i d\eta_i \, e^{-\bar{\eta}_i \eta_i} 
    \eta_i |h_i\rangle \langle h_i| \bar{\eta}_i
    \\ &=
    \int d \bar{\eta}_i d\eta_i \,
    (1 - \bar{\eta}_i \eta_i)
    \eta_i \bar{\eta}_i |h_i\rangle \langle h_i| 
    \\ &=
    \int d \bar{\eta}_i d\eta_i \, 
    \eta_i \bar{\eta}_i |h_i\rangle \langle h_i| 
    \\ &=
    |h_i\rangle \langle h_i| 
\end{align*}
$$

Thus the completeness relation (resolution of identity) becomes

$$
\sum_{\sigma} |\sigma_i \rangle \langle \sigma_i |
+ \int g_{\bar{\eta}_i \eta_i}
    |\eta_i\rangle \langle \eta_i |
= 1_i
$$

We notice that

$$
\int g_{\bar{\eta}_i \eta_i}
= \int d \bar{\eta}_i d\eta_i \,
    (1 - \bar{\eta}_i \eta_i) = 1
$$

Therefore, we are free to integrate the operator $|\sigma_i \rangle \langle \sigma_i |$ (which contains no Grassmann numbers) over $g$:

$$
\int g_{\bar{\eta}_i \eta_i} \,
\left(
    \sum_{\sigma} |\sigma_i \rangle \langle \sigma_i |
    + |\eta_i\rangle \langle \eta_i |
\right) = 1_i
$$

To save writing, we shall now start using

$$
|\eta_i \rangle \in \{
    |\uparrow_i \rangle, 
    |\downarrow_i \rangle, 
    |\eta_i \rangle
\}
$$ 

to collectively represent the spin states and the hole states (which is a slight abuse of notation), so that the resolution of identity can be compactly written as

$$
\sum_{\eta} \int g_{\bar{\eta}_i \eta_i} 
|\eta_i\rangle \langle \eta_i |
= 1_i
$$

Here $\sum_\eta$ means summation over the spin-up/down states and the hole coherent state, but $\int g_{\bar{\eta}_i \eta_i}$ integrates over the coherent states only. 

## Imaginary Time Evolution and Trotter Gate

As in the spinless case, we consider (1+1)d systems (using PBC) whose Hamiltonian consists of nearest-neighbor interactions only:

$$
H = \sum_i H_{i, i+1}
$$

and insert identities into the propagator

$$
\langle \eta^\prime | e^{-\beta H} | \eta \rangle
$$

so that each evolution slice corresponds to evolution by imaginary time $\epsilon \equiv \beta / M$:

$$
\begin{align*}
    &\langle \eta^\prime | e^{-\beta H} | \eta \rangle
    =
    \langle \eta^\prime | 
    e^{-\epsilon H} 1 e^{-\epsilon H} 1 ... 1 e^{-\epsilon H}
    | \eta \rangle
    \\
    &= 
    \sum_{\eta^1, ..., \eta^{M-1}}\int 
    \langle \eta^M | e^{-\epsilon H} | \eta^{M-1} \rangle
    g_{\bar{\eta}^{M-1} \eta^{M-1}} \cdots
    \\ & \qquad \qquad \cdots
    g_{\bar{\eta}^2 \eta^2}
    \langle \eta^2 | e^{-\epsilon H} | \eta^1 \rangle
    g_{\bar{\eta}^1 \eta^1}
    \langle \eta^1 | e^{-\epsilon H} | \eta^0 \rangle
\end{align*}
$$

where $|\eta^k\rangle$ is the state after $k$ evolution layers, and $\eta^0 \equiv \eta, \eta^M \equiv \eta^\prime$. 

Each layer of evolution can further be separated to 

$$
\begin{align*}
    &\langle \eta^{l+1} | e^{-\epsilon H} | \eta^{l} \rangle 
    =
    \langle \eta^{l+1} | e^{-\epsilon (H_e+H_o)} | \eta^{l} \rangle 
    \\ &\xrightarrow[\text{decomposition}]{\text{Trotter}}
    \langle \eta^{l+1} | e^{-\epsilon H_e} e^{-\epsilon H_o} | \eta^{l} \rangle 
    \\ &\xrightarrow[\text{relabel layers}]{\text{insert identity}}
    \sum_{\eta^{2k+1}} \int
    \langle \eta^{2k+2} | e^{-\epsilon H_e} | \eta^{2k+1} \rangle
    g_{\bar{\eta}^{2k+1} \eta^{2k+1}}
    \langle \eta^{2k+1}|e^{-\epsilon H_o} | \eta^{2k} \rangle 
\end{align*}
$$

where

$$
H_e = \sum_{i \text{ even}} H_{i, i+1}, \quad
H_o = \sum_{i \text{ odd}} H_{i, i+1}
$$

Then each layer of evolution involves $H_e$ or $H_o$ only. The terms in $H_e$ (or $H_o$) obviously commute, then we can proceed further and write

$$
\begin{align*}
    \langle \eta^{n+1} | e^{-\epsilon H_e} | \eta^{n} \rangle
    &= \prod_{i \text{ even}}
    \langle \eta_{i}^{n+1} \eta_{i+1}^{n+1} | 
    e^{-\epsilon H_{i, i+1}} | 
    \eta_{i}^{n} \eta_{i+1}^{n} \rangle
    \\
    \langle \eta^{n+1} | e^{-\epsilon H_o} | \eta^{n} \rangle
    &= \prod_{i \text{ odd}}
    \langle \eta_{i}^{n+1} \eta_{i+1}^{n+1} | 
    e^{-\epsilon H_{i, i+1}} | 
    \eta_{i}^{n} \eta_{i+1}^{n} \rangle
\end{align*}
$$

Now we obtain the elements of the two-site **Trotter gate** evolving from state $|\eta\rangle$ to state $|\theta\rangle$:

$$
\langle \theta_i \theta_{i+1} | 
e^{-\epsilon H_{i, i+1}} | 
\eta_i \eta_{i+1} \rangle
$$

which can be obtained from 

$$
\langle \theta_i \theta_{i+1} | H_{i,i+1} | \eta_i \eta_{i+1} \rangle
$$

via direct exponentiation 

$$
e^{-\epsilon H} \cong 1 - \epsilon H 
+ \frac{1}{2!}(-\epsilon H)^2 - \cdots
$$

## Tensor Elements of Trotter Gate

Suppose that

$$
|\theta_i \rangle \in \{
    \underbrace{
        |\uparrow_i \rangle, 
        |\downarrow_i \rangle
    }_{|j_i \rangle}, 
    |\theta_i \rangle
\}, \quad
|\eta_i \rangle \in \{
    \underbrace{
        |\uparrow_i \rangle, 
        |\downarrow_i \rangle
    }_{|k_i \rangle}, 
    |\eta_i \rangle
\}
$$

It corresponds to a set of numbers $\mathbf{T}$ by the relation

$$
\begin{align*}
    &\sum_{\theta, \eta} 
    \langle \theta_i \theta_{i+1} | H_{i,i+1} | \eta_i \eta_{i+1} \rangle 
    \\ &= 
    \sum_{m,n=0,1} \sum_{j,k=0,1}
    T_{j_{i+1} j_i k_i k_{i+1}}^{m_{i+1} m_i n_i n_{i+1}}
    \bar{\theta}_{i+1}^{m_{i+1}} \bar{\theta}_i^{m_i} 
    \eta_i^{n_i} \eta_{i+1}^{n_{i+1}} 
    \\
    &\equiv \sum_{m,n=0,1} 
    \mathbf{T}(\bar{\theta},\eta)_{j_{i+1} j_i k_i k_{i+1}}^{m_{i+1} m_i n_i n_{i+1}}
    \qquad
    m, n = 0, 1
\end{align*}
$$

The inclusion of the summation $\sum_{\theta, \eta}$ is to take the complete basis at each site into account. Compared with the spinless case, the object $\mathbf{T}$ now carries *subscripts*. 

As in the spinless case, the **2-dimensional** superscript (say) $n_i$ can be interpreted as

$$
0: \text{Filled (no hole)}, \quad
1: \text{Empty (hole)}
$$

The dimension of subscript (say) $k_i$ (corresponding to the state $|\eta_i \rangle$) **depends on the value of $n_i$**:

- $n_i = 0$ (filled): 2-dimensional, value determined by
    - 0: spin up
    - 1: spin down
- $n_i = 1$ (empty): 1-dimensional

The other subscripts are found in a similar way. 

### The Identity Gate

The elements of identity gate are found from

$$
\sum_{\theta, \eta}
\langle \theta_i \theta_{i+1} | \eta_i \eta_{i+1} \rangle
$$

By physical considerations, the number of spins/holes must be conserved at each site under the action of identity gate. Thus we only need to calculate the following cases:

#### Case 1: Both sites are filled

$$
\langle j_i j_{i+1} | k_i k_{i+1} \rangle 
= \langle j_i | k_i \rangle \langle j_{i+1} | k_{i+1} \rangle
$$

Since this case does not contain any Grassmann numbers, it contributes to $2 \times 2 = 4$ terms

<center>

|Grassmann index|Normal index|Element|
|:-:|:-:|:-:|
|`(0,0,0,0)`|$(\sigma_{i+1},\sigma_i,\sigma_i,\sigma_{i+1})$|1|

</center>

#### Case 2: Site $i$ is empty, site $(i+1)$ is filled

$$
\langle \theta_i j_{i+1} | \eta_i k_{i+1} \rangle 
=
\langle \theta_i | \eta_i \rangle
\langle j_{i+1} | k_{i+1} \rangle
$$

Using the definition of coherent states, we have

$$
\begin{align*}
    \langle \theta_i | \eta_i \rangle
    &= 
    \langle 0 | (1 - h_i \bar{\theta}_i)
    (1 - \eta_i h_i^\dagger) | 0 \rangle
    \\ &=
    \langle 0|0 \rangle
    + \langle 0 | h_i \bar{\theta}_i \eta_i h_i^\dagger | 0 \rangle
    \\ &=
    1 + \bar{\theta}_i \eta_i
\end{align*}
$$

However, the $1$ term should be discarded, since it means there are neither holes nor spins at site $i$, which *violates the no-double-occupancy constraint*. Thus we have the following nonzero elements of $T$:

<center>

|Grassmann index|Normal index|Element|
|:-:|:-:|:-:|
|`(0,1,1,0)`|`(s,0,0,s)`<br>(`s` = 0, 1)|1|

</center>

#### Case 3: Site $i$ is filled, site $(i+1)$ is empty

$$
\langle j_i \theta_{i+1} | k_i \eta_{i+1} \rangle
=
\langle j_i | k_i \rangle
\langle \theta_{i+1} | \eta_{i+1} \rangle
$$

Similar to **Case 2**, we obtain

$$
\begin{align*}
    \langle \theta_{i+1} | \eta_{i+1} \rangle
    &=
    1 + \bar{\theta}_{i+1} \eta_{i+1}
\end{align*}
$$

Discarding the term $1$, we are left with the following nonzero elements of $T$ (`s` = 0 or 1):

<center>

|Grassmann index|Normal index|Element|
|:-:|:-:|:-:|
|`(1,0,0,1)`|`(0,s,s,0)`<br>(`s` = 0, 1)|1|

</center>

#### Case 4: Both sites are empty

$$
\begin{align*}
    &\langle \theta_i \theta_{i+1} | \eta_i \eta_{i+1} \rangle
    \\
    &= \langle 0| (1 - c_{i+1} \bar{\theta}_{i+1})(1 - c_i \bar{\theta}_i) (1 - \eta_i c_i^\dagger) (1 - \eta_{i+1} c_{i+1}^\dagger) |0\rangle
    \\
    &= \langle 0| 1 + (-c_{i+1} \bar{\theta}_{i+1})(-\eta_{i+1} c_{i+1}^\dagger) 
    + (-c_i \bar{\theta}_i)(-\eta_i c_i^\dagger)
    \\
    & \qquad \quad
    + (-c_{i+1} \bar{\theta}_{i+1})(-c_i \bar{\theta}_i)(-\eta_i c_i^\dagger)(-\eta_{i+1} c_{i+1}^\dagger) |0\rangle
    \\
    &= 1 + \bar{\theta}_{i+1} \eta_{i+1} + \bar{\theta}_i \eta_i + \bar{\theta}_{i+1} \bar{\theta}_i \eta_i \eta_{i+1} 
\end{align*}
$$

The no-double-occupancy constraint keeps the last term only. Thus we have one more nonzero element of $T$:

<center>

|Grassmann index|Normal index|Element|
|:-:|:-:|:-:|
|`(1,1,1,1)`|`(0,0,0,0)`|1|

</center>

## Example: (1 + 1)D $t$-$J$ Model

Hamiltonian with chemical potential term

$$
\begin{align*}
    H &= t\sum_{i, \sigma} (c_{i,\sigma}^\dagger c_{i+1,\sigma} + h.c.)
    \\ &\quad 
    + J \sum_{i} (S_i \cdot S_{i+1} - \frac{1}{4} n_i n_{i+1})
    - \mu \sum_i n_i
    \\
    H_{i, i+1} &=
    t\sum_{\sigma} (c_{i,\sigma}^\dagger c_{i+1,\sigma} + h.c.)
    \\ &\quad 
    + J (S_i \cdot S_{i+1} - \frac{1}{4} n_i n_{i+1})
    - \frac{\mu}{2}(n_i + n_{i+1})
\end{align*}
$$

Fermion operator in the no-double-occupancy subspace:

$$
\tilde{c}_{i,\sigma}  = c_{i,\sigma} (1 - n_{i, -\sigma})
$$

where

$$
\begin{align*}
    (S_i \cdot S_{i+1})_{\sigma_i^\prime \sigma_{i+1}^\prime, \sigma_i \sigma_{i+1}} &\equiv 
    \sum_{\alpha=1}^3 (S_i^\alpha)_{\sigma_i^\prime \sigma_i} (S_{i+1}^\alpha)_{\sigma_{i+1}^\prime \sigma_{i+1}}
    \\
    n_i &\equiv \sum_{\sigma} n_{i,\sigma}
\end{align*}
$$

The no-double-occupancy constraint is included as part of the model definition. 

The gate axis order is chosen as below:

```
    i   i+1     (Site)
    1   0
    |___|
    |   |
    2   3
```

### Tensor Elements in the Hole Representation

- **Tight-binding term**

    $$
    \begin{align*}
        t \sum_{\sigma} (c_{i,\sigma}^\dagger c_{i+1,\sigma} + h.c.) 
        &\rightarrow 
        t \sum_{\sigma} (b_{i,\sigma}^\dagger h_i h_{i+1}^\dagger b_{i+1,\sigma} + h.c.)
        \\ &=
        -t \sum_{\sigma} (h_{i+1}^\dagger h_i b_{i,\sigma}^\dagger b_{i+1,\sigma} + h.c.)
    \end{align*}
    $$

    The nonzero elements satisfying the no-double-occupancy constraint are ("hop to" and "hop from" refer to the spin (boson))

    <center>

    |Hop to|Hop from|Grassmann index|Normal index|Element|
    |:-:|:-:|:-:|:-:|:-:|
    |$i+1,\sigma$|$i,\sigma$|`(0,1,0,1)`|`(σ,0,σ,0)`|$-t$|
    |$i,\sigma$|$i+1,\sigma$|`(1,0,1,0)`|`(0,σ,0,σ)`|$-t$|

    </center>

- **Spin operators**

    $\tau^\alpha (\alpha = 1,2,3)$ below are the Pauli matrices:

    $$
    \begin{align*}
        (S_i^\alpha)_{\sigma^\prime \sigma} \rightarrow
            b_{i,\sigma^\prime}^\dagger 
            \tau_{\sigma^\prime \sigma}^\alpha 
            b_{i,\sigma}
    \end{align*}
    $$

    Then

    $$
    \begin{align*}
        (S_i \cdot S_{i+1})_{\sigma_i^\prime \sigma_{i+1}^\prime, \sigma_i \sigma_{i+1}} 
        &= 
        \sum_{\alpha=1}^3 
        b_{i,\sigma_i^\prime}^\dagger 
        \tau_{\sigma_i^\prime \sigma_i}^\alpha 
        b_{i,\sigma_i}
        b_{i+1,\sigma_{i+1}^\prime}^\dagger 
        \tau_{\sigma_{i+1}^\prime \sigma_{i+1}}^\alpha 
        b_{i+1,\sigma_{i+1}}
        \\ &=
        \sum_{\alpha=1}^3 
        \tau_{\sigma_i^\prime \sigma_i}^\alpha 
        \tau_{\sigma_{i+1}^\prime \sigma_{i+1}}^\alpha 
        b_{i,\sigma_i^\prime}^\dagger 
        b_{i+1,\sigma_{i+1}^\prime}^\dagger 
        b_{i,\sigma_i} 
        b_{i+1,\sigma_{i+1}}
    \end{align*}
    $$

    Nonzero tensor elements satisfying no-double-occupancy constraint

    <center>

    |To|From|Grassmann index|Normal index|Element|
    |:-:|:-:|:-:|:-:|:-:|
    |$\sigma_i^\prime \sigma_{i+1}^\prime$|$\sigma_i \sigma_{i+1}$|`(0,0,0,0)`|$(\sigma_{i+1}^\prime, \sigma_i^\prime, \sigma_i, \sigma_{i+1})$|$J \sum_{\alpha=1}^3 \tau_{\sigma_i^\prime \sigma_i}^\alpha \tau_{\sigma_{i+1}^\prime \sigma_{i+1}}^\alpha$

    </center>

- **Site Repulsion/Attraction**

    $$
    -\frac{J}{4} n_i n_{i+1}
    \rightarrow -\frac{J}{4} n_i^b n_{i+1}^b
    $$

    where $n_i^b \equiv \sum_{\sigma} n_{i,\sigma}^b$. Then the nonzero tensor elements satisfying no-double-occupancy constraint are

    <center>

    |Site $i$|Site $i+1$|Grassmann index|Normal index|Element|
    |:-:|:-:|:-:|:-:|:-:|
    |$\sigma_i$|$\sigma_{i+1}$|`(0,0,0,0)`|$(\sigma_{i+1},\sigma_i,\sigma_i,\sigma_{i+1})$|$-J/4$

    </center>

- **Chemical Potential Term**

    $$
    -\frac{\mu}{2}(n_i + n_{i+1}) 
    \rightarrow
    -\frac{\mu}{2}(n_i^b + n_{i+1}^b)
    $$

    The nonzero tensor elements satisfying no-double-occupancy constraint are

    <center>

    |Site $i$|Site $i+1$|Grassmann index|Normal index|Element|
    |:-:|:-:|:-:|:-:|:-:|
    |$\sigma_i$|Empty|`(1,0,0,1)`|$(0,\sigma_i,\sigma_i,0)$|$-\mu/2$|
    |Empty|$\sigma_{i+1}$|`(0,1,1,0)`|$(\sigma_{i+1},0,0,\sigma_{i+1})$|$-\mu/2$|
    |$\sigma_i$|$\sigma_{i+1}$|`(0,0,0,0)`|$(\sigma_{i+1},\sigma_i,\sigma_i,\sigma_{i+1})$|$-\mu$|

    </center>

    To achieve the **Heisenberg limit** (i.e. no holes, or **half-filling**, which implies almost no hopping), we assign a very big $\mu$ (about 10 times of $t, J$), so that the energy cost to produce a hole is high. 

    If we use

    $$
    -\frac{\mu}{2}(n_i + n_{i+1}) 
    = + \frac{\mu}{2}(n_i^h + n_{i+1}^h) + \text{const}
    $$

    and omit the constant term, the nonzero tensor elements satisfying no-double-occupancy constraint are

    <center>

    |Site $i$|Site $i+1$|Grassmann index|Normal index|Element|
    |:-:|:-:|:-:|:-:|:-:|
    |Empty|Empty|`(1,1,1,1)`|$(0,0,0,0)$|$\mu$|
    |$\sigma_i$|Empty|`(1,0,0,1)`|$(0,\sigma_i,\sigma_i,0)$|$\mu/2$|
    |Empty|$\sigma_{i+1}$|`(0,1,1,0)`|$(\sigma_{i+1},0,0,\sigma_{i+1})$|$\mu/2$|

    </center>
