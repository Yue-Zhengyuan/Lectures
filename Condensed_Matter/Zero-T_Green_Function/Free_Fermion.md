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

# Example of Free Green's Function: <br>Free Fermion

For free fermion, the interaction picture coincides with the Heisenberg picture. We shall then omit the picture label $I$ or $H$ for the fields. The Hamiltonian is given by

$$
H = \sum_{\alpha} \epsilon_\alpha
c_{\alpha}^\dagger c_{\alpha}
$$

At the ground state, the electrons fill the lowest-energy states; the occupied state with maximum energy is called the **Fermi surface** (denoted by $F$). The energy of this ground state can be expressed as

$$
E_0^N = \sum_{\alpha < F} \epsilon_\alpha
$$

Therefore, electrons can only be created with $\alpha > F$, and annihilated with $\alpha < F$ (this is also interpreted as the creation of **holes**). 
