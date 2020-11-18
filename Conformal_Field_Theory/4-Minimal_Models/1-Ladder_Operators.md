# Ladder Operators

## Conformal Operators on the Vacuum State

The energy of the ground state is fixed to zero. This requires that both the holomorphic and the anti-holomorphic energy-momentum tensor 

$$
\begin{aligned}
    T(z)|0\rangle
    &= \sum_n z^{-n-2} L_n |0\rangle 
    \\
    \bar{T}(\bar{z})|0\rangle
    &= \sum_n \bar{z}^{-n-2} \bar{L}_n |0\rangle 
\end{aligned}
$$

are well-defined as $z, \bar{z} \to 0$ (no divergence). Then for $-n - 2 \le -1$, or $n \ge -1$, we must have

$$
\begin{aligned}
    L_n|0\rangle =0 \\
    \bar{L}_n|0\rangle =0
\end{aligned}
\qquad
n \ge -1
$$

These include the *global* conformal transformations generators $L_{-1},L_0,L_1$ and their anti-holomorphic counterparts.

Now we also have

$$
\langle 0| T(z) |0\rangle 
= \langle 0 | \bar{T}(\bar{z}) | 0\rangle =0
$$

## Conformal Operators on the Asymptotic State

Consider the $L_n, \bar{L}_n$ operators acting on the *asymptotic state*

$$
|h,\bar{h} \rangle 
\equiv \phi(0,0) |0\rangle
$$

Here $\phi(z, \bar{z})$ is a *primary field* with conformal dimensions $(h, \bar{h})$. Because we have already know the action on the vacuum, we may calculate

$$
[L_n,\phi(0,0)] |0\rangle 
= L_n\phi(0,0)|0\rangle -  \phi(0,0)L_n|0\rangle
$$

When $n\ge -1$, the second term vanishes. Then

$$
[L_n,\phi(0,0)] |0\rangle 
= L_n\phi(0,0) |0\rangle 
= L_n |h,\bar{h} \rangle
$$

Now we evaluate the commutator

$$
\begin{aligned}
    &[L_n,\phi(w,\bar{w})]
    = \frac{1}{2 \pi i} \oint_w dz \,
    z^{n+1} \underbrace{T(z)\phi(w,\bar{w})}_{\text{use OPE}} 
    \\[1.5em]
    &= \frac{1}{2 \pi i} \oint_w dz \,
    z^{n+1} \left[
        \frac{h \phi(w,\bar{w})}{(z-w)^2}
        + \frac{\partial_w\phi(w,\bar{w})}{z-w}
        + \text{reg.}
    \right]
    \\
    &= \left[
        \frac{d}{dz} \left(z^{n+1}h \phi(w,\bar{w})\right)
    \right]_{z=w} + \left[
        z^{n+1} \partial_w\phi(w,\bar{w})
    \right]_{z=w} 
    \\[1em]
    &= h(n+1) w^n \phi(w,\bar{w})
    + w^{n+1} \partial_w \phi(w,\bar{w})
\end{aligned}
$$

Similarly

$$
[\bar{L}_n, \phi(w,\bar{w})]
= \bar{h}(n+1)\bar{w}^n \phi(w,\bar{w})
+ \bar{w}^{n+1} \partial_{\bar{w}} \phi(w,\bar{w})
$$

Finally

$$
\begin{aligned}
    L_0|h,\bar{h} \rangle &= h|h,\bar{h} \rangle
    \\
    \bar{L}_0|h,\bar{h} \rangle &= \bar{h}|h,\bar{h} \rangle
    \\ 
    L_n|h,\bar{h} \rangle &= 0
    \\
    \bar{L}_n|h,\bar{h} \rangle &= 0
    \qquad (n > 0)
\end{aligned}
$$

Since $L_0+\bar{L}_0$ is proportional to the system Hamiltonian, we find
that $|h,\bar{h} \rangle$ *is an energy eigenstate*.

## Ladder Operators

