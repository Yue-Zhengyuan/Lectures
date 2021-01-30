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

# Beyond the Independent Electron Approximation

*Some constants:*

- Average occupied radius $r_s$

$$
\frac{1}{n}=\frac{V}{N}=\frac{4\pi  r_s^3}{3} \Longrightarrow  r_s=\left(\frac{3}{4\pi  n}\right)^{1/3}
$$

- Bohr radius

$$
a_0=\frac{\hbar ^2}{m e^2}
$$

- Fermi wave vector for degenerate electron gas (3D)

$$
k_F=\left(3\pi ^2n\right)^{1/3}=\left(\frac{9\pi }{4}\right)^{1/3}\frac{1}{r_s}
$$

## Hartree-Fock Approximation

For a system of interacting electrons in a lattice of positive ions, the
*many-body* Hamiltonian is

$$
H=\sum_{a=1}^N \left(\frac{1}{2m}p_a^2+\sum_R \frac{-Z e^2}{\left| x_a-R\right| }\right)+\frac{1}{2}\sum_{a\neq b} \frac{e^2}{\left| x_a-x_b\right|
}
$$

The Hartree-Fock approximation is a variational method, which relies on
the fact that for a time-independent Hamiltonian $H$:

$$
\langle H\rangle_{\Psi }=\frac{\langle \Psi |H|\Psi \rangle }{\langle \Psi |\Psi \rangle }\overset{\left\{\psi_n\right\} \text{orthonormal}}{\longrightarrow
}\langle \Psi |H|\Psi \rangle
$$

is minimized by the ground-state wave function. To get an approximate
solution of the ground-state energy, we construct $\Psi$
 of a certain
form, and minimize over its parameters.

A general $N$ electron state that respect the exchange property should
be written as the :

$$
\begin{aligned}
    \Psi (q_1, ... ,q_N)
    &= \frac{1}{\sqrt{N!}}\det
    \begin{pmatrix}
        \psi_1(q_1) & \psi_1(q_2) &  ...  & \psi_1(q_N) \\
        \psi_2(q_1) & \psi_2(q_2) &  ...  & \psi_2(q_N) \\
        \vdots  & \vdots  &  ...  & \vdots  \\
        \psi_N(q_1) & \psi_N(q_2) &  ...  & \psi_N(q_N) 
    \end{pmatrix}
    \\
    &= \frac{1}{\sqrt{N!}}\sum_{\mathcal{P}} (-1)^{\text{sgn}(\mathcal{P})}\psi_1\left(q_{\mathcal{P}(1)}\right) ... \psi_N\left(q_{\mathcal{P}(N)}\right)
\end{aligned}
$$

Here $q\equiv (x,s)$ represents both the coordinate and the spin of an
electron. The subscript of $\psi_n$ refers to both the spin and other
quantum numbers (e.g. the orbital angular momentum).

Then we can minimize $\langle H\rangle_{\Psi }$ with respect to the
single-electron wave functions $\{\psi_n\}$. These trial wave functions are assumed to be *orthonormal* in the sense that

$$
\int d^3q \psi_m^*(q)\psi_n(q)\equiv \sum_s \int d^3x\psi_m^*(x,s)\psi_n(x,s)=\delta_{m n}
$$

The integration over $q$ should be understood as summation over spin $s$ and integration over coordinates $x$. In the following, we shall write $\psi_n\left(q_a\right)$ simply as $\psi_n(a)$.

### Mathematical Preparations

To evaluate $$
\langle \Psi |H|\Psi \rangle$$
, we first list some formulas
that will be used later. For any *symmetric* operator $$
F$$
 (invariant
under exchange of two particles) and two Slater determinants
$$
\Psi ,\Psi '$$
, we can verify that

$$
\left\langle \Psi |F|\Psi '\right\rangle =\frac{1}{N!}\int d^{3N}q \det \left(
\begin{array}{ccc}
 \psi_1^*(1) &  ...  & \psi_1^*(N) \\
 \vdots  & \ddots & \vdots  \\
 \psi_N^*(1) &  ...  & \psi_N^*(N) \\
\end{array}
\right)F \det \left(
\begin{array}{ccc}
 \psi_1^{\prime }(1) &  ...  & \psi_1^{\prime }(N) \\
 \vdots  & \ddots & \vdots  \\
 \psi_N^{\prime }(1) &  ...  & \psi_N^{\prime }(N) \\
\end{array}
\right)
$$

