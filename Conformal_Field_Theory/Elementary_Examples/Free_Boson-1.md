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

# Free Massless Boson

<font size=5>

**Part 1: Primary Fields and Energy-Momentum Tensor**

</font>

In the Euclidean space, the action of free massless boson in real coordinates is

$$
\begin{aligned}
    S &= \frac{\kappa}{2} \int d^2x \,
    \sqrt{|g|} \, g^{\mu\nu}
    \p_\mu \phi \,\p_\nu \phi \\
    &= \frac{\kappa}{2} \int d^2x \,(
        (\partial_0 \phi)^2
        + (\partial_1 \phi)^2
    )
\end{aligned}
$$

where $g_{\mu \nu} = \operatorname{diag}(1,1)$ is the usual flat metric, and $g = \det g_{\mu \nu}$. The normalization constant $\kappa$ is usually chosen as $1/4\pi$.

## Scaling Dimension of $\phi$

The free massless boson field $\phi$ in general will have a nonzero scaling dimension $\Delta$ in order to make the action scaling invariant:

$$
\Delta = \frac{d}{2} - 1
$$

But we see that $d = 2$ is special: in this case **the field is really a scalar** with $\Delta = 0$ (or $(h,\bar{h}) = 0$). From the correlation function we already know that $\phi$ is not a quasi-primary field.

*Proof*: The action in a generic $d$-dimension flat space is (omitting the normalization)

$$
S = \int d^dx \, \p_\mu \phi(x) \,\p^\mu \phi(x)
$$

The scaling dimension describes the following field transformation

$$
x \to x' = \lambda x, \quad
\phi(x) \to \phi'(x') = \lambda^{-\Delta} \phi(x)
$$

Under scaling, the integration measure $d^dx$ in $S$ becomes

$$
d^dx \to d^dx' = \lambda^d d^dx
$$

while the derivative becomes

$$
\p'_\mu = \frac{\p x^\nu}{\p x'_\mu} \p_\nu
= \lambda^{-1} \p_\mu
$$

Therefore

$$
\begin{aligned}
    S' &= \int d^dx' \, \p'_\mu \phi'(x') \,\p'^\mu \phi'(x')
    \\
    &= \lambda^{d - 2(1+\Delta)}
    \int d^dx \, \p_\mu \phi(x) \, \p^\mu \phi(x)
    = \lambda^{d - 2(1+\Delta)} S
\end{aligned}
$$

To achieve scaling invariance, we set

$$
d - 2(1+\Delta) = 0 \, \Rightarrow \,
\Delta = \frac{d}{2} - 1 \quad \blacksquare
$$

## Correlation Function

Integrating by parts (i.e. removing some divergence term by converting it to vanishing surface integration at infinity), we can write $S$ as

$$
\begin{aligned}
    S &= -\frac{1}{2} \int d^2x \, \phi(x) \partial^2 \phi(x)
    \\
    &= \frac{1}{2} \int d^2x \, d^2y \, \phi(x) A(x,y) \phi(y)
\end{aligned}
$$

where we defined 

$$
A(x,y) = A(x-y) \equiv -(\partial_x^2) \delta(x-y)
$$

Thus the action is a *continuum limit* of a multi-variable Gaussian integral. Let us first review some results for the discrete integral: define the generating function

$$
\begin{aligned}
    Z(J)
    &=\int dx_1 ... dx_n \exp \left(-\frac{1}{2}x_iA_{i j}x_j+J_ix_i\right)
    \\
    &= \frac{(2\pi)^{n/2}}{(\det A)^{1/2}}
    \exp \left(
        \frac{1}{2} J_i [A^{-1}]_{i j}J_j
    \right)
\end{aligned}
$$

Then we find that the discrete version of the two-point function is

$$
\begin{aligned}
    \expect{x_a x_b}
    &\equiv \frac{
        \int dx_1 ... dx_n \, x_a x_b
        \exp \left(-\frac{1}{2}x_iA_{ij}x_j\right)
    }{
        \int dx_1 ... dx_n 
        \exp \left(-\frac{1}{2}x_iA_{i j}x_j\right)
    }
    \\
    &= \frac{1}{Z(0)} \left[
        \frac{\partial}{\partial J_a}
        \frac{\partial}{\partial J_b} Z(J)
    \right]_{J=0}
    \\
    &= [A^{-1}]_{a b}
