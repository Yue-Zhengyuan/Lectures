# Trotter Gate: <br>Fermion Models with Spin

## Trotter gate on sites $i$ and $(i+1)$

When spin-1/2 is added, we shall have *two* axes corresponding to each site: one axis represents spin-up particles, and the other represents spin-down particles:

$$
\langle \theta_{i,\uparrow} \theta_{i,\downarrow} \theta_{i+1,\uparrow} \theta_{i+1,\downarrow} | H_{i,i+1} | \eta_{i,\uparrow} \eta_{i,\downarrow} \eta_{i+1,\uparrow} \eta_{i+1,\downarrow} \rangle
$$

It corresponds to an 8-axis Grassmann tensor $\mathbf{T}$ by the relation

$$
\begin{align*}
    &\langle \theta_{i,\uparrow} \theta_{i,\downarrow} \theta_{i+1,\uparrow} \theta_{i+1,\downarrow} | H_{i,i+1} | \eta_{i,\uparrow} \eta_{i,\downarrow} \eta_{i+1,\uparrow} \eta_{i+1,\downarrow} \rangle 
    \\
    &= \sum_{m,n=0,1} 
    T^{
        m_{i+1,\downarrow} 
        m_{i+1,\uparrow} 
        m_{i,\downarrow} 
        m_{i,\uparrow} 
        n_{i,\uparrow} 
        n_{i,\downarrow} 
        n_{i+1,\uparrow} 
        n_{i+1,\downarrow}
    } 
    \\ &\qquad \qquad \times
    \bar{\theta}_{i+1,\downarrow}^{m_{i+1,\downarrow}} 
    \bar{\theta}_{i+1,\uparrow}^{m_{i+1,\uparrow}} 
    \bar{\theta}_{i,\downarrow}^{m_{i,\downarrow}}
    \bar{\theta}_{i,\uparrow}^{m_{i,\uparrow}}
    \eta_{i,\uparrow}^{n_{i,\uparrow}}
    \eta_{i,\downarrow}^{n_{i,\downarrow}}
    \eta_{i+1,\uparrow}^{n_{i+1,\uparrow}}
    \eta_{i+1,\downarrow}^{n_{i+1,\downarrow}}
    \\
    &\equiv \sum_{m,n=0,1} 
    \mathbf{T}(\bar{\theta},\eta)^{
        m_{i+1,\downarrow} 
        m_{i+1,\uparrow} 
        m_{i,\downarrow} 
        m_{i,\uparrow} 
        n_{i,\uparrow} 
        n_{i,\downarrow} 
        n_{i+1,\uparrow} 
        n_{i+1,\downarrow}
    }
\end{align*}
$$

with the following axis order:

```
    i   i  i+1 i+1  (Site)
    up  dn  up  dn  (Spin)
    3   2   1   0
    ↓---↓---↓---↓
    |           |
    ↓---↓---↓---↓
    4   5   6   7
    up  dn  up  dn  (Spin)
    i   i  i+1 i+1  (Site)
```

Similar to the spinless case, we have 

$$
\begin{align*}
    &\langle \theta_{i,\uparrow} \theta_{i,\downarrow} \theta_{i+1,\uparrow} \theta_{i+1,\downarrow} | H(c^\dagger,c) | \eta_{i,\uparrow} \eta_{i,\downarrow} \eta_{i+1,\uparrow} \eta_{i+1,\downarrow} \rangle
    \\
    &= \langle \theta_{i,\uparrow} \theta_{i,\downarrow} \theta_{i+1,\uparrow} \theta_{i+1,\downarrow} | \eta_{i,\uparrow} \eta_{i,\downarrow} \eta_{i+1,\uparrow} \eta_{i+1,\downarrow} \rangle
    H(\bar{\theta},\eta)
\end{align*}
$$

The identity gate is

