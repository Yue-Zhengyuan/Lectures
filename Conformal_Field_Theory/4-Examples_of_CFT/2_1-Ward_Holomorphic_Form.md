# Holomorphic Form of Ward Identities

We already seen that 

$$
\begin{aligned}
    \partial_\mu \langle {T^\mu}_\nu (x) X\rangle
    & = -\sum_{i=1}^n \delta(x-x_i) 
    \partial_\nu \langle X \rangle
    \\
    \varepsilon_{\mu \nu} 
    \langle T^{\mu \nu}(x) X \rangle
    &= -i \sum_{i=1}^n s_i \delta(x-x_i) \langle X\rangle
    \\
    \langle {T^\mu}_\mu(x) X \rangle
    &= -\sum_{i=1}^n \delta(x-x_i) 
    \Delta_i \langle X \rangle
\end{aligned}
$$

where 

- $X \equiv \Phi(x_1) \cdots \Phi(x_n)$
- $s_i, \Delta_i$ are the spin and the scaling dimension of the field $\Phi(x_i)$
- $s_i \varepsilon_{\mu \nu}$ is the spin generator in 2D

## Math Appendix: Dirac $\delta$-Function on the Complex Plane

$$
\delta (x,y)
=\frac{1}{\pi}\partial_{\bar{z}}\left(\frac{1}{z}\right)
=\frac{1}{\pi}\partial_z\left(\frac{1}{\bar{z}}\right)
$$

Here $z\equiv x+i y, \bar{z}\equiv x-i y$

*Proof*: