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

# Many-Body State for Identical Particles

Consider a system of $N$ particles (not necessarily indistinguishable). Suppose each particle has one-body Hilbert space $\mathcal{H}_k$ ($k = 1, ..., N$), and the interaction between the particles does not destroy it. Then the full Hilbert space for the system is

$$
\mathcal{H}(N) = \mathcal{H}_1 \otimes \cdots
\otimes \mathcal{H}_N
$$

If particle 1 is in state $\ket{\psi_1} \in \mathcal{H}_1$, ..., particle $N$ is in state $\ket{\psi_N} \in \mathcal{H}_N$, then the whole system is in the state

$$
\ket{\psi} \equiv \ket{\psi_1,...,\psi_N} 
= \ket{\psi_1} \otimes \cdots \otimes \ket{\psi_N}
$$

In the traditional wave function representation, we are in fact taking the inner product of $\ket{\psi}$ with the position eigenstate 

$$
\ket{x} \equiv \ket{x_1,...,x_N} =
\ket{x_1} \otimes \cdots \otimes \ket{x_N}
$$

Then

$$
\begin{aligned}
    \psi(x_1,...,x_N)
    & \equiv \braket{x_1,...,x_N}{\psi_1,...,\psi_N}
    \\
    &= \braket{x_1}{\psi_1} \cdots \braket{x_N}{\psi_N}
    \\
    &= \psi_1(x_1) \cdots \psi_N(x_N)
\end{aligned}
$$

## Particle Relabelling (Exchange)

If the $N$ particles are identical, we have

$$
\mathcal{H}_1 = \cdots = \mathcal{H}_N \equiv \mathcal{H}
\, \Rightarrow \,
\mathcal{H}(N) = \otimes^N \mathcal{H}
$$

For such a system, relabelling the particles should not change the many-body state except for some additional phase factors. The operation of relabelling is accomplished by 

<div class="result">

**The permutation operator $P_\sigma$:**

$$
P_\sigma \ket{\psi_1,...,\psi_N}
= \ket{\psi_{\sigma(1)}, ..., \psi_{\sigma(N)}}, \quad
\sigma \in S^N
$$

</div><br>

i.e. the names of the particles are changed from $\sigma(1),...,\sigma(N)$ to $1,...,N$. 

A special case is when $\sigma$ is just an exchange of two particles $i \ne j$; the permutation operator is then denoted by

$$
P_{ij} \ket{...,\psi_i,...,\psi_j,...}
= \ket{...,\psi_j,...,\psi_i,...}
$$

## State Symmetrization

To construct relabelling-independent many-body states, we need 

<div class="result">

**The anti-/symmetrization operators $S_\pm(N)$:**

$$
S_\pm(N) \equiv \frac{1}{N!} 
\sum_{\sigma \in S^N} (\pm 1)^\sigma P_\sigma
$$

</div><br>

The $1/N!$ factor is an average over all permutations, and $(-1)^\sigma$ refers to the parity of the permutation $\sigma$. They are also denoted by $S(N)$ and $A(N)$). The particle number is usually omitted when there is no ambiguity. 

The $S_\pm$ operators has the following properties:

- $P_\sigma S_\pm = S_\pm P_\sigma = (-1)^\sigma S_\pm$

- $S_\pm^\dagger = S_\pm$ (self-adjoint)

- $S_\pm^2 = S_\pm$ (is a projection operator)

With $S_\pm(N)$, we can construct the many-body (symmetrized) states in two different ways:

- **Boson**: exchanging two particles leaves the state unchanged
    
    $$
    \ket{\psi_+} = S(N) \ket{\psi_1,...,\psi_N}
    \Rightarrow P_{ij} \ket{\psi_+} = \ket{\psi_+}
    $$

- **Fermion**: exchanging two particles produces a minus sign

    $$
    \ket{\psi_-} = A(N) \ket{\psi_1,...,\psi_N}
    \Rightarrow P_{ij} \ket{\psi_-} = -\ket{\psi_-}
    $$

These symmetrized states $\ket{\psi_\pm}$ are in general not normalized. 

### Inner Product of Symmetrized States

Using the property $S_\pm^2 = S_\pm$, we calculate the inner product of two $N$-body symmetrized states

$$
\begin{aligned}
    \braket{u_\pm}{v_\pm} 
    &\equiv \amp{u_1,...,u_N}{S_\pm^2}{v_1,...,v_N}
    \\
    &= \amp{u_1,...,u_N}{S_\pm}{v_1,...,v_N}
    \\
    &= \frac{1}{N!} \sum_{\sigma \in S^N} (\pm 1)^\sigma
    \amp{u_1,...,u_N}{P_\sigma}{v_1,...,v_N}
    \\
    &= \frac{1}{N!} \sum_{\sigma \in S^N} (\pm 1)^\sigma
    \braket{u_1,...,u_N}{v_{\sigma(1)},...,v_{\sigma(N)}}
