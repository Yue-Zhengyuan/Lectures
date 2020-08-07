## Continuous Symmetry Transformations

### Continuous Symmetry

Our physical system is described by the following action depending on the fields and the *first-order* derivative of them:

$$
S=\int d^dx \mathcal{L}(\phi (x),\partial \phi (x))
$$

Now suppose we *move* the system to a new position (the amount of moving can be different for different parts) so that things originally at $x$ is now at $x'$ (*active view*). 

This is *not* due to change of the coordinate system (*passive view*). We can always put the change of
position in the form

$$
x\to x'(x)=x+\epsilon (x)
$$

Although we use the letter $\epsilon$, it is not necessarily a small quantity (nevertheless we shall soon make it so). 

At the same time, *the field will also be affected*: the new field at the new position $\phi' \left(x'\right)$ is some functional $\mathcal{F}$ of the old field at the old position $\phi (x)$

$$
\phi (x)\to \phi' \left(x'(x)\right)=\mathcal{F}(\phi (x))
$$

<center>

![image](Fig-2_1.png)   
*Transformation of field*

</center>



### Correlation Functions and Ward Identity

The is defined by the "mean value" of a product of the field at different places

$$
\langle 
    \phi \left(x_1\right) \cdots  \phi \left(x_n\right)
\rangle 
=\frac{1}{Z} \int [d\phi] \,
\phi(x_1) \cdots \phi(x_n)
\exp (-S[\phi])
$$

Here $Z$ is the "vacuum" functional

$$
Z=\int [d\phi] \exp (-S[\phi])
$$

If the system is symmetric under some transformation, *the correlation function at the same place should be invariant*:

$$
\begin{aligned}
    \langle
        \phi \left(x_1^{\prime} \right) \cdots  \phi \left(x_n^{\prime} \right)
    \rangle 
    &= \langle 
        \phi'(x_1^{\prime}) \cdots  \phi'(x_n^{\prime})
    \rangle 
    \\
    &=\langle 
        \mathcal{F}(\phi(x_1)) \cdots  \mathcal{F}(\phi(x_n))
    \rangle
\end{aligned}
$$

Now we use a single letter $X$ to represent the expression
$\phi(x_1) \cdots  \phi(x_n)$. Then

$$
\langle X' \rangle =\langle X \rangle
$$

We also assume that *the integration measure is invariant* under the
local transformation described by the parameters $\omega_a(x)$:

$$
[d\phi] = [d\phi']
$$

The new correlation is

$$
\begin{aligned}
    \left\langle X'\right\rangle 
    &= \frac{1}{Z} \int \left[d\phi' \right] 
    X'\exp \left(-S'\left[\phi' \right]\right)
    \\
    &= \frac{1}{Z} \int [d\phi] \,
    X'\exp \left(-S'\left[\phi
    '\right]\right)
    \\
    &= \frac{1}{Z} \int [d\phi]
    (X+\delta  X)
    \exp \left(
        -S[\phi]-\int d^dx \omega_a(x)\partial_{\mu}j_a^{\mu} 
    \right)
    \\
    &\simeq \frac{1}{Z} \int [d\phi](X+\delta  X)
    \exp (-S[\phi]) \left(
        1 - \int d^dx \omega_a(x)\partial_{\mu}j_a^{\mu} 
    \right)
    \\
    &\simeq \langle X \rangle 
    + \langle \delta X \rangle 
    \\ &\qquad
    - \frac{1}{Z} \int [d\phi] \, X 
    \exp (-S[\phi]) \left(
        \int d^dx \omega_a(x)\partial_{\mu}j_a^{\mu} 
    \right)
\end{aligned}
$$

Then, because $\left\langle X'\right\rangle =\langle X\rangle$

$$
\begin{aligned}
    \langle \delta  X\rangle 
    &=\frac{1}{Z} \int [d\phi]X \exp (-S[\phi])\left(\int d^dx \omega_a(x)\partial_{\mu}j_a^{\mu} \right)
    \\
    &=\frac{1}{Z} \int d^dx \,
    \omega_a(x)\int [d\phi]X\partial_{\mu}j_a^{\mu} \exp (-S[\phi])
    \\
    &=\int d^dx \, \omega_a(x) \,
    \partial_{\mu} \left(\frac{1}{Z} \int [d\phi]X j_a^{\mu} \exp (-S[\phi])\right)
    \\
    &=\int d^dx \, \omega_a(x) \, 
    \partial_{\mu} \left\langle
    X j_a^{\mu} \right\rangle
\end{aligned}
$$

Meanwhile, we can directly write down the $\langle \delta  X\rangle$ using the generators

$$
\begin{aligned}
    \delta  X
    &=\sum_{k=1}^n \phi \left(x_1\right) \cdots  
    \left(-i G_a\omega_a\left(x_k\right)\phi \left(x_k\right)\right) 
    \cdots \phi \left(x_n\right)
    \\
    &= -i\int d^dx \, 
    \delta^{(d)} (x - x_k)\,
    \omega_a(x)
    \sum_{k=1}^n \left[\phi \left(x_1\right) \cdots  \left(G_a\phi \left(x_k\right)\right) \cdots  \phi \left(x_n\right)\right]
\end{aligned}
$$

Now we obtain the so-called **Ward identity**

$$
\begin{aligned}
    &\partial_{\mu} \left\langle j_a^{\mu} \phi \left(x_1\right) \cdots  \phi \left(x_n\right)\right\rangle 
    \\
    &= -i\int d^dx \sum_{k=1}^n 
    \delta^{(d)} \left(x-x_k\right)\left\langle
    \phi \left(x_1\right) \cdots 
    \left(G_a\phi \left(x_k\right)\right) 
    \cdots \phi \left(x_n\right)\right\rangle
\end{aligned}
$$

### Ward Identity for Translation


### Conserved Charge as Transformation Generators

Recall the definition of the conserved charge associated with
$\omega_a$

$$
Q_a(x^0)=\int d^{d-1}x \, j_a^0
$$

Let 

$$
Y=\phi \left(x_2\right) \cdots  \phi \left(x_n\right)
$$ 

Note that it does not include the field at $x_1$, distinguishing it from the quantity $X$. 

Then we integrate both sides of the Ward identity with
respect to $x_1$, in a volume bounded by two surfaces $x_1^0=t_{\pm}$:

$$
\text{LHS}=\int_{t_-}^{t_+}dx_1^0\int d^{d-1}x_1\partial_{\mu} \left\langle j_a^{\mu} \phi \left(x_1\right)Y\right\rangle
$$

This can be converted (by Gauss' Theorem) to an integral on the two boundary surfaces :

$$
\text{LHS}=\left\langle Q_a\left(t_+\right)\phi \left(x_1\right)Y\right\rangle -\left\langle Q_a\left(t_-\right)\phi \left(x_1\right)Y\right\rangle
$$