\end{aligned}
$$

Take the continuum limit $x_a \to \phi(x_a)$, one obtain

$$
\expect{\phi(x) \phi(y)} = A^{-1}(x - y)
$$

which actually means

$$
-\partial_x^2 \expect{\phi(x) \phi(y)}
= \delta(x - y)
$$

With some mathematical tricks, one arrives at (the Yellow Book 2.3.4)

$$
\expect{\phi(x) \phi(y)}
= -\frac{1}{4\pi} \ln(|x-y|^2)
$$

We see that the field $\phi(x)$ in the massless free boson theory is *not quasi-primary*.

## Derivatives of the Field

The derivatives of the boson field, $\partial \phi$ and $\bar{\partial} \phi$, turns out to be chiral / anti-chiral primary fields. To show the chirality, we start from the equation of motion

$$
\partial^2 \phi = 0
$$

In complex coordinates $z, \bar{z} = x^0 \pm ix^1$, the laplacian $\partial^2$ is translated into

$$
\begin{aligned}
    \partial^2 &= g^{\mu \nu} \partial_\mu \partial_\nu
    = g^{a b} \partial_a \partial_b
    \\[0.5em] \text{with} \quad
    g^{ab} &= \begin{pmatrix}
        0 & 2 \\ 2 & 0
    \end{pmatrix}, \quad
    g_{ab} = \begin{pmatrix}
        0 & 1/2 \\ 1/2 & 0
    \end{pmatrix}
\end{aligned}
$$

Therefore

$$
\partial^2 \phi(x) = 0 \, \Rightarrow \,
\partial \bar{\partial} \phi(z,\bar{z}) = 0
$$

Then we define

$$
j(z) = i \partial \phi, \quad
\bar{j}(\bar{z}) = i \bar{\partial} \phi
$$

From the equation of motion we know that these are chiral and anti-chiral fields. We shall later show that these are primary fields after finding the energy-momentum tensor $T(z)$ and calculate the OPE.

<div class="remark">

*Remark*: Since $j, \bar{j}$ are *derivatives* of a *scalar* field, they classically behave like vectors, and we expect them to have conformal dimension $(h, \bar{h}) = (1,0)$ and $(0,1)$. This is indeed the case.

In CFT, one calls chiral (or anti-chiral) fields with conformal dimension $(1,0)$ (or $(0,1)$) as **currents**. The conserved current we have seen in Part 3 is a special case:

$$
j_z(z) = -\frac{1}{2\pi} \epsilon(z) T(z) ,\quad
j_{\bar{z}}(\bar{z})
= -\frac{1}{2\pi} \bar{\epsilon}(\bar{z}) \bar{T}(\bar{z})
$$

</div><br>

### Correlation Function and OPE

From the correlation function of the field $\phi$ itself (rewritten in complex coordinates)

$$
\expect{\phi(z) \phi(w)}
= -\frac{1}{4\pi \kappa} \Big[
    \ln(z - w) + \ln(\bar{z} - \bar{w})
\Big]
$$

we find

$$
\begin{aligned}
    \expect{j(z) j(w)}
    &= - \partial_z \partial_w \expect{\phi(z) \phi(w)}
    \\
    &= \frac{1}{4\pi \kappa} \frac{1}{(z-w)^2}
\end{aligned}
$$

which leads to the OPE ($\sim$ means "modulo regular terms")

$$
j(z) j(w) \sim \frac{1}{4\pi \kappa} \frac{1}{(z-w)^2}
$$

This can be translated into commutation rules of the Laurent modes of $j$ (as we have done for $L_n$, Laurent modes of $T(z)$): we expand $j$ as (note that it has $(h,\bar{h}) = (1,0)$, as least as a quasi-primary field)