$$
\begin{align*}
    &\langle \theta_{i,\uparrow} \theta_{i,\downarrow} \theta_{i+1,\uparrow} \theta_{i+1,\downarrow} | \eta_{i,\uparrow} \eta_{i,\downarrow} \eta_{i+1,\uparrow} \eta_{i+1,\downarrow} \rangle
    \\ &=
    \langle 0 |
    (1 - c_{i+1,\downarrow} \bar{\theta}_{i+1,\downarrow})
    (1 - c_{i+1,\uparrow} \bar{\theta}_{i+1,\uparrow})
    (1 - c_{i,\downarrow} \bar{\theta}_{i,\downarrow})
    (1 - c_{i,\uparrow} \bar{\theta}_{i,\uparrow})
    \\ & \qquad \times
    (1 - c_{i,\uparrow} \eta_{i,\uparrow})
    (1 - c_{i,\downarrow} \eta_{i,\downarrow})
    (1 - c_{i+1,\uparrow} \eta_{i+1,\uparrow})
    (1 - c_{i+1,\downarrow} \eta_{i+1,\downarrow})
    | 0 \rangle
    \\ &\downarrow \text{very tedious expansion}
    \\ &=
    1 + ...
\end{align*}
$$

After full expansion of the equation above, we obtain the following $\sum_{m=0}^{4} C_4^m = 16$ nonzero tensor elements, which all equal to 1:

<center>

<table>
    <thead>
        <tr> <th># of <br>Particles <th>Grassmann index <th> Element
    </thead>
    <tbody>
        <tr> <td><center>0 <td><code>(0,0,0,0,0,0,0,0) <td rowspan=16><center>1
        <tr> <td rowspan=4><center>1 <td><code>(0,0,0,1,1,0,0,0)
        <tr> <td><code>(0,0,1,0,0,1,0,0)
        <tr> <td><code>(0,1,0,0,0,0,1,0)
        <tr> <td><code>(1,0,0,0,0,0,0,1)
        <tr> <td rowspan=6><center>2 <td><code>(0,0,1,1,1,1,0,0)
        <tr> <td><code>(0,1,0,1,1,0,1,0)
        <tr> <td><code>(1,0,0,1,1,0,0,1)
        <tr> <td><code>(0,1,1,0,0,1,1,0)
        <tr> <td><code>(1,0,1,0,0,1,0,1)
        <tr> <td><code>(1,1,0,0,0,0,1,1)
        <tr> <td rowspan=4><center>3 <td><code>(1,1,1,0,0,1,1,1)
        <tr> <td><code>(1,1,0,1,1,0,1,1)
        <tr> <td><code>(1,0,1,1,1,1,0,1)
        <tr> <td><code>(0,1,1,1,1,1,1,0)
        <tr> <td><center>4 <td><code>(1,1,1,1,1,1,1,1)
    </tbody>
</table>

</center>

This can also be directly read out using the physical meaning of the identity gate. 

## Example: (1 + 1)D Hubbard Model

$$
\begin{align*}
    H_{i, i+1} 
    &= -t \sum_{\sigma} (c_{i,\sigma}^\dagger c_{i+1,\sigma} + c_{i+1,\sigma}^\dagger c_{i,\sigma})
    \\ &\quad 
    + \frac{V}{2} \left[
        \left( n_{i,\uparrow}-\frac{1}{2} \right)
        \left( n_{i,\downarrow}-\frac{1}{2} \right)
        \right. 
        \\ &\left. \qquad \qquad 
        + \left( n_{i+1,\uparrow}-\frac{1}{2} \right)
        \left( n_{i+1,\downarrow}-\frac{1}{2} \right)
        \right]
\end{align*}
$$

#### Tight-binding hopping term

$$
\begin{align*}
    H_{tb} &= -t \sum_{\sigma} (
        c_{i,\sigma}^\dagger c_{i+1,\sigma} + c_{i+1,\sigma}^\dagger c_{i,\sigma}
    ) \\
    &\rightarrow
    -t \sum_{\sigma} (
        \bar{\theta}_{i,\sigma} \eta_{i+1,\sigma} 
        + \bar{\theta}_{i+1,\sigma} \eta_{i,\sigma}
    ) \equiv H_{tb}(\bar{\theta},\eta)
\end{align*}
$$

The tensor elements are found from the expansion of

$$
\begin{align*}
    \langle \theta_{i,\uparrow} \theta_{i,\downarrow} \theta_{i+1,\uparrow} \theta_{i+1,\downarrow} | \eta_{i,\uparrow} \eta_{i,\downarrow} \eta_{i+1,\uparrow} \eta_{i+1,\downarrow} \rangle H_{tb}(\bar{\theta},\eta)
\end{align*}
$$

