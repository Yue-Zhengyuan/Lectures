# Fermion Coherent State

## Grassmann Numbers

Analogous to the boson case, we *define* the fermion coherent state as the eigenstate of the fermion annihilation operators $c_i$ (suppose there are $n$ kinds of fermions in the system):

$$
c_1c_2 \cdots c_n
| \eta_1\eta_2 \cdots \eta_n\rangle 
=\eta_1\eta_2 \cdots \eta_n| \eta_1\eta_2 \cdots\eta_n\rangle
$$

However, because the fermion operators *anti-commute*, we should have

$$
\cdots c_i \cdots c_j \cdots 
|\cdots \eta_i \cdots\eta_j \cdots\rangle 
= - \cdots\eta_j \cdots\eta_i \cdots 
| \cdots \eta_i \cdots \eta_j \cdots\rangle
$$

for any $i\neq j$. This means that $\eta_i$ are not ordinary numbers - they should *anti-commute with each other*:

$$
\{\eta_i,\eta_j\} = 0 \quad (i\neq j)
$$

They are called **Grassmann numbers**. For obvious reasons, we require 

$$
\{c_i,\eta_j\}=0 \quad
(i \neq j)
$$ 

The Hermitian conjugate of the definition is

$$
\langle \eta_1\eta_2 \cdots\eta_n|
c_n^\dagger \cdots c_2^\dagger c_1^\dagger 
= \langle \eta_1\eta_2 \cdots\eta_n|
\bar{\eta}_n \cdots \bar{\eta}_2 \bar{\eta}_1
$$

The Grassmann number $\bar{\eta}_i$ is the "conjugate" of $\eta_i$. Since $\{c_i^\dagger, c_j^\dagger\}=0$, we also impose
the relation $\{\bar{\eta}_i, \bar{\eta}_j\}=0$. 

We also require that the Grassmann numbers *always anti-commute* with the annihilation / creation operators. 

These anti-commutation relations form the **Grassmann algebra**.

## Building Coherent State from Vacuum

### One Kind of Fermions

First consider the case of only one kind of fermions. To build the coherent state from vacuum, we again examine the expansion

$$
| \eta \rangle =c_0| 0\rangle +c_1| 1\rangle
$$

We point out that the coefficients here are *Grassmann numbers*. Then

$$
\begin{aligned}
    c| \eta \rangle 
    &= c c_0| 0\rangle +c c_1| 1\rangle 
    = -c_0c| 0\rangle -c_1c| 1\rangle =-c_1| 0\rangle
    \\
    \eta | \eta \rangle 
    &=\eta | 0\rangle +\eta c_1| 1\rangle
\end{aligned}
$$

Now we conclude that

$$
c_1 = -\eta
$$

Again, $c_0$ is just a normalization and we can set it to be 1.

What about the $\eta c_1| 1\rangle$ term? Luckily, because of the anti-commutativity, any Grassmann number raised to power greater than 2 vanishes:

$$
\eta^n=0 \quad n\geq 2
$$

Then $\eta c_1| 1\rangle =-\eta^2| 1\rangle =0$. Therefore the **fermion coherent state** is given by

$$
| \eta \rangle 
= | 0\rangle -\eta | 1\rangle 
= (1-\eta c^\dagger)| 0\rangle
$$

The "Hermitian conjugate" of this state is

$$
\begin{aligned}
    \langle \eta |
    &= \langle 0| (1-c \bar{\eta})
    = \langle 0| (1+\bar{\eta} c)
    \\
    &= \langle 0|+\bar{\eta}\langle 0|c
    = \langle 0|+\bar{\eta}\langle 1|
\end{aligned}
$$

*Remark*: Because the exponential function simplifies greatly in the
fermion case, we can also write the coherent state as

$$
\begin{aligned}
    | \eta \rangle 
    &=\exp (-\eta c^\dagger)| 0\rangle
    \\ 
    \langle \eta |
    &=\langle 0|\exp (\bar{\eta} c)=\langle 0|\exp (-c \bar{\eta})
\end{aligned}
$$

Note the sign differences from the bosonic case.

### Many Kinds of Fermions

For systems containing multiple kinds of fermions,

$$
\begin{aligned}
    | \eta \rangle 
    &= \prod_k (1-\eta_kc_k^\dagger)| 0\rangle 
    \\
    &= \prod_k (| 0_k\rangle -\eta_k| 1_k\rangle)
    = \prod_k \exp (- \eta_k c_k^\dagger)| 0\rangle
\end{aligned}
$$

This easy generalization is true because $\eta c^\dagger$ as a whole commutes between different kind of fermions.

## Differentiation and Integration of Grassmann Variables

