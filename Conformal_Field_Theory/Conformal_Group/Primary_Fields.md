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

# Primary Fields

Under the mapping from $(x,y)$ in $\R^2$ to the complex plane, a field $\phi(x^0, x^1)$ becomes $\phi(z,\bar{z})$. It will be called a **primary field** if it transforms under any (global or local) conformal transformations $z \mapsto w(z)$ according to the formula

<div class="result">

**Primary field transformation:**

$$
\phi (z, \bar{z}) 
\mapsto 
\phi' (w, \bar{w})
= \left(\frac{dw}{dz}\right)^{-h}
\left(\frac{d\bar{w}}{d\bar{z}}\right)^{-\bar{h}}
\phi(z, \bar{z})
$$

</div><br>

The numbers $h, \bar{h}$ are called the **holomorphic (left)** and **anti-holomorphic (right) conformal dimensions**, respectively. They are *not* complex conjugates of each other.

If this transformation holds only for *global* conformal transformations, then $\phi$ is called a **quasi-primary field**. 

<div class="remark">

*Remark*:

- If the complexified $\phi$ only depends on $z$, it is called a **chiral field**; if $\phi$ only depends on $\bar{z}$, it is an called **anti-chiral field**. Examples include the chiral and anti-chiral energy-momentum tensors $T(z)$ and $\bar{T}(\bar{z})$. 

- $T(z)$ is *not* a primary field, but is indeed a quasi-primary field with $(h,\bar{h}) = (2,0)$. Its transformation will be briefly presented in Part 3.

</div><br>

## Scaling Dimension and Conformal Spin

Below we consider two special cases:

1. Scaling

    A (global) scaling in the complex plane means

    $$
    \begin{align*}
        w(z) &= \lambda z \\
        \bar{w}(\bar{z}) &= \lambda \bar{z}
    \end{align*}
    \qquad \lambda \in \mathbb{R}
    $$

    Then the quasi-primary field transforms as

    $$
    \phi (z, \bar{z}) 
    \mapsto 
    \phi' (w, \bar{w})
    = \lambda^{-(h + \bar{h})}
    \phi(z, \bar{z})
    $$

    Then we define the **scaling dimension** $\Delta$ as

    $$
    \Delta = h + \bar{h}
    $$

2. Rotation

    A (global) rotation in the complex plane is done by

    $$
    \begin{align*}
        w(z) &= z e^{i \theta} \\
        \bar{w}(\bar{z}) &= \bar{z} e^{-i \theta}
    \end{align*}
    \qquad \theta \in \mathbb{R}
    $$

    Then

    $$
    \phi (z, \bar{z}) 
    \mapsto 
    \phi' (w, \bar{w})
    = e^{-i\theta(h - \bar{h})}
    \phi(z, \bar{z})
    $$
    
    We define the **conformal spin** $s$ as

    $$
    s = h - \bar{h}
    $$

The terminologies of "scaling dimension" and "spin" in fact come from the general CFT in $d\ge 2$. For example, the scaling dimension is originally defined for fields $\phi(x)$ that transforms under scaling as (the Yellow Book 2.4.1)

$$
x \mapsto x' = \lambda x, \quad
\phi(x) \mapsto \phi'(x') = \lambda^{-\Delta} \phi(x)
$$

We can generalize this transformation rule: the Jacobian of the above uniform scaling is 

