# Boson Coherent State

## Eigenstate of Annihilation Operator

The boson **coherent state** is *defined* as the eigenstate of the (boson) annihilation operator:

$$
a |\alpha \rangle =\alpha |\alpha \rangle, 
\quad
\alpha \in \mathbb{C}
$$

A generalization is to introduce *multiple kinds* of bosons into the system. 

Let the annihilation operator of the $i$th kind of be $a_i$. Because the annihilation operators of different kinds of bosons *commute*, they have a common set of eigenstates labelled by $\alpha_1, \alpha_2, ... \in \mathbb{C}$:

$$
a_1 a_2 \cdots a_n 
|\alpha_1\alpha_2 \cdots \alpha_n\rangle 
= \alpha_1\alpha_2 \cdots \alpha_n
| \alpha_1\alpha_2 \cdots \alpha_n\rangle
$$

Its Hermitian conjugate is

$$
\langle \alpha_1\alpha_2 \cdots \alpha_n|
a_n^\dagger \cdots a_2^\dagger a_1^\dagger
=\langle \alpha_1\alpha_2 \cdots \alpha_n|
\bar{\alpha}_n \cdots \bar{\alpha}_2 \bar{\alpha}_1
$$

## Building Coherent State from Vacuum

## One Kind of Bosons

Expand the coherent state using the Fock space basis vectors (boson
number representation):

$$
\begin{aligned}
    | \alpha \rangle 
    &= \sum_{n\geq 0}  c_n| n\rangle 
    \\
    \Rightarrow 
    a| \alpha \rangle 
    &=\sum_{n\geq 0}  c_n(a| n\rangle )
    =\sum_{n\geq 1}  c_n\sqrt{n}|n-1\rangle 
    \\
    &=\sum_{n\geq 0}  c_{n+1}\sqrt{n+1}| n\rangle
\end{aligned}
$$

Meanwhile

$$
a| \alpha \rangle 
= \alpha | \alpha \rangle 
=\sum_{n\geq 0}  \alpha c_n| n\rangle
$$

Therefore,

$$
\alpha c_n = \sqrt{n+1}c_{n+1}
$$

By recursion, we find

$$
c_n = \frac{\alpha}{\sqrt{n}}c_{n-1}
= \frac{\alpha}{\sqrt{n}}\frac{\alpha}{\sqrt{n-1}}c_{n-2}
= \cdots  
= \frac{\alpha^n}{\sqrt{n!}}c_0
$$

For convenience, we set $c_0=1$. Using

$$
| n\rangle 
= \frac{a^\dagger}{\sqrt{n}}| n-1\rangle 
= \frac{a^\dagger}{\sqrt{n}}\frac{a^\dagger}{\sqrt{n-1}}| n-2\rangle 
= \cdots 
= \frac{(a^\dagger)^n}{\sqrt{n!}}| 0\rangle
$$

we obtain

$$
| \alpha \rangle 
= \sum_n  \frac{\alpha^n}{\sqrt{n!}}\frac{(a^\dagger)^n}{\sqrt{n!}}| 0\rangle 
= \sum_n  \frac{(\alpha a^\dagger)^n}{n!}| 0\rangle 
= \exp (\alpha a^\dagger)| 0\rangle
$$

Its Hermitian conjugate is

$$
\langle \alpha |
= \sum_n  \langle 0|\frac{\left(a \bar{\alpha}\right)^n}{n!}
= \sum_n  \langle 0|\frac{\left(\bar{\alpha} a\right)^n}{n!}
= \langle 0| \exp (a \bar{\alpha})
$$

## Many Kinds of Bosons

If we have many kinds of bosons, the result is

$$
| \alpha \rangle 
= \exp \left(\sum_k \alpha_k a_k^\dagger \right)| 0\rangle
$$

## Resolution of Identity

Suppose $\alpha =x+i y, \bar{\alpha}=x-i y \, (x,y\in \mathbb{R})$. We claim that

$$
\int \frac{dx dy}{\pi}e^{-(x^2+y^2)}
| \alpha \rangle \langle \alpha |
=\mathbf{1}
$$

*Proof*:

To prove the LHS is the identity, we only need to verify that for all Fock space basis states,

$$
\frac{1}{\pi} \left \langle m \mid
\int dx \, dy \, e^{-(x^2 + y^2)} \mid
\alpha \right \rangle 
\langle \alpha |n \rangle =\delta_{m n}
$$

Recall that

$$
| \alpha \rangle =\sum_{n\geq 0}  c_n| n\rangle ,
\quad
c_n=\frac{\alpha^n}{\sqrt{n!}}
$$

Then

