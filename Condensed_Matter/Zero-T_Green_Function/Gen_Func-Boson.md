# Green's Function: <br>Generating Functional (Boson)

## Motivation: Driven Harmonic Oscillator

### Single Oscillator

Consider the driven (bosonic) harmonic oscillator $H = H_0 + V(t)$:

$$
H_0 = \hbar \omega \left(
    b^\dagger b + \frac{1}{2}
\right) \qquad
\begin{align*}
    V(t) &= \bar{z}(t) b + b^\dagger z(t) \\
    [b, b^\dagger] &= 1
\end{align*}
$$

where $z(t), \bar{z}(t)$ are two *c*-number-valued functions; they are not complex conjugates of each other. In interaction picture, the time dependence of $b, b^\dagger$ can be easily determined (in the following the $I$ label is omitted):

$$
\begin{gathered}
    \begin{align*}
        \frac{\partial b}{\partial t}
        &= \frac{i}{\hbar} [H_0, b]
        \\
        &= i \omega [b^\dagger, b] b
        \\
        &= -i \omega b
    \end{align*} \qquad
    \begin{align*}
        \frac{\partial b^\dagger}{\partial t}
        &= \frac{i}{\hbar} [H_0, b^\dagger]
        \\
        &= i \omega b^\dagger [b, b^\dagger]
        \\
        &= i \omega b^\dagger
    \end{align*}
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
\begin{align*}
    S(\bar{z},z) &\equiv
    \amp{0}{S(-\infty, +\infty)}{0}
    \\
    S(-\infty, +\infty) &= T{\left[ \exp{
        \left(
            \frac{-i}{\hbar} \int_{-\infty}^{\infty} dt' \, V(t')
        \right)
    } \right]}
\end{align*}
$$

Here $\ket{0}$ is the *free* vacuum, or ground state of $H_0$. We now evaluate the time-ordered exponential explicitly. We first decomposed $S$ the product of many small evolution steps

$$
\begin{align*}
    S(t_f,t_i) &= \lim_{N \to \infty} S(t_f, t_{N-1})
    \cdots S(t_2,t_1) S(t_1, t_i)
    \\
    &= \lim_{N \to \infty} S_{N} \cdots S_2 S_1
    \\[0.5em] \text{with} \quad
    t_r &= t_i + r \, \delta t, \quad
    \delta t = \frac{t_f - t_i}{N} \quad
    (r = 1,...,N)
\end{align*}
$$

In each small step $S_r \, (n = 1,...,N)$, the time ordering can be removed, and the integral becomes product with $\delta t$:

$$
\begin{align*}
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
\end{align*}
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
\begin{align*}
    [A_r, A_s^\dagger]
    &= (\delta t/\hbar)^2 \bar{z}(t_r) z(t_s) [b(t_r), b^\dagger(t_s)]
    \\
    &= (\delta t/\hbar)^2 \bar{z}(t_r) z(t_s) e^{-i\omega(t_r - t_s)}
\end{align*}
$$

which is indeed a *c*-number. Then

$$
S = \lim_{N \to \infty}
e^{-A_N^\dagger} e^{A_N} \cdots e^{-A_1^\dagger} e^{A_1}
e^{-\sum_r [A_r,A^\dagger_r] / 2}
$$

Now we move all the $e^{A_r}$ to the right. From the theorem stated earlier, we have

$$
\begin{align*}
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
\end{align*}
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
\begin{align*}
    \expect{S(t_f,t_i)} &= e^{-\sum_{r > s} [A_r, A_s^\dagger]}
    e^{-\sum_r [A_r,A^\dagger_r] / 2} \\
    &= \exp \bigg[
        - \sum_{r \ge s} [A_r, A_s^\dagger] \left(
            1 - \frac{1}{2} \delta_{\alpha \beta}
        \right)
    \bigg]
    \\ &\quad (\text{note the change from} \, r > s \, \text{to} \, r \ge s) \\
    &= \exp \bigg[
        - (\delta t/\hbar)^2 \sum_{r \ge s} 
        \bar{z}(t_r) z(t_s) 
        e^{-i\omega(t_r - t_s)} \left(
            1 - \frac{1}{2} \delta_{\alpha \beta}
        \right)
    \bigg]
