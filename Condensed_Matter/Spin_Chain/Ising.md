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

# Transverse Field Ising Model

<div class="result">

**Transverse field Ising model (TFIM):**

- Non-boundary local spin Hamiltonian
    
    $$
    \begin{align*}
        H_j &= J_x S^x_j S^x_{j+1} - h S^z_j \\
        &= J (S_j^+ S_{j+1}^- + h.c.)
        + J (S_j^+ S_{j+1}^+ + h.c.)
        - h (n_j - \tfrac{1}{2})
        \\[0.7em] &\text{with} \quad
        J \equiv J_x/4
    \end{align*}
    $$

- Fermion Hamiltonian
    
    $$
    \begin{align*}
        H_F &= \sum_{j=1}^N \Big[
            J (c_j^\dagger c_{j+1} + h.c.)
            + J (c_j^\dagger c_{j+1}^\dagger + h.c.) 
            - h (n_j - \tfrac{1}{2})
        \Big]
    \end{align*}
    $$

</div><br>

## Introducing Majorana Fermions

The fermion Hamiltonian can be further simplified in terms of Majorana fermions $a_j, b_j$:

- For non-boundary terms, the conversion is straightforward:

    $$
    \begin{align*}
        (H_F)_j &= 
        \frac{J}{2} [
            (a_j - ib_j) (a_{j+1} + ib_{j+1})
            + (a_{j+1} - ib_{j+1}) (a_j + ib_j)
        ] \\ &\quad
        + \frac{J}{2} [
            (a_j - ib_j) (a_{j+1} - ib_{j+1})
            + (a_{j+1} + ib_{j+1}) (a_j + ib_j)
        ] \\ &\quad
        - \frac{h}{2} [
            (a_j - ib_j) (a_j + ib_j) - 1
        ] \\
        &= \frac{J}{2} [
            2\cancel{\{a_j, a_{j+1}\}} 
            + 2i a_{j+1} b_j - 2i b_j a_{j+1}
        ] \\ &\quad 
        - \frac{h}{2} [
            \cancel{a_j^2} + \cancel{b_j^2}
            + i(a_j b_j - b_j a_j)
        ] \\
        &= 2iJ a_{j+1} b_j + ih b_j a_j \quad
        (\text{Use} \ \{a_i,b_j\} = 0)
    \end{align*}
    $$

- For the boundary term $(H_F)_N$, we encounter the operator $a_{N+1}$. We now define it as
    
    $$
    \begin{align*}
        &\text{PBC} \ (c_{N+1} = c_1): & a_{N+1} &= a_1 \\
        &\text{APBC} \ (c_{N+1} = -c_1): & a_{N+1} &= -a_1
    \end{align*}
    $$

Finally

$$
H_F = i \sum_{j=1}^N \Big[
    2J a_{j+1} b_j + h b_j a_j
\Big]
$$

Due to $\{a_i, b_j\} = 0$, we may unify the two types of fermions $a, b$ by regarding them as the same fermion on different sites:

$$
a_j \to a_{2j-1}, \quad b_j \to a_{2j} \qquad(j = 1,...,N)
$$

The boundary conditions correspond to

$$
\begin{align*}
    &\text{PBC} \ (c_{N+1} = c_1): & a_{2N+1} &= a_1 \\
    &\text{APBC} \ (c_{N+1} = -c_1): & a_{2N+1} &= -a_1
\end{align*}
$$

<div class="result">

**TFIM in terms of Majorana fermion:**

$$
H_F = i \sum_{j=1}^N \Big[
    2J a_{2j+1} a_{2j} + h a_{2j} a_{2j-1}
\Big]
$$

</div><br>

<div class="remark">

*Remark*: We will see that the Ising model undergoes a quantum phase transition at $-2J_x = h$. Setting $-2J_x = h = 1$, the critical fermion Hamiltonian is even simpler:

$$
\begin{align*}
    H_F &= i \sum_{j=1}^{2N} a_{j+1} a_j
\end{align*}
$$

</div><br>


