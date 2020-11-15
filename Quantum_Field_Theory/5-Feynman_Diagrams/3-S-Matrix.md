# Cross Section

Consider a target of particles of type $A$ moving with velocity $v_A$, with density $\rho_A$ (particles per unit volume). We then shoot at it a bunch of particles of type $B$, with number density $\rho_B$ and velocity $v_B$ (parallel to $v_A$; this is always the case if we go to the center-of-mass frame).

<center>
<img src="Figures/scattering.png" width=400pt>
</center>

Particles $B$ will be scattered by particles $A$. Let: 

- $n$ be the number of incoming $B$ particles *per unit area* of the beam cross section that will go into the beam of $A$;
- $N$ be the *total* number of scattered $B$ particles.

The **cross section** of scattering is defined as

$$
\sigma = \frac{N}{n} = \frac{N}{\Phi_B T}
$$

- $\Phi_B = \rho_B|v_A - v_B|$ is the flux of $B$ *relative to $A$*; the volume density $\rho_B$ is assumed to be uniform everywhere in the $B$ beam;
- $T$ is the experiment time, which is assumed to be large but finite. 

We see that $\sigma$ has the dimension of area, hence its name. 

If we are only interested in the particles $B$ (with number $dN$) that falls in a differential region of parameters (say the phase space $d\Pi$), we also use the **differential cross section**

$$
d\sigma = \frac{dN}{n} 
= \frac{dN}{\rho_B|v_A - v_B| T}
$$

We can reexpress $d\sigma$ using the **scattering probability**. Let $dP$ be the probability that one particle $B$ will be scattered to the desired differential region of parameters. Then the (differential) number of scattered $B$ particles is just

$$
dN = \rho_B V \, dP
$$

For convenience, we assume that our scattering experiment is confined in a finite volume $V$. Then $\rho_B V$ is simply the *total* number of particles $B$ *all over the experiment space*. Therefore

$$
d\sigma = \frac{\rho_B V dP}{\rho_B|v_A - v_B| T}
= \frac{V}{|v_A - v_B| T} dP
$$

## *S*-Matrix and Scattering Probability

The scattering probability $dP$ can be related to the so-called ***S*-matrix**. 

Let $|\psi,t\rangle$ be the Schrödinger picture state at time $t$; its Heisenberg picture counterpart is simply denoted by $|\psi\rangle$.

The *free* states at $t = \pm \infty$ are called **asymptotic states**. The **$S$-matrix** describes the amplitude to go from $t = -\infty$ to $t = +\infty$:

$$
S_{fi} 
= \langle f|S|i \rangle
\equiv \langle f, + \infty | i,-\infty \rangle
$$

For free theory, $S = 1$. Thus for a general theory, we write

$$
S = 1 + i T
$$

where $T$ is the **transfer matrix**. Since $S$ should vanish unless the total 4-momentum is conserved, we normalize $T$ as

$$
\textstyle
i T = i \mathcal{M}
(2\pi)^4 \delta^4(\sum p_f - \sum p_i)
$$

where $\mathcal{M}$ is called the **invariant matrix element**. Now we can extract the "non-trivial" part of the $S$-matrix:

$$
i T_{fi}
= i \mathcal{M}_{fi} (2\pi)^4 
\delta^4(\textstyle{\sum p_f - \sum p_i})
$$

With $S$-matrix, the probability $dP$ that one particle $B$ will be scattered into $|f\rangle$ *and* fall in the momentum phase space $d\Pi$ (momentum states are uniformly distributed) is given by the product

$$
dP = \frac{|S_{fi}|^2}{
    \langle f|f \rangle
    \langle i|i \rangle
} d\Pi
$$

We now investigate the two parts of this $dP$:

- The normalization of the states should be treated carefully. Usually, the initial and final states will be chosen as the momentum eigenstates. For example, we write for $2 \to n$ scattering
    
    $$
    \begin{aligned}
        |i\rangle &= |\mathbf{p}_1, \mathbf{p}_2\rangle
        = |\mathbf{p}_1\rangle \otimes |\mathbf{p}_2\rangle
        \\
        |f\rangle &= |\mathbf{p}'_1, ..., \mathbf{p}'_n \rangle
        = |\mathbf{p}'_1\rangle \otimes \cdots \otimes |\mathbf{p}'_n\rangle
    \end{aligned}
    $$

    Recall that we defined the momentum eigenstates differently from non-relativistic theory

    $$
    |\mathbf{p}\rangle = \sqrt{2E_\mathbf{p}} a_\mathbf{p}^\dagger |0\rangle
    $$

    Therefore, its norm is

    $$
    \begin{aligned}
        \langle \mathbf{p} | \mathbf{p} \rangle
        &= 2E_\mathbf{p} 
        \langle 0| a_\mathbf{p} a_\mathbf{p}^\dagger |0\rangle
        \\
        &= 2E_\mathbf{p} 
        \langle 0| [a_\mathbf{p} a_\mathbf{p}^\dagger] + a_\mathbf{p}^\dagger a_\mathbf{p} |0\rangle
        \\
        &= 2E_\mathbf{p} (2\pi)^3 \delta^3(0)
    \end{aligned}
    $$

    which seems to be unphysical. However, with the finite volume (and the experiment time $T$), using

    $$
    \int \frac{d^3p}{(2\pi)^3} f(\mathbf{p})
    \to \frac{1}{V} \sum_\mathbf{p} f(\mathbf{p})
    $$

    the space delta functions can be regulated to

    $$
    \delta^3(\mathbf{p} - \mathbf{p}') 
    \to \frac{V}{(2\pi)^3} \delta_{\mathbf{p} \mathbf{p}'}
    $$

    and therefore

    $$
    \delta^3(0) \to \frac{V}{(2\pi)^3}, \quad
    \delta^4(0) \to \frac{TV}{(2\pi)^4}
    $$

    We now can write

    $$
    \begin{aligned}
        \langle i | i \rangle
        &= (2E_1 V) (2E_2 V) 
        \\
        \langle f | f \rangle
        &= (2E'_1 V) \cdots (2E'_n V)
    \end{aligned}
    $$

    We shall see that the $V$ factors will eventually cancel each other

- The phase space element is integrated all over the experimental space:

    $$
    d\Pi = \int_V
    \prod_{j=1}^n \frac{d^3x \, d^3p}{(2\pi)^3}
    = \prod_{j=1}^n \left[
        \frac{V}{(2\pi)^3} d^3 p
    \right]
    $$

    where $V$ is the volume of the experiment space. 