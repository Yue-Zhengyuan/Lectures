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

# Creation and Annihilation Operators

The number of particles can be variable. Then all possible states of the system of identical particles form the **Fock space**:

$$
\mathcal{F} \equiv \ket{0} \oplus \mathcal{H}(1)
\oplus \cdots \mathcal{H}(N) \oplus \cdots
$$

where $\ket{0}$ is the vacuum (no-particle) state. We can go back and forth between spaces of different number of particles using the creation/annihilation operators. 

The **creation operator**, which creates a particle at state $\ket{u}$, is defined as (note that $\ket{u},\ket{u_1},...\ket{u_N}$ below need *not* be one-body basis states)

<div class="result">

**Creation operator on an $N$-body state:**

$$
a_{\ket{u}}^\dagger S_\pm(N) \ket{u_1,...,u_N}
= \sqrt{N+1} S_\pm(N+1) \ket{u, u_1,...,u_N}
$$

</div><br>

As a special case, the action on vacuum ($N = 0$) is:

$$
a_{\ket{u}}^\dagger \ket{0} = \ket{u}
$$

Note that by convention, we put the new particle at the first slot of the symmetrized $(N+1)$-body state. This choice has no effect on boson systems, but matters for fermions (according to the first property of the $A(N)$ operator). Then, by repeating the definition, we obtain

<div class="result">

**Building the symmetrized state from vacuum:**

$$
S_\pm(N) \ket{u_1,...,u_N}
= \frac{1}{\sqrt{N!}} a^\dagger_{\ket{u_1}}
\cdots a^\dagger_{\ket{u_N}} \ket{0}
$$

</div><br>

The **annihilation operator** is defined as the Hermitian conjugate of the creation operator. We then immediately get its action on bras (using $S_\pm(N) = S^\dagger_\pm(N)$): 

$$
\bra{u_1,...,u_N} S_\pm(N) a_{\ket{u}}
= \sqrt{N+1} \bra{u, u_1,...,u_N} S_\pm(N+1) 
$$

It must remove one particle from the symmetrized state. To find its action on kets, we calculate the following amplitude:

$$
\begin{align*}
    &\amp{v_1,...,v_{N-1}}{S_\pm(N-1) a_\ket{u} S_\pm(N)}{u_1,...,u_N}
    \\
    &= \sqrt{N} \amp{u,v_1,...,v_{N-1}}{S_\pm^2(N)}{u_1,...,u_N}
    \\
    &= \frac{\sqrt{N}}{N!} D_\pm \begin{bmatrix}
        \braket{u}{u_1} & \cdots & \braket{u}{u_N} \\
        \braket{v_1}{u_1} & \cdots & \braket{v_1}{u_N} \\
        \vdots & & \vdots \\
        \braket{v_{N-1}}{u_1} & \cdots & \braket{v_{N-1}}{u_N}
    \end{bmatrix}
\end{align*}
$$

We expand $D_\pm$ with respect to the first row:

$$
\begin{align*}
    &= \frac{\sqrt{N}}{N!} \sum_{j=1}^N
    (\pm 1)^{j+1} \braket{u}{u_j} 
    D_\pm \{\braket{v_i}{u_k}\}_{k\ne j}
    \\
    &= \frac{1}{\sqrt{N}} \sum_{j=1}^N
    (\pm 1)^{j+1} \braket{u}{u_j}
    \amp{v_1,...,v_{N-1}}{S^2_\pm(N-1)}{u_1,...,\cancel{u_j},...,u_N}
\end{align*}
$$

Due to the arbitrariness of $\bra{v_1,...,v_{N-1}}$, we conclude that

<div class="result">

**Annihilation operator on an $N$-body state:**

$$
\begin{align*}
    &a_\ket{u} S_\pm(N) \ket{u_1,...,u_N}
    \\ &\quad
    = \frac{1}{\sqrt{N}} \sum_{j=1}^N (\pm 1)^{j+1}
    \braket{u}{u_j} S_\pm(N-1) 
    \ket{u_1,...,\cancel{u_j},...,u_N}
\end{align*}
$$

</div><br>

## The Algebra of Creation / Annihilation Operators

## Action on the Fock Basis

If we use the Fock basis, and let $\ket{u}$ be the $r$th basis state, then:

- For boson:

    $$
    \begin{align*}
        b_r^\dagger \sqrt{\frac{... N_r! ...}{N!}}
        \ket{...,N_r,...} 
        &= \sqrt{N+1} \sqrt{\frac{... (N_r+1)! ...}{(N+1)!}}
        \ket{...,N_r+1,...} 
        \\ \Rightarrow \quad
        b_r^\dagger \ket{...,N_r,...} 
        &= \sqrt{N_r + 1} \ket{...,N_r+1,...}
    \end{align*} 
    $$

- For fermion:

## Change of Basis

### The Field Operators

A special case of change of basis is to go to the *continuous position eigenstates*. The creation and annihilation operators in the position basis are called the **field operators**:

<div class="result">

**The field operators:**

$$
\begin{align*}
    \phi(x) &= \sum_r \braket{x}{r} a_r
    = \sum_r \phi_r(x) a_r
    \\
    \phi^\dagger(x) &= \sum_r a_r^\dagger \braket{r}{x} 
    = \sum_r \phi_r^*(x) a_r^\dagger
\end{align*}
$$

</div><br>