$$
\begin{aligned}
    \text{LHS} 
    &=\int \frac{dx dy}{\pi} e^{-(x^2 + y^2)}
    \langle m| \alpha \rangle 
    \langle \alpha | n\rangle 
    \\
    &= \int \frac{dx dy}{\pi} e^{-(x^2 + y^2)}
    \frac{\alpha^m}{\sqrt{m!}}
    \frac{\bar{\alpha}^m}{\sqrt{n!}}
\end{aligned}
$$

To evaluate this integral, we use the polar coordinates:

$$
\alpha =r e^{i \theta}, \quad 
\bar{\alpha}=r e^{-i \theta}
$$

Then

$$
\begin{aligned}
    \text{LHS} 
    &= \int \frac{r \, dr \, d\theta}{\pi \sqrt{m!n!}}
    e^{-r^2 + i(m-n)\theta} r^{m+n}
    \\
    &=\frac{1}{\pi \sqrt{m!n!}}
    \int_0^{\infty} dr \, r^{m+n+1} e^{-r^2}
    \underbrace{
        \int_0^{2\pi} d\theta \, e^{i(m-n)\theta}
    }_{2\pi \delta_{mn}}
    \\
    &= \delta_{m n} \frac{2}{n!}
    \int_0^{\infty} dr \, r^{2n+1}e^{-r^2}
    \\
    &=\delta_{m n}\frac{2}{n!}\frac{\Gamma (n+1)}{2}
    =\delta_{m n}
\end{aligned}
$$

*Remark*: We can also change the integration variables to $\bar{\alpha},\alpha$, which has the Jacobian

$$
\begin{aligned}
    \left|\frac{\partial \left(\bar{\alpha},\alpha \right)}{\partial (x,y)}\right|
    &= \det \begin{pmatrix}
        \partial \bar{\alpha}/\partial x & \partial \bar{\alpha}/\partial y \\
        \partial \alpha /\partial x & \partial \alpha /\partial y
    \end{pmatrix}
    \\
    &= \det \begin{pmatrix}
        1 & -i \\
        1 & i
    \end{pmatrix}
    = 2i
\end{aligned}
$$

Then

$$
dx dy = 
\left| \frac{\partial \left(\bar{\alpha},\alpha \right)}{\partial (x,y)}\right|^{-1}
d\bar{\alpha} d\alpha 
= \frac{d\bar{\alpha}d\alpha}{2i}
$$

So the resolution can also be written as

$$
\int \frac{d\bar{\alpha} d\alpha}{2\pi i}
\exp (-\bar{\alpha} \alpha)
| \alpha \rangle \langle \alpha |
= \mathbf{1}
$$

For more than one kind of bosons,

$$
\int  \prod_k  \left(
    \frac{d\bar{\alpha}_kd\alpha_k}{2\pi i}
\right)
\exp \left(
    -\sum_k  \bar{\alpha}_k \alpha_k
\right)
| \alpha \rangle \langle\alpha |
= \mathbf{1}
$$

## Operators in Coherent State Representation

From the theory of second quantization, a 2-body operator has the form

$$
A(a^\dagger,a)
= \sum_{n,m} A_{n m} a^{\dagger n} a^m
$$

i.e. it *first annihilates* $m$ bosons and *then create* $n$ bosons with amplitude $A_{n m}$. 

In the coherent state representation, its matrix elements are

$$
\langle \beta |A|\alpha \rangle 
= \sum_{n,m} A_{n m} 
\langle \beta |a^{\dagger n} a^m|\alpha \rangle 
= \sum_{n,m} A_{n m} \bar{\beta}^n \alpha^m 
\langle \beta |\alpha \rangle
$$

What is the overlap $\langle \beta |\alpha \rangle$? By definition,

$$
\langle \beta |\alpha \rangle 
= \langle 0 | 
e^{\bar{\beta} a} e^{\alpha a^\dagger}
| 0\rangle
$$

Using the theorem (when $[A,B]$ is a $c$-number)

$$
e^A e^B = e^{[A,B]} e^B e^A
$$

We have

$$
e^{\bar{\beta} a}e^{\alpha a^\dagger}
= e^{\bar{\beta}\alpha [a,a^\dagger]}
e^{\alpha a^\dagger} e^{\bar{\beta} a}
= e^{\bar{\beta}\alpha}
e^{\alpha a^\dagger} e^{\bar{\beta} a}
$$

But

$$
\langle 0|e^{\alpha a^\dagger}=\langle 0|, 
\quad
e^{\bar{\beta} a}| 0\rangle =| 0\rangle
$$

Thus