Therefore (these can also be directly written down according to the physical meaning of the Grassmann index)

<center>

|Hop from|Hop to|Other <br>Filled States|Grassmann index|Element|
|:-:|:-:|:-:|:-:|:-|
|$i+1\uparrow$|$i\uparrow$|None|`(0,0,0,1,0,0,1,0)`|$-t$|
|||$i\downarrow$|`(0,0,1,1,0,1,1,0)`|$+t$ <sup>Note|
|||$i+1\downarrow$|`(1,0,0,1,0,0,1,1)`|$-t$|
|||$i\downarrow$<br>$i+1\downarrow$|`(1,0,1,1,0,1,1,1)`|$+t$|
|$i+1\downarrow$|$i\downarrow$|None|`(0,0,1,0,0,0,0,1)`|$-t$|
|||$i\uparrow$|`(0,0,1,1,1,0,0,1)`|$-t$|
|||$i+1\uparrow$|`(0,1,1,0,0,0,1,1)`|$+t$|
|||$i\uparrow$<br>$i+1\uparrow$|`(0,1,1,1,1,0,1,1)`|$+t$|
|$i\uparrow$|$i+1\uparrow$|None|`(0,1,0,0,1,0,0,0)`|$-t$|
|||$i\downarrow$|`(0,1,1,0,1,1,0,0)`|$+t$|
|||$i+1\downarrow$|`(1,1,0,0,1,0,0,1)`|$-t$|
|||$i\downarrow$<br>$i+1\downarrow$|`(1,1,1,0,1,1,0,1)`|$+t$|
|$i\downarrow$|$i+1\downarrow$|None|`(1,0,0,0,0,1,0,0)`|$-t$|
|||$i\uparrow$|`(1,0,0,1,1,1,0,0)`|$-t$|
|||$i+1\uparrow$|`(1,1,0,0,0,1,1,0)`|$+t$|
|||$i\uparrow$<br>$i+1\uparrow$|`(1,1,0,1,1,1,1,0)`|$+t$|

</center>

----

**Note: Why some elements are *plus* $t$**

For example, let us consider the case 

<center>

`(0,0,1,1,0,1,1,0)` (hopping from $i+1\uparrow$ to $i\uparrow$, with $i\downarrow$ filled)

</center>

In the expansion of the gate elements, this case corresponds to the term

$$
\begin{align*}
    (\bar{\theta}_{i,\downarrow} \eta_{i,\downarrow})
    (\bar{\theta}_{i,\uparrow} \eta_{i+1,\uparrow})
    = 
    - \bar{\theta}_{i,\downarrow} \bar{\theta}_{i,\uparrow}
    \eta_{i,\downarrow} \eta_{i+1,\uparrow}
\end{align*}
$$

We see an additional minus sign pops out in order to match the axis order convention of the tensor. To intuitively understand the origin of the sign, 

----

#### On-site Repulsion/Attraction term

$$
\frac{V}{2} \left[
    \left( n_{i,\uparrow}-\frac{1}{2} \right)
    \left( n_{i,\downarrow}-\frac{1}{2} \right)
    +\left( n_{i+1,\uparrow}-\frac{1}{2} \right)
    \left( n_{i+1,\downarrow}-\frac{1}{2} \right)
\right]
$$

This term will have a constant term $V/4$, which we shall remove. Then this term becomes

$$
\begin{align*}
    H_V &=\frac{V}{2} \left[
        n_{i,\uparrow} n_{i,\downarrow}
        + n_{i+1,\uparrow} n_{i+1,\downarrow}
        - \frac{1}{2} \sum_{\sigma} (
            n_{i,\sigma} + n_{i+1,\sigma}
        )
    \right] 
    \\ &\rightarrow
    \frac{V}{2} \left[
        \bar{\theta}_{i,\downarrow}
        \bar{\theta}_{i,\uparrow}
        \eta_{i,\uparrow} \eta_{i,\downarrow}
        + \bar{\theta}_{i+1,\downarrow}
        \bar{\theta}_{i+1,\uparrow}
        \eta_{i+1,\uparrow} \eta_{i+1,\downarrow}
    \right.
    \\ & \quad \qquad
    \left.
        - \frac{1}{2} \sum_{\sigma} (
            \bar{\theta}_{i,\sigma} \eta_{i,\sigma} 
            + \bar{\theta}_{i+1,\sigma} \eta_{i+1,\sigma} 
        )
    \right] \equiv H_V(\bar{\theta},\eta)