Before we continue to write down the resolution of identity in the fermion case in analogy, we must first define how to differentiate and integrate functions of Grassmann numbers.

Since $\eta^n=0$ for all $n\geq 2$, the analytical functions of Grassmann variables are limited to *multi-linear functions* of its variables. 

For example, the most general form of an analytical function of two variables $\eta ,\bar{\eta}$ is

$$
f(\eta ,\bar{\eta})
= a_0 + a_1 \eta + a_1^{\prime} \bar{\eta} 
+ a_{12} \eta \bar{\eta}
\quad a_0,a_1,a_1^{\prime},a_{12}\in \mathbb{C}
$$

### Differentiation

The differentiation is almost the same as ordinary differentiation. However, the *order* is important: we must differentiate the *innermost* variable first, then going outside one after another. For example,

$$
\frac{\partial}{\partial \theta}
\frac{\partial}{\partial \eta} (\theta \eta)
= \frac{\partial}{\partial \theta}
\frac{\partial}{\partial \eta} (-\eta \theta)
= \frac{\partial}{\partial \theta}(-\theta)
= -1
$$

### Integration

Integration over Grassmann variables is *defined to be the same* as differentiation.

## Resolution of Identity

$$
\int \prod_k d\bar{\eta}_k d\eta_k 
\exp (- \bar{\eta}_k\eta_k) 
| \eta \rangle \langle \eta |
=\mathbf{1}
$$

*Proof*: 

Since differentiation and integration are equivalent for Grassmann numbers, the proof is much simpler than the bosonic case.

Recall that

$$
| \eta \rangle =\prod_k (1-\eta_kc_k^\dagger)| 0\rangle =\prod_k (| 0\rangle -\eta_k| 1\rangle)
$$

Then, using $\eta_k^2=0$ and $\bar{\eta}_k^2=0$

$$
\begin{aligned}
    \text{LHS}
    &= \int \prod_k d\bar{\eta}_kd\eta_k (1-\bar{\eta}_k\eta_k) | \eta \rangle \langle \eta |
    \\
    &=\int \prod
    _k d\bar{\eta}_kd\eta_k (1-\bar{\eta}_k\eta_k) (| 0\rangle -\eta_k| 1\rangle)(\langle 0|-\langle 1|\bar{\eta}_k)
    \\
    &=\int \prod_{k} d\bar{\eta}_kd\eta_k \left[ (1+\eta_k\bar{\eta}_k) | 0\rangle \langle 0|+\eta_k\bar{\eta}_k|
    1\rangle \langle 1| \right]
    \\
    &=| 0\rangle \langle 0|+| 1\rangle \langle 1|
    =\mathbf{1}
    \qquad \blacksquare
\end{aligned}
$$

## Operators in Coherent State Representation

We again want to find the matrix elements of the 2-body operator

$$
A(c^\dagger ,c)=\sum_{n,m} A_{n m} (c^\dagger)^nc^m
$$

Obviously, now the indices $m,n$ can only take two values 0 and 1. Then

$$
\begin{aligned}
    \langle \xi |A|\eta \rangle 
    &= \sum_{n,m} A_{n m} 
    \langle \xi |(c^\dagger)^n c^m|\eta \rangle 
    \\
    &=\sum_{n,m} A_{n m} \bar{\xi}^n\eta^m\langle \xi |\eta \rangle 
    \\
    &=\sum_{n,m} A_{n m}\langle \xi |\eta \rangle \bar{\xi}^n\eta^m
\end{aligned}
$$

The overlap $\langle \xi |\eta \rangle$ is evaluated to be

$$
\begin{aligned}
    \langle \xi |\eta \rangle 
    &= \langle 0 |\exp ( \bar{\xi} c)\exp (-\eta c^\dagger)|0\rangle 
    \\
    &= \langle 0|(1+\bar{\xi} c)(1-\eta c^\dagger)|0\rangle
    \\
    &= \langle 0|1-\eta c^\dagger +\bar{\xi} c-\bar{\xi} c \eta c^\dagger |0\rangle
\end{aligned}
$$

The middle two terms vanish obviously. The last term gives

$$
\langle 0|-\bar{\xi} c \eta c^\dagger |0\rangle 
= \langle 0|\bar{\xi} \eta c c^\dagger |0\rangle
=\bar{\xi} \eta \langle 0|c c^\dagger |0\rangle 
=\bar{\xi} \eta
$$

Hence

$$
\langle \xi |\eta \rangle 
= 1+\bar{\xi} \eta = e^{\bar{\xi} \eta}
$$

similar to the boson result. Finally

$$
\langle \xi |A|\eta \rangle 
= \sum_{n,m} A_{n m}\bar{\xi}^n\eta^me^{\bar{\xi} \eta}
= \sum_{n,m} A_{n m}e^{\bar{\xi} \eta}\bar{\xi}^n\eta^m
$$

