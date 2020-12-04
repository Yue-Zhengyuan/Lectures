<style>
    .remark {
        border-radius: 15px;
        padding: 20px;
        background-color: SeaGreen;
        color: White;
    }
</style>

# Dirac Equation

Starting from the Dirac Lagrangian (expressed in terms of the Dirac spinor)

$$
\mathcal{L} = \bar{\psi} (i \gamma^\mu \partial_\mu - m) \psi
$$

the equation of motion with respect to $\psi$ is

$$
\begin{aligned}
    0 &= \partial_{\mu} \left(
        \frac{\partial \mathcal{L}}{\partial \left(\partial_{\mu} \psi \right)}
    \right) 
    - \frac{\partial \mathcal{L}}{\partial \psi}
    \\
    &= i (\partial_\mu \bar{\psi}) \gamma^\mu - m \bar{\psi}
\end{aligned}
$$

Its Hermitian conjugate is called the **Dirac equation**:

$$
(i \gamma^\mu \partial_\mu - m) \psi(x) = 0
$$

## The Weyl Equations

In terms of the Weyl spinors, the Dirac equation is

$$
\begin{bmatrix}
    -m & i \sigma^\mu \partial_\mu
    \\
    i \bar{\sigma}^\mu \partial_\mu & -m
\end{bmatrix}
\begin{bmatrix}
    \psi_L \\ \psi_R
\end{bmatrix} = 0
$$

When $m = 0$, the equations for $\psi_L$ and $\psi_L$ decouple:

$$
\begin{aligned}
    i \bar{\sigma}^\mu \partial_\mu \psi_L &= 0
    \\
    i \sigma^\mu \partial_\mu \psi_R &= 0
\end{aligned}
$$

They are called the **Weyl equations**.

## Free Particle Solutions

The Dirac equation implies the Klein-Gordon equation, since

$$
\begin{aligned}
    0 &= (-i \gamma^\mu \partial_\mu - m)(i \gamma^\nu \partial_\nu - m) \psi(x)
    \\
    &= (\gamma^\mu \gamma^\nu \partial_\mu \partial_\nu - m^2) \psi
    \\
    &= (\tfrac{1}{2} \underbrace{\{\gamma^\mu, \gamma^\nu\}}_{2\eta^{\mu \nu}} \partial_\mu \partial_\nu + m^2) \psi
    \\
    &= (\partial^2 + m^2) \psi
\end{aligned}
$$

Based on this, we know that the *plane wave* solutions of the Dirac equation takes the form

$$
\psi(x) = u(p) e^{-ipx} \qquad p^2 = m^2
$$

A subtlety here is that $p^0$ can be either positive or negative. When $p^0$ is negative, we shall change the sign of the exponent to $+$ instead. Thus we have two types of solutions:

$$
\begin{aligned}
    &\text{Positive frequency:} &\quad
    \psi(x) &= u(p) e^{-ipx}
    \\
    &\text{Negative frequency:} &\quad
    \psi(x) &= v(p) e^{+ipx}
\end{aligned} \quad (p^2 = m^2)
$$

Here $u(p), v(p)$ are both 4-component objects. Next let us find the constraints on them. 

### Solution in the Rest Frame

Consider $u(p)$ first. Plugging the solution into the Dirac equation:

$$
(\gamma^\mu p_\mu - m) u(p) = 0
$$

It is convenient to go into the rest frame of the particle (by a boost), where $p = p_0 \equiv (m,0)$. Then

$$
(m \gamma^0 - m) u(p_0)
= m \begin{bmatrix}
    -1 & 1 \\ 1 & -1
\end{bmatrix} u(p_0) = 0
$$

The solution is

$$
u(p_0) = \sqrt{m} \begin{bmatrix}
    \xi \\ \xi
\end{bmatrix}
$$

where $\xi$ is a 2-component object (and we know that it should be a Weyl spinor), usually normalized by $\xi^\dagger \xi = 1$; the coefficient $\sqrt{m}$ in added for later convenience. 

<div class="remark">

*Remark*: We discover that we are only able to choose two components out of the four in the Dirac spinor $\psi$. This two remaining degrees of freedom is expected for spin-1/2 particles. 

</div><br>

### Solution in a General Frame

Now let us return to the "lab" frame by boost. Suppose that the particle is moving in the $z$-direction. The finite boost operator along the $z$-direction in the Weyl representation is given by

$$
S^{03} = -\frac{i}{2} \begin{bmatrix}
    \sigma^3 & 0 \\ 0 & -\sigma^3
\end{bmatrix}
$$

Thus the general $u(p)$ is ($\beta$ is the rapidity of the boost)

$$
\begin{aligned}
    u(p) &= \exp (-i \beta S^{03}) \, u(p_0)
    \\
    &= \begin{bmatrix}
        \bigg(
            \sqrt{E + p^3} \dfrac{1 - \sigma^3}{2}
            + \sqrt{E - p^3} \dfrac{1 + \sigma^3}{2}
        \bigg) \xi
        \\[1em]
        \bigg(
            \sqrt{E + p^3} \dfrac{1 + \sigma^3}{2}
            + \sqrt{E - p^3} \dfrac{1 - \sigma^3}{2}
        \bigg) \xi
    \end{bmatrix}
\end{aligned}
$$

which can be put into the vector form (and thus applicable to particles moving in any direction)

$$
u(p) = \begin{bmatrix}
    \sqrt{p_\mu \sigma^\mu} \xi
    \\[0.5em]
    \sqrt{p_\mu \bar{\sigma}^\mu} \xi
\end{bmatrix}
$$

Note that we have eliminated $m$ using the boost to the momentum (omitting the $x,y$ components)

$$
\begin{aligned}
    \begin{bmatrix}
        E \\ p^3
    \end{bmatrix} &= \exp \left\{
        -i\beta \begin{bmatrix}
            i & 0 \\ 0 & i
        \end{bmatrix}
    \right\} \begin{bmatrix}
        m \\ 0
    \end{bmatrix}
    \\
    &= \begin{bmatrix}
        m \cosh \beta \\ m \sinh \beta
    \end{bmatrix}
\end{aligned}
$$

### Spin-up and Spin-down Solutions and Helicity

It will later turn out that the spinor $\xi$ determines the *spin* of the particle:

$$
\begin{aligned}
    \xi &= \begin{bmatrix}
        1 \\ 0
    \end{bmatrix}: \text{spin up along } \mathbf{p}
    \\[1em]
    \xi &= \begin{bmatrix}
        0 \\ 1
    \end{bmatrix}: \text{spin down along } \mathbf{p}
\end{aligned}
$$

### Normalization of $u(p)$

The object $u^\dagger u$ is *not* Lorentz invariant:

$$
\begin{aligned}
    u^\dagger u 
    &= \begin{bmatrix}
        \xi^\dagger \sqrt{p_\mu \sigma^\mu} &
        \xi^\dagger \sqrt{p_\mu \bar{\sigma}^\mu}
    \end{bmatrix} \begin{bmatrix}
        \sqrt{p_\nu \sigma^\nu} \xi
        \\[0.5em]
        \sqrt{p_\nu \bar{\sigma}^\nu} \xi
    \end{bmatrix}
\end{aligned}
$$

Note that

$$
(p_\mu \sigma^\mu) (p_\nu \sigma^\nu)
= (p_\mu \bar{\sigma}^\mu) (p_\nu \bar{\sigma}^\nu)
=
$$

Using the identity

$$
(p_\mu \sigma^\mu)(p_\nu \bar{\sigma}^\nu)
= p^2 (= m^2)
$$
