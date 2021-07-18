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

## Periodic/Anti-Periodic Boundary Conditions

For the Ising chain, the PBC Hamiltonian $H^P$ and the $\mathbb{Z}_2$ symmetry generator $Z$ are combinations of local term:

<div class="result">

**Transverse field Ising model:**

$$
\begin{align*}
    H^P &= \sum_{j=1}^N H_j, \quad
    Z = \prod_{j=1}^N Z_j
    \\
    H_j &= - [J X_j X_{j+1} + h Z_j]
\end{align*}
$$

</div><br>

Next we determine the APBC Hamiltonian. 