The last equality is due to the fact that $e^{\bar{\xi} \eta}$
commutes with $\bar{\xi}^n\eta^m$.

Now we see that we can get the result by a formal replacement

$$
\langle \xi |A(c^\dagger ,c)|\eta \rangle 
= e^{\bar{\xi} \eta}A(\bar{\xi},\eta)
$$

## Coherent State Path Integral for Fermions

Similar to the bosonic case, we insert the *over-complete* coherent state basis:

$$
\begin{aligned}
    &\left\langle f\left|e^{-i H (c^\dagger ,c)T}\right|i\right\rangle 
    \\
    &=\int \left(
        \prod_{k=1}^{N-1} 
        d\bar{\eta}_k d\eta_k
        e^{-\bar{\eta}_k\eta_k}
    \right)
    \left\langle f\left|e^{-i H (c^\dagger ,c)\epsilon}\right|\eta_{N-1}\right\rangle 
    \\ &\qquad \times
    \left(
        \prod_{k=1}^{N-2} \left\langle
        \eta_{k+1}\left|e^{-i H (c^\dagger ,c)\epsilon}\right|c_k\right\rangle
    \right)
    \left\langle \eta_1\left|e^{-i H (c^\dagger ,c)\epsilon}\right|i\right\rangle 
    \\
    &=\int \left(
        \prod_{k=1}^{N-1} d\bar{\eta}_kd\eta_ke^{-\bar{\eta}_k\eta_k}
    \right)
    \left\langle f\left|1-i H(c^\dagger ,c)\epsilon \right|\eta_{N-1}\right\rangle 
    \\ &\qquad \times
    \left(
        \prod_{k=1}^{N-2} \left\langle \eta_{k+1}\left|1-i H(c^\dagger ,c)\epsilon \right|c_k\right\rangle
    \right)
    \left\langle \eta_1\left|1-i H(c^\dagger ,c)\epsilon \right|i\right\rangle
\end{aligned}
$$

After a calculation the same as the boson case, we arrive at

$$
\begin{aligned}
    &\left\langle f\left|e^{-i H (c^\dagger ,c)T}\right|i\right\rangle 
    \\
    &=\int \left(
        \prod_{k=0}^N d\bar{\eta}_kd\eta_k
    \right) \exp \left(
        -\frac{1}{2}(\bar{\eta}_0\eta_0+\bar{\eta}_N\eta_N)
    \right) 
    \\ &\qquad \times \left(
        \prod_{k=0}^{N-1} \exp \left[
            \frac{1}{2} (\partial_t\bar{\eta}_k)\eta_k\epsilon 
            -\frac{1}{2}\bar{\eta}_{k+1} (\partial_t\eta_{k+1})\epsilon 
            -i H(\bar{\eta}_{k+1},\eta_k)\epsilon
        \right]
    \right)
    \\ &\qquad \times
    \langle f| \eta_N \rangle 
    \langle \eta_0| i  \rangle 
    \\
    &=\int \left[d\bar{\eta}\right][d\eta ]
    \exp \left(
        i\int_0^Tdt \left[\frac{1}{2i}((\partial_t\bar{\eta})\eta -\bar{\eta}\partial
    _t\eta)-H(\bar{\eta},\eta)\right]
    \right)
    \\ &\qquad \times
    \underbrace{
        \exp \left(
            -\frac{1}{2}(\bar{\eta}_i\eta_i+\bar{\eta}_f\eta_f)
        \right)
        \langle f| \eta_f \rangle 
        \langle \eta_i | i \rangle
    }_{\text{the projection operator}}
\end{aligned}
$$

Because of the anti-commutativity of Grassmann numbers, we can combine the two terms with time derivative:

$$
\int dt \left[(\partial_t\bar{\eta})\eta -\bar{\eta}\partial_t\eta \right]=\int dt \left[\partial_t(\bar{\eta}\eta)-2\bar{\eta
}\partial_t\eta \right]=\int dt \left[-2\bar{\eta}\partial_t\eta \right]
$$

Finally

$$
\left\langle f\left|e^{-i H (c^\dagger ,c)T}\right|i\right\rangle =\int [d\bar{\eta}][d\eta ]
\exp \left(i\int_0^Tdt \left[i
\bar{\eta}\partial_t\eta -H(\bar{\eta},\eta)\right] \right) \\
\times \text{projection operator}
$$

This is the **coherent state path integral** for fermions. The action functional is

$$
S=\int_0^Tdt \left[i \bar{\eta}\partial_t\eta -H(\bar{\eta},\eta)\right]
$$