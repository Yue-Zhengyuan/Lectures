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

# Random Phase Approximation (RPA)

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

