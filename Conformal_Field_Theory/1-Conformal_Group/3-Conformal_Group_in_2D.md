# The Conformal Group in 2D

## Conformal Mappings

Apply the general constraint on conformal transformation

$$
\partial_{\mu}\epsilon_{\nu}(x) 
+ \partial_{\nu}\epsilon_{\mu}(x)
= \frac{2}{d} 
(\partial_{\rho} \epsilon^{\rho}(x))
\eta_{\mu \nu}
$$

to the $d=2$ case, we find

$$
\partial_0\epsilon_0 = \partial_1\epsilon_1, \quad
\partial_0\epsilon_1 = -\partial_1\epsilon_0
$$

which is the same as the **Cauchy-Riemann relations** between the real and the imaginary parts of a *holomorphic function* in complex analysis. Then it is useful to construct the **holomorphic coordinates** from the Euclidean coordinates $x^0,x^1$:

$$
z=x^0+i x^1, \quad \bar{z}=x^0-i x^1
$$

$$
\epsilon =\epsilon^0+i \epsilon^1, 
\quad
\bar{\epsilon}=\epsilon^0-i \epsilon^1
$$

The two variables in a pair are to be regarded as *independent of each other*.

Now we can conclude that:

*A holomorphic function $f(z)=z+\epsilon (z)$ gives an infinitesimal 2D conformal transformation* $z\to f(z)$.

## Differentiation and Integration in Holomorphic Coordinates

The inverse relations are

$$
x^0 = \frac{1}{2}\left(z+\bar{z}\right),
\quad
x^1 = -\frac{i}{2}\left(z-\bar{z}\right)
$$

We also define the derivatives

$$
\begin{aligned}
    \partial \equiv \partial_z
    &= \frac{\partial x^{\rho}}{\partial z}
    \frac{\partial}{\partial x^{\rho}}
    =\frac{1}{2} (\partial_0 - i\partial_1 ),
    \\
    \bar{\partial} \equiv \partial_{\bar{z}}
    &= \frac{\partial x^{\rho}}{\partial \bar{z}}
    \frac{\partial}{\partial x^{\rho}}
    =\frac{1}{2} (\partial_0 + i \partial_1 )
\end{aligned}
$$

### Jacobian

$$
\begin{aligned}
    \frac{D(z,\bar{z})}{D(x^0,x^1)}
    &= \det 
    \begin{pmatrix}
        \partial z / \partial x^0 & \partial z / \partial x^1 \\
        \partial \bar{z}/\partial x^0 & \partial \bar{z}/\partial x^1
    \end{pmatrix}
    \\
    &= \det 
    \begin{pmatrix}
        1 & i \\
        1 & -i \\
    \end{pmatrix}
    = -2i
\end{aligned}
$$

Therefore

$$ 
dz \, d\bar{z} = -2i \, dx^0 dx^1
$$

### Laplacian

In particular, the Laplacian $\partial_{\rho}\partial^{\rho}$
becomes $\partial \bar{\partial}$, since

$$
\begin{aligned}
    \partial \bar{\partial}\phi 
    &= \frac{\partial x^{\rho}}{\partial z}
    \frac{\partial}{\partial x^{\rho}} \left(
        \frac{\partial x^{\sigma}}{\partial\bar{z}}
        \frac{\partial \phi}{\partial x^{\sigma}}
    \right)
    \\
    &= \frac{\partial x^{\rho}}{\partial z}
    \left(
        \frac{\partial}{\partial x^{\rho}}
        \frac{\partial x^{\sigma}}{\partial \bar{z}}
    \right)
    \frac{\partial \phi}{\partial x^{\sigma}}
    +
    \frac{\partial x^{\rho}}{\partial z}
    \frac{\partial x^{\sigma}}{\partial\bar{z}}
    \left(
        \frac{\partial}{\partial x^{\rho}}
        \frac{\partial \phi}{\partial x^{\sigma}}
    \right)
    \\
    &=\frac{\partial x^{\rho}}{\partial z}
    \underbrace{\frac{\partial \delta_{\rho}^{\sigma}}{\partial \bar{z}}}_0
    \frac{\partial \phi}{\partial x^{\sigma}}
    +
