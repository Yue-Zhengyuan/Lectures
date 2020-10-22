# LSZ Reduction Formula

For a general $m \to n$ scattering

$$
|p_1,...,p_m \rangle \to |p'_1,...,p'_n \rangle
$$

The scattering amplitude is given by the **LSZ reduction formula**

$$
\begin{aligned}
    &\langle p'_1,...,p'_n|S|p_1,...,p_m\rangle
    \\
    &= \prod_{j=1}^m\left[
        i \int d^4 x_j \, e^{-i p_j x_j} (\partial_j^2 + m^2)
    \right] 
    \\ &\quad \times
    \prod_{j=1}^n \left[
        i \int d^4 x_n \, e^{+i p'_j x'_j} (\partial_j^2 + m^2)
    \right] 
    \\ & \quad \times
    \langle \Omega | T[
        \phi(x_1) \cdots \phi(x_m)
        \phi(x'_1) \cdots \phi(x'_n)
    ] | \Omega \rangle
\end{aligned}
$$

where $\partial_i^2 \equiv (\partial/\partial x_i)^2$. Note that the sign on the exponential factor is $-$ for $p_1,...,p_m$, and $+$ for $p'_1,...,p_n$. 