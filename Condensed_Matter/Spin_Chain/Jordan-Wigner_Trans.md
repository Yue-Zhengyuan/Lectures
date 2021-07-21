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

**Mapping a single spin to a single fermion:**

$$
\begin{gather*}
    S^+ = c^\dagger, \quad S^- = c \\ \Rightarrow
    S^z = S^+ S^- - 1/2 = c^\dagger c - 1/2
\end{gather*}
$$

</div><br>

Let us verify the (anti-)commutation relations: the spin operators satisfy

$$
\begin{align*}
    [S^a, S^b] &= i \epsilon^{abc} S^c
    \\
    \{S^a, S^b\} &= \delta^{ab} / 2
\end{align*} \qquad (a,b = x,y,z)
$$

Then we can also show that the ladder operators satisfy

$$
\{S^-, S^+\} = 1, \quad
\{S^\pm, S^\pm\} = 0, \quad
[S^+, S^-] = 2S^z
$$

which is the same as the fermion operators:

$$
\begin{gather*}
    \{c, c^\dagger\} = 1, \quad
    \{c, c\} = \{c^\dagger, c^\dagger\} = 0
    \\
    [c^\dagger, c] = 2 c^\dagger c - \{c, c^\dagger\}
    = 2 \left(n - \frac{1}{2} \right)
\end{gather*}
$$

## String (Kink) Operator

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
    \begin{align*}
        F_j &\equiv \exp\bigg[
            i\pi \sum_{l=1}^{j-1} n_l
        \bigg]
        = \prod_{l=1}^N \exp(i\pi n_l) \quad
        (\text{All $n_l$ commute})
        \\
        &= \prod_{l=1}^{j-1} (-1)^{n_l}
        = \prod_{l=1}^{j-1} (1 - 2n_l)
    \end{align*}
    $$

    In the last step we have used the fact that $n_l$ can only be 0, 1 and therefore $(-1)^{n_l} = 1 - 2n_l$. 

- Different string operators commute (since all $n_l$ commute):
    
    $$
    [F_i, F_j] = 0
    $$

- (Anti-)commutation relations with fermion operators

    $$
    \begin{align*}
        [F_j, c_m^{(\dagger)}] &= 0 \qquad j \le m \\
        \{F_j, c_m^{(\dagger)}\} &= 0 \qquad j > m
    \end{align*}
    $$

    ----

    *Proof*: We first observe the following commutation relations between $e^{i\pi n_l}$ and $c_m^{(\dagger)}$:
    
    $$
    \begin{array}{ll}
        l \ne m: \quad & [n_l, c_m^{(\dagger)}] = 0 \Rightarrow
        [e^{i\pi n_l}, c_m^{(\dagger)}] = 0
        \\[0.7em]
        l = m: \quad & 
        \begin{align*}
            \{e^{i\pi n_m}, c_m\}
            &= e^{i\pi n_m} c_m + c_m e^{i\pi n_m} \\
            &= e^{i\pi (1-1)} c_m + c_m e^{i\pi 1} = 0
            \\
            \{e^{i\pi n_m}, c_m^\dagger\}
            &= e^{i\pi n_m} c_m^\dagger + c_m^\dagger e^{i\pi n_m} \\
            &= e^{i\pi (0+1)} c_m + c_m e^{i\pi 0} = 0
        \end{align*}
    \end{array}
    $$

    - When $j \le m$, $e^{i\pi n_m}$ is not in $F_j$. Each term in $F_j$ commutes with $e^{i\pi n_m}$. Therefore
        
        $$ [F_j, c_m^{(\dagger)}] = 0 $$

    - When $j > m$, $e^{i\pi n_m}$ is in $F_j$. Then

        $$
        \{F_j, c_m^{(\dagger)}\}
        = e^{i\pi n_1} \cdots \cancel{e^{i\pi n_m}} 
        \cdots e^{i\pi n_{j-1}} \{e^{i\pi n_m} c_m^{(\dagger)}\}
        = 0 \quad \blacksquare
        $$

    ----

## Jordan-Wigner Transformation

### Mapping to Complex Fermion

