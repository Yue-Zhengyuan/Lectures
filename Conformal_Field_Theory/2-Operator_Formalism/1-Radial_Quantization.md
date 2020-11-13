# Radial Quantization

## From Cylinder to Complex Plane 

A CFT can be compactified on a *cylinder*: the axial direction of the cylinder represents time $t=x^0$. We can map the system to the *complex plane* by:

$$
z = e^{x^0 + ix^1} = e^{t + ix}
$$

Then constant $t$ (or $x^0$) points map to a *circle* centered at the origin, and the *radial direction* represent the time. The fields $\phi(t,x)$ are thus mapped to $\phi(z, \bar{z})$.

<center>

![radial quantization](Figures/rad_quant.png)   
*Radial quantization*

</center>

## Laurent Mode Expansion of the Fields

### Around the Origin

A field $\phi(z, \bar{z})$ of conformal dimensions $(h, \bar{h})$ can be expanded as a Laurent series around the origin 0:

$$
\phi(z, \bar{z})
= \sum_{m,n}
z^{-m-h} \bar{z}^{-n-\bar{h}} \phi_{m,n}
$$

Using the Cauchy Integral Formula, the modes are

$$
\phi_{m,n} = 
\frac{1}{2 \pi i} \oint dz \, z^{m+h-1} 
\frac{1}{2 \pi i} \oint d\bar{z} \, \bar{z}^{n+\bar{h}-1} \phi(z, \bar{z})
$$

### Around Any Point 

For simplicity, we now focus on holomorphic fields depending only on $z$. It is possible to expand around an arbitrary point $w$, instead of the origin:

$$
\begin{aligned}
    \phi(z) 
    &= \sum_n (z-w)^{-n-h} \phi_n(w), 
    \\
    \phi_n(w)
    &=\frac{1}{2 \pi i} \oint_w dz \, z^{n+h-1} \phi(z)
\end{aligned}
$$

### Hermitian Conjugate of Fields

The Hermitian conjugate of $\phi$ is *defined* as

$$
\phi^\dagger(z, \bar{z})
= \bar{z}^{-2h}z^{-2\bar{h}} 
\phi \left(\frac{1}{\bar{z}}, \, \frac{1}{z} \right)
$$

Using the Laurent expansion of $\phi(\bar{z}^{-1}, z^{-1})$, we obtain

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

Therefore, we must have

$$
\phi_{-m,-n} = \phi_{m,n}^\dagger
$$

## Asymptotic States

We assume the existence of a vacuum state $|0\rangle$ upon which a Hilbert space is constructed by application of creation
operators (or their likes).

In free-field theories, the *vacuum* may be defined as the state
annihilated by the *positive frequency part* of the field.

For an *interacting* field $\phi$, we assume that *the Hilbert space is
the same as for a free field*, except that the actual energy eigenstates
are different.

### In-State

Suppose then that the interaction is slowly turned off as
$t\to \pm \infty$ and that the *asymptotic* field

$$
\phi_{\text{in}} \propto \lim_{t\to -\infty} \phi(t,x)
$$

is *free*. The **asymptotic in-state** is defined as its action result on vacuum:

$$
|\phi_\text{in}\rangle
= \lim_{t\to -\infty} \phi(t,x) |0\rangle
$$

Within radial quantization, $t\to -\infty$ is mapped to $z, \bar{z} = 0$. Therefore

$$
\begin{aligned}
    |\phi_{\text{in}} \rangle 
    &= \lim_{z,\bar{z} \to 0} 
    \phi(z, \bar{z}) |0\rangle
    \\
    &= \lim_{z,\bar{z} \to 0} 
    \sum_{m,n} z^{-m-h} \bar{z}^{-n-\bar{h}} 
    \phi_{m,n} | 0\rangle
\end{aligned}
$$

In order for this to be well defined, we impose the requirement that all the singular terms are made to zero by

$$
\phi_{m,n} |0\rangle = 0 \qquad
m > -h, \, n > -\bar{h}
$$

then we are left with only one term, namely

$$
|\phi_\text{in}\rangle = \phi_{-h, -\bar{h}} |0\rangle
$$

### Out-State

The **asymptotic out-state** is defined as the Hermitian conjugate state of the in-state

$$
\begin{aligned}
    \langle \phi_{\text{out}} |
    &= \lim_{z,\bar{z} \to 0} \langle 0| 
    \phi^\dagger(z, \bar{z})
    \\
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

Again, we need to impose the requirement that

$$
\langle 0 | \phi_{m,n} = 0 \qquad
m < h, \, n < \bar{h}
$$

then

$$
\langle \phi_{\text{out}} | 
= \langle 0 | \phi_{h, \bar{h}}
= \langle 0 | \phi_{-h, -\bar{h}}^\dagger
$$