$$
=\int d^{3N}q \psi_1^*(1) ... \psi_N^*(N)F \det \left(
\begin{array}{ccc}
 \psi_1^{\prime }(1) &  ...  & \psi_1^{\prime }(N) \\
 \vdots  & \ddots & \vdots  \\
 \psi_N^{\prime }(1) &  ...  & \psi_N^{\prime }(N) \\
\end{array}
\right)
$$

Applying this to one-body symmetric operators, we obtain

$$
\left\langle \Psi \left|\sum_a  f_a\right|\Psi \right\rangle =\sum_a \int d^{3N}q \psi_1^*(1) ... \psi_N^*(N)f_a \sum_{\mathcal{P}} (-1)^{\text{sgn}(\mathcal{P})}\psi
_1(\mathcal{P}(1)) ... \psi_N(\mathcal{P}(N))
$$

Due to the orthonormality of the electron wave functions, the only
$$
\mathcal{P}$$
 that results in nonzero integral is the *identity
permutation.* Then

$$
\left\langle \Psi \left|\sum_a  f_a\right|\Psi \right\rangle =\sum_a \int d^3q_a\psi_a^*(a)f_a\psi_a(a)
$$

$$
=\sum_a \int d^3q_1 \psi_a^*(1)f_1\psi_a(1)
$$

Similarly, for two-body symmetric operators

$$
\left\langle \Psi \left|\sum_{a\neq b}  g_{a b}\right|\Psi \right\rangle =\sum_{a\neq b} \int d^3q_1d^3q_2\psi_a^*(1)\psi_b^*(2)g_{12}\left[\psi
_a(1)\psi_b(2)-\psi_a(2)\psi_b(1)\right]
$$

To make the spin variable explicit, the formula for two-body operators
can be written as

$$
\left\langle \Psi \left|\sum_{a\neq b}  g_{a b}\right|\Psi \right\rangle =\sum_{a\neq b} \int d^3x_1d^3x_2\psi_a^*(1)\psi_b^*(2)g_{12}\left[\psi
_a(1)\psi_b(2)-\delta \left(s_a,s_b\right)\psi_a(2)\psi_b(1)\right]
$$

The first term is called the , and the second term is called the . The
$$
i\neq j$$
 constraint is not needed here, because the direct and the
exchange terms cancel out when $$
i=j$$
.

#### The Calculation

In the many-body Hamiltonian, we recognize

$$
f_a=\frac{1}{2m}p_a^2+\sum_R \frac{-Z e^2}{\left| x_a-R\right| }
$$

$$
g_{a b}=\frac{1}{2}\frac{e^2}{\left| x_a-x_b\right| }
$$

Then

$$
\begin{aligned}
    \expect{H}_\Psi
    &=\sum_a \int d^3x \psi_a^*(x)\left(-\frac{\hbar ^2}{2m}\nabla ^2+U^{\text{ion}}(x)\right)\psi_a(x)\\
    &\quad
    +\frac{1}{2}\sum_{a, b} \int d^3xd^3x'\psi_a^*(x)\psi_b^*\left(x'\right)\frac{e^2}{\left| x-x'\right| }\psi_a(x)\psi_b\left(x'\right)\\
    &\quad
    -\frac{1}{2}\sum_{a, b} \int d^3xd^3x'\psi_a^*(x)\psi_b^*\left(x'\right)\frac{e^2}{\left| x-x'\right| }\delta \left(s_a,s_b\right)\psi_a\left(x'\right)\psi
    _b(x)
\end{aligned}
$$

### Hartree-Fock Equation

Minimizing $$
\langle H\rangle_{\Psi }$$
 with respect to $$
\psi_n^*$$
 under
the normalization constraint

$$
\int d^3q \psi_n^*(q)\psi_n(q)=1\text{      }\left(\text{with} \text{Lagrange} \text{multiplier} \epsilon_n\right)
$$

We obtain the **Hartree-Fock equation**:

