# Wick's Theorem

## Contraction of Field Operators

Given the normal-ordered product $N[\phi_1 \cdots \phi_n]$, the **contraction** of $\phi_i$ with $\phi_j$ is defined as the omission of these two operators from the normal order and their replacement by the two-point function $\langle \phi_i \phi_j \rangle$. For example

$$
N(\phi_1 \overgroup{\phi_2 \phi_3 \phi_4})
\, = \,
N(\phi_1 \phi_3) \langle \phi_2 \phi_4 \rangle
$$

## Wick's Theorem

The time-ordered product is equal to the normal-ordered product, plus **all possible ways** of contracting pairs of fields within it.

For example,

$$
\begin{aligned}
    \mathcal{T}(\phi_1 \phi_2) 
    &= \,
    N(\phi_1 \phi_2 + \overgroup{\phi_1 \phi_2})
    \\ &= \,
    N(\phi_1 \phi_2) + \langle \phi_1 \phi_2 \rangle
    \\
    \\
    \mathcal{T}(\phi_1 \phi_2 \phi_3)
    &= \,
    N(\phi_1 \phi_2 \phi_3
    + \overgroup{\phi_1 \phi_2} \phi_3
    \\ &\qquad \qquad
    + \overgroup{\phi_1 \phi_2 \phi_3}
    + \phi_1 \overgroup{\phi_2 \phi_3})
\end{aligned}
$$