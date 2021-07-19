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

## Boundary Conditions

For the Ising chain (transverse field Ising model, TFIM), the PBC Hamiltonian $H^P$ and the $\mathbb{Z}_2$ symmetry generator $Z$ are combinations of local term:

<div class="result">

**Transverse field Ising model (TFIM):**

- Local Hamiltonian and $\mathbb{Z}_2$ generator

    $$
    H_j = - (X_j X_{j+1} + h Z_j), \quad
    Z = \textstyle{\prod_{j=1}^N} Z_j
    $$

- APBC boundary term

    $$
    \begin{align*}
        H^A_N &= Z_1 H_N Z_1 
        = - Z_1 (X_N X_1 + h Z_N) Z_1 \\
        &= - (-X_N X_1 + h Z_N)
    \end{align*}
    $$

</div>
