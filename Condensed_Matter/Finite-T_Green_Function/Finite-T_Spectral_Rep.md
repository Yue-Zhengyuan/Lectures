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
    .imgtext{
        display: flex;
        align-items: center;
        justify-content: center;
    }
</style>

# Spectral Representation at Finite-*T*

## Lehmann Representation at Finite-*T*

Now we Fourier transform the usual time-ordered Green's function at finite temperature:

$$
\begin{aligned}
    i \bar{G}_{\alpha \beta}(t - t')
    &= \expect{T[a_\alpha(t) c^\dagger_\beta(t')]} \\
    &= e^{\beta F} \tr \left\{
        e^{-\beta H} T[a_\alpha(t) c^\dagger_\beta(t')]
    \right \}
\end{aligned}
$$

As usual, we first separate the time dependence from the $c$ operators: expressing the trace as a summation over energy eigenstates $\ket{m}$ (this label implicitly includes the number of particles), we have

$$
\begin{aligned}
    &\tr \left\{
        e^{-\beta H} T[a_\alpha(t) c^\dagger_\beta(t')]
    \right \}
    = \sum_m \amp{m}{
        e^{-\beta H} T[a_\alpha(t) c^\dagger_\beta(t')]
    }{m}
    \\
    &= \sum_m e^{-\beta E_m}
    \amp{m}{
        a_{\alpha} e^{-iH(t - t')} 
        a^\dagger_{\beta}
    }{m} e^{i E_m (t - t')} \theta(t - t')
    \\ &\quad
    \pm \sum_m e^{-\beta E_m} \amp{m}{
        a^\dagger_{\beta} e^{-iH(t' - t)}
        a_{\alpha}
    }{m} e^{i E_m (t' - t)} \theta(t' - t)
\end{aligned}
$$

As in the zero-*T* case, we insert identities to deal with $e^{\pm iH(t-t')}$: 

$$
\begin{aligned}
    &\amp{m}{
        a_{\alpha} e^{-iH(t - t')} 
        a^\dagger_{\beta}
    }{m}
    \\
    &= \sum_n \amp{m}{
        a_{\alpha} e^{-iH(t - t')} 
    }{n} \amp{n}{
        a^\dagger_{\beta}
    }{m}
    \\
    &= \sum_n e^{-iE_n(t - t')} \amp{m}{
        a_{\alpha}
    }{n} \amp{n}{
        a^\dagger_{\beta}
    }{m}

    \\[2em]

    &\amp{m}{
        a^\dagger_{\beta} e^{-iH(t' - t)}
        a_{\alpha}
    }{m}
    \\
    &= \sum_n \amp{m}{
        a^\dagger_{\beta} e^{-iH(t' - t)}
    }{n} \amp{n}{
        a_{\alpha}
    }{m}
    \\
    &= \sum_n e^{-iE_n(t' - t)} \amp{m}{
        a^\dagger_{\beta}
    }{n} \amp{n}{
        a_{\alpha}
    }{m}
\end{aligned}
$$

Collecting these results, we obtain (setting $t - t' \to t$)

$$
\begin{aligned}
    &i \bar{G}_{\alpha\beta}(t)
    \\
    &= e^{\beta F} \sum_{m,n} \bigg[
        e^{-\beta E_m} 
        \amp{m}{a_{\alpha}}{n} 
        \amp{n}{a^\dagger_{\beta}}{m} 
        e^{- i(E_n - E_m)t} \theta(t)
        \\ &\qquad \qquad \quad
        \mp e^{-\beta E_n} 
        \amp{n}{a^\dagger_{\beta}}{m} 
        \amp{m}{a_{\alpha}}{n} 
        e^{-i(E_n - E_m)t} \theta(-t)
    \bigg]
\end{aligned}
$$

Here we have secretly swapped the label $m,n$ for the second term in the summand. We note that the summand in both summations is nonzero when $\ket{n}$ has one more particle than $\ket{m}$ (i.e. $N_n = N_m + 1$). 

We can now Fourier transform: through a calculation parallel to the zero-*T* case

<div class="result">

**Green's function at finite temperature <br>(Lehmann representation):**

$$
\begin{aligned}
    \bar{G}_{\alpha\beta}(E)
    &= e^{\beta F} \sum_{m,n} 
    \amp{m}{a_{\alpha}}{n} 
    \amp{n}{a^\dagger_{\beta}}{m} 
    \\ &\quad \times \bigg[
        \frac{e^{-\beta E_m}}
        {E - (E_n - E_m) + i\eta} 
        \mp \frac{e^{-\beta E_n}}
        {E - (E_n - E_m) - i\eta}
    \bigg]
\end{aligned}
$$

</div><br>

<div class="remark">

*Remark*: If the basis $\alpha, \beta$ etc. are obtained from a conserved operator, then we may simply write

$$
\amp{m}{a_{\alpha}}{n} \amp{n}{a^\dagger_{\beta}}{m} 
= \delta_{\alpha \beta} |\amp{m}{a_\alpha}{n}|^2
$$

</div><br>

## Retarded and Advanced Green's Functions

In addition to the time-ordered Green's function, we also introduce two other kinds of Green's functions, which will appear in response theory:

<div class="result">

**Retarded and Advanced Green's functions:**

$$
\begin{aligned}
    i \bar{G}^R_{\alpha \beta}(t - t')
    &= \theta(t - t') \expect{
        [a_\alpha(t), a^\dagger_\beta(t')]_{\mp}
    } \\
    i \bar{G}^A_{\alpha \beta}(t - t')
    &= - \theta(t' - t) \expect{
        [a_\alpha(t), a^\dagger_\beta(t')]_{\mp}
    } 
\end{aligned}
$$

</div><br>

By similar calculations, one obtains

$$
\begin{aligned}
    &i \bar{G}^R_{\alpha\beta}(t)
    \\
    &= e^{\beta F} \sum_{m,n} \amp{m}{a_{\alpha}}{n} 
    \amp{n}{a^\dagger_{\beta}}{m} 
    \\ &\qquad \qquad \qquad \times
    (e^{-\beta E_m} \mp e^{-\beta E_n})
    e^{-i(E_n - E_m)t} \theta(t)
    \\
    &i \bar{G}^A_{\alpha\beta}(t)
    \\
    &= e^{\beta F} \sum_{m,n} 
    \amp{m}{a_{\alpha}}{n} 
    \amp{n}{a^\dagger_{\beta}}{m} 
    \\ &\qquad \qquad \qquad \times
    (- e^{-\beta E_m} \pm e^{-\beta E_n})
    e^{-i(E_n - E_m)t} \theta(-t)
\end{aligned}
$$

Their Fourier transforms are

<div class="result">

**Retarded/Advanced Green's function at finite temperature <br>(Lehmann representation):**

$$
\begin{aligned}
    \bar{G}^R_{\alpha\beta}(E)
    &= e^{\beta F} \sum_{m,n} 
    e^{-\beta E_m} \frac{
        [1 \mp e^{-\beta (E_n - E_m)}]
        \amp{m}{a_{\alpha}}{n} 
        \amp{n}{a^\dagger_{\beta}}{m} 
    }{
        E - (E_n - E_m) + i\eta
    } \\
    \bar{G}^A_{\alpha\beta}(E)
    &= e^{\beta F} \sum_{m,n} 
    e^{-\beta E_m} \frac{
        [1 \mp e^{-\beta (E_n - E_m)}]
        \amp{m}{a_{\alpha}}{n} 
        \amp{n}{a^\dagger_{\beta}}{m} 
    }{
        E - (E_n - E_m) - i\eta
    }
\end{aligned}
$$

</div><br>

## Relation between Green's Functions

From the structure of $\bar{G}^{R/A}$, we define 

<div class="result">

**The spectral function:**

$$
\begin{aligned}
    S_{\alpha \beta}(E)
    &= e^{\beta F} \sum_{m,n} 
    e^{-\beta E_m} (1 \mp e^{-\beta E})
    \amp{m}{a_{\alpha}}{n} 
    \amp{n}{a^\dagger_{\beta}}{m} 
    \\ &\qquad \qquad \times
    (2\pi) \delta[E - (E_n - E_m)]
\end{aligned}
$$

</div><br>

Let us now express the three kinds of Green's function in terms of $S$. The the Sokhotski–Plemelj theorem will be used below:

$$
\frac{1}{z \pm i\eta}
= \mathcal{P}\frac{1}{z} \mp i\pi \delta(z)
$$

- **Retarded/Advanced Green's function**

    From the Sokhotski–Plemelj theorem, one obtains

    $$
    \operatorname{Im} \bar{G}^A_{\alpha \beta}(E)
    = - \operatorname{Im} \bar{G}^R_{\alpha \beta}(E)
    = \frac{1}{2} S_{\alpha \beta}(E)
    $$

    The introduction of energy delta function in $S$ allows us to rewrite $\bar{G}^{R/A}$ as

    $$
    \begin{aligned}
        \bar{G}^R_{\alpha \beta}(E)
        &= \int_{-\infty}^{\infty} \frac{dE'}{2\pi}
        \frac{S_{\alpha \beta}(E')}
        {E - E' + i\eta}
        \\
        &= \int_{-\infty}^{\infty} \frac{dE'}{2\pi}
        S_{\alpha \beta}(E') \bigg[
            \mathcal{P} \frac{1}{E - E'}
            - i \pi \delta(E - E')
        \bigg]
        
        \\[1.5em]
        
        \bar{G}^A_{\alpha \beta}(E)
        &= \int_{-\infty}^{\infty} \frac{dE'}{2\pi}
        \frac{S_{\alpha \beta}(E')}
        {E - E' - i\eta}
        \\
        &= \int_{-\infty}^{\infty} \frac{dE'}{2\pi}
        S_{\alpha \beta}(E') \bigg[
            \mathcal{P} \frac{1}{E - E'}
            + i \pi \delta(E - E')
        \bigg]
    \end{aligned}
    $$

- **Time-ordered Green's function**

    We reexpress its Lehmann representation using the Sokhotski–Plemelj theorem:

    $$
    \begin{aligned}
        \bar{G}_{\alpha\beta}(E)
        &= e^{\beta F} \sum_{m,n} 
        \amp{m}{a_{\alpha}}{n} 
        \amp{n}{a^\dagger_{\beta}}{m} 
        \\ &\quad \times \bigg[
            e^{-\beta E_m} \left(
                \mathcal{P} \frac{1}{E - (E_n - E_m)} 
                - i\pi \delta[E - (E_n - E_m)]
            \right)
            \\ &\quad \quad
            \mp e^{-\beta E_n} \left(
                \mathcal{P} \frac{1}{E - (E_n - E_m)}
                + i\pi \delta[E - (E_n - E_m)]
            \right)
        \bigg]
        \\
        &= e^{\beta F} \sum_{m,n} 
        e^{-\beta E_m} \amp{m}{a_{\alpha}}{n} 
        \amp{n}{a^\dagger_{\beta}}{m} 
        \\ &\qquad \times \bigg[
            \mathcal{P} \frac{1}{E - (E_n - E_m)} 
            [1 \mp e^{-\beta(E_n - E_m)}]
            \\ &\qquad \quad
            - i\pi \delta[E - (E_n - E_m)]
            [1 \pm e^{-\beta(E_n - E_m)}]
        \bigg]
    \end{aligned}
    $$

    The first term in the square bracket can be converted using the delta function in $S$, yielding

    $$
    \begin{aligned}
        \bar{G}_{\alpha \beta}(E)
        &= \int_{-\infty}^{\infty} \frac{dE'}{2\pi} 
        S_{\alpha \beta}(E') 
        \\ &\qquad \times \bigg[
            \mathcal{P} \frac{1}{E - E'}
            - i\pi \delta(E - E') 
            \frac{1 \pm e^{-\beta E}}
            {1 \mp e^{-\beta E}}
        \bigg]
    \end{aligned}
    $$

Comparing this with the retarded and advanced Green's functions, we see that

$$
\begin{aligned}
    &(1 \mp e^{-\beta E})^{-1} \bar{G}^R_{\alpha \beta}(E)
    + (1 \mp e^{\beta E})^{-1} \bar{G}^A_{\alpha \beta}(E)
    \\
    &= \int_{-\infty}^{\infty} \frac{dE'}{2\pi}
    S_{\alpha \beta}(E') 
    \\ &\qquad \times 
    \bigg\{
        \mathcal{P} \frac{
            (1 \mp e^{-\beta E})^{-1}
            + (1 \mp e^{\beta E})^{-1}
        }{E - E'}
        \\ &\qquad \qquad
        - i \pi \delta(E - E') \left[
            (1 \mp e^{-\beta E})^{-1}
            - (1 \mp e^{\beta E})^{-1}
        \right]
    \bigg\}
    \\
    &= \bar{G}_{\alpha \beta}(E)
\end{aligned}
$$
