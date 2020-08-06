

### Central Extension and Virasoro Algebra

#### Central Extension of Lie Groups and Lie Algebra

A **central extension** of a group $G$ is a short exact sequence of groups

$$
1 \to A \to E \to G \to 1
$$

such that $A$ is in $Z(E)$, the **center** of the group $E$, which is the set of elements in $E$ that commute with every element of $E$:

$$
Z(E)\equiv
\{ z\in E \mid z g=g z, \, \forall g\in E\}
$$

Obviously, the center of $E$ is an *invariant* subgroup of $E$.

The set of isomorphism classes of central extensions of $G$ by $A$ (where $G$ acts *trivially* on $A$) is in one-to-one correspondence with the cohomology group $H^2(G,A)$.

#### Virasoro Algebra

There is a *unique* central extension of the Witt algebra, called the **Virasoro algebra**.

We first consider the holomorphic part. The generators $l_n$ are promoted to $L_n$, and a new element $c\in \mathbb{C}$ (the **central charge**) is introduced so that

$$
\begin{aligned}
    [L_n, L_m] &=(n-m)L_{m+n}+c p(n,m)
    \\
    [L_n, c] &= 0\\
    [c,c] &= 0
\end{aligned}
$$

where $p$ is a *bilinear* mapping onto $\mathbb{C}$ (this is required by
the bi-linearity of the Lie bracket). The last two equations mean that
$c$ commutes with all group elements in the Virasoro algebra. Similar
relations hold for the anti-holomorphic part ($\bar{l}_n\to \bar{L}_n$
etc).

Now we determine the explicit form of $p(n,m)$ for Virasoro algebra.

1\. Since the Lie bracket is *anti-symmetric*, we obtain

$\left[L_n,L_m\right]=(n-m)L_{m+n}+c p(n,m)\\
=-\left[L_m,L_n\right]=-(m-n)L_{n+m}-c p(m,n)$

$\Longrightarrow  p(n,m)=-p(m,n)$

2\. We can always make

$p(1,-1)=0, p(n,0)=0$

If they are not zero, we redefine the $L_n$ operators as

$L_n^{\prime}=L_n+\frac{c p(n,0)}{n} (n\neq 0), L_0^{\prime}=L_0+\frac{c p(1,-1)}{2}$

Then

$\left[L_n^{\prime},L_0^{\prime}\right]=\left[L_n,L_0\right]=n L_n+c p(n,0)=n L_n^{\prime}$

$\left[L_1^{\prime},L_{-1}^{\prime}\right]=\left[L_1,L_{-1}\right]=2L_0+c p(1,-1)=2L_0^{\prime}$

The motivation for the redefinition above is now clear.

3\. The Lie bracket should satisfy the *Jacobi identity*

$\left[\left[L_m,L_n\right],L_l\right]+\left[\left[L_l,L_m\right],L_n\right]+\left[\left[L_n,L_l\right],L_m\right]=0$

For $(m,n,l)\to (m,n,0)$, we have

$(m+n)p(n,m)=0 \Longrightarrow p(n,m)=p(n,-n)\delta_{m+n, 0}$

But we still have $p(1,-1)=0$, thus $p(n,-n)\neq 0$ *is possible only
when* $| n| \geq 2$.

For $(m,n,l)\to (-n+1,n,-1)$, we have

$(-2n+1)c p(1,-1)+(n+1)c p(n-1,-n+1)+(n-2)c p(-n,n)=0$

Or

$(n+1) p(n-1,-n+1)=(n-2) p(n,-n)$

which allows us to calculate $p(n,-n)$ recursively:

$p(n,-n)=\frac{n+1}{n-2}p(n-1,-n+1)\\
=\frac{(n+1)n}{(n-2)(n-3)}p(n-2,-n+2)\\
= \cdots =\left(
\begin{array}{c}
 n+1 \\
 3 \\
\end{array}
\right)p(2,-2)$

By convention, we set

$p(2,-2)=\frac{1}{2}$

Summarize all the above calculations, we finally find

$p(n,m)=\frac{1}{12}n\left(n^2-1\right)\delta_{m+n, 0}$

and the Virasoro algebra is

$\left[L_n,L_m\right]=(n-m)L_{n+m}+\frac{c}{12}n\left(n^2-1\right)\delta_{m+n, 0}$

#### Other Commutation Rules in Virasoro Algebra

Adding the anti-holomorphic parts into the algebra, we further obtain

$\left[\bar{L}_n,\bar{L}_m\right]=(n-m)\bar{L}_{n+m}+\frac{\bar{c}}{12}n\left(n^2-1\right)\delta_{m+n, 0}$

Here $\bar{c}$ is the central charge of the anti-holomorphic sector.
Some physical constraints (such as the conformal invariance on a torus)
will fix

$\bar{c}=c$

For the mixed commutator, we still have

$\left[L_n,\bar{L}_m\right]=0$



Ward-Takahashi Identity
-----------------------

#### Math Appendix: The Tetrad

On a Riemannian manifold, since it is "locally flat" at every point, we can introduce at each point a *local orthogonal frame of basis vectors* of the cotangent space:

$e^a=e_{\mu}^a(x)dx^{\mu} \quad (a=1,...,d)$

Here $d$ is the dimension of the manifold, and the basis vectors $e^a$ form a **tetrad**. A natural choice is

$e_{\mu}^ae_{\nu}^bg^{\mu \nu}=\eta^{a b}, g_{\mu \nu}=\eta_{a b}e_{\mu}^ae_{\nu}^b$

The lower (Greek) index of $e_{\mu}^a$ is called an **Einstein index**, and the upper (Latin) index is called a **Lorentz index**. They are raised or lowered by the metric tensor $g_{\mu \nu}$ and the Minkowski tensor $\eta_{a b}$, respectively.

Recall that under a change of coordinates $x\to x'(x)$, the metric
transforms according to

$g_{\mu \nu}(x)\to g_{\mu \nu}^{\prime}\left(x'\right)=\frac{\partial x^{\rho}}{\partial x'^{\mu}}\frac{\partial x^{\sigma}}{\partial
x'^{\nu}}g_{\rho \sigma}(x)$

but $\eta_{a b}$ does *not* change. Thus, using
$g_{\mu \nu}=\eta_{a b}e_{\mu}^ae_{\nu}^b$, we find that

$e_{\mu}^a(x)\to e_{\mu}^{\prime  a}\left(x'\right)=\frac{\partial x^{\nu}}{\partial x'^{\mu}}e_{\nu}^a(x)$

#### Math Appendix: Dirac $\delta$-Function on the Complex Plane

$\delta (x,y)=\frac{1}{\pi}\partial_{\bar{z}}\left(\frac{1}{z}\right)=\frac{1}{\pi}\partial_z\left(\frac{1}{\bar{z}}\right)$

Here $z\equiv x+i y, \bar{z}\equiv x-i y$

*Proof*:

#### Ward Identities for Translation, Rotation and Scale Invariance

$\langle T(z)X\rangle =\sum_{i=1}^n \left\{\frac{h_i}{\left(z-w_i\right)^2}\langle X\rangle +\frac{1}{z-w_i}\partial_{w_i}\langle X\rangle \right\}+\text{reg}.$

A similar result hold for the anti-holomorphic part.

#### Unified Ward Identity

The three Ward Identity above can be combined into a single equation.
Given an arbitrary conformal coordinates change
$x^{\nu}\to x^{\nu}+\epsilon
^{\nu}(x)$, we get

$\partial_{\mu}\left(\epsilon_{\nu}T^{\mu \nu}\right)=\epsilon_{\nu}\partial_{\mu}T^{\mu \nu}+\left(\partial_{\mu}\epsilon_{\nu}\right)T^{\mu
 \nu}$

To exploit the properties of conformal transformations

$\frac{1}{2}\left(\partial_{\mu}\epsilon_{\nu}+\partial_{\nu}\epsilon_{\mu}\right)=\frac{1}{2}\left(\partial_{\rho}\epsilon^{\rho}\right)\eta
_{\mu \nu}$

$\frac{1}{2}\left(\partial_{\mu}\epsilon_{\nu}-\partial_{\nu}\epsilon_{\mu}\right)=\frac{1}{2}\epsilon^{\alpha  \beta}\partial_{\alpha
}\epsilon_{\beta}\epsilon_{\mu \nu}$

(here $\frac{1}{2}\partial_{\rho}\epsilon^{\rho}$ is the local scale
factor $f(x)$, and
$\frac{1}{2}\epsilon^{\alpha  \beta}\partial_{\alpha
}\epsilon_{\beta}$ is the local rotation angle) we rewrite the second
term

$\partial_{\mu}\left(\epsilon_{\nu}T^{\mu \nu}\right)=\epsilon_{\nu}\partial_{\mu}T^{\mu \nu}+\frac{1}{2}\left(\partial_{\mu}\epsilon
_{\nu}+\partial_{\nu}\epsilon_{\mu}\right)T^{\mu \nu}+\frac{1}{2}\left(\partial_{\mu}\epsilon_{\nu}-\partial_{\nu}\epsilon_{\mu}\right)T^{\mu
 \nu}\\
=\epsilon_{\nu}\partial_{\mu}T^{\mu \nu}+\frac{1}{2}\left(\partial_{\rho}\epsilon^{\rho}\right)\eta_{\mu \nu}T^{\mu \nu}+\frac{1}{2}\epsilon
^{\alpha  \beta}\partial_{\alpha}\epsilon_{\beta}\epsilon_{\mu \nu}T^{\mu \nu}$

$\delta_{\epsilon ,\bar{\epsilon}}\langle X\rangle =-\frac{1}{2\pi  i}\oint_Cdz \epsilon (z)\langle T(z)X\rangle +\frac{1}{2\pi  i}\oint_Cd\bar{z}
\bar{\epsilon}\left(\bar{z}\right)\left\langle \bar{T}\left(\bar{z}\right)X\right\rangle$

The counter-clockwise contour $C$ needs to include all the positions
$\left(w_i,\bar{w}_i\right)$ of the fields contained in $X$.