# The XY Spin Chain

## Model Hamiltonian

The Hamiltonian of the (1+1)D anisotropic **XY spin chain** under external transverse field $h$ is

$$
H = - \sum_{i=0}^{N-1} \left[
    J_x S_i^x S_{i+1}^x 
    + J_y S_i^y S_{i+1}^y 
\right] - h \sum_{i=0}^{N-1} S_i^z
$$

Here we assume periodic boundary condition (PBC):

$$
S_N^a = S_0^a \qquad a=x,y,z
$$

The coefficients $J_x, J_y$ will control whether we have ferromagnetic $(J > 0)$ or anti-ferromagnetic $(J < 0)$ interaction in the $xy$-plane. 

## Mapping to Fermion Model

We first express $S_i^x, S_i^y$ using the raising and lowering operators $S_i^\pm$:

$$
S_i^{\pm} = S_i^x \pm i S_i^y 
\, \Rightarrow \, \left\{
\begin{aligned}
    S_i^x &= \frac{1}{2}(S_i^- + S_i^+)
    \\
    S_i^y &= \frac{i}{2}(S_i^- - S_i^+)
\end{aligned}
\right.
$$

Then

$$
\begin{aligned}
    &J_x S_i^x S_{i+1}^x 
    + J_y S_i^y S_{i+1}^y 
    \\
    &= \frac{J_x}{4} (S_i^- + S_i^+)(S_{i+1}^- + S_{i+1}^+)
    \\ &\quad - \frac{J_y}{4}(S_i^- - S_i^+)(S_{i+1}^- - S_{i+1}^+)
    \\
    &= t(S_i^- S_{i+1}^+ + \underbrace{S_i^+ S_{i+1}^-}_\text{commute})
    + \Delta (S_i^+ S_{i+1}^+ + \underbrace{S_i^- S_{i+1}^-}_\text{commute})
    \\
    &= t(S_i^+ S_{i+1}^- + h.c.)
     + \Delta (S_i^+ S_{i+1}^+ + h.c.)
\end{aligned}
$$

where we defined

$$
t \equiv \frac{J_x + J_y}{4} \qquad
\Delta \equiv \frac{J_x - J_y}{4}
$$

Therefore

$$
H = - \sum_{i=0}^{N-1} \left[
    t(S_i^+ S_{i+1}^- + h.c.)
    + \Delta (S_i^+ S_{i+1}^+ + h.c.) 
\right] - h \sum_{i=0}^{N-1} S_i^z
$$

Let us now apply Jordan-Wigner transformation to fermionize the model.

$$
\begin{aligned}
    \sum_i S_i^+ S_{i+1}^-
    &= \sum_i c_i^\dagger e^{i \phi_i} 
    \underbrace{c_{i+1} e^{-i \phi_{i+1}}}_\text{commute}
    \\
    &= \sum_i c_i^\dagger e^{i (\phi_{i} - \phi_{i+1})} c_{i+1} 
    \\
    &= \sum_i c_i^\dagger e^{-i \pi n_i} c_{i+1} 
\end{aligned}
$$

Each term will give nonzero outcome only when $n_i = 0$, but this behavior is the same if the $e^{-i\pi n_i}$ is absent. So we obtain the first conversion (**nearest neighbor / tight-binding hopping**)

$$
\sum_i (S_i^+ S_{i+1}^- + h.c.) 
= \sum_i (c_i^\dagger c_{i+1} + h.c.)
$$

Next,

$$
\begin{aligned}
    \sum_i S_i^+ S_{i+1}^+
    &= \sum_i c_i^\dagger e^{i \phi_i} 
    \underbrace{c_{i+1}^\dagger e^{i \phi_{i+1}}}_\text{commute}
    \\
    &= \sum_i c_i^\dagger e^{i (2\phi_i + \pi n_i)} c_{i+1}^\dagger
\end{aligned}
$$

But $e^{2 i \phi_i} = \exp(2\pi i \textstyle{\sum_{j < i} n_j}) = 1$, and the extra $e^{i\pi n_i}$ has no effect again. Therefore (such term is related to the **$p$-wave superconductivity**)

$$
\sum_i (S_i^+ S_{i+1}^+ + h.c.) 
= \sum_i (c_i^\dagger c_{i+1}^\dagger + h.c.)
$$

Finally, we obtain the fermion theory

$$
H = - \sum_{i=0}^{N-1} \left[
    t(c_i^\dagger c_{i+1} + h.c.)
    + \Delta (c_i^\dagger c_{i+1}^\dagger + h.c.) 
\right] - h \sum_{i=0}^{N-1} \bigg(n_i - \frac{1}{2} \bigg)
$$

We see that the magnetic field $h$ now plays the role of the *chemical potential* $\mu$. 

## Exact Solution in Momentum Space

To see the energy levels more clearly, we shall go to the momentum space (reciprocal lattice). We transform the Hamiltonian term by term:

- Tight-binding term

- $p$-Wave potential term

- Chemical potential term
