<style>
    .katex {
        font-size: 1.1em;
    }
    .remark {
        border-radius: 15px;
        padding: 20px;
        background-color: SeaGreen;
        color: White;
    }
    .result {
        border-radius: 15px;
        padding: 20px;
        background-color: DarkSlateBlue;
        color: White;
    }
</style>

# Canonical Quantization on Cylinder

*Additional Reference: Coleman, P. (2015). **Introduction to many-body physics**. Cambridge University Press. Section 2.4.*

Let us quantize the massless free boson defined on a cylinder. We first work in the Minkowski space, and write $(x^0, x^1) = (t,x)$. The Lagrangian in real coordinates is

$$
\begin{aligned}
    \mathcal{L} &= \frac{g}{2} \int dx \,
    \p_\mu \phi \,\p^\mu \phi \\
    &= \frac{g}{2} \int dx \,(
        (\partial_t \phi)^2
        - (\partial_x \phi)^2
    )
\end{aligned}
$$

The normalization constant $g$ is usually chosen to be $1/4\pi$. 

## Step 1: Fourier Mode Expansion

Since $\phi$ satisfy periodic boundary condition (for a moment we choose a general cylinder circumference $L$)

$$
\phi(t,x) = \phi(t, x + L)
$$

we expand it as a Fourier series

$$
\begin{aligned}
    \phi(t,x) &= \sum_{n\in \Z} e^{2\pi inx/L} \phi_n(t)
    \\
    \text{Inverse: }\quad
    \phi_n(t) &= \frac{1}{L} \int_0^L dx \,
    e^{-2\pi inx/L} \phi(t,x)
\end{aligned}
$$

<div class="remark">

*Remark*: Classically the field $\phi$ is real. Thus 

$$ 
\phi(t,x) = [\phi(t,x)]^\dagger
\,\Rightarrow\,
\phi_{-n}=\phi_n^\dagger
$$

</div><br>

Now we recast the Lagrangian using the Fourier modes 

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
    \\
    &= \frac{1}{2} gL
    \sum_n \left[
        \dot{\phi}_n \dot{\phi}_{-n}
        - \left( \frac{2\pi n}{L} \right)^2 \phi_n \phi_{-n}
    \right]
\end{aligned}
$$

Here we used the orthogonal relation

$$
\int_0^Ldx \, e^{2\pi i (n - m) x/L}
= L \delta_{n m}
$$

## Step 2: Commutation Rules and Hamiltonian

We can now construct the Hamiltonian, in the hope that the final expression will be *a collection of harmonic oscillators*. First, the momentum conjugate to $\phi_n$ is

$$
\pi_n
= \frac{\partial \mathcal{L}}{\partial \dot{\phi}_n}
= g L \dot{\phi}_{-n}
$$

which allow us to eliminate the time derivative $\dot{\phi}_n$. We then impose the commutation relation 

$$
[\phi_n, \pi_{-m}] = i \delta_{n m}
$$

The $\phi_n$ modes will commute with each other, and so do the $\pi_n$ modes.

<div class="remark">

*Remark*: Because $\phi_{-n}=\phi_n^\dagger$, we also have the reality condition for the momentum

$$
\pi_{-n}=\pi_n^\dagger
$$

The the above commutation rule can also be written as $[\phi_n, \pi^\dagger_m] = i\delta_{mn}$. The dagger choice will make the original position space $\phi(x), \pi(x)$ satisfy the equal-time commutation rule 

$$
[\phi(t,x), \pi(t,y)] = i\delta(x - y)
$$

</div><br>

Then the Hamiltonian is

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

This indeed is a sum of *decoupled harmonic oscillators*: each summand can be rewritten as