$$
-\frac{\hbar ^2}{2m}\nabla ^2\psi_n(x)+U^{\text{ion}}(x)\psi_n(x)+U^{\text{el}}(x)\psi_n(x)-\underbrace{\sum_i \int d^3x'\frac{e^2}{\left|
x-x'\right| }\psi_i^*\left(x'\right)\psi_n\left(x'\right)\psi_i(x)\delta \left(s_n,s_i\right)}_{\text{exchange} \text{term}}=\epsilon_n\psi_n(x)
$$

where

$$
U^{\text{el}}(x)\equiv \sum_{\text{other} a} \frac{e^2}{\left| x-x_a\right| }\to e^2\int d^3x'\frac{\sum_{ i} \psi_i^*\left(x'\right)\psi_i\left(x'\right)}{\left|
x-x'\right| }
$$

In an actual solid, $$
U^{\text{ion}}+U^{\text{el}}=0$$
, then only the
exchange term survives.

### Fourier Component of Energy

We use the plane waves as the basis functions:

$$
\psi_n(x)=\exp \left(i k_n\cdot x\right)
$$

Then (omitting the subscript of $$
k_n$$
; summation carried over $$
s_n=s_i$$
)

$$
\frac{\hbar ^2k^2}{2m}\exp (i k\cdot x)-\sum_i \int d^3x'\frac{e^2}{\left| x-x'\right| }\exp \left(i k \cdot x'\right)\exp \left(i k_i\cdot \left(x-x'\right)\right)=\epsilon
(k)\exp (i k\cdot x)
$$

Summation over occupied levels $$
i$$
 is just over $$
k'<k_F$$
. Thus, renaming
$$
k_i\to k'$$
, we have

