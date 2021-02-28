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

# Green's Function: <br>Generating Functional (Boson)

## Motivation: Driven Harmonic Oscillator

### Single Oscillator

Consider the driven (bosonic) harmonic oscillator $H = H_0 + V(t)$:

$$
H_0 = \hbar \omega \left(
    b^\dagger b + \frac{1}{2}
\right) \qquad
\begin{aligned}
    V(t) &= \bar{z}(t) b + b^\dagger z(t) \\
    [b, b^\dagger] &= 1
\end{aligned}
$$

where $z(t), \bar{z}(t)$ are two *c*-number-valued functions; they are not complex conjugates of each other. In interaction picture, the time dependence of $b, b^\dagger$ can be easily determined (in the following the $I$ label is omitted):

$$
\begin{gathered}
    \begin{aligned}
        \frac{\partial b}{\partial t}
        &= \frac{i}{\hbar} [H_0, b]
        \\
        &= i \omega [b^\dagger, b] b
        \\
        &= -i \omega b
    \end{aligned} \qquad
    \begin{aligned}
        \frac{\partial b^\dagger}{\partial t}
        &= \frac{i}{\hbar} [H_0, b^\dagger]
        \\
        &= i \omega b^\dagger [b, b^\dagger]
        \\
        &= i \omega b^\dagger
    \end{aligned}
    \\ \Downarrow \\
    b(t) = b e^{-i\omega t}, \quad
    b^\dagger(t) = b^\dagger e^{i\omega t}
\end{gathered}
$$

Then the non-free part $V(t)$ in interaction picture is simply

$$
V(t) = \bar{z}(t) b(t) + b^\dagger(t) z(t)
$$

One is interested in the vacuum expectation value (VEV) of the time-evolution operator from $t = -\infty$ to $+\infty$:

$$
\begin{aligned}
    S(\bar{z},z) &\equiv
    \amp{0}{S(-\infty, +\infty)}{0}
    \\
    S(-\infty, +\infty) &= T{\left[ \exp{
        \left(
            \frac{-i}{\hbar} \int_{-\infty}^{\infty} dt' \, V(t')
        \right)
    } \right]}
\end{aligned}
$$

Here $\ket{0}$ is the *free* vacuum, or ground state of $H_0$. We now evaluate the time-ordered exponential explicitly. We first decomposed $S$ the product of many small evolution steps

$$
\begin{aligned}
    S(t_f,t_i) &= \lim_{N \to \infty} S(t_f, t_{N-1})
    \cdots S(t_2,t_1) S(t_1, t_i)
    \\
    &= \lim_{N \to \infty} S_{N} \cdots S_2 S_1
    \\[0.5em] \text{with} \quad
    t_r &= t_i + r \, \delta t, \quad
    \delta t = \frac{t_f - t_i}{N} \quad
    (r = 1,...,N)
\end{aligned}
$$

In each small step $S_r \, (n = 1,...,N)$, the time ordering can be removed, and the integral becomes product with $\delta t$:

$$
\begin{aligned}
    S_r &\simeq \exp{
        \left(
            -(i/\hbar) \delta t \, V(t_{n}) / \hbar
        \right)
    } = \exp(A_r - A_r^\dagger)
    \\[0.5em] \text{with} \quad
    A_r &= -(i/\hbar) \delta t \, \bar{z}(t_r) b(t_r), 
    \quad
    A_r^\dagger
    = +(i/\hbar) \delta t \, b^\dagger(t_r) z(t_r)
\end{aligned}
$$

Strictly, $A_r^\dagger$ is not the Hermitian conjugate of $A_r$, but we use this notation for convenience. Then the full evolution operator can be expressed as

