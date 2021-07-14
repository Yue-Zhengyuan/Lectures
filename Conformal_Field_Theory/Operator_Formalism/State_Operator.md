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

# State-Operator Correspondence

## The Asymptotic In-State

Suppose then that the interaction is slowly turned off as
$t\to \pm \infty$ and that the *asymptotic* field

$$
\phi_{\text{in}} \propto \lim_{t\to -\infty} \phi(t,x)
$$

is *free*. The **asymptotic in-state** is defined as its action result on vacuum:

$$
|\phi_\text{in}\rangle
= \lim_{t\to -\infty} \phi(t,x) \ket{0}
$$

Within radial quantization, $t\to -\infty$ is mapped to $z, \bar{z} = 0$. Therefore

<div class="result">

**Asymptotic in-state:**

$$
|\phi_{\text{in}} \rangle 
= \lim_{z,\bar{z} \to 0} 
\phi(z, \bar{z}) \ket{0}
= \phi(0,0) \ket{0}
$$

</div><br>

This one-to-one relation between states at the field $\phi$ *at the origin* is called the **state-operator correspondence**.

## Hermitian Conjugation and Out-State

In the Hilbert space, we need to define a Hermitian conjugate of the in-state to take inner product with, called the **(asymptotic) out-state**:

$$
\bra{\phi_{\text{out}}} \equiv \ket{\phi_\text{in}}^\dagger
= \lim_{z,\bar{z} \to 0} \bra{0} \phi^\dagger(z, \bar{z})
$$

where we also introduce the Hermitian-conjugated field $\phi^\dagger(z,\bar{z})$.

In Minkowski space, Hermitian conjugation does not affect the spacetime coordinates. However, in Euclidean space, the time is related to the Minkowski time by Wick rotation:

$$
x^0_E = i x^0_M
$$

which will be reversed under Hermitian conjugation. This corresponds to the mapping

$$
e^{\omega(x^0 + ix^1)} \mapsto e^{\omega(-x^0+ ix^1)} 
\quad \text{or} \quad
z \mapsto \frac{1}{\bar{z}}
$$

Therefore, we define
 
<div class="result">

**Hermitian conjugate of a primary field:** 

$$
\phi^\dagger(z, \bar{z})
= \bar{z}^{-2h} z^{-2\bar{h}} 
\phi(\bar{z}^{-1}, z^{-1})
$$

</div><br>

To explain the pre-factors, let us take the inner product of the in-state and the out-state:

$$
\begin{aligned}
    \braket{\phi_\text{out}}{\phi_\text{in}}
    &= \lim_{z,\bar{z},w,\bar{w}\to 0}
    \amp{0}{\phi^\dagger(z,\bar{z}) \phi(w,\bar{w})}{0}
    \\
    &= \lim_{z,\bar{z},w,\bar{w}\to 0}
    \bar{z}^{-2h} z^{-2\bar{h}} 
    \amp{0}{\phi(\bar{z}^{-1}, z^{-1}) \phi(w,\bar{w})}{0}
    \\
    &= \lim_{\xi,\bar{\xi} \to \infty}
    \xi^{2h} \bar{\xi}^{2\bar{h}} 
    \amp{0}{\phi(\xi,\bar{\xi}) \phi(0,0)}{0}
\end{aligned}
$$

Here we defined $\xi = \bar{z}^{-1}, \bar{\xi} = z^{-1}$. On the RHS we encounter the 2-point function, which has the general form

$$
\amp{0}{\phi(\xi,\bar{\xi}) \phi(0,0)}{0}
= \frac{C_{\phi \phi}}{\xi^{2h} \bar{\xi}^{2\bar{h}}}
$$

Then we are left with

<div class="result">

**Inner product of in- and out-states:**

$$
\braket{\phi_\text{out}}{\phi_\text{in}} = C_{\phi \phi}
$$

</div><br>

