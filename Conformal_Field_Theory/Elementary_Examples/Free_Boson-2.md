# Free Massless Boson

<font size=5>

**Part 2: Canonical Quantization on Cylinder**

</font>


## Mode Expansion of the Field $\phi$

From the Laurent expansion

$$
\begin{align*}
    \partial \phi &= (-i) j(z) = (-i) \sum_n z^{-n-1} j_n \\
    \bar{\partial} \phi &= (-i) \bar{j}(\bar{z})
    = (-i) \sum_n \bar{z}^{-n-1} \bar{j}_n
\end{align*}
$$

one can integrate over $z, \bar{z}$ and obtain an expansion of $\phi$:

<div class="result">

**Mode expansion of free boson field on complex plane:**

$$
\phi(z, \bar{z})
= \phi_0 - i (j_0 \ln z + \bar{j}_0 \ln \bar{z})
+ i \sum_{n \ne 0} \frac{1}{n} (
    j_n z^{-n} + \bar{j}_n \bar{z}^{-n}
)
$$

</div><br>

Nevertheless, it will be helpful if we go back to the Minkowski spacetime, and perform the full steps of canonical quantization on the cylinder, then map to the complex plane to obtain this mode expansion.

### Step 1: Fourier Expand the Field

On a cylinder of circumference $L$, the field $\phi$ satisfies periodic boundary condition

$$
\phi(t,x) = \phi(t, x + L)
$$

we expand it as a Fourier series

$$
\begin{align*}
    \phi(t,x) &= \sum_{n\in \Z} e^{2\pi inx/L} \phi_n(t)
    \\
    \text{Inverse: }\quad
    \phi_n(t) &= \frac{1}{L} \int_0^L dx \,
    e^{-2\pi inx/L} \phi(t,x)