\end{aligned}
$$

## The Metric Tensor

The *flat* metric in the holomorphic coordinates becomes

$$
\begin{aligned}
    \eta'_{\mu \nu} 
    &= \begin{pmatrix}
        \eta_{z z} & \eta_{z \bar{z}} \\
        \eta_{\bar{z} z} & \eta_{\bar{z} \bar{z}}
    \end{pmatrix}
    \\
    &= \eta_{\rho \sigma} 
    \frac{\partial x^\rho}{\partial z^\mu}
    \frac{\partial x^\sigma}{\partial z^\nu}
    = \begin{pmatrix}
        0 & 1/2 \\
        1/2 & 0
    \end{pmatrix}
\end{aligned}
$$

Here $z^0=z, z^1=\bar{z}$. For example:

$$
\begin{aligned}
    \eta_{z \bar{z}}
    &= \eta_{\rho \sigma}
    \frac{\partial x^\rho}{\partial z}
    \frac{\partial x^\sigma}{\partial \bar{z}}
    \\
    &= \frac{\partial x^0}{\partial z}\frac{\partial x^0}{\partial
    \bar{z}}+\frac{\partial x^1}{\partial z}\frac{\partial x^1}{\partial \bar{z}}
    \\
    &=\frac{1}{2}\times \frac{1}{2}+\frac{-i}{2}\times \frac{i}{2}=\frac{1}{2}
\end{aligned}
$$

The inverse of the metric is then

$$
\eta'^{\mu \nu}
= (\eta'_{\mu \nu})^{-1}
= \begin{pmatrix}
    0 & 2 \\
    2 & 0
\end{pmatrix}
$$

## Global Conformal Transformations

The set of all *global* conformal transformations (everywhere well-defined) consists of mappings of the form

$$
f(z)=\frac{a z+b}{c z+d} 
\quad \left(
    a,b,c,d \in \mathbb{C} \, ;
    \,
    \det \begin{pmatrix}
        a & b \\
        c & d 
    \end{pmatrix} =1
\right)
$$

They are called **projective transformations**. The requirement $ad - bc = 1$ is just a normalization. 

----

*Proof of the form*:

----

Assigning the matrix 

$$
A = \begin{pmatrix}
    a & b \\
    c & d
\end{pmatrix}
$$

to the mapping, we can verify that the composition of two projective transformations $f_2 \circ f_1$ corresponds to the matrix $A_2 A_1$. 

Therefore, the **global conformal group** in 2D is *isomorphic* to the group $SL(2,\mathbb{C})$, the group of *complex invertible $2 \times 2$ matrices with unit determinant*.


## Generators of Conformal Transformation

The generators of (global or local) 2D conformal transformation can be found from the Laurent expansion (about the origin) of the mapping $z\to z+\epsilon (z)$: mathematically, we write

$$
z'= z + \sum_n \epsilon_n z^n
$$

However, in CFT, people adopt the convention

$$
z'=z+\sum_n  z^{n+1} \epsilon_n
$$

Then, for the transformation of a particular $n$, we have

$$
z' = z + z^{n+1} \epsilon_n
\equiv \left(1-l_n\right)z
$$

where $l_n$ is defined as the differential operator

$$
l_n \equiv -z^{n+1} \partial_z
$$

so that a finite transformation is the exponentiation $e^{-l_n}$. Thus $l_n$ is interpreted as a transformation **generator**.

Similarly, for the anti-holomorphic part, people write

$$
\bar{z}'
= \bar{z}+\sum_n  \bar{z}^{n+1} \bar{\epsilon}_n
= \left(1 - \sum_n \bar{l}_n\right) \bar{z}
$$

with

$$
\bar{l}_n=-\bar{z}^{n+1}\partial_{\bar{z}}
$$

The commutation rules of the generators $l_n,\bar{l}_n$ are

$$
\begin{aligned}
    [l_n, l_m] &= (n-m)l_{m+n}
    \\
    [\bar{l}_n, \bar{l}_m]
    &= (n-m)\bar{l}_{m+n}
    \\
    [l_n, \bar{l}_m] &= 0
\end{aligned}
$$

called the **Witt algebra**.
