# Gauge-Covariant Derivative

Consider a generic (possibly non-Abelian) Gauge transformation, defined by a symmetry operator $U(x)= e^{i\alpha(x)}$, acting on a field $\phi(x)$, such that

$$ 
\phi(x) \rightarrow \phi'(x) = U(x) \phi(x) \equiv e^{i\alpha(x)} \phi(x)
\\
\phi^\dagger(x) \rightarrow \phi{'}^{\dagger} = \phi^\dagger(x) U^\dagger (x) \equiv \phi^\dagger(x) e^{-i\alpha(x)}, \qquad U^\dagger = U^{-1}
$$

where $\alpha(x)$ is an element of the Lie algebra associated with the Lie group of symmetry transformations, and can be expressed in terms of the generators of the group, $\{t^a\}_{a}$, as $\alpha(x) = \alpha^a(x) t^a$.

The partial derivative $\partial_\mu$ transforms, accordingly, as

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

which in operatorial form takes the form

$$
D'_\mu = U(x) D_\mu U^\dagger(x)
$$

We thus compute (omitting the explicit $x$ dependencies for brevity)

$$
D_\mu \phi \rightarrow D'_\mu U \phi = UD_\mu \phi + (\delta D_\mu U + [D_\mu,U])\phi
$$

where

$$
D_\mu \rightarrow D'_\mu \equiv D_\mu + \delta D_\mu
$$

The requirement for $D_\mu$ to transform covariantly is now translated in the condition

$$ 
(\delta D_\mu U + [D_\mu,U])\phi = 0
$$

To obtain an explicit expression, we make the Ansatz

$$
D_\mu = \partial_\mu - ig A_\mu
$$

where the vector field $A_\mu$ satisfies

$$
A_\mu \rightarrow A'_\mu = A_\mu + \delta A_\mu
$$

from which it follows that

$$ 
\delta D_\mu \equiv -ig \delta A_\mu
$$

and

$$ 
\delta A_\mu = [U,A_\mu]U^\dagger -\frac{i}{g} [\partial_\mu,U]U^\dagger 
$$

which, using $U(x) = 1 + i \alpha(x) + O(\alpha^2)$, takes the form

$$ 
\delta A_\mu = \frac{1}{g} ( [\partial_\mu, \alpha] - ig [A_\mu,\alpha] ) + O(\alpha^2) = \frac{1}{g} [D_\mu, \alpha] + O(\alpha^2)
$$

We have thus found an object $D_\mu$ such that

$$
\phi^\dagger(x) D_\mu \phi(x) \rightarrow \phi'^\dagger(x) D'_\mu \phi'(x) = \phi^\dagger(x) D_\mu \phi(x)
$$