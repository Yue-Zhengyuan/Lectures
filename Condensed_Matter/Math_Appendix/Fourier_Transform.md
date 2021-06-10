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

# Fourier Series and Fourier Transform

## Discrete Fourier Transform

To build physical intuition of Fourier transform, consider a periodic 1D chain of $N$ sites. The distance between two nearest neighbors is $a$; the length of the chain (period in space) is therefore $L = Na$.

```
    Example: N = 4

                 |<--a-->|
    ..-- + ----- + ----- + ----- + --..
         0       1       2       3
```

The $n$th site is at the position

$$
x_n = na, \quad x_{n + N} = x_n
\, (\text{Periodicity})
$$

The site position label $n$ (in real space) is usually restricted into $[0, N-1] \cap \mathbb{Z}$, but can also be shifted by integers (e.g. to $[1,N]$) due to the periodicity.

Imagine a complex-number-valued function $f(x)$ of position. For each site of the chain the function takes value 

$$
f_n \equiv f(x_n), \quad
n = 0,...,N-1
$$

Obviously $f_n$ also has the periodicity $f_{n+N} = f_n$. The **discrete Fourier transform** of this spatial sequence is another sequence of $N$ numbers in "momentum space".

<div class="result">

**Discrete Fourier transform (DFT):**

$$
f(k_m) = \sum_{n=0}^{N-1} 
f(x_n) e^{ik_m x_n}, \quad
k_m = \frac{2\pi m}{L}
$$

The momentum label $m$ is usually restricted so that $k$ lies in the range $[-\pi/a, \pi/a)$ (the **1st Brillouin zone**, denoted by $\text{BZ}$)

