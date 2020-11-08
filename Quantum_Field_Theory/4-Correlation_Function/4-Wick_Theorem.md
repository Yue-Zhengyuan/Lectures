# Wick's Theorem

## Normal Ordering

The **normal ordering** of a product of $a_\bold{p}, a_\bold{p}^\dagger$ (free field annihilation/creation operators) put all the $a_\bold{p}$'s to the right of $a^\dagger_\bold{p}$. For example,

$$
N[a_\bold{p} a^\dagger_\bold{k} a_\bold{q}]
= a^\dagger_\bold{k} a_\bold{p} a_\bold{q}
$$

The order within the $a_\bold{p}$'s (or the $a^\dagger_\bold{p}$) is irrelevant, since they *commute*:

$$
[a_\bold{p}, a_\bold{q}] 
= [a_\bold{p}^\dagger, a_\bold{q}^\dagger] = 0
$$

One notable property of normal ordered products is that *their vacuum expectation values vanish*, since there is either nothing to be annihilated first, or there is nothing is the final vacuum state to be created. 

## Contraction of Field Operators

To evaluate the time-ordered product of the interaction picture fields (we drop the subscript $I$ for convenience)

$$
\langle 0 | T[\phi(x_1) \cdots \phi(x_n)] |0\rangle
$$

we expand the fields using the annihilation and creation operators (these operators are free, since $\phi$ are time-evolved by the free part of Hamiltonian)

$$
\begin{aligned}
    \phi(x) 
    &= \phi^+(x) + \phi^-(x)
    \\[1em]
    \text{with} \quad
    \phi^+(x) &= \int \frac{d^3 p}{(2\pi)^3} 
    \frac{1}{\sqrt{2 E_\bold{p}}}
    a_\bold{p} e^{-ipx} 
    \\
    \phi^-(x) &= \int \frac{d^3 p}{(2\pi)^3} 
    \frac{1}{\sqrt{2 E_\bold{p}}}
    a_\bold{p}^\dagger e^{+ipx} 
\end{aligned}
$$

The $+, -$ notation might be not quite match the $a, a^\dagger$ operators, but it is the standard choice. From properties of the $a, a^\dagger$ operators, we know that

$$
\phi^+(x) |0\rangle = 0, \qquad
\langle 0 | \phi^-(x) = 0
$$

We try expressing $T[\phi(x) \phi(y)]$ using the normal-ordered product in order to simplify the vacuum expectation value (now we use $\phi_x = \phi(x)$ to save writing). The normal ordering requires us to put $\phi^-$ in front of $\phi^+$

- When $x^0 > y^0$

    $$
    \begin{aligned}
        \phi_x \phi_y
        &= (\phi_x^+ + \phi_x^-)(\phi_y^+ + \phi_y^-)
        \\
        &= \phi_x^+ \phi_y^+ + \phi_x^+ \phi_y^-
        + \phi_x^- \phi_y^+ + \phi_x^- \phi_y^-
    \end{aligned}
    $$

    The second term is not in normal order. We change it to 

    $$
    \phi_x^+ \phi_y^- = \phi_y^- \phi_x^+
    + [\phi_x^+, \phi_y^-]
    $$

- Similarly, when $x^0 < y^0$
    
    $$
    \begin{aligned}
        \phi_y \phi_x
        &= (\phi_y^+ + \phi_y^-)(\phi_x^+ + \phi_x^-)
        \\
        &= \phi_y^+ \phi_x^+ + \phi_y^+ \phi_x^-
        + \phi_y^- \phi_x^+ + \phi_y^- \phi_x^-
    \end{aligned}
    $$

    The second term is not in normal order. We change it to 

    $$
    \phi_y^+ \phi_x^- = \phi_x^- \phi_y^+
    + [\phi_y^+, \phi_x^-]
    $$

    Besides, the first and the last terms are in fact

    $$
    \phi_y^+ \phi_x^+ = \phi_x^+ \phi_y^+ \qquad
    \phi_y^- \phi_x^- = \phi_x^- \phi_y^-
    $$

    This change of order is again guaranteed by the commutators

    $$
    [a_\bold{p}, a_\bold{q}] 
    = [a_\bold{p}^\dagger, a_\bold{q}^\dagger] = 0
    $$

To summarize, we have

<center> 
<img src="Figures/contr.svg" style="background-color:white">
</center>

where we have defined the **contraction** of *two* fields $\phi_x, \phi_y$ as

<center> 
<img src="Figures/contr_def.svg" style="background-color:white">
</center>

By taking the vacuum expectation value of both sides, we discover that the contraction is exactly the *Feynman propagator*:

<center> 
<img src="Figures/contr_feyn_prop.svg" style="background-color:white">
</center>

## Wick's Theorem

**Wick's theorem** states that the time-ordered product is equal to the normal-ordered product, plus **all possible ways** of contracting pairs of fields within it:

$$
\begin{aligned}
    &T[\phi(x_1) \cdots \phi(x_n)]
    \\[0.5em]
    &= N[\phi(x_1) \cdots \phi(x_n) + \text{all possible contractions}]
\end{aligned}
$$

*Proof (by induction)*:

From now on we use $\phi_m$ to represent $\phi(x_m)$. The simplest case $n = 2$ has already been verified:

<center> 
<img src="Figures/wick_2.svg" style="background-color:white">
</center>