With the string operator, the complete mapping from spin to (complex) fermion is

<div class="result">

**The Jordan-Wigner transformation:**

$$
\begin{gather*}
    S_j^+ = c_j^\dagger F_j = F_j c_j^\dagger, \quad 
    S_j^- = c_j F_j = F_j c_j
    \\[0.5em] \Rightarrow
    S^z_j = S^+_j S^-_j - 1/2 = c_j^\dagger c_j - 1/2
\end{gather*} \qquad (j = 1,...,N)
$$

</div><br>

<center>
<img src="images/spin-fermion.png" width="450px" alt="string operator">
</center>

<div class="remark">

*Remark*: In terms of spin operators, we have
    
- Expression of $F_j$
    
    $$
    F_j = \prod_{l=1}^{j-1} (1 - 2n_l)
    = \prod_{l=1}^{j-1} (-2S^z_l)
    = \prod_{l=1}^{j-1} (-Z_l)
    $$

- Commutation relations with spin operators

    $$
    \begin{align*}
        [F_j, S_m^{\pm}] &= 0 \qquad j \le m \\
        \{F_j, S_m^{\pm}\} &= 0 \qquad j > m
    \end{align*}
    $$

</div>

----

*Proof of the commutation relations*:

- When $j \le m$, $S^z_m$ is not in the string $F_j$, which then only includes operators on other sites than $m$. Thus $[F_j, S^\pm_m] = 0$ 

- When $j > m$, $S^z_m$ is in $F_j$. Then

    $$
    \{F_j, S_m^\pm\} = (-2)^{j-1} 
    S^z_1 \cdots \cancel{S^z_m} \cdots S^z_{j-1} 
    \underbrace{\{S^z_m, S_m^\pm\}}_{=0} = 0
    \quad \blacksquare
    $$

----

We are now prepared to check that the introduction of the string operator indeed gives us the correct commutation relations of fermions:

$$
\{c_i, c_j\} = \{c_i^\dagger, c_j^\dagger\} = 0, \quad
\{c_i, c_j^\dagger\} = \delta_{ij}
$$

----

*Proof*: Without loss of generality, we can assume $i < j$. Then

$$
\begin{align*}
    \{c_i, c_j^{(\dagger)}\} &= \{S^-_i F_i, S^\pm_j F_j\}
    = S^-_i (F_i S^\pm_j) F_j + S^\pm_j (F_j S^-_i) F_i \\
    &= S^-_i (S^\pm_j F_i) F_j + S^\pm_j (-S^-_i F_j) F_i \\
    &= S^-_i S^\pm_j F_i F_j - S^-_i S^\pm_j F_i F_j = 0
    \\~\\
    \{c_i, c_i^\dagger\} &= \{S^-_i F_i, S^+_i F_i\}
    = S^-_i F_i S^+_i F_i + S^+_i F_i S^-_i F_i \\
    &= \{S^-_i, S^+_i\} (F_i)^2 = 1 
    &\qquad \blacksquare
\end{align*}
$$

----

### Mapping to Majorana Fermion

The complex fermion $c_j$ can be rearranged into **Majorana fermions** $a_j, b_j$, whose corresponding operators are *Hermitian*:

$$
\begin{bmatrix}
    c_j \\ c_j^\dagger
\end{bmatrix} = \frac{1}{\sqrt{2}} \begin{bmatrix}
    a_j + i b_j \\ a_i - i b_j
\end{bmatrix}
\Rightarrow 
\begin{bmatrix}
    a_j \\ b_j
\end{bmatrix} = \frac{1}{\sqrt{2}} \begin{bmatrix}
    c_j + c_j^\dagger \\
    -i (c_j - c_j^\dagger)
\end{bmatrix}    
$$

$a, b$ operators have the following anti-commutation relations: 

$$
\{a_i, a_j\} = \{b_i, b_j\} = \delta_{ij}, \quad
\{a_i, b_j\} = 0
$$

----

*Proof*:

$$
\begin{align*}
    \{a_i, a_j\} &= \frac{1}{2} \{c_i+c_i^\dagger, c_j+c_j^\dagger\}
    \\ &= \frac{1}{2} \Big[
        \{c_i, c_j\} + \{c_i, c_j^\dagger\} 
        + \{c_i^\dagger, c_j\} + \{c_i^\dagger, c_j^\dagger\}
    \Big]
    \\ &= \frac{1}{2} (0 + \delta_{ij} + \delta_{ij} + 0)
    = \delta_{ij}
    \\~\\
    \{b_i, b_j\} &= \frac{-1}{2} \{c_i-c_i^\dagger, c_j-c_j^\dagger\}
    \\ &= \frac{-1}{2} \Big[
        \{c_i, c_j\} - \{c_i, c_j^\dagger\} 
        - \{c_i^\dagger, c_j\} + \{c_i^\dagger, c_j^\dagger\}
    \Big]
    \\ &= \frac{-1}{2} (0 - \delta_{ij} - \delta_{ij} + 0)
    = \delta_{ij}
    \\~\\
    \{a_i, b_j\} &\propto \{c_i + c_i^\dagger, c_j - c_j^\dagger\}
    \\ &= \{c_i, c_j\} - \{c_i, c_j^\dagger\}
    + \{c_i^\dagger, c_j\} - \{c_i^\dagger, c_j^\dagger\} 
    \\ &= 0 - \delta_{ij} + \delta_{ij} - 0 = 0
    \qquad \blacksquare
\end{align*}
$$

----

Next we determine the mapping from spin to Majorana fermions. 

$$
\begin{align*}
    c_j &= S_j^- F_j = (S^x_j - iS^y_j) F_j
    \overset{!}{=} \frac{1}{\sqrt{2}}(a_j + ib_j)
    \\
    c_j^\dagger &= S_j^+ F_j = (S^x_j + iS^y_j) F_j
    \overset{!}{=} \frac{1}{\sqrt{2}}(a_j - ib_j)
\end{align*}
$$

Comparing with the definition of $a_j, b_j$, we obtain (remember that $F_j$ is Hermitian)

<div class="result">

**Jordan-Wigner transformation to Majorana fermions:**

$$
a_j = \sqrt{2} S^x_j F_j, \quad
b_j = -\sqrt{2} S^y_j F_j \qquad
\bigg[ F_j = \prod_{l=1}^{j-1} (-Z_l) \bigg]
$$

</div><br>

Let us verify the anti-commutation relations of $a, b$ again using the spin representation. 

----

*Proof*: 

----

## Application: Heisenberg-like Spin Chain

Now we use Jordan-Wigner transformation to map the Hamiltonian $H^{A/P}$ of **Heisenberg-like models** to fermion Hamiltonian $H_F$. 

<div class="result">

**Heisenberg-like spin chain:**

- Local Hamiltonian and $\mathbb{Z}_2$ generator

    $$
    \begin{gather*}
        H_j = J_x S^x_j S^x_{j+1} + J_y S^y_j S^y_{j+1}
        + J_z S^z_j S^z_{j+1} - h S^z_j, \quad
        Z = \textstyle{\prod_{j=1}^N} Z_j
    \end{gather*}
    $$

- APBC boundary term

    $$
    \begin{align*}
        H^A_N &= Z_1 H_N Z_1 \\
        &= - J_x S^x_N S^x_1 - J_y S^y_N S^y_1 
        + J_z S^z_j S^z_{j+1} - h S^z_N
    \end{align*}
    $$

</div><br>

<div class="remark">

*Remark*: Important special cases of Heisenberg-like models

- **(Isotropic) Heisenberg model**: $J_x = J_y = J_z, \ h = 0$
- **Transverse field Ising model**: $J_y = J_z = 0$; critical value $-2J_x = h$
- **XY model**: $J_z = 0$
- **XXZ model**: $J_x = J_y, \ h = 0$

</div><br>

It is convenient to express $H_j$ in terms of $S^\pm$: 

