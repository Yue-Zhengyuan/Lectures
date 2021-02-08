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

# The Conformal Group in 2D

## Conformal Transformations in 2D and Complexification

The case $d = 2$ is so special that we can directly find what the *finite* conformal transformations look like. Consider a map $(x^0,x^1) \mapsto (w^0,w^1)$. The metric transforms according to

$$
\begin{aligned}
    \eta_{\alpha \beta}
    &= \frac{\partial w^\alpha}{\partial x^\mu}
    \frac{\partial w^\beta}{\partial x^\nu}
    g'_{\mu \nu}(w)
    \\
    &= \frac{\partial w^\alpha}{\partial x^\mu}
    \frac{\partial w^\beta}{\partial x^\nu}
    \Lambda(w) \eta_{\mu \nu}
\end{aligned}
$$

Writing down each component explicitly (in Euclidean space $\R^{2,0}$), we obtain:

$$
\begin{aligned}
    \frac{\partial w^0}{\partial x^0}
    \frac{\partial w^1}{\partial x^0}
    + \frac{\partial w^0}{\partial x^1}
    \frac{\partial w^1}{\partial x^1} &= 0
    \\
    \left( \frac{\partial w^0}{\partial x^0} \right)^2
    + \left( \frac{\partial w^0}{\partial x^1} \right)^2
    &= \Lambda(w)
    \\
    \left( \frac{\partial w^1}{\partial x^0} \right)^2
    + \left( \frac{\partial w^1}{\partial x^1} \right)^2
    &= \Lambda(w)
\end{aligned}
$$

These conditions are equivalent to either ($\partial_\alpha$ means $\partial/\partial x^\alpha$)

$$
\partial_0 w^0 = \partial_1 w^1, \quad
\partial_0 w^1 = -\partial_1 w^0
\tag{Holo.}
$$

or

$$
\partial_0 w^0 = -\partial_1 w^1, \quad
\partial_0 w^1 = \partial_1 w^0
\tag{Anti-holo.}
$$

The first set is the same as the **Cauchy-Riemann relations**, which implies that $w^0$ and $w^1$ are the real and the imaginary parts of a differentiable complex function (**holomorphic function**)

$$
w(z) = w^0(x^0, x^1) + i w^1(x^0, x^1), \quad
z \equiv x^0 + ix^1
$$

The second set is the Cauchy-Riemann relations for **anti-holomorphic functions**, which means that we can combine $w^0, w^1$ into

$$
\bar{w}(\bar{z}) = w^0(x^0, x^1) - i w^1(x^0, x^1), \quad
z \equiv x^0 - ix^1
$$

Now we have arrived at the conclusion:

<div class="result">
<center>

**The conformal group in 2D is the set of all analytic maps, <br>with map composition as group multiplication.**

</center>
</div><br>

<div class="remark">

*Remark*: For Minkowski space $\R^{1,1}$ things are slightly more complicated. We need to first perform the **Wick rotation** to change the metric back to that of $\R^{2,0}$:

$$
x^0 \mapsto \tilde{x}^0 = ix^0
$$

This choice makes the time evolution $e^{-iHx^0}$ become a decaying exponential $e^{-H \tilde{x}^0}$. Then after solving the problem in Euclidean space, we perform *analytical continuation* of the results, and set $x^0$ to be an imaginary number to recover physics in $R^{1,1}$. 

In the following, we always use the Euclidean space unless otherwise stated.

</div><br>

We also introduce the derivatives with respect to $z, \bar{z}$: using the inverse relations

$$
x^0 = \frac{1}{2}(z+\bar{z}),
\quad
x^1 = -\frac{i}{2}(z-\bar{z})
$$

we obtain

$$
\begin{aligned}
    \partial \equiv \partial_z
    &= \frac{\partial x^{\rho}}{\partial z}
    \frac{\partial}{\partial x^{\rho}}
    = \frac{1}{2} (\partial_0 - i\partial_1 ),
    \\
    \bar{\partial} \equiv \partial_{\bar{z}}
    &= \frac{\partial x^{\rho}}{\partial \bar{z}}
    \frac{\partial}{\partial x^{\rho}}
    = \frac{1}{2} (\partial_0 + i \partial_1 )
\end{aligned}
$$

which can also be inverted to give

$$
\partial_0 = \partial_z + \partial_{\bar{z}}, \quad
\partial_1 = i(\partial_z - \partial_{\bar{z}})
$$

Then one can verify that

$$
\partial \bar{w} = 0, \quad
\bar{\partial} w = 0
$$

i.e. $\bar{w}$ only depend on $\bar{z}$, and $w$ only depend on $z$.

<div class="remark">

*Remark*: The two variables $z, \bar{z}$ (and the two transformations $w, \bar{w}$) are usually regarded as *independent of each other*. This means that we even *treat $x^0, x^1$ as complex variables* (by analytic continuation); then the above definition is merely a change of complex variables. To go back to the physical space, simply impose the reality condition at the last stage. 