$$
S(t',t) = \lim_{N \to \infty}
e^{A_N - A_N^\dagger} \cdots e^{A_1 - A_1^\dagger}
$$

We shall normal-order (putting $A_r^\dagger$ to the left) this product to remove terms having no contribution to the VEV. The following theorem will be used: 

<div class="result">

**Theorem:** For two operators $A, B$, if $[A,B]$ is a *c*-number, then

$$
e^{A+B} = e^B e^A e^{[A,B]/2}, \quad
e^A e^B = e^B e^A e^{[A,B]}
$$

</div><br>

In our context, we set $A \to A_r, B \to A_s^\dagger$, and find

$$
\begin{aligned}
    [A_r, A_s^\dagger]
    &= (\delta t/\hbar)^2 \bar{z}(t_r) z(t_s) [b(t_r), b^\dagger(t_s)]
    \\
    &= (\delta t/\hbar)^2 \bar{z}(t_r) z(t_s) e^{-i\omega(t_r - t_s)}
\end{aligned}
$$

which is indeed a *c*-number. Then

$$
S = \lim_{N \to \infty}
e^{-A_N^\dagger} e^{A_N} \cdots e^{-A_1^\dagger} e^{A_1}
e^{-\sum_r [A_r,A^\dagger_r] / 2}
$$

Now we move all the $e^{A_r}$ to the right. From the theorem stated earlier, we have

$$
\begin{aligned}
    S &= \cdots 
    e^{-A_3^\dagger} e^{A_3}
    e^{-A_2^\dagger} \underbrace{e^{A_2}
    e^{-A_1^\dagger}} e^{A_1}
    e^{-\sum_r [A_r,A^\dagger_r] / 2}

    \\ &\Downarrow \quad(\text{Move} \, e^{A_2}) \\

    &= \cdots e^{-A_3^\dagger} \underbrace{e^{A_3}
    e^{-A_2^\dagger} e^{-A_1^\dagger}}
    e^{A_2} e^{A_1}
    e^{-[A_2, A_1^\dagger]}
    e^{-\sum_r [A_r,A^\dagger_r] / 2}

    \\ &\Downarrow \quad(\text{Move} \, e^{A_3}) \\

    &= \cdots e^{-A_3^\dagger}
    e^{-A_2^\dagger} e^{-A_1^\dagger} 
    e^{A_3} e^{A_2} e^{A_1} \\ &\qquad \times
    e^{-[A_3, A_2^\dagger] - [A_3, A_1^\dagger]}
    e^{-[A_2, A_1^\dagger]}
    e^{-\sum_r [A_r,A^\dagger_r] / 2} \\
\end{aligned}
$$

From these simple examples, we can conclude that the final result is

$$
S = \underbrace{
    e^{-\sum_r A_r^\dagger} e^{\sum_r A_r}
}_{\normord{S}}
e^{-\sum_{r > s} [A_r, A_s^\dagger]}
e^{-\sum_r [A_r,A^\dagger_r] / 2}
$$

Due to the exponential function, $\expect{\normord{S}} = 1$. Therefore

$$
\begin{aligned}
    \expect{S(t_f,t_i)} &= e^{-\sum_{r > s} [A_r, A_s^\dagger]}
    e^{-\sum_r [A_r,A^\dagger_r] / 2} \\
    &= \exp \bigg[
        - \sum_{r \ge s} [A_r, A_s^\dagger] \left(
            1 - \frac{1}{2} \delta_{\a \b}
        \right)
    \bigg]
    \\ &\quad (\text{note the change from} \, r > s \, \text{to} \, r \ge s) \\
    &= \exp \bigg[
        - (\delta t/\hbar)^2 \sum_{r \ge s} 
        \bar{z}(t_r) z(t_s) 
        e^{-i\omega(t_r - t_s)} \left(
            1 - \frac{1}{2} \delta_{\a \b}
        \right)
    \bigg]
\end{aligned}
$$

In the $N \to +\infty$ limit, setting $t_r \to t, t_s \to t'$, we obtain

$$
\begin{aligned}
    (\delta t)^2 \sum_{r \ge s} &\to 
    \int_{t_i}^{t_f} dt \int_{t_i}^t dt'
    \\
    &= \int_{t_i}^{t_f} dt \, dt' \, \theta(t - t')
    \\[1em]
    \delta_{\a \b} &\to \delta(t - t')
\end{aligned}
$$

Due to the step function, the delta function does *not* contribute to the integral. Finally, sending $t_i \to -\infty, t_f \to +\infty$, we obtain

$$
\begin{aligned}
    S(\bar{z},z) &= \exp \bigg[
        \frac{-i}{\hbar} \int_{-\infty}^{\infty} dt \, dt'
        \bar{z}(t) G(t - t') z(t')
    \bigg] 
    \\[1em] \text{with} \quad
    G(t - t') &= \frac{-i}{\hbar} \theta(t - t') 
    e^{-i\omega(t - t')}
\end{aligned}
$$

### Multiple Oscillators

In general, for a system consisting of many independent oscillator modes (omitting the constant shift), we may add linear driving force for each mode

$$
H_0 = \sum_\a \hbar \omega_\a b_\a^\dagger b_\a
, \quad
V(t) = \sum_\a \Big[ \bar{z}_\a(t) b_\a + b^\dagger_\a z_\a(t) \Big]
$$

After a similar procedure, one find

<div class="result">

**Vacuum expectation value of $S$ (from $t = -\infty$ to $+\infty$):**

$$
S(\bar{z},z) \equiv \amp{0}{S}{0} = \exp \bigg[
    \frac{-i}{\hbar} \int_{-\infty}^{\infty} dt \, dt'
    \sum_{\a,\b}
    \bar{z}_\a(t) G_{\a \b}(t - t') 
    z_\b(t')
\bigg] 
$$

where $G_{\a \b}(t - t')$ is called the **single-particle (sp) Green's function**:

$$
G_{\a \b}(t - t') = \frac{-i}{\hbar} 
\delta_{\a \b} \, 
\theta(t - t') e^{-i\omega_\a(t - t')}
$$

</div><br>

## Green's Function

### Alternative Expression

We expand the functional $S(\bar{z},z)$ as a Dyson series:

$$
\begin{aligned}
    S(\bar{z},z) &\equiv
    \amp{0}{T{\left[ \exp{
        \left(
            \frac{-i}{\hbar} \int_{-\infty}^{\infty} dt \, V(t)
        \right)
    } \right]}}{0}
    \\
    &= \sum_{n=0}^\infty \frac{(-i)^n}{n! \hbar^n} 
    \int_{-\infty}^{\infty} dt_1 \cdots dt_n \,
    \amp{0}{T[V(t_1) \cdots V(t_n)]}{0} \\
    &= \exp \bigg[
        \frac{-i}{\hbar} \int_{-\infty}^{\infty} dt \, dt'
        \sum_{\a, \b}
        \bar{z}_\a(t) G_{\a \b}(t - t') z_\b(t')
    \bigg] 
\end{aligned}
$$

The zeroth terms of both sides are 1. For the term of first order in both $z, \bar{z}$: 

- LHS
    
    Note that $V(t)$ itself has zero VEV, thus the first order term corresponds to $n = 2$:

    $$
    \begin{aligned}
        \text{LHS}_1
        &= \frac{(-i)^2}{2\hbar^2} \int dt_1 \, dt_2
        \amp{0}{T[V(t_1) V(t_2)]}{0} \\
        &= \frac{(-i)^2}{2\hbar^2} \int dt_1 \, dt_2
        \sum_{\a, \b} \amp{0}{T \Big\{
            [\bar{z}_\a b_\a + b_\a^\dagger z_\a]_{t_1}
            [\bar{z}_\b b_\b + b_\b^\dagger z_\b]_{t_2}
        \Big \}}{0} \\
        &= \frac{(-i)^2}{2\hbar^2} \int dt_1 \, dt_2
        \sum_{\a, \b} \amp{0}{T \Big\{
            [\bar{z}_\a b_\a]_{t_1} [b_\b^\dagger z_\b]_{t_2}
            + [b_\a^\dagger z_\a]_{t_1} [\bar{z}_\b b_\b]_{t_2}
        \Big \}}{0} 
    \end{aligned}
    $$

    In the last step we used the property that only terms containing one $b$ and one $b^\dagger$ may survive. But the two remaining terms are in fact the same, since we are free to rename $t_1,t_2$ to $t_2,t_1$, or rename $r,s$ to $s,r$. Thus

    $$
    \text{LHS}_1 = \left(\frac{-i}{\hbar}\right)^2
    \int dt_1 \, dt_2 
    \sum_{\a, \b} \bar{z}_\a(t_1)
    \amp{0}{T[b_\a(t_1) b_\b^\dagger(t_2)]}{0}
    z_\b(t_2)
    $$

- RHS
    
    Expansion of RHS is simple:

    $$
    \text{RHS}_1 
    = \frac{-i}{\hbar} \int_{-\infty}^{\infty} dt \, dt'
    \sum_{\a, \b} \bar{z}_\a(t) G_{\a \b}(t - t') z_\b(t')
    $$

By comparison, we obtain an alternative expression of the sp Green's function:

<div class="result">

**Single-particle Green's function:**

$$
G_{\a \b}(t - t') = \frac{-i}{\hbar}
\amp{0}{T[b_\a(t) b_\b^\dagger(t')]}{0}
$$

</div><br>

<div class="remark">

*Remark*: This definition can be generalized to arbitrary interacting systems.

<div class="result">

**Single-particle Green's function with interaction:**

$$
G_{\a \b}(t,t')
= \frac{-i}{\hbar} \amp{\Psi_0^N}{
    T[b_{\a H}(t) b^\dagger_{\b H}(t')]
}{\Psi_0^N}
$$

</div><br>

where:

- $\ket{\Psi_0^N}$: $N$-particle ground state (of full Hamiltonian)
    
    For non-interacting systems (such as free boson), it is also denoted by $\ket{0}$.

- $b_{\a H}^{(\dagger)}$: Annihilation (creation) operator of state $\a$ in Heisenberg picture
    
    For non-interacting systems, this is the same as $b_{\a}^{(\dagger)}$ in interaction picture, since the two pictures coincide.

</div><br>

### Green's Function from Functional Derivatives

The sp Green's function can also be obtained from $S(\bar{z},z)$ by taking functional derivatives. Recall that $S(\bar{z},z)$ has Gaussian structure:

$$
S(\bar{z},z) = \exp \bigg[
    \frac{-i}{\hbar} \sum_{\a,\b}
    \int_{-\infty}^{\infty} dt_\a \, dt_\b \,
    \bar{z}(\a) G(\a - \b) z(\b)
\bigg] 
$$

Here we used the shorthand $(\a) \to {}_\a(t_\a), (\b) \to {}_\b(t_\b)$. Then

$$
\begin{aligned}
    \frac{\delta S}{\delta z(\mu)}
    = S \times \frac{-i}{\hbar} \sum_{\a,\b} 
    \frac{\delta}{\delta z(\mu)}
    \int_{-\infty}^{\infty} dt_\a \, dt_\b \,
    \bar{z}(\a) G(\a - \b) z(\b)
\end{aligned}
$$

Thus we have the following dictionary for taking the derivatives:

$$
i \frac{\delta}{\delta \bar{z}(\a)} \to b(\a), \quad
i \frac{\delta}{\delta z(\a)} \to b^\dagger(\a)
$$

where $b(\a)$ is a shorthand for $b_\a(t_\a)$. 

### *n*-Particle Green's Function

## Energy Formulation

Since we usually deal with time-independent Hamiltonian, the Green's function must also have time-translation symmetry:

$$
G_{\a \b}(t,t') = G_{\a \b}(t - t')
$$

Then we may Fourier transform the time to obtain Green's function in energy (or frequency) formulation:

$$
\begin{aligned}
    G_{\a \b}(\omega)
    &= \int_{-\infty}^{\infty} dt \, 
    e^{+i \omega t} G_{\a \b}(t)
    \\ &\Updownarrow \\
    G_{\a \b}(t)
    &= \int_{-\infty}^{\infty} \frac{d \omega}{2\pi} \, 
    e^{-i \omega t} G_{\a \b}(\omega)
\end{aligned}
$$

