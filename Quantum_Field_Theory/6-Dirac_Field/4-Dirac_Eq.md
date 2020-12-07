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

Here $u(p), v(p)$ are both 4-component objects. Next let us find the constraints on them. Plugging the solution into the Dirac equation:

$$
(\gamma^\mu p_\mu - m) u(p) = 0, \quad
(\gamma^\mu p_\mu + m) v(p) = 0, \quad
$$

More explicitly:

$$
\begin{bmatrix}
    -m & p_\mu \sigma^\mu
    \\
    p_\mu \bar{\sigma}^\mu & -m
\end{bmatrix} u(p) = 0, \quad
\begin{bmatrix}
    m & p_\mu \sigma^\mu
    \\
    p_\mu \bar{\sigma}^\mu & m
\end{bmatrix} v(p) = 0
$$

### Solution in the Rest Frame

It is convenient to go into the rest frame of the particle (by a boost), where $p = p_0 \equiv (m,0)$. Then

$$
\begin{bmatrix}
    -1 & 1 \\ 1 & -1
\end{bmatrix} u(p) = 0, \quad
\begin{bmatrix}
    1 & 1 \\ 1 & 1
\end{bmatrix} v(p) = 0
$$

The solution is

$$
u(p_0) = \sqrt{m} \begin{bmatrix}
    \xi \\ \xi
\end{bmatrix}, \quad
v(p_0) = \sqrt{m} \begin{bmatrix}
    \eta \\ -\eta
\end{bmatrix}
$$

where $\xi, \eta$ are 2-component objects (and we know that they are Weyl spinors), usually normalized by $\xi^\dagger \xi = 1$ and $\eta^\dagger \eta = 1$; the coefficient $\sqrt{m}$ in added for later convenience. 

Obviously there will be two linearly independent $\xi$ (or $\eta$). They will be labelled by $\xi^s, \eta^s$ with $s = 1,2$. 

### Solution in a General Frame

Now let us return to the "lab" frame by boost. Suppose that the particle is moving in the $z$-direction. The finite boost operator along the $z$-direction in the Weyl representation is given by

$$
S^{03} = \frac{i}{2} \begin{bmatrix}
    -\sigma^3 & 0 \\ 0 & \sigma^3
\end{bmatrix}
$$

Thus the general $u(p)$ is ($\beta$ is the rapidity of the boost)

$$
\begin{aligned}
    u(p) &= \exp (-i \beta S^{03}) \, u(p_0)
    \\
    &= \sqrt{m} \begin{bmatrix}
        e^{-\beta/2} & 0 & 0 & 0 \\
        0 & e^{\beta/2} & 0 & 0 \\
        0 & 0 & e^{\beta/2} & 0 \\
        0 & 0 & 0 & e^{-\beta/2}
    \end{bmatrix} u(p_0)
    \\
    &= \sqrt{m} \begin{bmatrix}
        \begin{bmatrix}
            e^{-\beta/2} & 0 \\
            0 & e^{\beta/2}
        \end{bmatrix} \xi
        \\[1em]
        \begin{bmatrix}
            e^{\beta/2} & 0 \\
            0 & e^{-\beta/2}
        \end{bmatrix} \xi
    \end{bmatrix}
\end{aligned}
$$

Now we can eliminate $m$ using the boost to the momentum to $p^\mu = (E,0,0,p^3)$ (below we omit the $x,y$ components)

$$
\begin{aligned}
    \begin{bmatrix}
        E \\ p^3
    \end{bmatrix} &= \exp \left\{
        -i\beta \begin{bmatrix}
            0 & i \\ i & 0
        \end{bmatrix}
    \right\} \begin{bmatrix}
        m \\ 0
    \end{bmatrix}
    \\
    &= \begin{bmatrix}
        \cosh \beta & \sinh \beta \\ 
        \sinh \beta & \cosh \beta
    \end{bmatrix} \begin{bmatrix}
        m \\ 0
    \end{bmatrix}
    \\
    &= \begin{bmatrix}
        m \cosh \beta \\ m \sinh \beta
    \end{bmatrix}
    \\[1em]
    \Rightarrow
    e^\beta &= \frac{E + p^3}{m}, \quad
    e^{-\beta} = \frac{E - p^3}{m}, \quad
\end{aligned}
$$

Then

$$
u(p) = \begin{bmatrix}
    \begin{bmatrix}
        \sqrt{E-p^3} & 0 \\
        0 & \sqrt{E+p^3}
    \end{bmatrix} \xi \\[1em]
    \begin{bmatrix}
        \sqrt{E+p^3} & 0 \\
        0 & \sqrt{E-p^3}
    \end{bmatrix} \xi \\
\end{bmatrix}
$$

This can be put into the vector form (and thus applicable to particles moving in any direction): be careful that  

$$
p_\mu = \eta_{\mu \nu} p^\nu = (E,0,0,-p^3)
$$

By direct calculation 

$$
\begin{aligned}
    p_\mu \sigma^\mu &= \begin{bmatrix}
        E - p^3 & 0 \\
        0 & E + p^3
    \end{bmatrix}
    \\
    p_\mu \bar{\sigma}^\mu &= \begin{bmatrix}
        E + p^3 & 0 \\
        0 & E - p^3
    \end{bmatrix}
\end{aligned}
$$

We finally obtain (here we put back the label $s$ to represent two linearly independent solutions)

$$
u^s(p) = \begin{bmatrix}
    \sqrt{p_\mu \sigma^\mu} \xi^s
    \\[0.5em]
    \sqrt{p_\mu \bar{\sigma}^\mu} \xi^s
\end{bmatrix}
$$

Similarly, for the negative-frequency solution

$$
v^s(p) = \begin{bmatrix}
    \sqrt{p_\mu \sigma^\mu} \eta^s
    \\[0.5em]
    -\sqrt{p_\mu \bar{\sigma}^\mu} \eta^s
\end{bmatrix}
$$

### Spinor Normalization

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

To make a Lorentz scalar, we define

$$
\bar{u}(p) \equiv u^\dagger(p) \gamma^0
$$

(and similarly for $v(p)$). Then



Using the identity

$$
(p_\mu \sigma^\mu)(p_\nu \bar{\sigma}^\nu)
= p^2 (= m^2)
$$

