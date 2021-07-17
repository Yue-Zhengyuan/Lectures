# Energy-Momentum Tensor and Metric

## Alternative Definition of Energy-Momentum Tensor

Since the tensor $T^{\mu \nu}$ can be made symmetric, we can write

$$
\begin{align*}
    \delta S
    &= \int d^dx \epsilon_{\nu} \partial_{\mu}T^{\mu  \nu}
    = -\int d^dx T^{\mu  \nu} \partial_{\mu} \epsilon_{\nu}
    \\
    &= -\frac{1}{2} \int d^dx \,
    T^{\mu \nu} (
        \partial_{\mu} \epsilon_{\nu}
        + \partial_{\nu} \epsilon_{\mu}
    )
\end{align*}
$$

But in flat spacetime, we recognize that

$$
\delta  g_{\mu  \nu}
= -(
    \partial_{\mu} \epsilon_{\nu}
    +\partial_{\nu} \epsilon_{\mu}
)
$$

Therefore, we may generalize the energy-momentum tensor as the
functional derivative of the action with respect to the metric:

$$
\delta  S = -\frac{1}{2} \int d^dx \, 
T^{\mu  \nu} \delta  g_{\mu  \nu}
$$

which is also applicable to curved spacetime with minor modification:

## Tetrad

On a Riemannian manifold, since it is "locally flat" at every point, we can introduce at each point a *local orthogonal frame of basis vectors* of the cotangent space:

$$
e^a=e_{\mu}^a(x)dx^{\mu} \quad (a=1,...,d)
$$

Here $d$ is the dimension of the manifold, and the basis vectors $e^a$ form a **tetrad**. A natural choice is

$$
e_{\mu}^ae_{\nu}^bg^{\mu \nu}=\eta^{a b}, 
\quad
g_{\mu \nu}=\eta_{a b}e_{\mu}^ae_{\nu}^b
$$

The lower (Greek) index of $e_{\mu}^a$ is called an **Einstein index**, and the upper (Latin) index is called a **Lorentz index**. They are raised or lowered by the metric tensor $g_{\mu \nu}$ and the Minkowski tensor $\eta_{a b}$, respectively.

Recall that under a change of coordinates $x\to x'(x)$, the metric
transforms according to

$$
g_{\mu \nu}(x)
\to g_{\mu \nu}^{\prime}(x')
= \frac{\partial x^{\rho}}{\partial x'^{\mu}}
\frac{\partial x^{\sigma}}{\partial x'^{\nu}}
g_{\rho \sigma}(x)
$$

but $\eta_{a b}$ does *not* change. Thus, using
$g_{\mu \nu}=\eta_{a b}e_{\mu}^ae_{\nu}^b$, we find that

$$
e_{\mu}^a(x) \to e_{\mu}^{\prime a}(x')
= \frac{\partial x^{\nu}}{\partial x'^{\mu}}
e_{\nu}^a(x)
$$