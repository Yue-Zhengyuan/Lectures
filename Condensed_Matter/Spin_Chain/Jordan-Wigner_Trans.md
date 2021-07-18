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

## Similarity between Spin-1/2 and Fermion Operators

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

Under these basis vectors, 

$$
\begin{align*}
    S^+ = c^\dagger &= \begin{bmatrix}
        0 & 1 \\
        0 & 0
    \end{bmatrix}
    = \frac{1}{2}(\sigma^x + i \sigma^y)
    = S^x + iS^y
    \\
    S^- = c &= \begin{bmatrix}
        0 & 0 \\
        1 & 0
    \end{bmatrix}
    = \frac{1}{2}(\sigma^x - i \sigma^y)
    = S^x - iS^y
\end{align*}
$$

where $\sigma^a \, (a = x,y,z)$ are Pauli matrices. The $S^z$ operator can also be expressed using the fermion operators:

$$
\begin{align*}
    S^z &= \frac{1}{2}\sigma^z = \frac{1}{2} \begin{bmatrix}
        1 & 0 \\
        0 & -1
    \end{bmatrix} 
    = S^+ S^- - \frac{1}{2} 
    \\[0.5em]
    &\to c^\dagger c - \frac{1}{2}
    = n - \frac{1}{2}
\end{align*}
$$

Let us also check that the (anti-)commutation relations: the spin operators satisfy

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
    = 2 \left(n - \tfrac{1}{2} \right)
\end{align*}
$$

## Jordan-Wigner Transformation

Next, let us we try to generalize the above mapping to a 1D spin chain (with $N$ sites). Each site of the chain will correspond to an independent fermion. The naive mapping is

$$
S_i^+, S_i^-, S_i^z \longleftrightarrow 
c_i^\dagger, c_i, n_i - \tfrac{1}{2}
\qquad i = 1,...,N
$$

However, different fermion operators should *anti-commute*, while the spin operators at different sites *commute*:

$$
[S_i^{(\pm)}, S_j^{(\pm)}] = 0 \qquad
\{c_i^{(\dagger)}, c_j^{(\dagger)}\} = 0 \qquad (i \ne j)
$$

The bracket means we are referring to either $c^\dagger$ or $c$, and $S^+$ or $S^-$. One way to overcome this difficulty is to introduce a **string operator** to the fermion operators. This leads to 

<div class="result">

**The Jordan-Wigner transformation:**

$$
\begin{align*}
    S_j^z &= n_j - \tfrac{1}{2}
    \\
    S_j^+ &= c_j^\dagger e^{i \phi_j}
    \\
    S_j^- &= c_j e^{-i \phi_j}