$$
\begin{aligned}
    m \in \text{BZ}
    &= \bigg[-\frac{N}{2}, \frac{N}{2} \bigg) \cap \mathbb{Z} 
    \\
    &= \left\{\begin{aligned}
        &-\frac{N}{2}, ..., \frac{N}{2}-1 
        &\quad& N \, \text{even}
        \\
        &-\frac{N-1}{2}, ..., \frac{N-1}{2}
        &\quad& N \, \text{odd}
    \end{aligned}\right.
\end{aligned}
$$

</div><br>

<div class="remark">

*Remark*:

- The range of $m$ can also be shifted by integers, due to the periodicity of the transformed sequence:
    
    $$
    \begin{aligned}
        f(k_{m+N})
        &= \sum_{n=0}^{N-1} 
        f(x_n) e^{ik_{m+N} x_n} \\
        &= \sum_{n=0}^{N-1} 
        f(x_n) e^{ik_m x_n} \underbrace{
            e^{i(2\pi/a)na}
        }_{=\exp(2\pi in) = 1} = f(k_m)
    \end{aligned}
    $$

- Another motivation of DFT is transforming a periodic time sequence $f(t_n)$ (with time interval $a$, and $\beta \equiv Na$) to frequency representation $f(\omega_n)$. But it is conventional to write the time-frequency transform with an extra minus sign on the exponential factor:

    $$
    f(\omega_m) = \sum_{n=0}^{N-1} 
    f(t_n) e^{-i\omega_m t_n}, \quad
    \omega_m = \frac{2\pi m}{\beta}
    $$

</div><br>

## Inverse Transform

One can perform an *inverse* transform to recover $f(x_n)$ from $f(k_m)$:

<div class="result">

**Inverse Discrete Fourier Transform:**

$$
f(x_n) = \frac{1}{N} \sum_{m \in BZ}
f(k_m) e^{-ik_m x_n}
$$

</div><br>

*Proof*: 

$$
\begin{aligned}
    \text{RHS} &= \frac{1}{N} \sum_m 
    \sum_{n'} f(x_{n'}) e^{ik_m (x_{n'} - x_n)}
    \\
    &= \frac{1}{N} \sum_{m,n'} f(x_{n'})
    \exp \bigg[
        i \frac{2\pi m}{Na} (n' - n)a
    \bigg]
    \\
    &= \frac{1}{N} \sum_{n'} f(x_{n'}) 
    \underbrace{
        \sum_m \exp \bigg[
            i \frac{2\pi m}{N} (n' - n)
        \bigg]
    }_{= N\delta_{n'n}}
    \\
    &= f(x_n) \qquad \blacksquare
\end{aligned}
$$

<div class="remark">

*Remark*: From the proof above, we see that the foundation of discrete Fourier transform is the following two orthogonality relations.

$$
\sum_{m \in BZ} e^{i k_m (x_n - x_{n'})} = N \delta_{n,n'}
, \quad 
\sum_{n=0}^{N-1} e^{i (k_m - k_{m'}) x_n} = N \delta_{m,m'}
$$

In fact, the summation range in both equations can be shifted by integers due to periodicity of the exponential factors. 

</div><br>

## Fourier Series

The **Fourier series** is obtained from DFT by keeping the period $L = Na$ fixed, while $a \to 0$ (*or* $N \to \infty$). In this case, 

- The site position $x_n = na$ becomes a continuous variable $x$.
- The momentum $k_m = 2\pi m/L$ remains discrete, but now $m$ takes value from all $\mathbb{Z}$.

Define the increment in $x$

$$
\Delta x = a
$$

The DFT formulas become

$$
\begin{aligned}
    f(k_m) &= \sum_{n=0}^{N-1} f(x_n) e^{ik_m x_n} 
    = \sum_{n=0}^{N-1} \frac{\Delta x}{a} \,f(x_n) e^{ik_m x_n}
    \\
    &\to \frac{1}{a} \int_0^L dx \, f(x) e^{ik x}
    
    \\[1.5em]

    f(x) &= \frac{1}{N} \sum_{m=-\infty}^{\infty} 
    f(k_m) e^{-ik_m x}
\end{aligned}
$$

However, from physical considerations, function $f$ should be *rescaled*. We can imagine that as $a \to 0$, the amount of any physical quantity $f$ (e.g. mass, charge, displacement from equilibrium) assigned to each single site ("averaging" over the whole chain) approaches 0 as $O(1/N)$, or equivalently $O(a)$. Thus we scale it up by the factor $1/a$:

<div class="result">

**Rescaling in the limit of continuous space:**

$$
f_{\text{continuum}}(x) 
= \frac{1}{a} f_{\text{lattice}}(x)
$$

</div><br>

Thus, replace $f(x)$ by $a f(x)$ in the above transformation (keep $f(k)$ unchanged), we obtain

<div class="result">

**Fourier series of function $f(x)$**

$$
\begin{aligned}
    f(x) &= \sum_{m=-\infty}^{\infty} 
    f(k_m) e^{-ik_m x}
    \\
    f(k_m) &= \frac{1}{L} \int_0^L dx \, f(x) e^{ik_m x}
\end{aligned}
$$

</div><br>

The orthogonality relations related to Fourier series are

$$
\begin{aligned}
    \sum_{n=0}^{N-1} e^{i (k_m - k_{m'}) x_n} 
    = \frac{1}{a} \sum_{n=0}^{N-1} 
    \Delta x \, e^{i (k_m - k_{m'}) x_n} 
    &= N \delta_{m,m'}
    \\ &\Downarrow \\
    \int_0^L dx \, e^{i(k_m - k_{m'}) x}
    &= L \delta_{m,m'}
\end{aligned}
$$

## Continuous Fourier Transform

The **continuous Fourier transform** is obtained from the Fourier series by sending $L \to \infty$ (i.e. from DFT by *first* sending $a \to 0$, *then* $N \to \infty$). When taking the infinite chain limit, it is more convenient to shift the range of $n$ to 

$$
n \in \bigg[-\frac{N}{2}, \frac{N}{2} \bigg) \cap \mathbb{Z} 
\ \Rightarrow \ 
x_n \in \bigg[-\frac{L}{2}, \frac{L}{2} \bigg]
$$

Both $x, k$ will become continuous labels. Define the increment in $x, k$:

$$
\Delta x = a, \quad \Delta k = \frac{2\pi}{L} = \frac{2\pi}{Na}
$$

Then the DFT formulas become

$$
\begin{aligned}
    f(k) &= \sum_n f(x_n) e^{ik x_n}
    = \frac{1}{a} \sum_n \Delta x \, f(x_n) e^{ik x_n}
    \\
    &\xrightarrow{a \to 0} 
    \frac{1}{a} \int_{-L/2}^{L/2} dx \, f(x) e^{ikx}
    \\
    &\xrightarrow{L \to \infty}
    \frac{1}{a} \int_{-\infty}^{\infty} dx \, f(x) e^{ikx}

    \\

    f(x) &= \frac{1}{N} \sum_{m} f(k_m) e^{-ik_m x}
    = \frac{a}{2\pi} \sum_m \Delta k \, f(k_m) e^{-ik_m x}
    \\
    &\xrightarrow{a \to 0}
    a \int_{-\infty}^{\infty} \frac{dk}{2\pi}
    f(k) e^{-ikx} \quad
    \left(
        \text{Originally} \, 
        a \int_{-\pi/a}^{\pi/a} \frac{dk}{2\pi}
    \right)
\end{aligned}
$$

As before, we perform the rescaling:

$$
f_{\text{continuum}}(x) 
= \frac{1}{a} f_{\text{lattice}}(x)
$$

Replacing $f(x)$ by $af(x)$ in the above two transforms, we obtain

<div class="result">

**Continuous Fourier transform and its inverse:**

$$
\begin{aligned}
    f(k) &= \int_{-\infty}^{\infty} dx \, f(x) e^{ikx}
    \\
    f(x) &= \int_{-\infty}^{\infty} \frac{dk}{2\pi} \, f(k) e^{ikx}
\end{aligned}
$$

</div><br>

In the orthogonality relations, Kronecker deltas are replaced by Dirac delta functions:

$$
\begin{aligned}
    \sum_m e^{i k_m (x_n - x_{n'})} 
    = \frac{Na}{2\pi} \sum_m \Delta k \, e^{i k_m (x_n - x_{n'})} 
    &= N \delta_{n,n'}
    \\ &\Downarrow \\
    \frac{1}{2\pi} \sum_m \Delta k \, e^{i k_m (x_n - x_{n'})} 
    &= \frac{1}{a} \delta_{n,n'}
    \\ &\Downarrow \\
    \int \frac{dk}{2\pi} e^{ik(x - x')}
    &= \delta(x - x')
    
    \\ \\
    
    \sum_n e^{i (k_m - k_{m'}) x_n} 
    = \frac{1}{a} \sum_n \Delta x \, e^{i(k_m - k_{m'}) x_n}
    &= N \delta_{m,m'}
    \\ &\Downarrow \\
    \int dx \, e^{i(k - k') x}
    &= 2\pi \delta(k - k')
\end{aligned}
$$
