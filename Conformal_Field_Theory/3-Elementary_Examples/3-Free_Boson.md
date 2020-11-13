# Example: Free Boson

Usual Action $(c=1,\,x^0=t,\,x^1=x)$

$$
\begin{aligned}
    S &= \frac{g}{2} \int dx^2 
    \partial_\mu \phi \partial^\mu \phi
    \\
    &= \frac{g}{2} \int dx \, dt \,
    [(\partial_t \phi)^2 - (\partial_x \phi)^2]
\end{aligned}
$$

Lagrangian $(S = \int dt \, \mathcal{L}$)

$$
\mathcal{L} = \frac{g}{2} \int dx \,
[(\partial_t \phi)^2 - (\partial_x \phi)^2]
$$

Usually the normalization constant $g$ is set as $1/4\pi$.

## Canonical Quantization on the Cylinder

Let us put the boson field $\phi$ on a cylinder with circumference $L$; this makes the space in which the field lives **compact** (i.e. connected and closed). We also take the periodic boundary condition:

$$
\phi(t,x+L) = \phi(t,x)
$$

Due to the spatial periodicity, we expand the field as a Fourier series:

$$
\begin{aligned}
    \phi(t,x) 
    &= \sum_n e^{2 \pi i n x / L}
    \phi_n(t)
    \\
    \phi_n(t) &= \frac{1}{L} 
    \int dx \, e^{-2 \pi i n x / L}
    \phi(t,x)
\end{aligned}
$$

Since the field is real, we get

$$ 
\phi_{-n}=\phi_n^\dagger
$$

Now we recast the Lagrangian using the Fourier modes (in the process of canonical quantization, we always use the Minkowski space)

$$
\begin{aligned}
    \mathcal{L}
    &=\frac{g}{2} \int dx \,
    [(\partial_t \phi)^2 - (\partial_x \phi)^2]
    \\
    &= \frac{g}{2} \int dx \left[
        \sum_{n,m}  
        e^{2\pi i n x/L} e^{2\pi i m x/L}
        \dot{\phi}_n(t) \dot{\phi}_m(t)
        \right.
        \\ &\qquad
        \left.
        -\left(\frac{2\pi i}{L} \right)^2
        \sum_{n,m}  n m \,
        e^{2\pi i n x/L} e^{2\pi i m x/L}
        \phi_n(t) \phi_m(t)
    \right]
\end{aligned}
$$

First, we integrate over $x$ and make use of the completeness relation

$$
\int_0^Ldx \, e^{2\pi i (n - m) x/L}
= L \delta_{n m}
$$

Then

$$
\mathcal{L}
= \frac{1}{2} gL
\sum_n \left[
    \dot{\phi}_n \dot{\phi}_{-n}
    - \left( \frac{2\pi n}{L} \right)^2 \phi_n \phi_{-n}
\right]
$$

We can now construct the Hamiltonian: the momentum conjugate to $\phi_n$ is

$$
\pi_n
= \frac{\partial \mathcal{L}}{\partial \dot{\phi}_n}
= g L \dot{\phi}_{-n}
$$

(the sum over all $n$ cancels the factor $1/2$) and we impose the commutation relation 

$$
[\phi_n, \pi_m] = i \delta_{n m}
$$

Because $\phi_{-n}=\phi_n^\dagger$, we also have the reality condition for the momentum

$$
\pi_{-n}=\pi_n^\dagger
$$

Then

$$
\begin{aligned}
    H &=\sum_n  \pi_n\dot{\phi}_n-\mathcal{L} 
    \\
    &= \sum_n  \pi_n \frac{\pi_{-n}}{g L}
    - \frac{1}{2} g L \sum_n \frac{\pi_{-n}}{g L} \frac{\pi_n}{g L}
    + \frac{1}{2} g L \sum_n  \left(\frac{2\pi  n}{L} \right)^2 \phi_n \phi_{-n} 
    \\
    &=\frac{1}{2 g L} \sum_n  \left[
        \pi_n\pi_{-n}
        + (2\pi n g)^2 \phi_n \phi_{-n} 
    \right]