\end{align*}
$$

Without need to worry about the possible sign changes (as in the hopping terms), we can directly write down the tensor elements of $H_V$: 

<center>

|Site $i$|Site $i+1$|Grassmann index|Element|
|:-:|:-:|:-:|:-:|
|Empty|Empty|`(0,0,0,0,0,0,0,0)`|0|
||$\uparrow$|`(0,1,0,0,0,0,1,0)`|$-V/4$|
||$\downarrow$|`(1,0,0,0,0,0,0,1)`|$-V/4$|
||$\uparrow \downarrow$|`(1,1,0,0,0,0,1,1)`|0|
|$\uparrow$|Empty|`(0,0,0,1,1,0,0,0)`|$-V/4$|
||$\uparrow$|`(0,1,0,1,1,0,1,0)`|$-V/2$|
||$\downarrow$|`(1,0,0,1,1,0,0,1)`|$-V/2$|
||$\uparrow \downarrow$|`(1,1,0,1,1,0,1,1)`|$-V/4$|
|$\downarrow$|Empty|`(0,0,1,0,0,1,0,0)`|$-V/4$|
||$\uparrow$|`(0,1,1,0,0,1,1,0)`|$-V/2$|
||$\downarrow$|`(1,0,1,0,0,1,0,1)`|$-V/2$|
||$\uparrow \downarrow$|`(1,1,1,0,0,1,1,1)`|$-V/4$|
|$\uparrow \downarrow$|Empty|`(0,0,1,1,1,1,0,0)`|0|
||$\uparrow$|`(0,1,1,1,1,1,1,0)`|$-V/4$|
||$\downarrow$|`(1,0,1,1,1,1,0,1)`|$-V/4$|
||$\uparrow \downarrow$|`(1,1,1,1,1,1,1,1)`|0|

</center>

## Merging Axes at the Same Site

For convenience, we first change the gate axis order to

```
    2   3   0   1
    ↓---↓---↓---↓
    |           |
    ↓---↓---↓---↓
    4   5   6   7
```

In the original tensor network, the Trotter gates are contracted as

```
        |           |   |           |
        ↓---↓---↓---↓   ↓---↓---↓---↓
        4   5   6   7   4   5   6   7
        0   1   2   3   0   1   2   3
        ↓---↓   ↓---↓---↓---↓   ↓---↓
            |   |           |   |
        ↓---↓   ↓---↓---↓---↓   ↓---↓
        6   7   4   5   6   7   4   5
        2   3   0   1   2   3   0   1
        ↓---↓---↓---↓   ↓---↓---↓---↓
        |           |   |           |
```

But we are more accustomed to treating 4-axis gates. Thus we may [merge the axes](../GTensor/decomposition.md) of the 8-axis gate to obtain a 4-axis one 

$$
\mathbf{T}_{(i_0 i_1)(i_2 i_3)(i_4 i_5)(i_6 i_7)}^{(n_0 n_1)(n_2 n_3)(n_4 n_5)(n_6 n_7)}
\rightarrow
\mathbf{T}_{I_0 I_1 I_2 I_3}^{N_0 N_1 N_2 N_3}
$$

corresponding to the following code:

```python
gate_4axis = gate_8axis.merge_axes((2,2,2,2), (1,1,-1,-1))
```

```
    (2   3) (0   1)       1   0
    (↓---↓)-(↓---↓)       ↓---↓
    |             |  -->  |   |
    (↓---↓)-(↓---↓)       ↓---↓
    (4   5) (6   7)       2   3
    (up dn) (up dn)       i  i+1  (Site)
    (  i  ) ( i+1 )
```

To maintain the number of elements, the new normal indices $I_0, ..., I_3$ will have dimension

$$
\begin{align*}
    \dim{I_k} &= \frac{\dim{n_{2k}} \dim{n_{2k+1}} \dim{i_{2k}} \dim{i_{2k+1}}}{\dim{N_k}} \\
    &= \frac{2 \times 2 \times 1 \times 1}{2} = 2,
    \qquad k \in \{0,...,3\}
\end{align*}
$$

### Physical Meaning of the Merged Axes