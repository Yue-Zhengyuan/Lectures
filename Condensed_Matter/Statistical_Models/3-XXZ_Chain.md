# The XXZ Spin Chain

The Hamiltonian of the (1+1)D anisotropic **XXZ spin chain** is (periodic boundary condition is assumed)

$$
H = -J \sum_{i=0}^{N-1} (
    S_i^x S_{i+1}^x + S_i^y S_{i+1}^y
) - J_z \sum_{i=0}^{N-1} S_i^z S_{i+1}^z
$$

The model name comes from the fact that the coupling coefficient in the $X$ and $Y$ directions are the same, but they are different from that in $Z$. 

## Mapping to Fermion Model

Using $S_i^\pm$ to represent the Hamiltonian, we have

$$
\begin{aligned}
    &S_i^x S_{i+1}^x + S_i^y S_{i+1}^y
    \\
    &= \frac{1}{4}(S_i^- + S_i^+)(S_{i+1}^- + S_{i+1}^+)
    \\ &\qquad - \frac{1}{4}(S_i^- - S_i^+)(S_{i+1}^- - S_{i+1}^+)
    \\
    &= \frac{1}{2}(S_i^- S_{i+1}^+ + S_i^+ S_{i+1}^-)
    \\
    &= \frac{1}{2}(S_{i}^+ S_{i+1}^- + h.c.)
\end{aligned}
$$

Then

$$
H = -\frac{J}{2} \sum_{i=0}^{N-1} (
    S_{i}^+ S_{i+1}^- + h.c.
) - J_z \sum_{i=0}^{N-1} S_i^z S_{i+1}^z
$$

This is mapped by Jordan-Wigner transformation to

$$
H = -\frac{J}{2} \sum_{i=0}^{N-1} (
    c_i^\dagger c_{i+1} + h.c.
) - J_z \sum_{i=0}^{N-1} \left(n_i - \frac{1}{2}\right)
\left(n_{i+1} - \frac{1}{2}\right)
$$

which is the same as the $t$-$V$ model of spinless fermion:

$$
H = -t \sum_{i=0}^{N-1} (
    c_i^\dagger c_{i+1} + h.c.
) + V \sum_{i=0}^{N-1} \left(n_i - \frac{1}{2}\right)
\left(n_{i+1} - \frac{1}{2}\right)
$$