\end{align*}
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
\begin{align*}
    \mathcal{L}
    &=\frac{\kappa}{2} \int_0^L dx \,
    [(\partial_t \phi)^2 - (\partial_x \phi)^2]
    \\
    &= \frac{\kappa}{2} \int_0^L dx \left[
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
    &= \frac{1}{2} \kappa L
    \sum_n \left[
        \dot{\phi}_n \dot{\phi}_{-n}
        - \left( \frac{2\pi n}{L} \right)^2 \phi_n \phi_{-n}
    \right]
\end{align*}
$$

Here we used the orthogonal relation

$$
\int_0^Ldx \, e^{2\pi i (n - m) x/L}
= L \delta_{n m}
$$

### Step 2: Impose Commutation Rules

We can now construct the Hamiltonian, in the hope that the final expression will be *a collection of harmonic oscillators*. First, the momentum conjugate to $\phi_n$ is

$$
\pi_n
= \frac{\partial \mathcal{L}}{\partial \dot{\phi}_n}
= \kappa L \dot{\phi}_{-n}
$$

which allow us to eliminate the time derivative $\dot{\phi}_n$.

<div class="remark">

*Remark*: Because $\phi_{-n}=\phi_n^\dagger$, we also have the reality condition for the momentum

$$
\pi_{-n}=\pi_n^\dagger
$$

</div><br>

We then impose the (equal-time) commutation relation (following the choice for free boson on the plane)

$$
[\phi_n, \pi_m^\dagger] = i \delta_{n m}
$$

The $\phi_n$ modes will commute with each other, and so do the $\pi_n$ modes. Then the Hamiltonian is

$$
\begin{align*}
    H &=\sum_n  \pi_n\dot{\phi}_n-\mathcal{L}
    \\
    &= \sum_n  \pi_n \frac{\pi_{-n}}{\kappa L}
    - \frac{1}{2} \kappa L \sum_n \frac{\pi_{-n}}{\kappa L} \frac{\pi_n}{\kappa L}
    + \frac{1}{2} \kappa L \sum_n  \left(\frac{2\pi  n}{L} \right)^2 \phi_n \phi_{-n}
    \\
    &=\frac{1}{2 \kappa L} \sum_n  \left[
        \pi_n\pi_{-n}
        + (2\pi n \kappa)^2 \phi_n \phi_{-n}
    \right] \equiv \sum_n H_n
\end{align*}
$$

This indeed is a sum of *decoupled harmonic oscillators*: each summand can be rewritten as

$$
H_n = \frac{1}{2m} \pi_n\pi_{-n}
+ \frac{1}{2}m \omega_n^2 \phi_n \phi_{-n}
\quad \text{with} \quad \left\{
\begin{align*}
    m &= \kappa L \\
    \omega_n &= \frac{2\pi |n|}{L}
\end{align*}
\right.
$$

However, *the $n=0$ mode has zero frequency*, which needs special treatment when defining the creation and annihilation operators.

### Step 3: Construct Creation and Annihilation Operators

For each mode $n \ne 0$, we can define the creation and annihilation operators in a way analogous to the simple harmonic oscillator:

$$
\begin{align*}
    b_n
    &= \sqrt{\frac{m \omega_n}{2}}
    \left(
        \phi_n
        + \frac{i}{m \omega_n} \pi_n
    \right)
    \\
    b_n^\dagger
    &= \sqrt{\frac{m \omega_n}{2}}
    \left(
        \phi_{-n}^\dagger
        - \frac{i}{m \omega_n} \pi_{-n}
    \right)
\end{align*}
$$

Using the commutator $[\phi_n, \pi_{-m}] = i \delta_{n m}$ and the reality condition for $\phi$ and $\pi$, we can verify that

$$
[b_n, b_m]=0, \quad
[b_n^\dagger, b_m^\dagger]=0, \quad
[b_n, b_m^\dagger]=\delta_{n m}
$$

The inverse expressions of $\phi, \pi$ in terms of $a, a^\dagger$ are

$$
\begin{align*}
    \phi_n &= \frac{1}{\sqrt{2m\omega_n}} (b_n + b_{-n}^\dagger)
    \\
    \pi_n &= -i \sqrt{\frac{m \omega_n}{2}}(b_n - b_{-n}^\dagger)
\end{align*}
$$

It follows that (no commutation rules are used here)

$$
\begin{align*}
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
\end{align*}
$$

Then the Hamiltonian can be written as

$$
\begin{align*}
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
    &= \frac{1}{2m} \pi_0^2 + \sum_{n \ne 0}
    \omega_n \left(
        b_{n}^\dagger b_{n}
        + \frac{1}{2}
    \right)
\end{align*}
$$

### Step 4: Determine Time Dependence in Heisenberg Picture

In the Heisenberg picture, we have the following equation of motion for an operator $O$:

$$
\frac{d}{dt} O(t) = i\, [H, O(t)] \quad
(\hbar = 1)
$$

- $n = 0$ (the zero mode)

    First, we notice that $\phi_0$ does not appear in $H$. This means that

    $$
    \frac{d}{dt} \pi_0(t)
    = i  \, [H, \pi_0(t)] = 0
    $$

    i.e. $\pi_0$ is a constant of motion.

    Then for $\phi_0(t)$, we obtain

    $$
    \begin{align*}
        \frac{d}{dt} \phi_0
        &= i \, [H, \phi_0]
        \\
        &= \frac{i}{2 m} \, [\pi_0^2, \phi_0]
        = \frac{\pi_0}{m}
    \end{align*}
    \quad \Rightarrow \quad
    \phi_0(t) = \phi_0(0) + \frac{\pi_0}{m} t
    $$

    which can be interpreted as uniform motion with velocity $\pi_0/m$.

- $n \ne 0$

    $$
    \begin{align*}
        \frac{\partial b_n}{\partial t}
        &= i \omega_n [b_n^\dagger b_n, b_n]
        \\
        &= i \omega_n [b_n^\dagger, b_n] b_n
        \\
        &= -i \omega_n b_n
    \end{align*} \qquad
    \begin{align*}
        \frac{\partial b_n^\dagger}{\partial t}
        &= i \omega_n [b_n^\dagger b_n, b_n^\dagger]
        \\
        &= i \omega_n b_n^\dagger [b_n, b_n^\dagger]
        \\
        &= i \omega_n b_n
    \end{align*}
    $$

    Therefore

    $$
    b_n(t) = b_n(0) e^{-i\omega_n t}, \quad
    b_n^\dagger(t) = b_n^\dagger(0) e^{i\omega_n t}
    $$

### Step 5: Map to Complex Plane

So far the quantization process is the same as free boson on the plane. But now we shall exploit the relation $\omega_n \propto |n|$, and absorb (in a way that is very hard to memorize) the $|n|$ factor into the creation and annihilation operators

$$
a_n =
\begin{cases}
    -i \sqrt{n} b_{n} & n > 0 \\
    +i \sqrt{-n} b_{-n}^\dagger & n < 0
\end{cases}
\quad
\bar{a}_n =
\begin{cases}
    -i \sqrt{n} b_{-n} & n > 0 \\
    +i \sqrt{-n} b_{n}^\dagger & n < 0
\end{cases}
$$

We note that $\bar{a}_n \ne a_n^\dagger$. With this definition:

- The commutation rules ($m,n \ne 0$):

    $$
    [a_n, a_m] = n \delta_{n + m}, \quad
    [\bar{a}_n, \bar{a}_m] = n \delta_{n+m}, \quad
    [a_n, \bar{a}_m] = 0
    $$

- The time dependence of $a_n, \bar{a}_n$:
   
    $$
    a_n(t) = a_n(0) e^{-2\pi int/L}, \quad
    \bar{a}_n(t) = \bar{a}_n(0) e^{-2\pi int/L}
    $$

<!-- - Hamiltonian in terms of $a, \bar{a}$: -->

- $\phi$ in terms of $a, \bar{a}$:

    $$
    \phi_n
    = \frac{1}{\sqrt{2m\omega_n}} (b_n + b_{-n}^\dagger)
    = \frac{1}{\sqrt{4\pi \kappa |n|}} (b_n + b_{-n}^\dagger)
    $$

    - For $n > 0$:

        $$
        \begin{align*}
            b_n &= \frac{i}{\sqrt{n}} a_n, \quad
            b_{-n}^\dagger = \frac{-i}{\sqrt{n}} \bar{a}_{-n}
            \\ \Rightarrow \quad
            \phi_n &= \frac{i}{n \sqrt{4 \pi \kappa}}
            (a_n - \bar{a}_{-n})
        \end{align*}
        $$

    - For $n < 0$:

        $$
        \begin{align*}
            b_n &= \frac{i}{\sqrt{-n}} \bar{a}_{-n}, \quad
            b_{-n}^\dagger = \frac{-i}{\sqrt{-n}} a_n
            \\ \Rightarrow \quad
            \phi_n &= \frac{i}{(-n) \sqrt{4 \pi \kappa}}
            (\bar{a}_{-n} - a_n)
        \end{align*}
        $$

    Thus in both case we get the same result. Then the time dependence of $\phi_n(t)$ is

    $$
    \phi_n(t)
    = \frac{i}{n \sqrt{4 \pi \kappa}} (
        a_n e^{-2\pi int/L}
        - \bar{a}_{-n} \, e^{2\pi int/L}
    )
    $$

Finally

$$
\begin{align*}
    \phi(x,t)
    &= \sum_n e^{2 \pi i n x / L} \phi_n(t)
    \\
    &= \phi_0 + \frac{1}{\kappa L} \pi_0 t
    \\ & \quad
    + \frac{i}{\sqrt{4\pi \kappa}} \sum_{n \ne 0}
        \frac{1}{n} (
        a_n e^{2\pi in(x - t)/L}
        - \bar{a}_{-n} e^{2\pi in(x + t)/L}
    )
    \\
    &= \phi_0 - \frac{1}{\kappa L} i \pi_0 \tau
    \\ & \quad
    + \frac{i}{\sqrt{4\pi \kappa}} \sum_{n \ne 0}
        \frac{1}{n} (
        a_n e^{2\pi n(-\tau + ix)/L}
        - \bar{a}_{-n} e^{2\pi n(\tau + ix)/L}
    )
\end{align*}
$$

In the last step we changed to the Euclidean spacetime by Wick rotation $(\tau \to it)$. Now we can map the cylinder to complex plane using

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

**Mode expansion of free boson field on complex plane:**

$$
\phi(z, \bar{z})
= \phi_0 - \frac{i}{4\pi \kappa} \pi_0 \ln (z \bar{z})
+ \frac{i}{\sqrt{4\pi \kappa}}
\sum_{n \ne 0} \frac{1}{n} (
    a_n z^{-n} + \bar{a}_n \bar{z}^{-n}
)
$$

</div><br>

<div class="remark">

*Remark*: The periodic boundary condition $\phi(x) = \phi(x+L)$ becomes the invariance under rotation 

$$
z \to w = e^{2\pi i} z, \, \bar{z} \to \bar{w} = e^{-2\pi i} \bar{z}
$$ 

Then we get a further requirement on the zero modes $j_0, \bar{j}_0$ (obviously the $n \ne 0$ terms, which are not multi-valued, is not affected)

$$
\begin{align*}
    j_0 \ln z + \bar{j}_0 \ln \bar{z}
    &= j_0 \ln w + \bar{j}_0 \ln \bar{w}
    \\
    &= j_0 \ln z + \bar{j}_0 \ln \bar{z}
    + 2\pi i(j_0 - \bar{j}_0)
    \\[0.5em] \Rightarrow \quad
    j_0 &= \bar{j}_0
\end{align*}
$$

</div><br>

Its derivative, the holomorphic field $j(z) = i \partial \phi$, is then (a similar result holds for $\bar{j}(\bar{z})$)

$$
\begin{align*}
    j (z)
    &= \frac{1}{4\pi \kappa} \frac{\pi_0}{z}
    + \frac{1}{\sqrt{4\pi \kappa}} \sum_{n \ne 0}
    a_n z^{-n-1}
    \\
    &= \frac{1}{\sqrt{4\pi \kappa}} \sum_{n}
    a_n z^{-n-1}
\end{align*}
$$

where, for convenience, we defined

$$
a_0 \equiv \bar{a}_0 \equiv
\frac{\pi_0}{\sqrt{4\pi \kappa}}
$$

Note that $\pi_0$ only has nonzero commutator with $\phi_0$ (namely $[\phi_0, \pi_0] = i$), therefore it also commutes with all other $a_{n \ne 0}$.

<div class="remark">

*Remark*: Now we recognize that the Laurent modes of the current $j(z), \bar{j}(\bar{z})$ is related to the $a, \bar{a}$ operators by

$$
j_n = \frac{1}{\sqrt{4\pi \kappa}} a_n, \quad
\bar{j}_n = \frac{1}{\sqrt{4\pi \kappa}} \bar{a}_n
$$

Then we recover the commutation rules for $j_n$ (and $\bar{j}_n$, for all integers $n$):

$$
[a_n, a_m] = n \, \delta_{n+m, 0}
\,\Rightarrow \,
[j_n, j_m] = \frac{1}{4\pi \kappa} n \, \delta_{n+m, 0}
$$

</div><br>

## The Basis States

### Vertex Operator and the "Conformal Vacuum"

Since $\pi_0$ (or equivalently $a_0$) is a constant of motion, we may build the basis states of the Hilbert space using eigenstates of $\pi_0$:

$$
\pi_0 \ket{\alpha} = \alpha \ket{\alpha}
$$

Here $\alpha$ is the eigenvalue of $\pi_0$, which can take a continuous range of values. It turns out that this state $\ket{\alpha}$ can be obtained from the true vacuum $\ket{0}$ by the action of the **vertex operator**:

$$
\ket{\alpha} = V_\alpha(0,0) \ket{0}
$$

<div class="result">

**The Vertex Operator:**

$$
\begin{align*}
    V_\alpha(z,\bar{z})
    &\equiv \normord{e^{i\alpha \phi(z,\bar{z})}}
    \\
    &= \exp {\left\{
        i \alpha \phi_0
        - \frac{\alpha}{\sqrt{4\pi \kappa}} \sum_{n<0}
        \frac{1}{n} (a_n z^{-n} + \bar{a}_n \bar{z}^{-n})
    \right\}} \\ &\quad \times
    \exp {\left\{
        \frac{\alpha}{4\pi \kappa} \pi_0 \ln (z \bar{z})
        - \frac{\alpha}{\sqrt{4\pi \kappa}} \sum_{n > 0}
        \frac{1}{n} (a_n z^{-n} + \bar{a}_n \bar{z}^{-n})
    \right\}}
\end{align*}
$$

</div><br>

*Proof*: We want to prove that

$$
\pi_0 V_\alpha(0,0) \ket{0} = \alpha V_\alpha(0,0) \ket{0}
$$

To do this, we need to following theorem: for two operators $A,B$, if $[B,A]$ is a *c*-number, then

$$
[B, e^A] = e^A [B,A]
$$

Setting $B = \pi_0, \, A = i\alpha \phi$, and noting that $\pi_0$ will commute with all $a_n, \bar{a}_n$, we obtain

$$
\begin{align*}
    [\pi_0, i\alpha \phi]
    = \left[
        \pi_0, i\alpha \phi_0
    \right] = \alpha
\end{align*}
$$

Therefore, using $\pi_0 \ket{0} = 0$, we obtain

$$
\begin{align*}
    [\pi_0, V_\alpha] &= \alpha V_\alpha
    \\ &\Downarrow \\
    \pi_0 V_\alpha(0) \ket{0}
    &= ([\pi_0, V_\alpha(0)] + V_\alpha(0) \pi_0) \ket{0} \\
    &= \alpha V_\alpha\ket{0}
    \qquad \blacksquare
\end{align*}
$$

The state $\ket{\alpha}$ is sometimes called the **conformal vacuum** because

<div class="result">

**$a_n, \bar{a}_n \, (n > 0)$ behave like annihilation operators:**

$$
a_n \ket{\alpha} = \bar{a}_n \ket{\alpha} = 0
\quad (n > 0)
$$

</div><br>

*Proof*: We prove for $a_n$ only; the argument for $\bar{a}_n$ is almost the same. Again, we shall exploit the theorem

$$
[B, e^A] = e^A [B,A]
$$

Now we set $B = a_n \, (n \ne 0), \, A = i\alpha \phi$. Note that $a_n$ commutes with $\phi_0, \pi_0, \bar{a}_n$, then

$$
\begin{align*}
    [a_n, i\alpha \phi]
    &= \frac{-\alpha}{\sqrt{4\pi \kappa}}
    \sum_{m \ne 0} \frac{1}{m} z^{-m}
    \underbrace{[a_n, a_m]}_{n \, \delta_{n+m, 0}}
    \\
    &= \frac{\alpha z^n}{\sqrt{4\pi \kappa}}
\end{align*}
$$

Therefore,

$$
\begin{align*}
    [a_n, V_\alpha(z,\bar{z})]
    &= \frac{\alpha z^n}{\sqrt{4\pi \kappa}}
    V_\alpha(z, \bar{z})
    \\ &\Downarrow \\
    a_n V_\alpha(0) \ket{0}
    &= ([a_n, V_\alpha(0)] + V_\alpha(0) a_n) \ket{0} \\
    &= 0 \quad (n > 0)
    \qquad \blacksquare
\end{align*}
$$

### $\ket{\alpha}$ as an Eigenstate of $L_0$

The $\pi_0$ eigenstate $\ket{\alpha}$ turns out to be also an eigenstate of $L_0$. To show this, we express $L_0$ in terms of $a_n$ (or equivalently $j_n$)

$$
\begin{align*}
    L_0 &= 2\pi \kappa \, N[jj]_0 \\
    &= 2\pi \kappa \bigg[
        \sum_{k \le -1} j_k j_{-k}
        + \sum_{k > -1} j_{-k} j_k
    \bigg] \\
    &= 2\pi \kappa \bigg[
        j_0 j_0 + 2 \sum_{k \ge 1} j_{-k} j_k
    \bigg] \\
    &= \frac{1}{2} a_0^2 + \sum_{k \ge 1} a_{-k} a_k
\end{align*}
$$

Therefore (do not forget the normalization $a_0 = \pi_0/\sqrt{4\pi \kappa}$)

$$
L_0 \ket{\alpha} = \frac{\alpha^2}{8\pi \kappa} \ket{\alpha}
$$

<div class="remark">

*Remark*: One can even confirm that $V_\alpha(z,\bar{z})$ are primary fields with conformal dimension

$$
(h, \bar{h}) = \left(
    \frac{\alpha^2}{8\pi \kappa},
    \frac{\alpha^2}{8\pi \kappa}
\right)
$$

Thus $\ket{\alpha}$ is the highest weight state associated with the primary field $V_\alpha$.

</div></br>

### Field Modes as Ladder Operators

When discussing the representations of Virasoro algebra, the ladder operator is chosen as $L_{\pm m}$. But the same effect can also be achieved using the Laurent modes of a primary field $\phi$: assume that $\ket{h}$ is an eigenstate of $L_0$ with eigenvalue $h$ (*it need not be the highest weight state built from $\phi$ itself*), then

<div class="result">

**Field Laurent modes as ladder operators:**

<center><b>

$\phi_{\pm m}|h\rangle$ is the eigenstate of $L_0$ with
eigenvalue $h\mp m$

</b></center>
</div><br>

*Proof*: From the commutation rule

$$
[L_n, \phi_m] = (n(h-1)-m) \phi_{n+m}
$$

we get

$$
[L_0, \phi_{\pm m}] = \mp m \phi_{\pm m}
$$

which has the *same* form as $\left[L_0,L_{\pm m} \right]$. Therefore, $\phi_{\pm m}$ can also serve as the ladder operators. Nevertheless, let us repeat the verification:

$$
\begin{align*}
    L_0 (\phi_{\pm m}|h\rangle )
    &= [L_0, \phi_{\pm m}] |h\rangle
    + \phi_{\pm m} L_0 |h\rangle
    \\
    &= \mp m \phi_{\pm m} |h\rangle
    + h \phi_{\pm m} |h\rangle
    \\
    &= (h\mp m) (\phi_{\pm m} |h\rangle) \qquad \blacksquare
\end{align*}
$$

For free massless boson, we then have two choices to build the Hilbert space: the ladder operators are chosen as $a_n, \bar{a}_n \, (n > 0)$, but the highest weight state can either be $\ket{\alpha}$ or $\ket{0}$ (regarded as the state corresponding to the identity field). The states are then (building on $\ket{\alpha}$, say)

$$
a_{-1}^{n_1} a_{-2}^{n_2} \cdots
\bar{a}_{-1}^{m_1} \bar{a}_{-2}^{m_2} \cdots \ket{\alpha}
\qquad (n_i, m_i \ge 0)
$$

