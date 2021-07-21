# XXZ Spin Chain

<div class="result">

**XXZ spin chain:**

- Non-boundary local spin Hamiltonian
    
    $$
    \begin{align*}
        H_j &= J_\perp (S^x_j S^x_{j+1} + S^y_j S^y_{j+1})
        + J_z S^z_j S^z_{j+1} - h S^z_j \\
        &= \frac{J_\perp}{2} (S_j^+ S_{j+1}^- + h.c.)
        + J_z S^z_j S^z_{j+1} - h S^z_j
    \end{align*}
    $$

- Fermion Hamiltonian
    
    $$
    \begin{align*}
        H_F &= \sum_{j=1}^N \bigg[
            \frac{J_\perp}{2}(c_j^\dagger c_{j+1} + h.c.)
            \\ &\qquad \quad
            + J_z \left(n_j - \frac{1}{2}\right)
            \left(n_{j+1} - \frac{1}{2}\right)
            - h \left(n_j - \frac{1}{2}\right)
        \bigg]
    \end{align*}
    $$

</div><br>

## The Luttinger Liquid Phase

<center>
<img src="images/xxz_phase.png" width="300pt">
</center>

The XXZ chain is in the Luttinger liquid phase when

$$
-1 \le \frac{J_z}{J_\perp} \le 1
\quad \text{or} \quad
-1 \le \frac{V}{2t} \le 1
$$

By comparison with Bethe ansatz exact solution, the Luttinger parameter (compactified radius) $K$ and the velocity $u$ can be determined as ($0 \le g \le 1$)

$$
\frac{J_z}{J_\perp} = -\cos (\pi g)
\  \Rightarrow \  \left\{
\begin{align*}
    K &= \frac{1}{2g} \\
    u &= \frac{1}{1-g} \sin(\pi(1-g)) \frac{J_\perp}{2}
\end{align*}
\right.
$$

To recast this result, 