\end{aligned}
$$

The last line can be put into matrix form:

<div class="result">

**Inner product of symmetrized states:**

$$
\braket{u_\pm}{v_\pm} = \frac{1}{N!} D_\pm \begin{bmatrix}
    \braket{u_1}{v_1} & \cdots & \braket{u_1}{v_N} \\
    \vdots & & \vdots \\
    \braket{u_N}{v_1} & \cdots & \braket{u_N}{v_N}
\end{bmatrix}
$$

</div><br>

where $D_+$ is the matrix *permanent*, and $D_-$ is the matrix *determinant*. 

In particular, when $\bra{u_\pm}$ is the position state $\bra{x_\pm}$ (or even with the particle spin $\bra{(x,s)_\pm}$), we recover the symmetrized wave function $v_\pm(x)$ of the state $\ket{v_\pm}$. 

## The Occupation Number (Fock) Basis

Pick an *orthonormal* basis $\{\ket{r}\} \, (r = 1,2,...)$ for the one-body Hilbert space $\mathcal{H}$. The corresponding position space wave function will later be denoted as

$$
\phi_r(x) = \braket{x}{r} \qquad
r = 1,2,...
$$

Let us denote the basis state occupied by particle $i$ as $\ket{r_i}$. Then the tensor products

$$
\ket{r_1,...,r_N} \equiv 
\ket{r_1} \otimes \cdots \otimes \ket{r_N}
\quad
(\ket{r_i} \in \{\ket{r}\} ; \, i = 1,...,N)
$$

naturally form an orthonormal basis for the $N$-body Hilbert space $\mathcal{H}(N)$.

For a system of $N$ identical particles, only the anti-/symmetrized states are allowed. These states form a *subspace* $\mathcal{H}(N)_\pm$ of the original Hilbert space $\mathcal{H}(N)$. 

The symmetrized subspace can be described by another set of basis, called the **occupation number basis**. These basis states are constructed by anti-/symmetrizing the original basis states of $\mathcal{H}(N)$: if the system has $N_r$ particles in state $\ket{r} \, (r = 1,2,...)$, then the corresponding basis state (for bosons or fermions, respectively) is

$$
\begin{aligned}
    \ket{N_1,N_2,...} &\equiv \text{const} \times 
    S_\pm \ket{r_1,...,r_N}
    \\
    &= \text{const} \times \ket{(r_1,...,r_N)_\pm}
\end{aligned}
$$

In this definition, we conventionally set $r_1 \le \cdots \le r_N$. Obviously, $N_1 + N_2 + \cdots = N$, and

$$
\begin{aligned}
    \text{Bosons: } &\quad 0 \le N_r \le N \\
    \text{Fermions: } &\quad 0 \le N_r \le 1
\end{aligned}
$$

By definition, it is obvious that for two Fock basis states $\ket{N_1,N_2,...}$ and $\ket{N'_1, N'_2,...}$, if $N_r \ne N'_r$ for any $r$, they are orthogonal. To make the Fock basis *orthonormal*, we will determine the constant (normalization factor) below.

### Normalization of the Fock Basis

Calculate the inner product:

$$
\begin{aligned}
    &\braket{N_1,N_2,...}{N_1,N_2,...}
    \\
    &= \frac{\text{const}^2}{N!}
    \sum_{\sigma \in S^N} (\pm 1)^\sigma
    \braket{r_1}{r_{\sigma(1)}} \cdots
    \braket{r_N}{r_{\sigma(N)}}
\end{aligned}
$$

The the orthonormal condition for the states $\ket{r}$ means that $\braket{r_i}{r_{\sigma(i)}} = 1$ only when the particles $i$ and $\sigma(i)$ are in the same state; otherwise it is 0. In other words, the permutations that have nonzero contribution to the state norm can only shuffle particles in the same state. The number of such commutations is then $N_1! \times N_2! \times \cdots$. Then for bosons, we have

$$
\frac{\text{const}^2}{N!}
N_1! N_2! \cdots \overset{!}{=} 1
$$

For fermions, things are even simpler. Since each state can at most have one particle, only the identity permutation contributes. Then

$$
\frac{\text{const}^2}{N!} \overset{!}{=} 1
$$

Since $N_r = 0,1$ for fermions (then $N_r!$ is always 1), we can combine the two cases and simply write

<div class="result">

**The Fock basis:**

$$
\ket{N_1,N_2,...} \equiv 
\sqrt{\frac{N!}{N_1! N_2! \cdots}}
\ket{(r_1,...,r_N)_\pm}
$$

</div><br>
