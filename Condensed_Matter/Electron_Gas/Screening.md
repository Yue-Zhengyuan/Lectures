# Screening in Electron Gas

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