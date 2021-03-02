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

# Spectral Representation

*Notation notes:*

- $\hbar = 1$;
- Whenever $\pm$ or $\mp$ occurs, the upper sign is for boson, and the other is for fermion.

## Fourier Transform of Time

We introduce the time Fourier transform of the Green's function:

$$
\begin{aligned}
    G_{\a \b}(E)
    &= \int_{-\infty}^{\infty} dt \, 
    e^{+i E t} G_{\a \b}(t)
    \\ &\Updownarrow \\
    G_{\a \b}(t)
    &= \int_{-\infty}^{\infty} \frac{d E}{2\pi} \, 
    e^{-i E t} G_{\a \b}(E)
\end{aligned}
$$

To proceed, we first get an alternative expression of the original Green's function 

$$
\begin{aligned}
    i G_{\alpha\beta}(t-t')
    &= \amp{\Psi_0^N}
    {T[a_{\alpha H}(t) a^\dagger_{\beta H}(t')]}{\Psi_0^N}
    \\
    &= \amp{\Psi_0^N}{
        a_{\alpha H}(t) a^\dagger_{\beta H}(t')
    }{\Psi_0^N} \theta(t - t')
    \\ &\quad
    \pm \amp{\Psi_0^N}{
        a^\dagger_{\beta H}(t') a_{\alpha H}(t)
    }{\Psi_0^N} \theta(t' - t)
\end{aligned}
$$

where $\ket{\Psi_0^N}$ is the $N$-particle ground state with energy $E_0^N$, i.e.

$$
H \ket{\Psi_0^N} = E_0^N \ket{\Psi_0^N}
$$

Recall that in Heisenberg picture

$$
O_H(t) = e^{iHt} O e^{-iHt}
$$

then we may write the time dependence explicitly as

$$
\begin{aligned}
    &i G_{\alpha\beta}(t-t')
    \\
    &= \amp{\Psi_0^N}{
        a_{\alpha} e^{-iH(t - t')} 
        a^\dagger_{\beta}
    }{\Psi_0^N} e^{iE_0^N (t - t')} \theta(t - t')
    \\ &\quad
    \pm \amp{\Psi_0^N}{
        a^\dagger_{\beta} e^{-iH(t' - t)}
        a_{\alpha}
    }{\Psi_0^N} e^{iE_0^N(t' - t)} \theta(t' - t)
\end{aligned}
$$

We then insert identities (using eigenstates of $H$) to deal with $e^{\pm iH(t-t')}$: 

$$
\begin{aligned}
    &\amp{\Psi_0^N}{
        a_{\alpha} e^{-iH(t - t')} 
        a^\dagger_{\beta}
    }{\Psi_0^N}
    \\
    &= \sum_m \amp{\Psi_0^N}{
        a_{\alpha} e^{-iH(t - t')} 
    }{\Psi_m^{N+1}} \amp{\Psi_m^{N+1}}{
        a^\dagger_{\beta}
    }{\Psi_0^N}
    \\
    &= \sum_m e^{-iE_m^{N+1}(t - t')} \amp{\Psi_0^N}{
        a_{\alpha}
    }{\Psi_m^{N+1}} \amp{\Psi_m^{N+1}}{
        a^\dagger_{\beta}
    }{\Psi_0^N}

    \\[2em]

    &\amp{\Psi_0^N}{
        a^\dagger_{\beta} e^{-iH(t' - t)}
        a_{\alpha}
    }{\Psi_0^N}
    \\
    &= \sum_n \amp{\Psi_0^N}{
        a^\dagger_{\beta} e^{-iH(t' - t)}
    }{\Psi_n^{N-1}} \amp{\Psi_n^{N-1}}{
        a_{\alpha}
    }{\Psi_0^N}
    \\
    &= \sum_n e^{-iE_n^{N-1}(t' - t)} \amp{\Psi_0^N}{
        a^\dagger_{\beta}
    }{\Psi_n^{N-1}} \amp{\Psi_n^{N-1}}{
        a_{\alpha}
    }{\Psi_0^N}
\end{aligned}
$$

Collecting these results, we obtain (setting $t - t' \to t$)

$$
\begin{aligned}
    &i G_{\alpha\beta}(t)
    \\
    &= \sum_m \amp{\Psi_0^N}{
        a_{\alpha}
    }{\Psi_m^{N+1}} \amp{\Psi_m^{N+1}}{
        a^\dagger_{\beta}
    }{\Psi_0^N} e^{- i(E_m^{N+1} - E_0^N)t} 
    \theta(t)
    \\ &\quad
    \mp \sum_n \amp{\Psi_0^N}{
        a^\dagger_{\beta}
    }{\Psi_n^{N-1}} \amp{\Psi_n^{N-1}}{
        a_{\alpha}
    }{\Psi_0^N} e^{-i(E_0^N - E_n^{N-1})t} 
    \theta(-t)
\end{aligned}
$$

<div class="remark">

*Remark*: It is implicitly assumed that states with more particles always has larger energy, therefore

$$
E_m^{N+1} - E_0^N > 0, \quad
E_0^N - E_n^{N-1} > 0
$$

</div><br>

Now the time dependence is completely separated from the operators, making the Fourier transform easier. Here we need one theorem from complex analysis:

<div class="result">

**Fourier transform of the step function:**

$$
\theta(t) = - \lim_{\eta \to 0^+}
\int_{-\infty}^{\infty} \frac{dE}{2\pi i} 
\frac{e^{-iE t}}{E + i\eta}
$$

</div><br>

----

*Proof*:

----

We then obtain some immediate corollaries:

$$
\begin{aligned}
    \theta(-t) &= - \int_{-\infty}^{\infty} 
    \frac{dE}{2\pi i} 
    \frac{e^{+iE t}}{E + i\eta}
    \quad (\text{set} \ -E \to E)
    \\
    &= + \int_{-\infty}^{\infty} 
    \frac{dE}{2\pi i} 
    \frac{e^{-iE t}}{E - i\eta}
    
    \\[2em]

    e^{- i E_0 t} \theta(\pm t)
    &= \mp \int_{-\infty}^{\infty} 
    \frac{dE}{2\pi i} 
    \frac{e^{-i(E + E_0) t}}
    {E \pm i\eta}
    \quad (\text{set} \ E + E_0 \to E)
    \\
    &= \mp \int_{-\infty}^{\infty} 
    \frac{dE}{2\pi i}
    \frac{e^{-iE t}}
    {E - E_0 \pm i\eta}
\end{aligned}
$$

This integral provides the Fourier transformation. Thus we obtain 

<div class="result">

**Green's function in energy <br>(Lehmann representation):**

$$
\begin{aligned}
    G_{\alpha\beta}(E)
    &= \sum_m \frac{
        \amp{\Psi_0^N}{
            a_{\alpha}
        }{\Psi_m^{N+1}} \amp{\Psi_m^{N+1}}{
            a^\dagger_{\beta}
        }{\Psi_0^N}
    }{
        E - (E_m^{N+1} - E_0^N) + i\eta
    } \\ &\quad
    \mp \sum_n \frac{
        \amp{\Psi_0^N}{
            a^\dagger_{\beta}
        }{\Psi_n^{N-1}} \amp{\Psi_n^{N-1}}{
            a_{\alpha}
        }{\Psi_0^N}
    }{
        E - (E_0^N - E_n^{N-1}) - i\eta
    }
\end{aligned}
$$

</div><br>

More compactly, we have the operator expression (by removing the identities we inserted earlier)

<div class="result">

**Green's function in energy <br>(Lehmann representation, operator form):**

$$
\begin{aligned}
    G_{\alpha \beta}(E)
    &= \amp{\Psi_0^N}{
        a_\alpha 
        \frac{1}{E - (H - E_0^N) + i\eta}
        a_\beta^\dagger
    }{\Psi_0^N}
    \\ &\quad
    \mp \amp{\Psi_0^N}{
        a_\beta^\dagger 
        \frac{1}{E - (E_0^N - H) - i\eta}
        a_\alpha
    }{\Psi_0^N}
\end{aligned}
$$

Here $H$ is the Hamiltonian *operator*.

</div><br>

## Spectral Functions

<div class="result">

**The Sokhotski–Plemelj theorem:**

$$
\frac{1}{z \pm i\eta}
= \mathcal{P}\frac{1}{z} \mp i\pi \delta(z)
$$

</div><br>