To find excited states above the asymptotic state, we need the *ladder operators*. It turns out that they can be chosen as the Laurent modes $\phi_n$ of the holomorphic field $\phi(w)$ with conformal dimension $h$.

$$
\phi(z) = \sum_n z^{-n-h} \phi_n, \quad
\phi_n = \frac{1}{2 \pi i} \oint dz \, z^{n+h-1} \phi(z)
$$

To show this, we calculate the commutator $[L_n, \phi_m]$ using the equation

$$
[A,B] = \oint_0 dw \oint_w dz \, a(z) b(w)
$$

Recall that

$$
L_n = \frac{1}{2 \pi i} \oint dz z^{n+1} T(z)
$$

then

$$
\begin{aligned}
    &\left[L_n,\phi_m\right]
    \\
    &= \frac{1}{2 \pi i} \oint_0 dw \, w^{m+h-1} 
    \frac{1}{2 \pi i} \oint_w dz \, z^{n+1}T(z)\phi(w)
    \\
    &= \frac{1}{2 \pi i} \oint_0 dw \, w^{m+h-1} 
    \frac{1}{2 \pi i} \oint_w dz \, z^{n+1} 
    \left[
        \frac{h \phi(w)}{(z-w)^2}
        + \frac{\partial_w\phi(w)}{z-w}
        + \text{reg.}
    \right]
    \\
    &= \frac{1}{2 \pi i} \oint_0 dw \,
    w^{m+h-1} \left[
        h (n+1) w^n \phi(w) 
        + w^{n+1} \partial_w \phi(w)
    \right]
    \\
    &= \frac{1}{2 \pi i} \oint_0 dw \left[
        h (n+1) w^{m+n+h-1} \phi(w)
        + \underbrace{w^{m+n+h} \partial_w\phi(w)}_{\text{integrate by parts}}
    \right]
    \\
    &= \frac{1}{2 \pi i} \oint_0 dw \left[
        h(n+1)w^{m+n+h-1} \phi(w)
        - (m+n+h) w^{m+n+h-1} \phi(w)
    \right]
    \\
    &= \frac{1}{2 \pi i} \oint_0 dw \,
    (n(h-1)-m) w^{m+n+h-1} \phi(w)
\end{aligned}
$$

This implies that

$$
[L_n, \phi_m] = (n(h-1)-m) \phi_{n+m}
$$

In particular,

$$
\begin{aligned}
    [L_0, \phi_m] &= -m \phi_m\\
    [L_0, \phi_{-m}] &= m \phi_{-m}
\end{aligned}
$$

This means that $\phi_{\pm m} (m>0)$ act as *lowering and raising operators for the eigenstates of* $L_0$: from $L_0|h\rangle =h|h\rangle$ we obtain

$$
\begin{aligned}
    L_0 (\phi_{\pm m}|h\rangle )
    &= [L_0, \phi_{\pm m}] |h\rangle 
    + \phi_{\pm m} L_0 |h\rangle 
    \\
    &= \mp m \phi_{\pm m} |h\rangle 
    + h \phi_{\pm m} |h\rangle 
    \\
    &= (h\mp m) (\phi_m |h\rangle)
\end{aligned}
$$

i.e. $\phi_{\pm m}|h\rangle$ is the eigenstate of $L_0$ with
eigenvalue $h\mp m$.

But we still have another choice. Recall that in the Virasoro algebra

$$
[L_n, L_m] 
= (n-m) L_{n+m}
+ \frac{c}{12} n (n^2 - 1) \delta_{n+m, 0}
$$

Specially, for $n=0$

$$
\begin{aligned}
    [L_0, L_m] &= -m L_m\\
    [L_0, L_{-m}] &= m L_{-m}
\end{aligned}
$$

which has the *same* form as $\left[L_0,\phi_{\pm m} \right]$. Therefore, $L_{\pm m} (m>0)$ can also *lower and raise the conformal dimension*.

Finally, we remark that

$$ L_{-n}=L_n^\dagger $$