\end{aligned}
$$

Now we change $n\to -n$:

$$
\begin{aligned}
    H 
    &=\frac{1}{2 g L} \sum_n \left[
        \pi_{-n} \pi_n
        + (2\pi  n g)^2\phi_{-n} \phi_n
    \right]
    \\
    &=\sum_n \left[
        \frac{1}{2 g L} \pi_n^\dagger \pi_n
        + \frac{1}{2} g L \left(\frac{2\pi n}{L} \right)^2 \phi_n^\dagger \phi_n
    \right]
\end{aligned}
$$

This represents a sum of *decoupled harmonic oscillators* of frequencies: by setting $m = gL$ in the SHO Hamiltonian

$$
H = \frac{1}{2m} p^2 + \frac{1}{2}m \omega^2 x^2
$$

we can easily recognize that

$$
\omega_n=\frac{2\pi |n|}{L}
$$

However, *the $n=0$ mode vanishes* (but in SHO we have $\omega_0 = \hbar \omega / 2 \ne 0$): it is a consequence of the absence of a mass term, which, with the boundary conditions chosen, is the same as conformal invariance.

## Creation and Annihilation Operators

For each mode $n$, we can define the creation and annihilation operators in a way analogous to the simple harmonic oscillator:

SHO:

$$
H=\frac{1}{2}m \omega^2x^2+\frac{1}{2m}p^2 
\Rightarrow
a=\sqrt{\frac{m \omega}{2}} \left(x+\frac{i}{m \omega}p\right)
$$

Free boson CFT (we use $\tilde{a}$, since we shall modify the definition later):

$$
\begin{aligned}
    \tilde{a}_n 
    &=\sqrt{\frac{1}{2}g L \frac{2\pi |n|}{L}} \left(\phi_n+\frac{i}{g L \, 2\pi |n|/L} \pi_n^\dagger \right)
    \\
    &=\frac{1}{\sqrt{4\pi|n| g}} (
        2\pi|n| g \phi_n + i \pi_n^\dagger
    )
\end{aligned}
$$

Obviously this definition does not apply to the $n=0$ mode. 

Using the commutator $[\phi_n, \pi_m] = i \delta_{n m}$ and the reality condition for $\phi$ and $\pi$, we can verify that

$$
[\tilde{a}_n, \tilde{a}_m]=0, \quad 
[\tilde{a}_n^\dagger, \tilde{a}_m^\dagger]=0, \quad 
[\tilde{a}_n, \tilde{a}_m^\dagger]=\delta_{n m}
$$

The inverse expressions of $\phi, \pi$ in terms of $\tilde{a}, \tilde{a}^\dagger$ are

$$
\begin{aligned}
    \phi_n 
    &= \frac{1}{\sqrt{4 \pi |n| g}}
    (\tilde{a}_n + \tilde{a}_{-n}^\dagger)
    \\
    \pi_n
    &= i \sqrt{\pi |n| g} (\tilde{a}_n^\dagger - \tilde{a}_{-n})
\end{aligned}
$$

Then the Hamiltonian can be written as

$$
\begin{aligned}
    H 
    &=\sum_n \left[
        \frac{1}{2 g L} \pi_n^\dagger \pi_n
        + \frac{1}{2} g L \left(\frac{2\pi n}{L} \right)^2 \phi_n^\dagger \phi_n
    \right]
    \\
    &= \frac{1}{2gL} \pi_0^\dagger \pi_0
    \\ &\qquad
    + \sum_{n \ne 0} \left[
        \frac{\pi |n|}{L} (
            \tilde{a}_n^\dagger \tilde{a}_n 
            + \tilde{a}_n \tilde{a}_n^\dagger
            + \tilde{a}_{-n}^\dagger \tilde{a}_{-n} 
            + \tilde{a}_{-n} \tilde{a}_{-n}^\dagger
        )
    \right]
    \\
    &= \frac{1}{2gL} \pi_0^2
    + \frac{2\pi}{L} \sum_{n \ne 0}
        |n| (
            \tilde{a}_n^\dagger \tilde{a}_n 
            + \tilde{a}_n \tilde{a}_n^\dagger
        )