$$
j(z) = \sum_n z^{-n-1} j_n, \quad
j_n = \frac{1}{2 \pi i} \oint dz \, z^{n} j(z)
$$

Then

$$
\begin{aligned}
    [j_n, j_m]
    &= \frac{1}{(2 \pi i)^2} \left[
        \oint dz \, z^{n} j(z),
        \oint dw \, w^{m} j(w)
    \right]
    \\
    &= \frac{1}{(2 \pi i)^2}
    \oint_0 dw \, w^{m} \oint_w dz \, z^{n}
    \underbrace{j(z)j(w)}_{\text{use OPE}}
    \\
    &= \frac{1}{4\pi \kappa} \frac{1}{(2 \pi i)^2}
    \oint_0 dw \, w^{m} \oint_w dz \, z^{n}
    \left[
        \frac{1}{(z-w)^2} + \cdots
    \right]
\end{aligned}
$$

Integrate over $z$ using Cauchy Integral Formula

$$
\begin{aligned}
    \frac{1}{2 \pi i} \oint_w dz \, z^{n}
    \left[
        \frac{1}{(z-w)^2} + \cdots
    \right]
    &= \frac{1}{1!} \left[
        \frac{d}{dz} (z^{n})
    \right]_{z=w}
    \\[1em]
    &= n w^{n-1}
\end{aligned}
$$

Then complete the integration over $w$

$$
\begin{aligned}
    [j_n, j_m]
    &= \frac{1}{4\pi \kappa} \frac{1}{2 \pi i}
    \oint_0 dw \Big[n w^{m+n-1}\Big]
    \\
    &= \frac{n}{4\pi \kappa} \left[
        \frac{d}{dw} (w^{m+n})
    \right]_{w = 0}
    = \frac{1}{4\pi \kappa} n \, \delta_{m+n,0}
\end{aligned}
$$

The results are summarized below

<div class="result">

**OPE of the derivatives of free massless boson:**

Defining $j(z) = i \partial \phi$ (with $(h,\bar{h}) = (1,0)$), then

$$
\begin{aligned}
    j(z) j(w) \sim \frac{1}{4\pi \kappa} \frac{1}{(z-w)^2},
    \quad
    [j_n, j_m] = \frac{1}{4\pi \kappa} n \, \delta_{m+n, 0}
\end{aligned}
$$

Similar results hold for the anti-chiral derivative $\bar{j}(\bar{z}) = i \bar{\partial} \phi$.

</div><br>

<div class="remark">

*Remark*: The commutation relations for $j_n$ can also be obtained via the standard canonical quantization (to be done later).

</div><br>

## Energy-Momentum Tensor
   
Using the original real coordinates, one finds the canonical energy-momentum tensor:

$$
\begin{aligned}
    T_{\mu \nu}
    &= -\eta_{\mu \nu} \mathcal{L}
    + \frac{\partial \mathcal{L}}{\partial (\partial^\mu \phi)}
    \partial_\nu \phi
    \\
    &= \kappa \left(
        - \frac{1}{2} \eta_{\mu \nu}
        \partial_\alpha \phi  \, \partial^\alpha \phi
        + \partial_\mu \phi \, \partial_\nu \phi
    \right)
\end{aligned}
$$

which happens to be the same as the Hilbert energy-momentum tensor, and symmetric. Now we take the trace:

$$
\begin{aligned}
    {T^{\nu}}_\nu &= \eta^{\nu \mu} T_{\mu \nu}
    \\
    &= \kappa \left(-\frac{d}{2} + 1\right) \partial_\alpha \phi  \, \partial^\alpha \phi
\end{aligned}
$$

We see that $T_{\mu \nu}$ is traceless *if and only if* $d = 2$. This means that the massless free boson theory has conformal invariance only (? according to Schellekens' *Introduction to conformal field theory*, Section 1.6) for $d = 2$. 

### Complexified $T$

Next we can transform it into the complex coordinates using the tensor transformation rules ($z^{0,1} = z, \bar{z}$):

$$
\begin{aligned}
    T_{ab}(z,\bar{z})
    &= \frac{\partial x^\mu}{\partial z^a}
    \frac{\partial x^\nu}{\partial z^b}
    T_{\mu \nu}(x^0, x^1)
    \\
    &= \kappa \begin{pmatrix}
        \partial\phi \, \partial\phi & 0 \\
        0 & \bar{\partial}\phi \, \bar{\partial}\phi
    \end{pmatrix}
\end{aligned}
$$

The non-diagonal elements vanish, as expected. We extract the diagonal elements:

$$
\begin{aligned}
    T(z) &\equiv -2\pi T_{zz}
    = -2\pi \kappa \, \partial\phi \, \partial\phi
    = 2\pi \kappa j^2(z)
    \\
    \bar{T}(\bar{z}) &\equiv -2\pi T_{\bar{z}\bar{z}}
    = -2\pi \kappa \, \bar{\partial}\phi \, \bar{\partial}\phi
    = 2\pi \kappa \bar{j}^2(\bar{z})
\end{aligned}
$$

### Normal Ordering in Quantization

From the OPE of $j(z)j(w) \propto (z-w)^{-2}$, we see that the classically defined $T(z)$ is in fact singular. Thus in the quantum theory we introduce the **normal ordering** (denoted by $\normord{O}$ or $N[O]$) to remove this singular part:

<div class="result">

**Energy-momentum tensor of free massless boson:**

$$
T(z) = 2\pi \kappa \, \normord{j j}(z), \quad
\bar{T}(\bar{z}) = 2\pi \kappa \, \normord{\bar{j} \bar{j}}(z)
$$

</div><br>

From this relation we can express the Virasoro generators $L_n$ in terms of the current $j$:

$$
L_n = 2\pi \kappa \, N[j j]_n
$$

### $j(z)$ is Primary

In general, to show a field $\phi(z)$ is primary, one can check that its OPE with $T(z)$ has the form

$$
T(z) \phi(w)
= \frac{1}{(z-w)^2} h \phi(w)
+ \frac{1}{z-w} \p_w \phi(w)
+ \cdots
$$

Let us now examine the current $j(z)$: when finding the OPE, we do not care about the regular (normal ordered) terms; thus (on the LHS there is an implicit time ordering, allowing us to apply Wick's theorem)

$$
\begin{aligned}
    T(z) j(w) &\sim 2\pi \kappa \,
    (\normord{j j})(z) \, j(w)
    \\
    &= 2\pi \kappa \, (
        \normord{j^\bullet(z) j(z)} j^\bullet(w)
        + \normord{j(z) j^\bullet(z)} j^\bullet(w)
    ) \\
    &= \frac{j(z)}{(z-w)^2}
    \sim \frac{j(w)}{(z-w)^2} + \frac{\partial j(w)}{z - w}
\end{aligned}
$$

Therefore $h = 1$. 

Alternatively, one can translate this OPE into a commutation relation between the Laurent modes of $T(z)$ and $\phi(w)$:

<div class="result">

**Commutation rules for $L_n$ and primary field Laurent modes**

$$
[L_n, \phi_m] = (n(h-1)-m) \phi_{n+m}
$$

</div><br>

*Proof*: In Part 4, we proved

$$
[L_n,\phi(w)] = h(n+1) w^n \phi(w)
+ w^{n+1} \partial_w \phi(w)
$$

Let us continue by plugging in the Laurent expansion of $\phi(w)$:

$$
\phi(z) = \sum_n z^{-n-h} \phi_n, \quad
\phi_n = \oint \frac{dz}{2\pi i} \, z^{n+h-1} \phi(z)
$$

we obtain

$$
\begin{aligned}
    [L_n, \phi_m]
    &= \oint \frac{dw}{2\pi i}  \, w^{m+h-1}
    [L_n, \phi(w)]
    \\
    &= \oint \frac{dw}{2\pi i} \, \bigg[
        h(n+1) w^{n+m+h-1} \phi(w)
        + \underbrace{w^{n+m+h} \partial_w \phi(w)}_{\text{integrate by parts}}
    \bigg]
    \\
    &= \oint \frac{dw}{2\pi i} \left[
        h(n+1) - (m+n+h)
    \right] w^{m+n+h-1} \phi(w)
    \\
    &= (n(h-1) - m) \oint \frac{dw}{2\pi i} \,
    w^{(m+n)+h-1} \phi(w)
    \\
    &= (n(h-1)-m) \phi_{n+m} \qquad \blacksquare
\end{aligned}
$$

Then let us evaluate the commutator

$$
[L_n, j_m] = 2\pi \kappa \, [N[j j]_n, j_m]
$$

Using the normal ordered product

$$
N[AB]_n
= \sum_{k \le -h_A} A_k B_{n-k}
+ \sum_{k > -h_A} B_{n-k} A_k
$$

Then (using $[AB, C] = A[B,C] + [A,C]B$)

$$
\begin{aligned}
    [L_n, j_m]
    &= 2\pi \kappa \sum_{k \le -1} [j_k j_{n-k}, j_m]
    + 2\pi \kappa \sum_{k > -1} [j_{n-k} j_k, j_m]
    \\
    &= 2 \pi \kappa \sum_{k \le -1} \Big\{
        j_k [j_{n-k}, j_m] + [j_k, j_m] j_{n-k}
    \Big\} \\ &\quad
    + 2\pi \kappa \sum_{k > -1} \Big\{
        j_{n-k} [j_k, j_m] + [j_{n-k}, j_m] j_k
    \Big\}
    \\
    &= \frac{1}{2} \sum_{k \le -1} \Big\{
        j_k (n-k)\delta_{n+m,k}
        + k \delta_{-m,k} j_{n-k}
    \Big\} \\ &\quad
    + \frac{1}{2} \sum_{k > -1} \Big\{
        j_{n-k} k \delta_{-m,k}
        + (n-k) \delta_{n+m,k} j_k
    \Big\}
    \\
    &= - m j_{m+n}
\end{aligned}
$$

Remarkably, this result is independent of the normalization $\kappa$. Comparing with

$$
[L_n, \phi_m] = (n(h-1)-m) \phi_{n+m}
$$

we have again confirmed that $j(z)$ is a primary field with $h = 1$ (obviously $\bar{h} = 0$). Similarly, $\bar{j}(\bar{z})$ is also primary with $(h, \bar{h}) = (0,1)$.

## The Central Charge

One can extract the central charge from the OPE of $T(z)$:

$$
T(z)T(w)
= \frac{c/2}{(z-w)^4} + \frac{2T(w)}{(z-w)^2}
+ \frac{\p T(w)}{z-w} + \cdots
$$

By direct calculation (with Wick's theorem)

$$
\begin{aligned}
    T(z)T(w) &\sim (2\pi \kappa)^2
    (\normord{jj})(z) (\normord{jj})(w)
    \\
    &= (2\pi \kappa)^2 (
        2 \, \normord{j^\bullet(z) j^{\bullet 2}(z)
        j^\bullet(w) j^{\bullet 2}(w)}
        \\ &\qquad \qquad
        + 4 \, \normord{j^\bullet(z) j(z) j^\bullet(w) j(w)}
    ) \\
    &= \frac{1/2}{(z - w)^4}
    + \frac{4\pi \kappa}{(z-w)^2} \normord{j(z) j(w)}
    \\
    &= \frac{1/2}{(z - w)^4}
    + \frac{2 T(w)}{(z-w)^2}
    + \frac{\partial T(w)}{z - w}
\end{aligned}
$$

where we Taylor expanded the last term as

$$
j(z) j(w) = j(w) j(w)
+ \frac{1}{2} \partial_w (j(w) j(w)) (z - w)
$$

The $1/2$ factor is introduced to remove double counting. By comparison, we see

<div class="result">

**Central charge of free massless boson (2D):**

$$
c = 1
$$

</div><br>

Again, instead of explicitly evaluating this OPE, we can start from the corresponding Laurent mode algebra, i.e. the Virasoro algebra

$$
[L_n, L_m] = (n-m)L_{n+m}
+ \frac{c}{12} n (n^2 - 1) \delta_{n+m, 0}
$$

Of course one can plug in $L_n = 2\pi \kappa \, N[j j]_n$ and perform tedious calculations, but there exists a neater way to find $c$ by evaluating some inner products. We shall exploit the following result (recall that $L_n \ket{0} = 0$ for $n \ge -1$):

$$
\begin{aligned}
    |L_{-2} \ket{0}|^2
    &= \amp{0}{L_2 L_{-2}}{0}
    \\
    &= \amp{0}{[L_2 L_{-2}] + \cancel{L_{-2} L_2}}{0}
    \\
    &= \amp{0}{\cancel{4 L_0} + \frac{c}{12}2(2^2 - 1)}{0}
    \\
    &= \frac{c}{2}
\end{aligned}
$$

Now we focus on this particular term $L_2 L_{-2}$:

$$
\amp{0}{L_2 L_{-2}}{0}
= (2\pi \kappa)^2 \amp{0}{N[jj]_2 N[jj]_{-2}}{0}
$$

It seems difficult to calculate

$$
\begin{aligned}
    N[jj]_{-2} \ket{0}
    &= \bigg[
        \sum_{k \le -1} j_k j_{-2-k}
        + \sum_{k > -1} j_{-2-k} j_k
    \bigg] \ket{0}
    \\
    \bra{0} N[jj]_2
    &= \bra{0} \bigg[
        \sum_{k \le -1} j_k j_{2-k}
        + \sum_{k > -1} j_{2-k} j_k
    \bigg]
\end{aligned}
$$

However, because $j$ is a primary field, the requirement that $j(z = 0)$ is well-defined again lead to the following conditions on the Laurent modes (see Part 3)

$$
\begin{aligned}
    j_n \ket{0} &= 0 \qquad n > -1 \, &(n \ge 0)\\
    \bra{0} j_n &= 0 \qquad n < 1 \, &(n \le 0)
\end{aligned}
$$

Then lots of terms are eliminated:

$$
\begin{aligned}
    N[jj]_{-2} \ket{0}
    &= j_{-1} j_{-1} \ket{0}
    \\
    \bra{0} N[jj]_2
    &= \bra{0} (j_2 j_0 + j_1 j_1)
\end{aligned}
$$

Furthermore

$$
\bra{0} j_2 j_0
= \bra{0} ([j_2, j_0] + \cancel{j_0 j_2}) = 0
$$

Then

$$
\begin{aligned}
    \amp{0}{L_2 L_{-2}}{0}
    &= (2\pi \kappa)^2 \amp{0}{j_1 j_1 j_{-1} j_{-1}}{0}
    \\
    &= (2\pi \kappa)^2 \bra{0}{
        j_1 \underbrace{[j_1, j_{-1}]}_{1/4\pi \kappa} j_{-1}
        + j_1 j_{-1} j_1 j_{-1}
    }\ket{0}\\
    &= \pi \kappa \amp{0}{j_1 j_{-1}}{0}
    + (2\pi \kappa)^2 \amp{0}{j_1 j_{-1} j_1 j_{-1}}{0}
    \\
    &= \pi \kappa \amp{0}{[j_1, j_{-1}] + \cancel{j_{-1}j_1}}{0}
    \\ &\quad
    + (2\pi \kappa)^2 \bra{0} {
        [j_1, j_{-1}] [j_1, j_{-1}]
        + \cancel{\cdots}
    } \ket{0}
    \\
    &= \frac{1}{4} + \frac{1}{4} = \frac{1}{2}
    \overset{!}{=} \frac{c}{2}
\end{aligned}
$$

Therefore $c = 1$.

<div class="remark">

*Remark*: If we introduce multiple independent boson fields in the theory

$$
S = \frac{\kappa}{2} \sum_{i=1}^n \int d^2x \,[
    (\partial_0 \phi_i)^2
    + (\partial_1 \phi_i)^2
]
$$

Then one can show that the central charge will become $n$, reflecting the nature of the central charge as some kind of measurement of degrees of freedom. 

</div><br>