exactly cancelling the $\bar{\xi}^{2h} \xi^{2\bar{h}}$ factor. Hence the introduction of the pre-factor in $\phi^\dagger$ is justified.

## Laurent Mode Expansion of Quasi-Primary Fields

A quasi-primary field $\phi(z, \bar{z})$ of conformal dimensions $(h, \bar{h})$ can be expanded as a Laurent series around the origin 0 (or in general any point $w$ in the complex plane):

$$
\phi(z, \bar{z})
= \sum_{m,n \in \Z}
z^{-m-h} \bar{z}^{-n-\bar{h}} \phi_{m,n}
$$

Using the Cauchy Integral Formula, the modes are

$$
\phi_{m,n} = 
\frac{1}{2 \pi i} \oint dz \, z^{m+h-1} 
\frac{1}{2 \pi i} \oint d\bar{z} \, \bar{z}^{n+\bar{h}-1} \phi(z, \bar{z})
$$

With the Laurent modes, the in-state can be written as

$$
|\phi_{\text{in}} \rangle 
= \lim_{z,\bar{z} \to 0} 
\sum_{m,n} z^{-m-h} \bar{z}^{-n-\bar{h}} 
\phi_{m,n} | 0\rangle
$$

All the singular terms should be made to zero. Therefore we require 

<div class="result">

**Field Laurent modes on vacuum ket:**

$$
\phi_{m,n} \ket{0} = 0 \qquad
m > -h \quad \text{and} \quad n > -\bar{h}
$$

</div><br>

<div class="remark">

*Remark*: For this reason, we define

$$
\ket{h, \bar{h}} \equiv \ket{\phi_{\text{in}}}
= \phi(0,0) \ket{0}
$$

This notation will be used in Part 4.

</div><br>

For the out-state, we Laurent expand $\phi^\dagger$:

$$
\begin{aligned}
    \phi^\dagger(z, \bar{z})
    &=\bar{z}^{-2h}z^{-2\bar{h}} 
    \sum_{m,n}
    \bar{z}^{m+h} z^{n+\bar{h}} \phi_{m,n} 
    \\
    &= \sum_{m,n}
    \bar{z}^{m-h} z^{n-\bar{h}} \phi_{m,n}
\end{aligned}
$$

Meanwhile, direct Hermitian conjugation of the Laurent expansion of the field $\phi(z,\bar{z})$ givens

$$
\phi^\dagger(z, \bar{z})
= \sum_{m,n}
\bar{z}^{-m-h} z^{-n-\bar{h}} \phi_{m,n}^\dagger
$$

Therefore, we our requirement implies

<div class="result">

**Hermitian conjugate of field Laurent modes:**

$$
\phi_{-m,-n} = \phi_{m,n}^\dagger
$$

</div><br>

Finally, consider the action of teh Laurent modes on vacuum *bras*. Repeat the definition of out-state here:

$$
\begin{aligned}
    \langle \phi_{\text{out}} |
    &= \lim_{z,\bar{z} \to 0}
    \bar{z}^{-2h}z^{-2\bar{h}} \langle 0 |
    \phi (\bar{z}^{-1}, z^{-1})
\end{aligned}
$$

Now we change $z^{-1}, \bar{z}^{-1}$ to $\bar{w}, w$. Then

$$
\begin{aligned}
    \langle \phi_{\text{out}} |
    &= \lim_{w, \bar{w} \to \infty}
    w^{2h} \bar{w}^{2\bar{h}} \langle 0 |
    \phi (w, \bar{w})
    \\
    &= \lim_{w, \bar{w} \to \infty}
    \sum_{m,n} w^{-m+h} \bar{w}^{-n+\bar{h}} 
    \langle 0 | \phi_{m,n}
\end{aligned}
$$

For well-definition, we need to impose the requirement that

<div class="result">

**Field Laurent mode on vacuum bra-vector:**

$$
\bra{0} \phi_{m,n} = 0 \qquad
m < h \quad \text{and} \quad n < \bar{h}
$$

</div><br>