</div><br>

## Transformation Generators and Witt Algebra

The infinitesimal version of 2D conformal transformations must have the form

$$
w(z) = z + \epsilon(z), \quad
\bar{w}(\bar{z}) = \bar{z} + \bar{\epsilon}(\bar{z})
$$

The generators of 2D infinitesimal conformal transformation are found from the *Laurent expansion* (about the $z, \bar{z} = 0$) of $\epsilon (z)$ and $\bar{\epsilon}(\bar{z})$:

$$
\begin{aligned}
    \epsilon (z) &= \sum_n z^{n+1} \epsilon_n
    \\
    \bar{\epsilon}(\bar{z}) &= \sum_n \bar{z}^{n+1} \bar{\epsilon}_n
\end{aligned}
$$

We define the differential operators

<div class="result">

**Conformal transformation generators in the complex plane:**

$$
l_n \equiv -z^{n+1} \partial_z, \quad
\bar{l}_n=-\bar{z}^{n+1}\partial_{\bar{z}}
$$

</div><br>

Then for the transformation of a particular $n$, we have

$$
\begin{aligned}
    z' &= z + z^{n+1} \epsilon_n
    \equiv \left(1-l_n\right)z
    \\
    \bar{z}'
    &= \bar{z} + \bar{z}^{n+1} \bar{\epsilon}_n
    = (1 - \bar{l}_n) \bar{z}
\end{aligned}
$$

so that a finite transformation is the exponentiation $e^{-l_n}, e^{-\bar{l}_n}$.

The commutation rules of the generators $l_n,\bar{l}_n$ are collectively known as

<div class="result">

**The Witt algebra:**

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

</div><br>

<div class="remark">

*Remark*: 

- The algebra of $l_n$ and $\bar{l}_n$ are completely separated. 

- The number of independent infinitesimal conformal transformations is *infinite*. This is *special to 2D*.

</div><br>

## The Global Subgroup

We notice that the generators $l_n, \bar{l}_n$ are not everywhere well-defined; things will go wrong at $z = 0$ and $z = \infty$. One usually goes to the *Riemann sphere* $\C \cup \{\infty\}$ to include the point of infinity. 

Let us first examine $l_n$:

$$
z \to 0: \quad
l_n = -z^{n+1} \partial_z \quad
\text{non-singular for} \, n \ge -1
$$

At $z=\infty$, we introduce $w = 1/z$ (then $\partial_z = -w^2 \partial_w$) and let $w\to 0$:

$$
w \to 0: \quad
l_n = w^{-n+1} \partial_w \quad
\text{non-singular for} \, n \le 1
$$

Thus only $l_{-1}, l_0, l_1$ (and similarly $\bar{l}_{-1}, \bar{l}_0, \bar{l}_1$) are *globally* defined generators. Let us examine what kind of transformations they generate (in the complex plane).

- $l_{-1}$ generates the **translation**
    
    $$
    z' = z + \epsilon_{-1}
    \xrightarrow{\text{finite}}
    z' = z + b
    $$