\end{align*}
$$

In the $N \to +\infty$ limit, setting $t_r \to t, t_s \to t'$, we obtain

$$
\begin{align*}
    (\delta t)^2 \sum_{r \ge s} &\to 
    \int_{t_i}^{t_f} dt \int_{t_i}^t dt'
    \\
    &= \int_{t_i}^{t_f} dt \, dt' \, \theta(t - t')
    \\[1em]
    \delta_{\alpha \beta} &\to \delta(t - t')
\end{align*}
$$

Due to the step function, the delta function does *not* contribute to the integral. Finally, sending $t_i \to -\infty, t_f \to +\infty$, we obtain

$$
\begin{align*}
    S(\bar{z},z) &= \exp \bigg[
        \frac{-i}{\hbar} \int_{-\infty}^{\infty} dt \, dt'
        \bar{z}(t) G(t - t') z(t')
    \bigg] 
    \\[1em] \text{with} \quad
    G(t - t') &= \frac{-i}{\hbar} \theta(t - t') 
    e^{-i\omega(t - t')}
\end{align*}
$$

### Multiple Oscillators

In general, for a system consisting of many independent oscillator modes (omitting the constant shift), we may add linear driving force for each mode

$$
H_0 = \sum_\alpha \hbar \omega_\alpha b_\alpha^\dagger b_\alpha
, \quad
V(t) = \sum_\alpha \Big[ \bar{z}_\alpha(t) b_\alpha + b^\dagger_\alpha z_\alpha(t) \Big]
$$

After a similar procedure, one find

<div class="result">

**Vacuum expectation value of $S$ (from $t = -\infty$ to $+\infty$):**

$$
S(\bar{z},z) \equiv \amp{0}{S}{0} = \exp \bigg[
    \frac{-i}{\hbar} \int_{-\infty}^{\infty} dt \, dt'
    \sum_{\alpha,\beta}
    \bar{z}_\alpha(t) G_{\alpha \beta}(t - t') 
    z_\beta(t')
\bigg] 
$$

where $G_{\alpha \beta}(t - t')$ is called the **single-particle (sp) Green's function**:

$$
G_{\alpha \beta}(t - t') = \frac{-i}{\hbar} 
\delta_{\alpha \beta} \, e^{-i\omega_\alpha(t - t')}
\theta(t - t') 
$$

</div><br>

## Green's Function

### Alternative Definition of Sp Green's Function

We expand the functional $S(\bar{z},z)$ as a Dyson series:

$$
\begin{align*}
    S(\bar{z},z) 
    &= \sum_{n=0}^\infty \frac{(-i)^n}{n! \hbar^n} 
    \int_{-\infty}^{\infty} dt_1 \cdots dt_n \,
    \amp{0}{T[V(t_1) \cdots V(t_n)]}{0} \\
    &= \exp \bigg[
        \frac{-i}{\hbar} \int_{-\infty}^{\infty} dt \, dt'
        \sum_{\alpha, \beta}
        \bar{z}_\alpha(t) G_{\alpha \beta}(t - t') z_\beta(t')
    \bigg] 
\end{align*}
$$

The zeroth terms of both sides are 1. For the term of first order in both $z, \bar{z}$: 

- LHS
    
    Note that $V(t)$ itself has zero VEV, thus the first order term corresponds to $n = 2$:

    $$
    \begin{align*}
        \text{LHS}_1
        &= \frac{(-i)^2}{2\hbar^2} \int dt_1 \, dt_2
        \amp{0}{T[V(t_1) V(t_2)]}{0} \\
        &= \frac{(-i)^2}{2\hbar^2} \int dt_1 \, dt_2
        \sum_{\alpha, \beta} \amp{0}{T \Big\{
            [\bar{z}_\alpha b_\alpha + b_\alpha^\dagger z_\alpha]_{t_1}
            [\bar{z}_\beta b_\beta + b_\beta^\dagger z_\beta]_{t_2}
        \Big \}}{0} \\
        &= \frac{(-i)^2}{2\hbar^2} \int dt_1 \, dt_2
        \sum_{\alpha, \beta} \amp{0}{T \Big\{
            [\bar{z}_\alpha b_\alpha]_{t_1} [b_\beta^\dagger z_\beta]_{t_2}
            + [b_\alpha^\dagger z_\alpha]_{t_1} [\bar{z}_\beta b_\beta]_{t_2}
        \Big \}}{0} 
    \end{align*}
    $$

    In the last step we used the property that only terms containing one $b$ and one $b^\dagger$ may survive. But the two remaining terms are in fact the same, since we are free to rename $t_1,t_2$ to $t_2,t_1$, or rename $r,s$ to $s,r$. Thus

    $$
    \text{LHS}_1 = \left(\frac{-i}{\hbar}\right)^2
    \int dt_1 \, dt_2 
    \sum_{\alpha, \beta} \bar{z}_\alpha(t_1)
    \amp{0}{T[b_\alpha(t_1) b_\beta^\dagger(t_2)]}{0}
    z_\beta(t_2)
    $$

- RHS
    
    Expansion of RHS is simple:

    $$
    \text{RHS}_1 
    = \frac{-i}{\hbar} \int_{-\infty}^{\infty} dt \, dt'
    \sum_{\alpha, \beta} \bar{z}_\alpha(t) G_{\alpha \beta}(t - t') z_\beta(t')
    $$

By comparison, we obtain an alternative definition of the sp Green's function:

<div class="result">

**Single-particle Green's function:**

$$
G_{\alpha \beta}(t - t') = \frac{-i}{\hbar}
\amp{0}{T[b_\alpha(t) b_\beta^\dagger(t')]}{0}
$$

</div><br>

We can re-derive the explicit formula of $G_{\alpha \beta}$ from this alternative definition. 

$$
\begin{align*}
    &i \hbar G_{\alpha \beta}(t - t') 
    = \amp{0}{T[b_\alpha(t) b_\beta^\dagger(t')]}{0} \\
    &= \amp{0}{b_\alpha(t) b_\beta^\dagger(t')}{0} \theta(t - t')
    + \underbrace{
        \amp{0}{b_\beta^\dagger(t') b_\alpha(t)}{0}
    }_{=0} \theta(t' - t)
    \\
    &= \amp{0}{b_\alpha b_\beta^\dagger}{0}
    e^{-i \omega_\alpha t + i \omega_\beta t'} \theta(t - t')
    \\
    &= \amp{0}{
        [b_\alpha, b_\beta^\dagger] 
        + \cancel{b_\beta^\dagger b_\alpha}
    }{0} e^{-i \omega_\alpha t + i \omega_\beta t'} 
    \theta(t - t')
    \\
    &= \delta_{\alpha \beta} e^{-i \omega_\alpha (t - t')}
    \theta(t - t')
\end{align*}
$$

### Green's Function from Functional Derivatives

The sp Green's function can also be obtained from $S(\bar{z},z)$ 

$$
\begin{align*}
    S(\bar{z},z) &= \amp{0}{T e^{
        -(i/\hbar) \int d\tau \, V(\tau)
    }}{0}
    \\[1em]
    V(\tau) &= \sum_\mu [
        \bar{z}_\mu(\tau) b_\mu(\tau) 
        + b^\dagger_\mu(\tau) z_\mu(\tau)
    ]
\end{align*}
$$

by taking functional derivatives with respect to $\bar{z}$ or $z$. For this reason $S(\bar{z},z)$ is called a **generating functional**. For example,

$$
\begin{align*}
    \frac{\delta S}{\delta \bar{z}_\alpha(t)}
    &= \amp{0}{T\left[
        \frac{-i}{\hbar} \int d\tau 
        \frac{\delta V(\tau)}{\delta \bar{z}_\alpha(t)}
        \times e^{-(i/\hbar) \int d\tau \, V(\tau)}
    \right]}{0}
    \\
    \frac{\delta V(\tau)}{\delta \bar{z}_\alpha(t)}
    &= \sum_\mu \underbrace{
        \frac{\delta \bar{z}_\mu(\tau)}
        {\delta \bar{z}_\alpha(t)} 
    }_{= \delta_{\mu \alpha} \delta(\tau - t)}
    b_\mu(\tau) 
    = b_\alpha(\tau) \theta(\tau - t)
\end{align*} 
$$

Thus we obtain

$$
\begin{align*}
    i\hbar \frac{\delta S}{\delta \bar{z}_\alpha(t)}
    &= \amp{0}{T\left[
        b_\alpha(t)
        e^{-(i/\hbar) \int d\tau \, V(\tau)} 
    \right]}{0} \\
    &= \amp{0}{T[b_\alpha(t) S]}{0}
\end{align*}
$$

A similar result holds for derivative with respect to $z_\alpha(t)$: 

$$
i\hbar \frac{\delta S}{\delta z_\alpha(t)}
= \amp{0}{T[b^\dagger_\alpha(t) S]}{0}
$$

Obviously the derivations can be applied repeatedly, with the following rules to add new operators to time-ordered product on the RHS:

<div class="result">

**$S(\bar{z}, z)$ as generating functional:**

$$
i\hbar \frac{\delta}{\delta \bar{z}_\alpha(t_\alpha)}
\to b_\alpha(t_\alpha), \quad
i\hbar \frac{\delta}{\delta z_\alpha(t_\alpha)}
\to b^\dagger_\alpha(t_\alpha)
$$

</div><br>

Later derivations will add the new operator between the old ones and the $S$. Finally, if we set all the $z, \bar{z}$ to zero after the derivations, the $S$ will not appear in the final result, and we get the VEV of a product of various $b$'s and $b^\dagger$'s. Now we see that the sp Green's function can be obtained from

$$
\begin{align*}
    i\hbar G_{\alpha \beta}(t - t')
    &= \amp{0}{T[b_\alpha(t) b^\dagger_\beta(t')]}{0}
    \\
    &= \left[
        (i \hbar)^2 
        \frac{\delta}{\delta \bar{z}_\beta(t')}
        \frac{\delta}{\delta \bar{z}_\alpha(t)}
        S(\bar{z},z)
    \right]_{z,\bar{z} = 0}
\end{align*}
$$

----

Let us verify this result by plugging in

$$
S(\bar{z},z) = \exp \bigg[
    \frac{-i}{\hbar} \sum_{\mu,\nu}
    \int dt_\mu \, dt_\nu \,
    \bar{z}(\mu) G(\mu - \nu) z(\nu)
\bigg] 
$$

Here we used the shorthand $(\alpha) \to {}_\alpha(t_\alpha)$, etc. Then

$$
\begin{align*}
    i \hbar \frac{\delta S}{\delta \bar{z}(\alpha)}
    &= S \times \sum_{\mu,\nu}
    \int dt_\mu \, dt_\nu \,
    \underbrace{
        \frac{\delta \bar{z}(\mu)}{\delta \bar{z}(\alpha)} 
    }_{= \delta(\mu - \alpha)}
    G(\mu - \nu) z(\nu)
    \\
    &= S \times \underbrace{
        \sum_\nu 
        \int dt_\nu \, G(\alpha - \nu) z(\nu)
    }_{\equiv \mathcal{I}}
\end{align*}
$$

For the second derivative, we need to calculate

$$
\begin{align*}
    i \hbar \frac{\delta}{\delta z(\beta)} (S \mathcal{I})
    &= i \hbar \left[
        \frac{\delta S}{\delta z(\beta)} \mathcal{I}
        + S \frac{\delta \mathcal{I}}{\delta z(\beta)}
    \right]

    \\[1em]
    
    i \hbar \frac{\delta S}{\delta z(\beta)}
    &= S \times \sum_\mu 
    \int dt_\mu \, \bar{z}(\mu) G(\mu - \beta)
    \xrightarrow{z,\bar{z} = 0} 0
    
    \\[1em]

    i \hbar \frac{\delta \mathcal{I}}{\delta z(\beta)}
    &= i\hbar \, G(\alpha - \beta)
\end{align*}
$$

Thus we are left with (and note that $S(\bar{z}=0, z=0) = 1$)

$$
\left[
    (i \hbar)^2 
    \frac{\delta}{\delta \bar{z}(\beta)}
    \frac{\delta}{\delta \bar{z}(\alpha)}
    S(\bar{z},z)
\right]_{z,\bar{z} = 0}
= i\hbar \, G(\alpha - \beta)
\qquad \blacksquare
$$

----