$$
\langle \beta |\alpha \rangle =e^{\bar{\beta}\alpha}
$$

Finally

$$
\langle \beta |A|\alpha \rangle =\sum_{n,m} A_{n m}e^{\bar{\beta}\alpha}\bar{\beta}^n\alpha^m
$$

Now we see that the result can be obtained by a formal replacement

$$
\langle \beta |A(a^\dagger,a)|\alpha \rangle 
= e^{\bar{\beta}\alpha} A(\bar{\beta},\alpha)
$$

## Coherent State Path Integral for Bosons

Now we consider the propagator from and to some arbitrary states (not
necessarily labelled by the coordinates), and use the second-quantized,
normal-ordered Hamiltonian. Instead of inserting a complete set of
basis, we insert the *over-complete* coherent state basis:

$\left\langle f\left|e^{-i H \left(a^\dagger,a\right)T}\right|i\right\rangle =\int \left(\prod_{k=1}^{N-1} \frac{d\bar{\alpha}_kd\alpha_k}{2\pi
 i}e^{-\bar{\alpha}_k\alpha_k}\right)\left\langle f\left|1-i H\left(a^\dagger,a\right)\epsilon \right|\alpha_{N-1}\right\rangle \left(\prod
_{k=1}^{N-2} \left\langle \alpha_{k+1}\left|1-i H\left(a^\dagger,a\right)\epsilon \right|\alpha_k\right\rangle \right)\left\langle \alpha_1\left|1-i
H\left(a^\dagger,a\right)\epsilon \right|i\right\rangle$

Here the subscript $k$ in $\alpha_k$ denotes time, not species of
bosons. For the inserted terms, using the replacement derived in the
last section

$\left\langle \alpha_{k+1}\left|1-i H\left(a^\dagger,a\right)\epsilon \right|\alpha_k\right\rangle =e^{\bar{\alpha}_{k+1}\alpha_k}\left(1-i
H\left(\bar{\alpha}_{k+1},\alpha_k\right)\epsilon \right)$

Now we have

$\left\langle f\left|e^{-i H \left(a^\dagger,a\right)T}\right|i\right\rangle =\int \left(\prod_{k=1}^{N-1} \frac{d\bar{\alpha}_kd\alpha_k}{2\pi
 i}e^{-\bar{\alpha}_k\alpha_k}\right)\left\langle f\left|1-i H\left(a^\dagger,a\right)\epsilon \right|\alpha_{N-1}\right\rangle \left(\prod
_{k=1}^{N-2} e^{\bar{\alpha}_{k+1}\alpha_k}\left(1-i H\left(\bar{\alpha}_{k+1},\alpha_k\right)\epsilon \right)\right)\left\langle \alpha_1\left|1-i
H\left(a^\dagger,a\right)\epsilon \right|i\right\rangle$

To deal with the initial and final state, we also expand them using the
coherent state basis

$| i\rangle =\int \frac{d\bar{\alpha}_0d\alpha_0}{2\pi i}e^{-\bar{\alpha}_0\alpha_0}| \alpha_0\rangle \left\langle \left.\alpha_0\right|
i\right\rangle$

$\langle f|=\int \frac{d\alpha_Nd\bar{\alpha}_N}{-2\pi (-i)}e^{-\bar{\alpha}_N\alpha_N}\left\langle f\left| \alpha_N\right.\right\rangle \langle
\alpha_N|=\int \frac{d\alpha_Nd\bar{\alpha}_N}{2\pi i}e^{-\bar{\alpha}_N\alpha_N}\left\langle f\left| \alpha_N\right.\right\rangle \langle
\alpha_N|$

Then