- $l_0$ generates the following transformation

    $$
    z' = z + \epsilon_0 z
    \xrightarrow{\text{finite}}
    z' = az \quad (a \in \C)
    $$

    which is a combination of scaling (by $|a|$) and rotation (by $\operatorname{Arg} a$). To separate the two, we go to the polar coordinates 

    $$
    \left.
    \begin{aligned}
        z &= re^{i\phi} \\
        \bar{z} &= re^{-i\phi}
    \end{aligned} \right\}
    \Rightarrow \left\{
    \begin{aligned}
        r &= \sqrt{z \bar{z}}\\
        \phi &= \frac{1}{2i} \ln \frac{z}{\bar{z}}
    \end{aligned}
    \right.
    $$

    Then the $l_0$ generator can be expressed as

    $$
    \begin{aligned}
        l_0 &= -z \partial_z
        \\
        &= - z \left(
            \frac{\partial r}{\partial z} \partial_r
            + \frac{\partial \phi}{\partial z} \partial_\phi
        \right)
        \\
        &= -\frac{1}{2} r \partial_r + \frac{i}{2} \partial_\phi 
    \end{aligned}
    $$

    Similarly

    $$
    \bar{l}_0 = -\frac{1}{2} r \partial_r 
    - \frac{i}{2} \partial_\phi
    $$

    Then we recognize that

    $$
    \begin{aligned}
        \text{Scaling: } &\quad &
        l_0 + \bar{l}_0 &= -r \partial_r
        \\
        \text{Rotation: } &\quad &
            i(l_0 - \bar{l}_0) &= - \partial_\phi
        \end{aligned}
    $$

- $l_1$ generates the following transformation

    $$
    z' = z + \epsilon_1 z^2
    \xrightarrow{\text{finite}}
    z' = \frac{z}{cz + 1}
    $$

    which is a special case of the **SCT**. 

The combination of the above transformations has the general form

<div class="result">

**Global conformal transformations in 2D**:

$$
f(z)=\frac{a z+b}{c z+d} 
\quad \left(
    a,b,c,d \in \mathbb{C} \, ;
    \,
    ad - bc \ne 0
\right)
$$

(There is another similar one for $\bar{z}$.)

</div><br>

Usually we require $ad - bc = 1$, which is just a normalization. We observe that

- If we compose two such transformations $f_2 \circ f_1$, the new coefficients $A,B,C,D$ for the composition are obtained via matrix multiplication
    
    $$
    \begin{pmatrix}
        A & B \\
        C & D
    \end{pmatrix} = \begin{pmatrix}
        a_2 & b_2 \\ c_2 & d_2
    \end{pmatrix} \begin{pmatrix}
        a_1 & b_1 \\ c_1 & d_1
    \end{pmatrix}
    $$

- The mapping $f$ is invariant under $(a,b,c,d) \mapsto (-a,-b,-c,-d)$

Therefore

<div class="result">
<center>

**The global conformal group in 2D is <br> isomorphic to $SL(2,\C) / \Z_2$.**

</center>
</div><br>

## Conformal Generators in 2D

Here we re-express the conformal generators $P_\mu, D, L_{\mu \nu}, K_\mu$ using the $l_n, \bar{l}_n \, (n = -1,0,1)$ operators in 2D (Euclidean $\R^{2,0}$). To do this, we shall use the conversion

$$
\begin{aligned}
    x_0 &= \frac{1}{2} (z+\bar{z}),
    &\quad
    x_1 &= -\frac{i}{2} (z-\bar{z})
    \\[1em]
    \partial_0 &= \partial + \bar{\partial}, 
    &\quad
    \partial_1 &= i(\partial - \bar{\partial})
\end{aligned}
$$

Note that in Euclidean space, the variables with upper indices are the same as those with lower indices.

- Translation
    
    $$
    \begin{aligned}
        P_0 &= -i \partial_0
        = -i (\partial + \bar{\partial})
        \\ &= i (l_{-1} + \bar{l}_{-1})
        \\
        P_1 &= -i \partial_1
        = \partial - \bar{\partial}
        \\ &= -l_{-1} + \bar{l}_{-1}
    \end{aligned}
    $$

- Scaling (dilation)
    
    $$
    \begin{aligned}
        D &= -i (x_0 \partial_0 + x_1 \partial_1)
        \\
        &= -\frac{i}{2} [
            (z + \bar{z})(\partial + \bar{\partial})
            + (z - \bar{z})(\partial - \bar{\partial})
        ]
        \\
        &= -i (z\partial + \bar{z} \bar{\partial})
        = i(l_0 + \bar{l}_0)
    \end{aligned}
    $$

- Rotation
    
    $$
    \begin{aligned}
        L_{10} &= i (x_1 \partial_0 - x_0 \partial_1)
        \\
        &= \frac{1}{2} (
            (z - \bar{z})(\partial + \bar{\partial})
            + (z + \bar{z})(\partial - \bar{\partial})
        )
        \\
        &= z\partial - \bar{z} \bar{\partial}
        = -l_0 + \bar{l}_0
    \end{aligned}
    $$

- SCT
    
    Let us first calculate:

    $$
    \begin{aligned}
        x^{\nu}\partial_{\nu}
        &= x_0 \partial_0 + x_1 \partial_1
        \\
        &= \frac{1}{2} (z+\bar{z})(\partial + \bar{\partial})
        + \frac{1}{2} (z-\bar{z})(\partial - \bar{\partial})
        \\
        &= z\partial + \bar{z} \bar{\partial}
        \\
        x^2 &\equiv x^{\nu} x_{\nu}
        \\
        &= (x_0)^2 + (x_1)^2
        \\
        &= \frac{1}{4} (z+\bar{z})^2
        - \frac{1}{4} (z-\bar{z})^2
        \\
        &= z \bar{z}
    \end{aligned}
    $$

    Then
    
    $$
    \begin{aligned}
        K_0 &= -i (
            2x_0 x^{\nu}\partial_{\nu}
            - x^2 \partial_0
        ) \\
        &= -i[
            (z + \bar{z})(z\partial + \bar{z} \bar{\partial})
            - z \bar{z} (\partial + \bar{\partial})
        ]
        \\
        &= -i(z^2\partial + \bar{z}^2 \bar{\partial})
        = i (l_1 + \bar{l}_1)
        \\
        K_1 &= -i (
            2x_1 x^{\nu}\partial_{\nu}
            - x^2 \partial_1
        ) \\
        &= - (z - \bar{z})(z\partial + \bar{z} \bar{\partial})
        - z \bar{z} (\partial - \bar{\partial})
        \\
        &= -z^2 \partial + \bar{z}^2 \bar{\partial}
        = l_1 - \bar{l}_1
    \end{aligned}
    $$