$$
\begin{aligned}
    \epsilon (k)
    &= \frac{\hbar ^2k^2}{2m}-\sum_{k'<k_F} \int d^3x'\frac{e^2}{\left| x-x'\right| }
    e^{-i(k-k')\cdot (x-x')}\\
    &\to \frac{\hbar ^2k^2}{2m}-\int_{k'<k_F}\frac{d^3k'}{(2\pi)^3}\underbrace{
        \int d^3x'\frac{e^2}{\left| x-x'\right| }
        e^{-i(k-k')\cdot(x-x')}
    }_{\text{Fourier transform}}
\end{aligned}
$$

Using the Fourier transform of the Coulomb potential

$$
V(r)=\frac{e^2}{r}\leftrightarrow V(k)=\frac{4\pi  e^2}{k^2}
$$

i.e.

$$
\frac{4\pi  e^2}{k^2}=\int d^3x \frac{e^2}{r}e^{-i k\cdot x}
$$

We obtain

$$
\epsilon (k)=\frac{\hbar ^2k^2}{2m}-\int_{k'<k_F}\frac{d^3k'}{(2\pi)^3}\frac{4\pi  e^2}{\left| k-k'\right| ^2}
$$

Setting

$$
F(x)\equiv 1+\frac{1-x^2}{2x}\ln \left| \frac{1+x}{1-x}\right|
$$

we finally have

$$
\epsilon (k)=\frac{\hbar ^2k^2}{2m}-\frac{k_Fe^2}{\pi }F\left(\frac{k}{k_F}\right)
$$

#### Appendix: Evaluation of the Integral

To do the integration easily, we use spherical polar coordinates, and
choose $z$ axis to be in the same direction of $k$:

$$
\begin{aligned}
    I &\equiv 
    \int_{k'<k_F}\frac{d^3k'}{(2\pi)^3}\frac{4\pi  e^2}{\left| k-k'\right| ^2}
    \\
    &=\int_{k'<k_F}
    \frac{k'^2 \sin \theta  dk'd\theta d\varphi }{(2\pi)^3}\frac{4\pi  e^2}{\left(k'\sin  \theta \right)^2+\left(k'\cos
    \theta -k\right)^2}
    \\
    &=\frac{e^2}{\pi }\int_0^{k_F}dk'\int_0^{\pi } d\theta  
    \frac{k'^2 \sin  \theta }{k'^2 -2k k'\cos  \theta +k^2}
    \\
    &=\frac{e^2}{\pi }\int_0^{k_F}dk'\int_0^{\pi } d\theta  
    \frac{k'^2 \sin  \theta }{k'^2-2k k'\cos  \theta +k^2}
\end{aligned}
$$

Setting $$
u=\cos  \theta$$
, then

$$
\begin{aligned}
    I &= \frac{e^2}{\pi }\int_0^{k_F}dk'
    k'^2 \int_{-1}^1 du 
    \frac{1}{k'^2-2k k'u+k^2}\\
    &= \frac{e^2}{k \pi }\int_0^{k_F}dk'k'\ln \left| \frac{k'+k}{k'-k}\right|
\end{aligned}
$$

Integrate by parts:

$$
\int_0^{k_F}dk'k'\ln \left| \frac{k'+k}{k'-k}\right| =\frac{1}{2}\int_0^{k_F}d\left(k^{\text{$$
\prime $$
2}}\right)\ln \left| \frac{k'+k}{k'-k}\right|
\\
=\left[\frac{k^{\text{$$
\prime $$
2}}}{2}\ln \left| \frac{k'+k}{k'-k}\right| \right]_{k'=0}^{k'=k_F}-\frac{1}{2}\int_0^{k_F} k^{\text{$$
\prime $$
2}} \,
d\left[\ln \left| \frac{k'+k}{k'-k}\right| \right]\\
=\frac{k_F^2}{2}\ln \left| \frac{k_F+k}{k_F-k}\right| +k\int_0^{k_F}dk'\frac{k^{\text{$$
\prime $$
2}}}{k^{\text{$$
\prime $$
2}}-k^2} \\
=\frac{k_F^2}{2}\ln \left| \frac{k_F+k}{k_F-k}\right| +k \left(k_F-\frac{k}{2}\ln \left| \frac{k_F+k}{k_F-k}\right| \right)\\
=k k_F+\frac{k_F^2-k^2}{2}\ln \left| \frac{k_F+k}{k_F-k}\right|
$$

Then, setting $$
x\equiv k\left/k_F\right.$$
, we obtain

$$
I=\frac{e^2}{\pi }\left(k_F+\frac{1}{2}\left(\frac{k_F^2}{k}-k\right)\ln \left| \frac{k_F+k}{k_F-k}\right| \right)\\
=\frac{k_Fe^2}{\pi }\left(1+\frac{1}{2}\left(\frac{k_F}{k}-\frac{k}{k_F}\right)\ln \left| \frac{1+k\left/k_F\right.}{1-k\left/k_F\right.}\right|
\right)\\
=\frac{k_Fe^2}{\pi }\left[1+\frac{1}{2}\left(\frac{1}{x}-x\right)\ln \left| \frac{1+x}{1-x}\right| \right]
$$

### 2. Single-Electron Energy Levels

Screening
---------

### 1. General Discussion

The potential $$
\phi$$
 felt by an electron in a realistic solid consists
of two parts:

1\. Produced to the positive charges (nuclei) $$
\phi ^{\text{ext}}
$$

2\. Induced by the screening electrons $$
\phi ^{\text{ind}}$$
:

We assume that $$
\phi ,\phi ^{\text{ext}}$$
 are related by some *linear
response relation*

$$
\phi ^{\text{ext}}(x)=\int d^3x'\varepsilon \left(x,x'\right)\phi \left(x'\right)
$$

$$
\varepsilon$$
 is called the . If the electron gas is isotropic,
$$
\varepsilon$$
 must depend only on the separation between $$
x$$
 and $$
x'$$
.
Then

$$
\phi ^{\text{ext}}(x)=\int d^3x'\varepsilon \left(x-x'\right)\phi \left(x'\right)
$$

Now we can apply Fourier transform: let

$$
\varepsilon (x)=\int \frac{d^3q}{(2\pi)^3}\exp (i q\cdot x)\epsilon (q)
$$

$$
\Longrightarrow  \phi ^{\text{ext}}(x)=\int \frac{d^3x'd^3q}{(2\pi)^3}\exp (i q\cdot x)\exp \left(-i q\cdot x'\right)\varepsilon (q)\phi \left(x'\right)\\
=\int \frac{d^3q}{(2\pi)^3}\exp (i q\cdot x)\left[\varepsilon (q)\underbrace{\int d^3x'\exp \left(-i q\cdot x'\right)\phi \left(x'\right)}_{\phi
(q)}\right]\\
\equiv \int \frac{d^3q}{(2\pi)^3}\exp (i q\cdot x)\phi ^{\text{ext}}(q)
$$

By comparison, we obtain

$$
\phi (q)=\frac{\phi ^{\text{ext}}(q)}{\varepsilon (q)}
$$

After obtaining the Fourier components, we make use of the Poisson
equations: separate the potential and the charge density into two parts

$$
\phi =\phi ^{\text{ext}}+\phi ^{\text{ind}}, \rho =\rho ^{\text{ext}}+\rho ^{\text{ind}}
$$

Then

$$
\nabla ^2\phi (x)=-4\pi  \rho (x)\text{              }\Longrightarrow \text{  }q^2\phi (q)=4\pi  \rho (q)
$$

$$
\nabla ^2\phi ^{\text{ext}}(x)=-4\pi  \rho ^{\text{ext}}(x)\text{    }\Longrightarrow \text{  }q^2\phi ^{\text{ext}}(q)=4\pi  \rho ^{\text{ext}}(q)
$$

$$
\nabla ^2\phi ^{\text{ind}}(x)=-4\pi  \rho ^{\text{ind}}(x)\text{    }\Longrightarrow \text{  }q^2\phi ^{\text{ind}}(q)=4\pi  \rho ^{\text{ind}}(q)
$$

For weak $$
\phi$$
, the induced charge density $$
\rho ^{\text{ind}}$$
 will be
a linear response to $$
\phi$$
. Then we can set

$$
\rho ^{\text{ind}}(q)=\chi (q)\phi (q)
$$

here $$
\chi$$
 is called the .

$$
\Longrightarrow  \frac{q^2}{4\pi }\left(\phi (q)-\phi ^{\text{ext}}(q)\right)=\chi (q)\phi (q)
$$

$$
\Longrightarrow  \phi (q)=\frac{\phi ^{\text{ext}}(q)}{1-4\pi  \chi (q)\left/q^2\right.}
$$

We now obtain the relation between $$
\varepsilon (q)$$
 and $$
\chi (q)$$
:

$$
\varepsilon (q)=1-\frac{4\pi }{q^2}\chi (q)=1-\frac{4\pi }{q^2}\frac{\rho ^{\text{ind}}(q)}{\phi (q)}
$$

To really calculate $$
\chi (q)$$
, we use one of the following two
approximation methods.

### 2. Thomas-Fermi Theory (Semiclassical Approximation)

One-electron Schrödinger equation

$$
-\frac{\hbar ^2}{2m}\nabla ^2\psi_n(x)-e \phi (x)\psi_n(x)=\epsilon_n\psi_n(x)
$$

The single electron energy is approximated by

$$
\epsilon (k)=\frac{\hbar ^2k^2}{2m}-e \phi (x)
$$

requiring that $$
\phi (x)$$
 vary slowly on the scale of a Fermi
wavelength. Then the equilibrium number density of the electrons is
given by the Fermi distribution (including the spin degeneracy of 2)

$$
n(x)=\int \frac{d^3k}{(2\pi)^3}\frac{2}{\exp \left[\beta  \left(\frac{\hbar ^2k^2}{2m}-e \phi (x)-\mu \right)\right]+1}
$$

Compared with the density of free electron gas ($$
\phi =0$$
) as a function
of $$
\mu
$$

$$
n_0(\mu)=\int \frac{d^3k}{(2\pi)^3}\frac{2}{\exp \left[\beta  \left(\frac{\hbar ^2k^2}{2m}-\mu \right)\right]+1}
$$

we find $$
n(x)=n_0(\mu +e \phi (x))$$
. Then the induced charge density is

$$
\rho ^{\text{ind}}(x)=-e\left[n_0(\mu +e \phi (x))-n_0(\mu)\right]
$$

Since $$
\phi$$
 is small, we can expand $$
n_0$$
 with respect to $$
\mu$$
:

$$
\rho ^{\text{ind}}(x)=-e^2\frac{\partial n_0}{\partial \mu }\phi (x)
$$

Compared with $$
\rho ^{\text{ind}}(q)=\chi (q)\phi (q)$$
, we find

$$
\chi (q)=-e^2\frac{\partial n_0}{\partial \mu }
$$

which is *independent of* $$
q$$
. Simultaneously, we obtain

$$
\varepsilon (q)=1-\frac{4\pi }{q^2}\chi (q)=1+\frac{4\pi  e^2}{q^2}\frac{\partial n_0}{\partial \mu }
$$

Usually people define a

$$
k_0=4\pi  e^2\frac{\partial n_0}{\partial \mu }
$$

Then

$$
\varepsilon (q)=1+\frac{k_0^2}{q^2}
$$

### 3. Lindhard Theory (Random Phase Approximation, RPA)

In the Lindhard theory, we use the perturbation method to get the
single-electron wave function to first order:

$$
\psi_k(x)=\psi_k^0(x)+\sum_{q\neq 0} c_q\psi_{k+q}^0(x)
$$

with the coefficients

$$
c_q=\frac{\left\langle \psi_{k+q}^0|-e \phi (x)|\psi_k^0\right\rangle }{\epsilon ^0(k)-\epsilon ^0(k+q)},\text{  }\epsilon ^0(k)=\frac{\hbar
^2k^2}{2m}
$$

Note that the free electron states $$
\psi_k^0$$
 are *plane waves*. Then
the amplitude
$$
\left\langle \psi_{k+q}^0|\phi (x)|\psi_k^0\right\rangle$$
 simply
gives the Fourier component $$
\phi (q)$$
:

$$
\begin{aligned}
    \left\langle \psi_{k+q}^0|\phi (x)|\psi_k^0\right\rangle =\langle k+q|\phi (x)|k\rangle =\int d^3x\langle k+q|\phi (x)|x\rangle \langle x|k\rangle
    \\
    =\int d^3x \phi (x)\langle k+q|x\rangle \langle x|k\rangle =\int d^3x \phi (x)e^{-i(k+q)\cdot x+i k\cdot x}\\
    =\int d^3x \phi (x)e^{-i q\cdot x}=\phi (q)
\end{aligned}
$$

To obtain $$
\chi (q)$$
, we can take a potential with $$
\pm q$$
 component
only (the $$
-q$$
 component is needed to ensure that $$
\phi (x)$$
 is *real*):

$$
\phi (x)=\phi (q)e^{i q\cdot x}+\phi (-q)e^{-i q\cdot x}, \phi (-q)=\phi ^*(q)
$$

Then the only nonzero $$
c$$
's are

$$
c_q=\frac{-e \phi (q)}{\epsilon ^0(k)-\epsilon ^0(k+q)}, c_{-q}=\frac{-e \phi ^*(q)}{\epsilon ^0(k)-\epsilon ^0(k-q)}
$$

and

$$
\begin{aligned}
    \psi_k(x)=\psi_k^0(x)+c_q\psi_{k+q}^0(x)+c_{-q}\psi_{k-q}^0(x)\\
    =e^{i k\cdot x}+c_qe^{i (k+q)\cdot x}+c_{-q}e^{i (k-q)\cdot x}
\end{aligned}
$$

The charge density is again given by the Fermi distribution:

$$
\begin{aligned}
    \rho (x)=-e\sum_k \frac{2\left| \psi_k(x)\right| {}^2}{\exp \left(\beta \left(\epsilon_k-\mu \right)\right)+1}\\
    \simeq -e\sum_k \frac{2\left| \psi_k(x)\right| {}^2}{\exp \left(\beta \left(\epsilon_k^0-\mu \right)\right)+1}=-e\sum_k f(k)\left| \psi_k(x)\right|
    {}^2
\end{aligned}
$$

with the Fermi distribution (with spin degeneracy 2)

$$
f(k)=\frac{2}{\exp \left(\beta \left(\epsilon_k^0-\mu \right)\right)+1}
$$

Comparing with the free electron result

$$
\rho_0(x)=-e\sum_k f(k)
$$

the difference is (up to $$
O(c)$$
)

$$
\begin{aligned}
    \rho ^{\text{ind}}(x)=\rho (x)-\rho_0(x)=-e\sum_k f(k)\left(\left| \psi_k(x)\right| {}^2-1\right)\\
    =-e\sum_k f(k)\left[\left(c_q+c_{-q}^*\right)e^{i q\cdot x}+\left(c_{-q}+c_q^*\right)e^{-i q\cdot x}\right]\\
    =\left[e^2\phi (q)\sum_k f(k)\left(\frac{1}{\epsilon ^0(k)-\epsilon ^0(k+q)}+\frac{ 1}{\epsilon ^0(k)-\epsilon ^0(k-q)}\right)\right]+\text{complex}
    \text{conjugate}\\
    =\rho ^{\text{ind}}(q)+\rho ^{\text{ind}}(-q)
\end{aligned}
$$

which also has two components ($$
\pm q$$
), as expected. Therefore

$$
\chi (q)=e^2\sum_k \left(\frac{f(k)}{\epsilon ^0(k)-\epsilon ^0(k+q)}+\frac{f(k)}{\epsilon ^0(k)-\epsilon ^0(k-q)}\right)
$$

To make the result more symmetric, in the first summation, we change
$$
k\to k-q/2$$
; in the second summation, we change $$
k\to k+q/2$$
. Then

$$
\chi (q)=e^2\sum_k \left(\frac{f(k-q/2)}{\epsilon ^0(k-q/2)-\epsilon ^0(k+q/2)}+\frac{f(k+q/2)}{\epsilon ^0(k+q/2)-\epsilon ^0(k-q/2)}\right)
$$

$$
=-e^2\sum_k \frac{f(k-q/2)-f(k+q/2)}{\hbar ^2k\cdot q/m}
$$

The continuous limit of the expression is

$$
\chi (q)=-e^2\int \frac{d^3k}{(2\pi)^3}\frac{f(k-q/2)-f(k+q/2)}{\hbar ^2k\cdot q/m}
$$