$$
H_n = \frac{1}{2m} \pi_n\pi_{-n}
+ \frac{1}{2}m \omega_n^2 \phi_n \phi_{-n} 
\quad \text{with} \quad \left\{
\begin{aligned}
    m &= gL \\
    \omega_n &= \frac{2\pi |n|}{L}
\end{aligned}
\right.
$$

However, *the $n=0$ mode has zero frequency* (but in SHO we have $\omega_0 = \hbar \omega / 2 \ne 0$). Thus we shall treat this "zero mode" separately below. 

## Step 3: Construct Creation and Annihilation Operators

For each mode $n$, we can define the creation and annihilation operators in a way analogous to the simple harmonic oscillator: 

$$
\begin{aligned}
    b_n 
    &= \sqrt{\frac{m \omega_n}{2}} 
    \left(
        \phi_n 
        + \frac{i}{m \omega_n} \pi_{n} 
    \right)
    \\
    b_n^\dagger
    &= \sqrt{\frac{m \omega_n}{2}} 
    \left(
        \phi_{-n} 
        - \frac{i}{m \omega_n} \pi_{-n} 
    \right)
\end{aligned}
$$

Obviously this definition does not apply to the $n=0$ mode. 

Using the commutator $[\phi_n, \pi_{-m}] = i \delta_{n m}$ and the reality condition for $\phi$ and $\pi$, we can verify that

$$
[b_n, b_m]=0, \quad 
[b_n^\dagger, b_m^\dagger]=0, \quad 
[b_n, b_m^\dagger]=\delta_{n m}
$$

The inverse expressions of $\phi, \pi$ in terms of $a, a^\dagger$ are

$$
\begin{aligned}
    \phi_n &= \frac{1}{\sqrt{2m\omega_n}} (b_n + b_{-n}^\dagger)
    \\
    \pi_n &= -i \sqrt{\frac{m \omega_n}{2}}(b_n - b_{-n}^\dagger)
\end{aligned}
$$

It follows that (no commutation rules are used here)

$$
\begin{aligned}
    \pi_n \pi_{-n}
    &= \frac{m \omega_n}{2} (
        b_{-n}^\dagger b_{-n}
        + b_n b_n^\dagger
        - b_{-n}^\dagger b_n^\dagger
        - b_n b_{-n}
    )
    \\[1em]
    \phi_n \phi_{-n} 
    &= \frac{1}{2m \omega_n} (
        b_{-n}^\dagger b_{-n}
        + b_n b_n^\dagger
        + b_{-n}^\dagger b_n^\dagger
        + b_n b_{-n}
    )
\end{aligned}
$$

Then the Hamiltonian can be written as

$$
\begin{aligned}
    H 
    &= \frac{1}{2m} \pi_0^2 + \sum_{n \ne 0} H_n
    \\
    &= \frac{1}{2m} \pi_0^2 + \sum_{n \ne 0} 
    \frac{\omega_n}{4} \bigg[
        (
            b_{-n}^\dagger b_{-n}
            + b_n b_n^\dagger
            - b_{-n}^\dagger b_n^\dagger
            - b_n b_{-n}
        )
        \\ &\qquad \qquad \qquad + (
            b_{-n}^\dagger b_{-n}
            + b_n b_n^\dagger
            + b_{-n}^\dagger b_n^\dagger
            + b_n b_{-n}
        )
    \bigg]
    \\
    &= \frac{1}{2m} \pi_0^2 + \sum_{n \ne 0} 
    \frac{\omega_n}{2} (
        b_{-n}^\dagger b_{-n}
        + b_n b_n^\dagger
    )
    \\
    &= \frac{1}{2gL} \pi_0^2 
    + \frac{\pi}{L} \sum_{n \ne 0} |n| (
        b_n^\dagger b_n
        + b_n b_n^\dagger
    )
\end{aligned}
$$

We may absorb the $|n|$ factor into the operators: define

$$
a_n = 
\begin{cases}
    -i \sqrt{|n|} b_n & n > 0 \\
    i \sqrt{|n|} b_{-n}^\dagger & n < 0
\end{cases}
\quad
\bar{a}_n = 
\begin{cases}
    -i \sqrt{|n|} b_{-n} & n > 0 \\
    i \sqrt{|n|} b_n^\dagger & n < 0
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

## Step 4: Determine Time Dependence of Operators

In the Heisenberg picture, since the Hamiltonian is time-independent, we have the following equation of motion for an operator $A$:

$$
\frac{d}{dt} A(t) 
= i\, [H, A(t)] \quad
(\hbar = 1)
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
    \\ & \quad
    + \frac{i}{\sqrt{4\pi g}} \sum_{n \ne 0} 
        \frac{1}{n} (
        a_n e^{2\pi in(x - t)/L}
        - \bar{a}_{-n} e^{2\pi in(x + t)/L}
    )
\end{aligned}
$$

## Step 5: Map to Complex Plane

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

<div class="result">

**Mode expansion of free boson field on cylinder:**

$$
\phi(z, \bar{z})
= \phi_0 - \frac{i}{4\pi g}\ln (z \bar{z})
+ \frac{i}{\sqrt{4\pi g}}
\sum_{n \ne 0} \frac{1}{n} (
    a_n z^{-n} + \bar{a}_n \bar{z}^{-n}
)
$$

</div><br>

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