\end{aligned}
$$

We may absorb the $\sqrt{|n|}$ factor into the operators: define

$$
a_n = 
\begin{cases}
    -i \sqrt{|n|} \tilde{a}_n & n > 0 \\
    i \sqrt{|n|} \tilde{a}_{-n}^\dagger & n < 0
\end{cases}
\quad
\bar{a}_n = 
\begin{cases}
    -i \sqrt{|n|} \tilde{a}_{-n} & n > 0 \\
    i \sqrt{|n|} \tilde{a}_n^\dagger & n < 0
\end{cases}
$$

We note that $\bar{a}_n \ne a_n^\dagger$. The commutation rules are

$$
[a_n, a_m] = n \delta_{n + m}, \quad
[\bar{a}_n, \bar{a}_m] = n \delta_{n+m}, \quad
[a_n, \bar{a}_m] = 0
$$

Then

$$
\begin{aligned}
    H 
    &= \frac{1}{2gL} \pi_0^2
    %\\ &\qquad
    + \frac{2\pi}{L} \sum_{n > 0}
        n (
            \tilde{a}_n^\dagger \tilde{a}_n 
            + \tilde{a}_n \tilde{a}_n^\dagger
        )
    \\ &\qquad
    + \frac{2\pi}{L} \sum_{n < 0}
        (-n) (
            \tilde{a}_n^\dagger \tilde{a}_n 
            + \tilde{a}_n \tilde{a}_n^\dagger
        )
    \\
    &= \frac{1}{2gL} \pi_0^2
    + \frac{2\pi}{L} \sum_{n \ne 0}
        (
            a_{-n} a_n
            + \bar{a}_{-n} \bar{a}_n
        )
\end{aligned}
$$

## Field Operator in Heisenberg Picture

In the Heisenberg picture $(\hbar = 1)$:

$$
\frac{d}{dt} A(t) 
= i\, [H, A(t)]
$$

- $n = 0$

    First, we notice that $\phi_0$ does not appear in $H$. This means that

    $$
    \frac{d}{dt} \pi_0(t) 
    = i  \, [H, \pi_0(t)] = 0
    $$

    i.e. $\pi_0$ is a constant of motion (*good* quantum number).

    Then for $\phi_0(t)$, we obtain

    $$
    \begin{aligned}
        \frac{d}{dt} \phi_0 
        &= i \, [H, \phi_0]
        \\
        &= \frac{i}{2gL} \, [\pi_0^2, \phi_0]
        = \frac{\pi_0}{gL}
    \end{aligned}
    \Rightarrow
    \phi_0(t) = \phi_0(0) + \frac{1}{gL} \pi_0 t
    $$

- $n \ne 0$

    In this case, we can exploit the $a, \bar{a}$ operators. Notice the commutation relation

    $$
    \begin{aligned}
        [H, a_n] 
        &= \frac{2\pi}{L} [a_{-n} a_n, a_n]
        = - \frac{2\pi}{L} n a_n
        \\
        [H, \bar{a}_n]
        &= \frac{2\pi}{L} [\bar{a}_{-n} \bar{a}_n, \bar{a}_n]
        = - \frac{2\pi}{L} n \bar{a}_n
    \end{aligned}
    $$

    Therefore

    $$
    a_n(t) = a_n(0) \, e^{-2\pi int/L}
    , \quad
    \bar{a}_n(t) = \bar{a}_n(0) \, e^{-2\pi int/L}
    $$

    Expressing $\phi, \pi$ in terms of $a, \bar{a}$:

    $$
    \phi_n 
    = \frac{i}{n \sqrt{4 \pi g}} (a_n - \bar{a}_{-n})
    , \quad
    \pi_n
    = \sqrt{\pi g} (\bar{a}_n + a_{-n})
    $$

    we obtain

    $$
    \begin{aligned}
        \phi_n(t) 
        &= \frac{i}{n \sqrt{4 \pi g}} (
            a_n e^{-2\pi int/L}
            - \bar{a}_{-n} \, e^{2\pi int/L}
        )
        \\
        \pi_n(t)
        &= \sqrt{\pi g} (
            \bar{a}_n e^{-2\pi int/L}
            + a_{-n} e^{2\pi int/L}
        )
    \end{aligned}
    $$

