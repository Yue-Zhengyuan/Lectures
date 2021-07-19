<style>
    .katex {
        font-size: 1.1em;
    }
    .remark {
        border-radius: 15px;
        padding: 20px;
        background-color: SeaGreen;
        color: White;
    }
    .result {
        border-radius: 15px;
        padding: 20px;
        background-color: DarkSlateBlue;
        color: White;
    }
</style>

# Jordan-Wigner Transformation

## Mapping A Single Spin-1/2 to A Single Fermion

The up and down states of a *single* spin-1/2 site can be thought as the occupied and empty states of a *one*-particle (spinless) fermion states:

$$
\begin{align*}
    \text{(Up)} \quad 
    \ket{\uparrow} &\longleftrightarrow \ket{1} = c^\dagger \ket{0}
    &&\text{(Occupied)}
    \\
    \text{(Down)} \quad 
    \ket{\downarrow} &\longleftrightarrow \ket{0}
    &&\text{(Empty)}
\end{align*}
$$

Under these basis vectors, we define the ladder operators for the spin

$$
\begin{align*}
    S^+ &= \begin{bmatrix}
        0 & 1 \\
        0 & 0
    \end{bmatrix}
    = S^x + iS^y
    \\
    S^- &= \begin{bmatrix}
        0 & 0 \\
        1 & 0
    \end{bmatrix}
    = S^x - iS^y
\end{align*}
$$

where $\sigma^a \, (a = x,y,z)$ are Pauli matrices. We then have the following mapping for a single spin:

<div class="result">

**A single spin and a single fermion:**

$$
S^z = c^\dagger c - \frac{1}{2}, \quad
S^+ = c^\dagger, \quad S^- = c
$$

</div><br>

Let us verify the (anti-)commutation relations: the spin operators satisfy

$$
\begin{align*}
    [S^a, S^b] &= i \epsilon^{abc} S^c
    \\
    \{S^a, S^b\} &= \frac{1}{2} \delta^{ab}
\end{align*} \qquad (a = x,y,z)
$$

Then we can also show that the ladder operators satisfy

$$
\{S^-, S^+\} = 1 \qquad
\{S^\pm, S^\pm\} = 0 \qquad
[S^+, S^-] = 2S_z 
$$

which is the same as the fermion operators:

$$
\begin{align*}
    \{c, c^\dagger\} &= 1 \qquad
    \{c, c\} = \{c^\dagger, c^\dagger\} = 0
    \\
    [c^\dagger, c] &= 2 c^\dagger c - \{c, c^\dagger\}
    = 2 \left(n - \frac{1}{2} \right)
\end{align*}
$$

## String/Kink Operator

Next, let us we try to generalize the above mapping to a 1D spin chain (with $N$ sites). Each site of the chain will correspond to an independent fermion. The naive mapping is

$$
S_j^+, S_j^-, S_j^z \longleftrightarrow 
c_j^\dagger, c_j, n_j - \tfrac{1}{2}
\qquad j = 1,...,N
$$

However, different fermion operators should *anti-commute*, while the spin operators at different sites *commute*:

$$
[S_i^{(\pm)}, S_j^{(\pm)}] = 0 \qquad
\{c_i^{(\dagger)}, c_j^{(\dagger)}\} = 0 \qquad (i \ne j)
$$

The bracket means we are referring to either $c^\dagger$ or $c$, and $S^+$ or $S^-$. One way to overcome this difficulty is to introduce a **string (kink) operator** to the fermion operators:

<div class="result">

**The string operator for fermion:**

$$
F_j \equiv e^{i\phi_j}, \quad 
\phi_j = \pi \sum_{l=1}^{j-1} c_l^\dagger c_l \quad 
(\text{define} \ \phi_1 \equiv 0 \Rightarrow F_1 = 1)
$$

</div><br>

### Properties of the String

- Since $n_l \equiv c_l^\dagger c_l = 0,1$, one can easily see that $F_j = F_j^\dagger = F_j^{-1}$. 

- It is useful to derive an alternative expression for the string $F_j$:

    $$
    F_j \equiv \exp\bigg[
        i\pi \sum_{l=1}^{j-1} n_l
    \bigg]
    = \prod_{l=1}^{j-1} (-1)^{n_l}
    = \prod_{l=1}^{j-1} (1 - 2n_l)
    $$

    In the last step we have used the fact that $n_l$ can only be 0, 1 and therefore $(-1)^{n_l} = 1 - 2n_l$. 

- (Anti-)commutation relations with fermion operators

    $$
    \begin{align*}
        [F_j, c_l^{(\dagger)}] &= 0 \qquad j \le l \\
        \{F_j, c_l^{(\dagger)}\} &= 0 \qquad j > l
    \end{align*}
    $$

    ----

    *Proof*: 

    ----

## Jordan-Wigner Transformation

With the string operator, the complete mapping from spin to fermion is

<div class="result">

**The Jordan-Wigner transformation:**

$$
S_j^+ = c_j^\dagger F_j = F_j c_j^\dagger, \quad 
S_j^- = c_j F_j = F_j c_j
\quad (j = 1,...,N)
$$

</div><br>

<div class="remark">

*Remark*: The expression of $S^z_j$ in terms of fermion operators is then (using $F_j^2 = 1$)

$$
\begin{align*}
    S^z_j &= S^+_j S^-_j - 1/2 = c_j^\dagger c_j - 1/2
\end{align*}
$$

</div><br>

<center>
<img src="images/spin-fermion.png" width="450px" alt="string operator">
</center>

Let us check that the introduction of the string operator indeed gives us the correct commutation relations of the fermion operators.

