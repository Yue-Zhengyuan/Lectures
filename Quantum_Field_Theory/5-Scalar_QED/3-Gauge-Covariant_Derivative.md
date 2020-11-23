# Gauge-Covariant Derivative

## Gauge-Covariant Derivative

A generic (possibly non-Abelian) **gauge transformation** is defined by a *unitary* symmetry operator 

$$
U(x)= e^{i\alpha(x)} \qquad U^\dagger = U^{-1}
$$

$\alpha(x)$ is an element of the Lie algebra associated with the Lie group of the transformations, and can be expressed in terms of the generators of the group, $\{t^a\}$, as 

$$
\alpha(x) = \sum_a \alpha_a(x) t^a
$$

----

*Example*:

The $U(1)$ group simply has the number 1 as its generator. Thus $\alpha(x)$ is just a real-valued function. 

----

The gauge transformation of the field $\phi(x)$ gives

$$ 
\begin{aligned}
    \phi(x) \rightarrow \phi'(x) 
    &= U(x) \phi(x) \equiv e^{i\alpha(x)} \phi(x)
    \\
    \phi^\dagger(x) \rightarrow \phi'^{\dagger}(x) 
    &= \phi^\dagger(x) U^\dagger (x) \equiv \phi^\dagger(x) e^{-i\alpha(x)}
\end{aligned}
$$ 

Terms like $|\phi(x)|^2$ will then be gauge invariant. 

The partial derivatives $\partial_\mu \phi$ transforms, accordingly, as

$$
\begin{aligned}
    \partial_\mu \phi(x)
    \rightarrow \partial_\mu \phi'(x) 
    &= U(x) \partial_\mu \phi(x) + (\partial_\mu U) \phi(x)
    \\
    &\equiv e^{i\alpha(x)} \partial_\mu \phi(x) + i (\partial_\mu \alpha) e^{i\alpha(x)} \phi(x) 
\end{aligned}
$$

and a kinetic term of the form $\phi^\dagger \partial_\mu \phi$ is thus not invariant under this transformation.

We can introduce the **gauge-covariant derivative** $D_\mu$ in this context as a generalization of the partial derivative $\partial_\mu$ which transforms covariantly under the Gauge transformation, i.e. an object satisfying

$$
D_\mu \phi(x) \rightarrow D'_\mu \phi'(x) = U(x) D_\mu \phi(x)
$$

The transformed $D'_\mu$ can be expressed as

$$
\begin{aligned}
    D'_\mu \phi'(x) 
    &= D'_\mu U(x) \phi(x) = U(x) D_\mu \phi(x)
    \\[0.5em] \Rightarrow \, \,
    D'_\mu &= U(x) D_\mu U^\dagger(x)
\end{aligned}
$$

Let

$$
D_\mu \rightarrow D'_\mu \equiv D_\mu + \delta D_\mu
$$

We thus compute (omitting the explicit $x$ dependencies for brevity)

$$
\begin{aligned}
    D_\mu \phi \rightarrow D'_\mu \phi'
    &= D'_\mu U \phi 
    \\
    &= D_\mu U \phi + \delta D_\mu U \phi
    \\
    &= UD_\mu \phi + (\delta D_\mu U + [D_\mu,U])\phi
\end{aligned}
$$

The requirement for $D_\mu$ to transform covariantly is now translated in the condition

$$ 
(\delta D_\mu U + [D_\mu,U])\phi = 0
$$

To obtain an explicit expression, we make the Ansatz

$$
D_\mu = \partial_\mu - iq A_\mu
$$

where the vector field $A_\mu$ (the **gauge field**) transforms by

$$
A_\mu \rightarrow A'_\mu = A_\mu + \delta A_\mu
$$

Comparing with $D'_\mu \equiv D_\mu + \delta D_\mu$, we recognize that

$$ 
\delta D_\mu \equiv -iq \, \delta A_\mu
$$

Then the condition for covariance becomes

$$
\begin{aligned}
    \delta D_\mu U + [D_\mu,U] 
    &= -iq \, \delta A_\mu U + 
    [\partial_\mu - iq A_\mu, U]
    \\
    &= -iq \, \delta A_\mu U + [\partial_\mu, U]
    - iq [A_\mu, U]
    \\
    &= 0
\end{aligned}
$$

Therefore

$$ 
\delta A_\mu = [U,A_\mu]U^\dagger -\frac{i}{q} [\partial_\mu,U]U^\dagger 
$$

which, using $U(x) = 1 + i \alpha(x) + O(\alpha^2)$, takes the form

$$ 
\delta A_\mu 
= \frac{1}{q} ( [\partial_\mu, \alpha] - iq [A_\mu,\alpha] ) 
+ O(\alpha^2) 
= \frac{1}{q} [D_\mu, \alpha] + O(\alpha^2)
$$

----

*Example*:

For $U(1)$ gauge transformation, since $\alpha(x)$ is just an ordinary real-valued function, we have

$$
[\partial_\mu, \alpha] = \partial_\mu \alpha
\qquad
[A_\mu,\alpha] = 0
$$

Therefore

$$
\delta A_\mu = \frac{1}{q} \partial_\mu \alpha
$$

This result is in fact exact for $U(1)$ gauge transformation:

$$
\begin{aligned}
    \delta A_\mu
    &= [U,A_\mu]U^\dagger -\frac{i}{q} [\partial_\mu,U]U^\dagger
    \\
    &= \underbrace{[e^{i\alpha}, A_\mu]}_{=0} e^{-i\alpha}
    - \frac{i}{q} \underbrace{[\partial_\mu, e^{i\alpha}]}_{=i e^{i\alpha} \partial_\mu \alpha}
    e^{-i\alpha}
    \\
    &= \partial_\mu \alpha
\end{aligned}
$$

----

## The Lagrangian for Scalar QED