$$
S_j^{\pm} = S_j^x \pm i S_j^y 
\, \Rightarrow \, \left\{
\begin{align*}
    S_j^x &= \frac{1}{2}(S_j^- + S_j^+)
    \\
    S_j^y &= \frac{i}{2}(S_j^- - S_j^+)
\end{align*}
\right.
$$

The first two terms of $H_j$ can then be written as

$$
\begin{align*}
    &\frac{J_x}{4} (S_j^- + S_j^+)(S_{j+1}^- + S_{j+1}^+)
    - \frac{J_y}{4}(S_j^- - S_j^+)(S_{j+1}^- - S_{j+1}^+)
    \\
    &= t(S_j^+ S_{j+1}^- + S_j^- S_{j+1}^+)
    + \Delta (S_j^+ S_{j+1}^+ + S_j^- S_{j+1}^-)
    \\
    &\boxed{
        = t(S_j^+ S_{j+1}^- + h.c.)
        + \Delta (S_j^+ S_{j+1}^+ + h.c.)
    }
    \\[1em]
    &\text{with} \qquad 
    t \equiv \frac{J_x + J_y}{4}, \quad
    \Delta \equiv \frac{J_x - J_y}{4}
\end{align*}
$$

The mapping of $S^z$-terms is the same for all boundary conditions:

$$
S^z_j \to n_j - 1/2
$$

Next we focus on the transformation of the $t,\Delta$-terms, which will be affected by the boundary condition. The following identity will be useful:

$$
F_j F_{j+1} 
= \prod_{l=1}^{j-1} (-1)^{n_l} \prod_{l'=1}^{j} (-1)^{n_{l'}}
= (-1)^{n_j}
$$

### Non-Boundary Terms

- **"Spin Hopping" $t$-Term**

    $$
    \begin{align*}
        S_j^+ S_{j+1}^-
        &= c_j^\dagger F_j c_{j+1} F_{j+1}
        = c_j^\dagger c_{j+1} F_j F_{j+1}
        \\
        &= c_j^\dagger c_{j+1} (-1)^{n_j}
        \\
        &= c_j^\dagger c_{j+1} \quad
        (\text{$\ne 0$ only when input $n_j = 0$})
    \end{align*}
    $$

    Combining with the h.c. term, we arrive at:

    $$
    S_j^+ S_{j+1}^- + h.c. = c_j^\dagger c_{j+1} + h.c.
    $$

- **"Spin Pairing" $\Delta$-Term**

    $$
    \begin{align*}
        S_j^+ S_{j+1}^+
        &= c_j^\dagger F_j c_{j+1}^\dagger F_{j+1}
        = c_j^\dagger c_{j+1}^\dagger F_j F_{j+1}
        \\
        &= c_j^\dagger c_{j+1}^\dagger (-1)^{n_j} 
        = c_j^\dagger c_{j+1}^\dagger
    \end{align*}
    $$

    The last equality follows from the same argument as for the previous term. Therefore (this term is related to the **$p$-wave superconductivity**)

    $$
    S_j^+ S_{j+1}^+ + h.c. = c_j^\dagger c_{j+1}^\dagger + h.c.
    $$

<div class="result">

**Local non-boundary term of fermion theory:** ($j = 1,...,N-1$)

$$
\begin{align*}
    (H_F)_j &= t(c_j^\dagger c_{j+1} + h.c.)
    + \Delta (c_j^\dagger c_{j+1}^\dagger + h.c.) 
    \\ &\quad
    + J_z (n_j - \tfrac{1}{2}) (n_{j+1} - \tfrac{1}{2})
    - h (n_j - \tfrac{1}{2})
\end{align*} \quad 
$$

</div><br>

### The Boundary Term $H_N$

Since the spin chain contains only nearest neighbor interaction, the only boundary term is $H_N$, which must be transformed carefully:

$$
\begin{align*}
    H^P_N &= + t(S_N^+ S_1^- + h.c.)
    + \Delta (S_N^+ S_1^+ + h.c.) + (\text{$S^z$-terms})
    \\
    H^A_N &= - t(S_N^+ S_1^- + h.c.)
    - \Delta (S_N^+ S_1^+ + h.c.) + (\text{$S^z$-terms})
\end{align*}
$$

The $S^z$-term can be transformed ordinarily. We focus on the first two terms:

$$
S_N^+ S_1^{(\pm)} = c_N^\dagger F_N c_1^{(\dagger)} \cancel{F_1}
= c_N^\dagger F_N c_1^{(\dagger)}
$$

Introduce the the **fermion number parity** operator

$$
P \equiv (-1)^{n_\text{tot}} = \exp(i\pi n_\text{tot})
\quad \bigg( n_\text{tot} \equiv \sum_{l=1}^N n_l \bigg)
$$

Obviously $P^2 = 1$, so its eigenvalues are $\pm 1$ ($n_\text{tot}$ is even or odd). Then we express $F_N$ in terms of $P$:

$$
\begin{align*}
    F_N &= F_N (-1)^{2n_N} = P (-1)^{n_N} \\ \Rightarrow
    S_N^+ S_1^{(\pm)} &= c_N^\dagger P (-1)^{n_N} c_1^{(\dagger)}
    \\
    &= c_N^\dagger P c_1^{(\dagger)} \qquad 
    (\text{$\ne 0$ only when input $n_N = 0$})
    \\
    &= - c_N^\dagger c_1^{(\dagger)} P \qquad
    (\{P, c_j^{(\dagger)}\} = 0 \ \text{for any} \ j)
\end{align*}
$$

Now we *require* that the boundary term of the fermion theory $(H_F)_N$ has the same form as the non-boundary term:
    
$$
\begin{align*}
    (H_F)_N &= t(c_N^\dagger c_{N+1} + h.c.)
    + \Delta (c_N^\dagger c_{N+1}^\dagger + h.c.) 
    \\ &\quad
    + J_z (n_j - \tfrac{1}{2}) (n_{j+1} - \tfrac{1}{2})
    - h \left(n_N - \tfrac{1}{2} \right)
\end{align*}
$$

($c_{N+1}$ will be defined shortly) so that the fermion Hamiltonian for *both* PBC and APBC are the *same*:

<div class="result">

**Hamiltonian of the fermion theory:**

$$
\begin{align*}
    H_F &= \sum_{j=1}^N \Big[
        t(c_j^\dagger c_{j+1} + h.c.)
        + \Delta (c_j^\dagger c_{j+1}^\dagger + h.c.) 
        \\ &\qquad \quad
        + J_z (n_j - \tfrac{1}{2}) (n_{j+1} - \tfrac{1}{2})
        - h (n_j - \tfrac{1}{2})
    \Big]
\end{align*}
$$

</div><br>

Then we need to define $c_{N+1}$ (i.e. choose the boundary condition for the fermion theory) as:

<div class="result">

**Boundary condition of fermion theory:**

$$
\begin{array}{ccc}
    \text{Spin BC} & c_{N+1}^{(\dagger)}\ \text{Definition} & \text{Fermion BC}
    \\[4pt] \hline \\[-8pt]
    \text{Periodic} & -c_1^{(\dagger)} P & \begin{aligned}
        P = -1 & \Rightarrow \text{Periodic} \\
        P = +1 & \Rightarrow \text{Anti-Periodic}
    \end{aligned}
    \\[10pt] \hline \\[-8pt]
    \text{Anti-Periodic} & +c_1^{(\dagger)} P & \begin{aligned}
        P = -1 & \Rightarrow \text{Anti-Periodic} \\
        P = +1 & \Rightarrow \text{Periodic}
    \end{aligned}
\end{array}
$$

</div><br>

<div class="remark">

*Remark*: The boundary conditions for the fermion theory are usually called:

- PBC: **Ramond (R) sector**
- APBC: **Neveu-Schwarz (NS) sector**

</div><br>

This leads to:

<div class="result">

**Relation between spin theory $H^{A/P}$ and fermion theory $H_F$:**

$$
\begin{align*}
    H^P &= \frac{1+P}{2} H_F^{(A)} + \frac{1-P}{2} H_F^{(P)}
    \\
    H^A &= \frac{1-P}{2} H_F^{(A)} + \frac{1+P}{2} H_F^{(P)}
\end{align*}
$$

where $H_F^{(A/P)}$ refers to $H_F$ with APBC/PBC. 

</div><br>
