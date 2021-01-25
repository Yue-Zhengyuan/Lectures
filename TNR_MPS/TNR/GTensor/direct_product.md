<style>
    .remark {
        border-radius: 15px;
        padding: 20px;
        background-color: SeaGreen;
        color: White;
    }
    .result {
        border-radius: 15px;
        padding: 20px;
        background-color: FireBrick;
        color: White;
    }
</style>

# Direct Product of Grassmann Tensors

*Program implementation: `gtensor.directprod`*

The **direct product** of two Grassmann tensors $\mathbf{A}(\theta), \mathbf{B}(\eta)$ is defined as

$$
\begin{aligned}
    [\mathbf{A} \otimes \mathbf{B}]_{i_1 ... i_r, j_1 ... j_s}^{m_1 ... m_r, n_1 ... n_s} 
    &\equiv 
    \mathbf{A}(\theta)_{i_1 ... i_r}^{m_1 ... m_r} 
    \mathbf{B}(\eta)_{j_1 ... j_s}^{n_1 ... n_s} 
    \\
    &= A_{i_1 ... i_r}^{m_1 ... m_r} 
    B_{j_1 ... j_s}^{n_1 ... n_s} 
    \theta_1^{m_1} ... \theta_r^{m_r} 
    \eta_1^{n_1} ... \eta_s^{n_s}
\end{aligned}
$$

The tensor elements are then simply related by ordinary direct product of ordinary tensors:

$$
[A \otimes B]_{i_1 ... i_r, j_1 ... j_s}^{m_1 ... m_r, n_1 ... n_s} 
= A_{i_1 ... i_r}^{m_1 ... m_r} 
B_{j_1 ... j_s}^{n_1 ... n_s} 
$$

The result tensor obviously has the parity

$$
P(\mathbf{A} \otimes \mathbf{B})
= P(\mathbf{A}) + P(\mathbf{B})
$$
