# *S*-Matrix from Feynman Diagrams

## LSZ Reduction Formula

For a general $m \to n$ scattering of real scalar (interacting) particles

$$
|\mathbf{p}_1,...,\mathbf{p}_m \rangle \to |\mathbf{p}'_1,...,\mathbf{p}'_n \rangle
$$

The scattering amplitude is related to the correlation function by the **LSZ reduction formula**

$$
\begin{aligned}
    &\langle \mathbf{p}'_1,...,\mathbf{p}'_n|S|\mathbf{p}_1,...,\mathbf{p}_m\rangle
    \\
    &= \prod_{j=1}^m\left[
        i \int d^4 x_j \, e^{-i p_j x_j} (\square_j + m^2)
    \right] 
    \\ &\quad \times
    \prod_{j=1}^n \left[
        i \int d^4 x_n \, e^{+i p'_j x'_j} (\square'_j + m^2)
    \right] 
    \\ & \quad \times
    \langle \Omega | T[
        \phi(x_1) \cdots \phi(x_m)
        \phi(x'_1) \cdots \phi(x'_n)
    ] | \Omega \rangle
\end{aligned}
$$

where $\square_i \equiv (\partial/\partial x_i)^2, \square'_i \equiv (\partial/\partial x'_i)^2$. Note that the sign on the exponential factor is $-$ for incoming particles $p_1,...,p_m$, and $+$ for outgoing particles $p'_1,...,p'_n$. If we are dealing with complex scalar particles or even photons, the formula will be accordingly modified. 

----

*Proof*:

----

## Feynman Rules for Scattering Amplitude