Recall that $\phi_n(t)$ are obtained from the Fourier transform, finally

$$
\begin{aligned}
    \phi(x,t) 
    &= \sum_n e^{2 \pi i n x / L} \phi_n(t)
    \\
    &= \phi_0 + \frac{1}{gL} \pi_0 t
    + \frac{i}{\sqrt{4\pi g}} \sum_{n \ne 0} 
        \frac{1}{n} (
        a_n e^{2\pi in(x - t)/L}
        - \bar{a}_{-n} e^{2\pi in(x + t)/L}
    )
\end{aligned}
$$

## The Holomorphic Fields

Going to the Euclidean spacetime by Wick rotation $(t \to i \tau)$, define

$$
z \equiv e^{2\pi (\tau - ix)/L}, \quad
\bar{z} \equiv e^{2\pi (\tau + ix)/L}
$$

Note that $\tau$ can then be expressed as

$$
z \bar{z} = e^{4 \pi \tau/L}
\Rightarrow
\tau = \frac{L}{4\pi} \ln (z \bar{z})
$$

We can rewrite $\phi(x,t)$ as

$$
\phi(z, \bar{z})
= \phi_0 - \frac{i}{4\pi g}\ln (z \bar{z})
+ \frac{i}{\sqrt{4\pi g}}
\sum_{n \ne 0} \frac{1}{n} (
    a_n z^{-n} + \bar{a}_n \bar{z}^{-n}
)
$$

Its derivatives are primary fields: e.g. the holomorphic field $\partial \phi$ is

$$
\begin{aligned}
    i \partial \phi (z)
    &= \frac{1}{4\pi g} \frac{\pi_0}{z}
    + \frac{1}{\sqrt{4\pi g}} \sum_{n \ne 0} 
    a_n z^{-n-1}
    \\
    &= \frac{1}{\sqrt{4\pi g}} \sum_{n} 
    a_n z^{-n-1}
\end{aligned}
$$

where, for convenience, we defined

$$
a_0 \equiv \bar{a}_0 \equiv 
\frac{\pi_0}{\sqrt{4\pi g}} 
$$

## Vertex Operators

The **vertex operators** for free boson is defined as

$$
\begin{aligned}
    \mathcal{V}_\alpha(z,\bar{z}) 
    &\equiv \, :e^{i \alpha \phi(z,\bar{z})}:
    \\
    &= \exp \left\{
        i \alpha \phi_0
        + \frac{\alpha}{\sqrt{4\pi g}}
        \sum_{n>0} \frac{1}{n} (
            a_{-n} z^n + \bar{a}_{-n} \bar{z}^n
        )
    \right\}
    \\ &\quad \times
    \exp \left\{
        \frac{\alpha}{4\pi g} \pi_0
        - \frac{\alpha}{\sqrt{4\pi g}}
        \sum_{n>0} \frac{1}{n} (
            a_{n} z^{-n} + \bar{a}_{n} \bar{z}^{-n}
        )
    \right\}
\end{aligned}
$$

----

*Proposition*: The vertex operators are **primary fields**, with dimensions

$$
h(\alpha) = \bar{h}(\alpha) 
= \frac{\alpha^2}{8\pi g}
$$

----

## The Fock Space

## Twisted (Anti-Periodic) Boundary Condition

## Compactified Boson

