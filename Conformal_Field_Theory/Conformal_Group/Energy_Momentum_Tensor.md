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

# Energy-Momentum Tensor in CFT

The **energy-momentum tensor** $T^{\mu \nu}$ is a rather mysterious object due to various definitions and its non-uniqueness. 

- **Definition 1 (Canonical)**: as the conserved current of spacetime (rigid) translation symmetry, as shown earlier. 
    
    $$
    {(T_c)^\mu}_\nu = 
    \frac{\partial \mathcal{L}}
    {\partial (\partial_\mu \phi)} 
    \partial_\nu \phi
    - \delta_\nu^\mu \mathcal{L}
    $$
    
    This is in general not symmetric. However, one can make it so by adding a term $B$ satisfying the following relations 
    
    $$
    T^{\mu \nu} = (T_c)^{\mu \nu} + \partial_\rho B^{\rho \mu \nu},
    \quad
    B^{\rho \mu \nu} = -B^{\mu \rho \nu}
    $$

    without destroying the (classical) conservation $\partial_\mu T^{\mu \nu} = 0$.

- **Definition 2 (Hilbert)**: from the change of (matter) action due to a variation of the metric:

    $$
    \delta S = \frac{1}{2} \int d^d x
    \sqrt{g} T^{\mu \nu} \delta g_{\mu \nu}
    \quad (g \equiv \det g_{\mu \nu})
    $$

    The $T^{\mu \nu}$ defined in this way is obviously symmetric. 
    
If the theory is invariant under the transformation ($\delta S = 0$), one can show that $T^{\mu \nu}$ is (classically) conserved:

$$
D_\mu T^{\mu \nu} = 0
\xrightarrow{\text{flat space}}
\partial_\mu T^{\mu \nu} = 0
$$

### Traceless $T^{\mu \nu}$ Implies Conformal Invariance

Recall that for an arbitrary infinitesimal coordinate transformation

$$
x'^\mu = x^\mu + \epsilon^\mu(x)
$$

the variation of action is (with a symmetric $T^{\mu \nu}$)

$$
\begin{align*}
    \delta S 
    &= - \int d^dx \, (\partial_\mu \epsilon_\nu) T^{\mu \nu}
    \\
    &= -\frac{1}{2} \int d^dx \, T^{\mu \nu}
    (\partial_\mu \epsilon_\nu + \partial_\nu \epsilon_\mu)
\end{align*}
$$

For conformal transformations

$$
\begin{align*}
    \partial_{\mu} \epsilon_{\nu}(x)
    + \partial_{\nu} \epsilon_{\mu}(x)
    &= f(x) \eta_{\mu \nu}
    \\
    f(x) &= \frac{2}{d} (\partial \cdot \epsilon) (x)
\end{align*}
$$

then

$$
\delta S = -\frac{1}{d} \int d^dx \, {T^\mu}_\mu
(\partial \cdot \epsilon)
$$

It follows that

<div class="result">
<center><b>

$T^{\mu \nu}$ is traceless $\Rightarrow$
Conformal invariance

</b></center>
</div><br>

<div class="remark">

*Remark*: The converse is not true, since $\partial \cdot \epsilon$ is not an arbitrary function of $x$. However, one can show that (see the Yellow Book 4.2.2):

<i>

> <br>
> Under certain conditions, the energy-momentum tensor of a theory with scale invariance can be made traceless, much in the same way as it can be made symmetric in a theory with rotation invariance. If this is possible, then it follows from the above that full conformal invariance is a consequence of scale invariance and Poincaré invariance. 
> 
> We know of no general proof that the energy-momentum tensor of a two-dimensional field theory with scale invariance can be made traceless. However, we shall hold it to be true. <br><br>

</i>

</div><br>

### 2D $T^{\mu \nu}$ in Complex Coordinates

Recall that in 2D, one transforms to the complex coordinates $z, \bar{z}$ by

$$
z = x^0 + ix^1, \quad
\bar{z} = x^0 - ix^1
$$

with the inverse relation

$$
x^0 = \frac{1}{2}(z+\bar{z}),
\quad
x^1 = -\frac{i}{2}(z-\bar{z})
$$

The energy-momentum tensor will then transform to:

$$
\begin{align*}
    \begin{pmatrix}
        T_{zz} & T_{z \bar{z}} \\
        T_{\bar{z} z} & T_{\bar{z}\bar{z}}
    \end{pmatrix}
    = \frac{\partial x^\rho}{\partial z^\mu}
    \frac{\partial x^\sigma}{\partial z^\nu}
    T_{\rho \sigma}(x)
\end{align*}
$$

For example:

$$
\begin{align*}
    T_{z z} 
    &=
    \frac{\partial x^0}{\partial z} \frac{\partial x^0}{\partial z}T_{00}
    + \frac{\partial x^0}{\partial z} \frac{\partial x^1}{\partial z}T_{01}
    \\ &\qquad
    +\frac{\partial x^1}{\partial z} \frac{\partial x^0}{\partial z}T_{10}
    + \frac{\partial x^1}{\partial z} \frac{\partial x^1}{\partial z}T_{11}
    \\
    &= \frac{1}{2} \frac{1}{2}T_{00}
    + \frac{1}{2} \frac{-i}{2}T_{01}
    + \frac{-i}{2} \frac{1}{2}T_{10}
    + \frac{-i}{2} \frac{-i}{2}T_{11}
    \\
    &= \frac{1}{4} (T_{00} - 2i T_{10} - T_{11})
\end{align*}
$$

Proceeding in the same way, we find

$$
\begin{align*}
    T_{\bar{z} \bar{z}} 
    &= \frac{1}{4} (T_{00} + 2i \, T_{10} - T_{11})
    \\
    T_{z \bar{z}} = T_{\bar{z}z}
    &= \frac{1}{4} (T_{00}+T_{11})
\end{align*}
$$

Since the energy-momentum tensor for 2D CFT is *traceless*, we can simplify further:

$$
\begin{align*}
    T_{z z}
    &= \frac{1}{2} (T_{00}-i T_{10})
    \\
    T_{\bar{z} \bar{z}}
    &=\frac{1}{2} (T_{00}+i T_{10})
    \\
    T_{z \bar{z}} = T_{\bar{z}z} &=0
\end{align*}
$$

<div class="remark">

*Remark*: At first sight, $T_{zz} + T_{\bar{z}\bar{z}} = T_{00} \ne 0$ will make people think something's wrong. But the trace of the complexified $T_{\mu \nu}$ should be taken with the *complexified* metric $g_{\mu \nu}$, which we shall verify later.

</div><br>

The classical conservation $\partial^\mu T_{\mu \nu} = 0$ implies that $T_{z z},T_{\bar{z} \bar{z}}$ depends only on $z$ and $\bar{z}$ respectively, so we define

<div class="result">

**Energy-momentum tensor in 2D**

$$
T(z)\equiv -2\pi  T_{z z}(z), 
\quad
\bar{T}(\bar{z}) \equiv -2\pi T_{\bar{z} \bar{z}}(\bar{z})
$$

</div><br>

*Proof*: In Euclidean spacetime, $\partial^{\mu}T_{\mu  \nu}=0$ is explicitly

$$
\partial_0T_{00}+\partial_1T_{10}
= \partial_0T_{01}+\partial_1T_{11}
= 0
$$

Since the energy-momentum tensor is traceless and symmetric:

$$
\begin{align*}
    \partial_{\bar{z}}T_{z z}
    &= \frac{1}{4} 
    (\partial_0 + i\partial_1)
    (T_{00} - i T_{10})
    \\
    &= \frac{1}{4} (
        \partial_0T_{00}
        - i \partial_0 T_{10}
        + i \partial_1 T_{00}
        +\partial_1T_{10}
    )
    \\
    &= \frac{1}{4} (
        \partial_0T_{00}
        - i \partial_0 T_{01}
        - i \partial_1 T_{11}
        +\partial_1T_{10}
    )
    \\
    &= \frac{1}{4} [
        (\partial_0T_{00} + \partial_1T_{10})
        - i (\partial_0T_{01} + \partial_1T_{11})
    ]
    = 0
\end{align*}
$$

Similarly, we can show that $\partial_zT_{\bar{z} \bar{z}}=0$. $\blacksquare$

### 2D Flat Metric in Complex Coordinates

Let us transform the Euclidean metric in 2D into complex coordinates:

$$
\begin{align*}
    \begin{pmatrix}
        g_{zz} & g_{z \bar{z}} \\
        g_{\bar{z} z} & g_{\bar{z}\bar{z}}
    \end{pmatrix}
    = \frac{\partial x^\rho}{\partial z^\mu}
    \frac{\partial x^\sigma}{\partial z^\nu}
    g_{\rho \sigma}(x)
\end{align*}
$$

One then obtain

$$
\begin{align*}
    \begin{pmatrix}
        g_{zz} & g_{z \bar{z}} \\
        g_{\bar{z} z} & g_{\bar{z}\bar{z}}
    \end{pmatrix} &= \begin{pmatrix}
        0 & 1/2 \\ 1/2 & 0
    \end{pmatrix} \\[1em]
    \begin{pmatrix}
        g^{zz} & g^{z \bar{z}} \\
        g^{\bar{z} z} & g^{\bar{z}\bar{z}}
    \end{pmatrix} &= \begin{pmatrix}
        0 & 2 \\ 2 & 0
    \end{pmatrix}
\end{align*}
$$

Let us verify that the complexified energy-momentum tensor is still traceless:

$$
\begin{align*}
    {T^\mu}_\mu &= g^{\mu \nu} T_{\nu \mu}
    \\
    &= \operatorname{Tr} \left[ \begin{pmatrix}
        0 & 2 \\ 2 & 0
    \end{pmatrix} \begin{pmatrix}
        \frac{1}{2} (T_{00}-i T_{10}) & 0 \\
        0 & \frac{1}{2} (T_{00}+i T_{10})
    \end{pmatrix} \right]
    \\
    &= 0
\end{align*}
$$