\end{align*} \quad \text{with} \ \left\{
\begin{align*}
    n_j &= c_j^\dagger c_j
    \\
    \phi_j &= \pi \textstyle{\sum_{l=1}^{j-1} n_l}
\end{align*} \right.
$$

Here $F_j \equiv e^{i\phi_j}$ is the required string operator; we also define the phase on the first site $\phi_1 = 0$. 

</div><br>

<center>
<img src="images/spin-fermion.png" width="450px" alt="string operator">
</center>

## Properties of the String

It is useful to derive an alternative expression for the string $F_j$:

$$
F_j \equiv \exp\bigg[
    i\pi \sum_{l=1}^{j-1} n_l
\bigg]
= \prod_{l=1}^{j-1} (-1)^{n_l}
= \prod_{l=1}^{j-1} (1 - 2n_l)
$$

In the last step we have used the fact that $n_l$ can only be 0, 1 and therefore $(-1)^{n_l} = 1 - 2n_l$. 

In addition, we have

$$
\begin{align*}
    \{e^{i \phi_j}, c_l^{(\dagger)}\} &= 0 \qquad j > l
    \\
    [e^{i \phi_j}, c_l^{(\dagger)}] &= 0 \qquad j \le l
\end{align*}
$$

----

*Proof*: We first consider

$$
\{e^{i\pi n_j}, c_j\}
= e^{i\pi n_j} c_j + c_j e^{i\pi n_j}
$$

The first term is nonzero when $c_j$ acts on $|1\rangle$, but then $n_j = 0$; while in the second term, the $n_j$ acts first and get value 1. Thus

$$
\{e^{i\pi n_j}, c_j\}
= e^{i\pi 0} c_j + c_j e^{i\pi 1} = 0
$$

Similarly 

$$
\begin{align*}
    \{e^{i\pi n_j}, c_j^\dagger\}
    &= e^{i\pi n_j} c_j^\dagger + c_j^\dagger e^{i\pi n_j}
    \\
    &= e^{i\pi 1} c_j^\dagger + c_j^\dagger e^{i\pi 0}
    = 0
\end{align*}
$$

Meanwhile, for $i \ne j$

$$
[n_i, c_j^{(\dagger)}] = 
$$

----

## (Anti-)Commutation Relations

Let us check that the introduction of the string operator indeed gives us the correct commutation relations of the spin operators.

Starting from the fermion anti-commutation relation, we calculate (assume $j > k$)

$$
[S_j^{(\pm)}, S_k^{(\pm)}]
$$

## Boundary Condition of the Fermion Theory

Usually, we impose the **periodic boundary condition** on the spin chain

$$
S_{N+1}^a = S_1^a \qquad a = x,y,z
$$

Here $N$ is the number of spin sites. Under the Jordan-Wigner transformation 

$$
\begin{align*}
    S_{N+1}^{(\pm)} &= c_{N+1}^{(\dagger)} e^{\pm i \phi_{N+1}}
    = c_{N+1}^{(\dagger)} \exp(\pm i \pi n_\text{tot})
    \\
    S_1^{(\pm)} &= c_1^{(\dagger)} e^{\pm i \phi_1}
    = c_1^{(\dagger)}
\end{align*}
$$

Here $n_\text{tot} \equiv \sum_i n_i$ is the total number of fermions. Thus, depending on $n_\text{tot}$, the original spin theory is separated into *two sectors* of the fermion theory:

- The **even** sector with **anti-periodic** boundary condition
    
    $$
    n_\text{tot} = \text{even}
    \qquad
    c_{N+1}^{(\dagger)} = -c_1^{(\dagger)}
    $$

- The **odd** sector with **periodic** boundary condition
    
    $$
    n_\text{tot} = \text{odd}
    \qquad
    
    $$

The two boundary condition will alow different values of the lattice momentum $k$ in the fermion theory. The Fourier transform of the $c_i^{(\dagger)}$ operators gives ($a$ is the lattice spacing, and $x_j = ja$; using the symmetric convention):

$$
\begin{align*}
    c_j &= \frac{1}{\sqrt{N}} \sum_k 
    c_k e^{+i k x_j} 
    \\
    c_j^\dagger &= \frac{1}{\sqrt{N}} \sum_k
    c_k^\dagger e^{-i k x_j}
\end{align*}
\, \Longleftrightarrow \,
\begin{align*}
    c_k &= \frac{1}{\sqrt{N}} \sum_j 
    c_j e^{-i k x_j} \\
    c_k^\dagger &= \frac{1}{\sqrt{N}} \sum_j 
    c_j^\dagger e^{+i k x_j}
\end{align*}
$$

where $j$ sums over the lattice sites, and $k$ sums over the reciprocal lattice in the 1st Brillouin zone (BZ). Then, for the two boundary conditions:

- PBC: $c_{N} = c_1$

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

- Anti-PBC: $c_{N} = -c_1$
    
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

## Appendix: Anti-Commutation Rules for $c_k^{(\dagger)}$

We now prove that

$$
\begin{align*}
    \{c_k, c_k\} &= \{c_k^\dagger, c_k^\dagger\} = 0
    \\
    \{c_{-k}, c_{-k}\} &= \{c_{-k}^\dagger, c_{-k}^\dagger\} = 0
    \\
    \{c_k, c_{-k}^\dagger\} &= \{c_{-k}, c_k^\dagger\} = 0
    \\
    \{c_k, c_{k}^\dagger\} &= \{c_{-k}, c_{-k}^\dagger\} = 1
    \\
    \{c_{k}, c_{-k}\} &= \{c_{k}^\dagger, c_{-k}^\dagger\} = 0
\end{align*}
$$