The free boson Lagrangian is *invariant* under a constant shift of the field:

$$
\phi \to \phi + \text{const}
$$

Thus we may restrict the range of the field to a *circle* (the radius $R$ is called the **compactification radius**), i.e. make the identification

$$
\phi(x,t) = \phi(x,t) + 2\pi R
$$

thus $\phi$ may be regarded as some *angular variable*.

To achieve this, two modifications are needed:

- $\pi_0 R \equiv e \in \mathbb{Z}$

    This is required to well-define the vertex operators $\mathcal{V}_\alpha$. 

    *Proof*:


- The periodic boundary condition is generalized to
    
    $$
    \phi(x+L,t) = \phi(x,t) + 2\pi m R \, 
    (= \phi(x,t))
    $$

    This means that as we goes around the circumference of the cylinder, the field $\phi$ winds around its circle by $m$ times. Thus $m$ is called the **winding number** of the field configuration.

With these modifications, the general $\phi(x,t)$ becomes $(e \in \mathbb{Z})$

$$
\begin{aligned}
    \phi(x,t) 
    &= \phi_0 + \frac{1}{gL} \frac{e}{R} t
    + \frac{2\pi mR}{L} x
    \\ &\quad
    + \frac{i}{\sqrt{4\pi g}} \sum_{n \ne 0} 
        \frac{1}{n} (
        a_n e^{2\pi in(x - t)/L}
        - \bar{a}_{-n} e^{2\pi in(x + t)/L}
    )
\end{aligned}
$$

Note that the additional term $2\pi mRx/L$ is not the only way to achieve the generalized PBC, but it is the simplest. 

In the holomorphic coordinates $z, \bar{z}$:

$$
\begin{aligned}
    \phi(z,\bar{z})
    &= \phi_0
    - i \left(
        \frac{e}{4\pi g R} + \frac{1}{2}m R
    \right) \ln z
    + \frac{i}{\sqrt{4\pi g}} \sum_{n \ne 0}
    \frac{1}{n} a_n z^{-n}
    \\ &\qquad
    - i \left(
        \frac{e}{4\pi g R} - \frac{1}{2}m R
    \right) \ln \bar{z}
    + \frac{i}{\sqrt{4\pi g}} \sum_{n \ne 0}
    \frac{1}{n} \bar{a}_n \bar{z}^{-n}
    \\
    i \partial \phi(z)
    &= \left(
        \frac{e}{4\pi gR} + \frac{1}{2}mR
    \right) \frac{1}{z}
    + \frac{1}{\sqrt{4\pi g}} 
    \sum_{n \ne 0} a_n z^{-n-1}
    \\
    i \bar{\partial} \phi(\bar{z})
    &= \left(
        \frac{e}{4\pi gR} - \frac{1}{2}mR
    \right) \frac{1}{\bar{z}}
    + \frac{1}{\sqrt{4\pi g}} 
    \sum_{n \ne 0} \bar{a}_n \bar{z}^{-n-1}
\end{aligned}
$$

Here we see that $a_0, \bar{a}_0$ should be redefined to

$$
\begin{aligned}
    a_0 
    &= \sqrt{4\pi g} \left(
        \frac{e}{4\pi gR} + \frac{1}{2}mR
    \right)
    \\
    \bar{a}_0 
    &= \sqrt{4\pi g} \left(
        \frac{e}{4\pi gR} - \frac{1}{2}mR
    \right)
\end{aligned}
$$

Then the generators $L_0, \bar{L}_0$ are found to be

$$
\begin{aligned}
    L_0 
    &= \sum_{n>0} a_{-n} a_n 
    + 2\pi g \left(
        \frac{e}{4\pi gR} + \frac{1}{2}mR
    \right)^2
    \\
    \bar{L}_0 
    &= \sum_{n>0} \bar{a}_{-n} {a}_n 
    + 2\pi g \left(
        \frac{e}{4\pi gR} - \frac{1}{2}mR
    \right)^2
\end{aligned}
$$