$\left.\left\langle f\left|e^{-i H \left(a^\dagger,a\right)T}\right|i\right\rangle =\int \left(\prod_{k=0}^N \frac{d\bar{\alpha}_kd\alpha
_k}{2\pi i}e^{-\bar{\alpha}_k\alpha_k}\right)\left\langle f\left| \alpha_N\right.\right\rangle \langle \alpha_N|1-i H\left(a^\dagger,a\right)\epsilon
|\alpha_{N-1}\right\rangle \left(\prod_{k=1}^{N-2} e^{\bar{\alpha}_{k+1}\alpha_k}\left(1-i H\left(\bar{\alpha}_{k+1},\alpha_k\right)\epsilon
\right)\right)\left\langle \alpha_1|1-i H\left(a^\dagger,a\right)\epsilon | \alpha_0\rangle \left\langle \left.\alpha_0\right| i\right\rangle
\right.\\
=\int \left(\prod_{k=0}^N \frac{d\bar{\alpha}_kd\alpha_k}{2\pi i}e^{-\bar{\alpha}_k\alpha_k}\right)\left(\prod_{k=0}^{N-1} e^{\bar{\alpha
}_{k+1}\alpha_k}\left(1-i H\left(\bar{\alpha}_{k+1},\alpha_k\right)\epsilon \right)\right)\left\langle f\left| \alpha_N\right.\right\rangle \left\langle
\left.\alpha_0\right| i\right\rangle \\
=\int \left(\prod_{k=0}^N \frac{d\bar{\alpha}_kd\alpha_k}{2\pi i}\right)\left(\prod_{k=0}^N e^{-\bar{\alpha}_k\alpha_k}\right)\left(\prod
_{k=0}^{N-1} e^{\bar{\alpha}_{k+1}\alpha_k}\right)\left(\prod_{k=0}^{N-1} e^{-i H\left(\bar{\alpha}_{k+1},\alpha_k\right)\epsilon}\right)\left\langle
f\left| \alpha_N\right.\right\rangle \left\langle \left.\alpha_0\right| i\right\rangle$

We try to rearrange the exponentials to produce an $\epsilon$ factor in
order to merge it with the Hamiltonian term and get an integration over
time. ${}{}$There are two ways of doing it:

Method 1:

$\prod_{k=0}^N e^{-\bar{\alpha}_k\alpha_k}\prod_{k=0}^{N-1} e^{\bar{\alpha}_{k+1}\alpha_k}=e^{-\bar{\alpha}_N\alpha_N}\prod_{k=0}^{N-1}
e^{\left(\bar{\alpha}_{k+1}-\bar{\alpha}_k\right)\alpha_k}=e^{-\bar{\alpha}_N\alpha_N}\prod_{k=0}^{N-1} e^{ \left(\partial_t\bar{\alpha}_k\right)\alpha
_k\epsilon}$

Method 2:

$\prod_{k=0}^N e^{-\bar{\alpha}_k\alpha_k}\prod_{k=0}^{N-1} e^{\bar{\alpha}_{k+1}\alpha_k}=\prod_{k=0}^N e^{-\bar{\alpha}_k\alpha_k}\prod
_{k=1}^N e^{\bar{\alpha}_k\alpha_{k-1}}=e^{-\bar{\alpha}_0\alpha_0}\prod_{k=1}^N e^{-\bar{\alpha}_k\left(\alpha_k-\alpha_{k-1}\right)}=e^{-\bar{\alpha
}_0\alpha_0}\prod_{k=1}^N e^{-\bar{\alpha}_k \left(\partial_t\alpha_k\right)\epsilon}$

To make the final result more symmetric, we take the square root of both
and multiply them together:

$\left\langle f\left|e^{-i H \left(a^\dagger,a\right)T}\right|i\right\rangle =\int \left(\prod_{k=0}^N \frac{d\bar{\alpha}_kd\alpha_k}{2\pi
 i}\right) \exp \left(-\frac{1}{2}\left(\bar{\alpha}_0\alpha_0+\bar{\alpha}_N\alpha_N\right)\right)\left(\prod_{k=0}^{N-1} \exp \left[\frac{1}{2}\left(\partial
_t\bar{\alpha}_k\right)\alpha_k\epsilon -\frac{1}{2}\bar{\alpha}_{k+1} \left(\partial_t\alpha_{k+1}\right)\epsilon -i H\left(\bar{\alpha}_{k+1},\alpha
_k\right)\epsilon \right]\right)\left\langle f\left| \alpha_N\right.\right\rangle \left\langle \left.\alpha_0\right| i\right\rangle$

$=\int \left[d\bar{\alpha}\right][d\alpha ]\exp \left(i\int_0^Tdt \left[\frac{1}{2i}\left(\alpha \partial_t\bar{\alpha}-\bar{\alpha}\partial
_t\alpha \right)-H\left(\bar{\alpha},\alpha \right)\right]\right)\underbrace{\exp \left(-\frac{1}{2}\left(\bar{\alpha}_i\alpha_i+\bar{\alpha}_f\alpha
_f\right)\right)\left\langle f\left| \alpha_f\right.\right\rangle \left\langle \left.\alpha_i\right| i\right\rangle}_{\text{the} \text{projection
operator}}$

This is the for bosons. The action functional appears here is

$S=\int_0^Tdt \left[\frac{1}{2i}\left(\alpha \partial_t\bar{\alpha}-\bar{\alpha}\partial_t\alpha \right)-H\left(\bar{\alpha},\alpha \right)\right]$

We have recovered the notation
$\alpha_N\to \alpha_f,\alpha_0\to \alpha_i$