$$
\det \left(
    \frac{\partial x'}{\partial x}
\right)
= \abs{
    \frac{\partial x'}{\partial x}
} = \lambda^d
$$

Thus the transformation of $\phi$ above is in fact a special case of (the Yellow Book 4.2.1)

<div class="result">

**General (spinless) primary fields in $d \ge 2$:**

$$
\phi(x') = \abs{
    \frac{\partial x'}{\partial x}
}^{-\Delta/d} \phi(x)
$$

</div><br>

This is the general definition of spinless ($s = 0$) primary fields in all $d \ge 2$, where we use the Jacobian to perform *local* scaling. Let us check that the definition of the $d = 2$ primary fields is consistent with the above general definition. 

Now we need to impose the condition that $\bar{z}, \bar{w}$ are indeed complex conjugate of $z, w$. For $s = 0$, we have $h = \bar{h} = \Delta / 2$. Differentiation of $w(z)$ is independent of the direction of $dz$, so we choose $dz = dx^0$ and obtain

$$
\frac{dw}{dz} = \frac{dw}{dx^0} 
= \frac{\partial w^0}{\partial x^0}
+ i \frac{\partial w^1}{\partial x^0}
$$

Similarly

$$
\frac{d\bar{w}}{d\bar{z}} = \frac{d\bar{w}}{dx^0} 
= \frac{\partial w^0}{\partial x^0}
- i \frac{\partial w^1}{\partial x^0}
$$

Then

$$
\frac{dw}{dz} \frac{d\bar{w}}{d\bar{z}}
= \left(\frac{\partial w^0}{\partial x^0}\right)^2
+ \left(\frac{\partial w^1}{\partial x^0}\right)^2
$$

Using the Cauchy-Riemann relations, we can put this into a nicer form:

$$
\begin{align*}
    \frac{dw}{dz} \frac{d\bar{w}}{d\bar{z}}
    &= \frac{\partial w^0}{\partial x^0}
    \frac{\partial w^1}{\partial x^1}
    - \frac{\partial w^0}{\partial x^1}
    \frac{\partial w^1}{\partial x^0}
    \\[1em]
    &= \abs{
        \frac{\partial x'}{\partial x}
    }
\end{align*}
$$

Then

$$
\phi(x') = \abs{
    \frac{\partial x'}{\partial x}
}^{-h} \phi(x)
= \abs{
    \frac{\partial x'}{\partial x}
}^{-\Delta/2} \phi(x)
$$

which is a special case ($d = 2$) of the general formula.

## Infinitesimal Conformal Transformations of Primary Fields

For the infinitesimal transformation

$$
\begin{align*}
    z &\mapsto 
    w(z)=z+\epsilon (z)
    \\
    \bar{z} &\mapsto 
    \bar{w}(\bar{z}) = \bar{z} + \bar{\epsilon}(\bar{z})
\end{align*}
$$

(note that $\epsilon (z)$ and $\bar{\epsilon}(\bar{z})$ are two *independent* transformations; we do not impose the reality condition), we have

$$
\left(\frac{dw}{dz}\right)^{-h}
= (1 + \partial_z\epsilon)^{-h}
= 1 - h \partial_z \epsilon (z)
+ O(\epsilon^2)
$$

$$
\left(\frac{d\bar{w}}{d\bar{z}}\right)^{-\bar{h}}
= (1 + \partial_{\bar{z}}\bar{\epsilon})^{-\bar{h}}
= 1 - \bar{h}\partial_{\bar{z}}\bar{\epsilon}(\bar{z})
+ O(\bar{\epsilon}^2)
$$

Then

$$
\phi' (w, \bar{w})
\simeq \left(
    1 - h\partial_z\epsilon (z)
    - \bar{h}\partial_{\bar{z}}\bar{\epsilon}(\bar{z})
\right) \phi (z, \bar{z})
$$

Meanwhile, Taylor expansion gives

$$
\phi' (z, \bar{z})
\simeq \phi' (w, \bar{w})
- \epsilon (z)\partial \phi (z, \bar{z})
- \bar{\epsilon}(\bar{z})\bar{\partial} \phi (z, \bar{z})
$$

Thus the variation of the field due to both $\epsilon$ and $\bar{\epsilon}$ is

<div class="result">

**Conformal transformation of primary fields:**

$$
\begin{align*}
    \delta_{\epsilon ,\bar{\epsilon}}\phi (z,\bar{z})
    &\equiv \phi' (z, \bar{z}) - \phi (z, \bar{z})
    \\
    &= - (
        h \phi \partial \epsilon 
        + \epsilon \partial \phi
    ) - (
        \bar{h} \phi \bar{\partial} \bar{\epsilon}
        + \bar{\epsilon} \bar{\partial} \phi
    )
\end{align*}
$$

</div><br>

