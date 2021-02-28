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

# Grassmann Gaussian Integral

For Grassmann numbers, *integration is the same as differentiation.* This leads to many different properties of Gaussian integrals for Grassmann variables.

## Integral of "Real" Variables

We first consider Gaussian integral of purely non-conjugate variables ($n$ must be an *even* integer in order that the integral does not vanish)

$Z(0)=\int d\eta_1 ... d\eta_n\exp \left(-\frac{1}{2}\sum_{i,j=1}^n \eta_iA_{i j}\eta_j\right)=\\
\int d\eta_n ... d\eta_1\exp \left(-\frac{1}{2}\sum_{i,j=1}^n \eta_iA_{i j}\eta_j\right)$

This is motivated by the **Majorana (real) fermion**. Because $n$ is even, it makes no difference if we write the integral measure in reverse order. The matrix $A$ here, however, is assumed to be a real *anti-symmetric* matrix. The additional factor 1/2 is introduced to account for repeated counting:

$\frac{1}{2}\sum_{i,j=1}^n \eta_iA_{i j}\eta_j=\sum_{i<j}  \eta_iA_{i j}\eta_j\text{ }\Longrightarrow \text{ }Z(0)=\int d\eta_n ... d\eta
_1\exp \left(-\sum_{i<j}  \eta_iA_{i j}\eta_j\right)$

The corresponding generating function is

$Z(\xi )=\int d\eta_n ... d\eta_1\exp \left(-\sum_{i<j} \eta_iA_{i j}\eta_j+\sum_{i=1}^n  \xi_i\eta_i\right)\\
=\int d\eta_n ... d\eta_1\prod_{i<j} \left(1-\eta_iA_{i j}\eta_j\right)\prod_{i=1}^n  \left(1+\xi_i\eta_i\right)$

The result contains a new structure, called the **Pfaffian** (denoted $\operatorname{Pf} A$), whose square equals $\det A$:

$Z(0)=\operatorname{Pf} A,\text{      }\\
Z(\xi )=Z(0) \exp \left(\frac{1}{2}\sum_{i,j=1}^n  \xi_i\left(A^{-1}\right)_{i j}\xi_j\right)=Z(0) \exp \left(\sum_{i<j}  \xi_i\left(A^{-1}\right)_{i
j}\xi_j\right)$

What the "Pfaffian" is and why $n$ should be an even number will be made clear in the following proof.

*Proof*: Consider the source-free $n$-*variable* integral first. Similar to the $n$-*species* case, the nonzero contribution comes from the terms containing *one and only one* $\eta_i$ for *each* $i$. we obtain

$Z(0)=\int  d\eta_n ... d\eta_1\sum_{\sigma} \text{ }\left(-\eta_{\sigma (1)}A_{\sigma (1)\sigma (2)}\eta_{\sigma (2)}\right)\left(-\eta
_{\sigma (3)}A_{\sigma (3)\sigma (4)}\eta_{\sigma (4)}\right) ... \\
\left(-\eta_{\sigma (n-1)}A_{\sigma (n-1)\sigma (n)}\eta_{\sigma (n)}\right)\\
=\sum_{\sigma} (-1)^{p(\sigma )}\int  d\eta_n ... d\eta_1 \left(\eta_1 ... \eta_n\right)A_{\sigma (1)\sigma (2)} ... A_{\sigma
(n-1)\sigma (n)}=\\
\sum_{\sigma} (-1)^{p(\sigma )}A_{\sigma (1)\sigma (2)} ... A_{\sigma (n-1)\sigma (n)}$

Here we demand that the permutation $\sigma$ should satisfy:

1\. Because in the product expansion of the exponential function, we
have $i<j$, then

$\sigma (1)<\sigma (3)< ... <\sigma (n-1)$

2\. Because each $\eta_i$ can appear only once

$\sigma (1)<\sigma (2), \sigma (3)<\sigma (4),  ... , \sigma (n-1)<\sigma (n)$

Now we see that if $n$ is an odd number, the second requirement cannot
be satisfied, and the integral is zero.

The expression

$Z(0)=\sum_{\sigma} (-1)^{p(\sigma )}A_{\sigma (1)\sigma (2)} ... A_{\sigma (n-1)\sigma (n)}$

is *defined* as the Pfaffian of the anti-symmetric matrix $A$.

Now turn on the source term. We first rewrite the generating function in
a clearer form

$Z(\xi )=\int d\eta_n ... d\eta_1\prod_{i<j} \left(1-\eta_iA_{i j}\eta_j\right)\prod_{i=1}^n  \left(1+\xi_i\eta_i\right)\\
=\int d\eta_n ... d\eta_1$

### Wick's Theorem

Similar to the ordinary real case, we can find the $m$-point function from the generating function:

$\left\langle \eta_{a(1)} ... \eta_{a(m)}\right\rangle \equiv \frac{\int d\eta_n ... d\eta_1 \eta_{a(1)} ... \eta_{a(m)}\exp
\left(-\frac{1}{2}\eta_iA_{i j}\eta_j\right)}{\int d\eta_n ... d\eta_1 \exp \left(-\frac{1}{2}\eta_iA_{i j}\eta_j\right)}=\\
\left.\frac{\partial}{\partial \xi_{a(m)}} ... \frac{\partial}{\partial \xi_{a(1)}}\mathcal{Z}(\xi )\right]_{\xi =0}$

To fix the sign, we demand that the sequence $a(1), ... a(m)$
should be ordered from small to large:

$a(1)<a(2)< ... <a(m)$

If any two of them are *equal*, then the correlation function vanishes
because of the anti-commutativity of the Grassmann variables.

In the Grassmann case, *the differentiation order matters*, and Wick's
theorem will involve sign changes for some terms.

- Basic element: Two-point functions

    $$
    \left\langle \eta_a\eta_b\right\rangle 
    = [A^{-1}]_{a b}
    $$

    *Proof*:

    The first derivative we need to calculate is

    $\frac{\partial}{\partial \xi_a}\exp \left(\frac{1}{2}\sum_{i,j=1}^n \xi_i [A^{-1}]_{i j}\xi_j\right)$

    However, when differentiating on the second $\xi$, we need to bring it
    to the front (swapping position with the first $\xi$), producing a
    negative sign. we obtain

    $\frac{\partial}{\partial \xi_a}\exp \left(\frac{1}{2}\sum_{i,j=1}^n \xi_i [A^{-1}]_{i j}\xi_j\right)=\\
    \left(-\frac{1}{2}\sum_{i=1}^n  \xi_i [A^{-1}]_{i a}+\frac{1}{2}\sum_{j=1}^n  [A^{-1}]_{a j}\xi_j\right) \exp ( ... )$

    We still define it as the structure $B_a$ linear in $\xi$

    $B_a[\xi ]=-\frac{1}{2}\sum_{i=1}^n  \xi_i [A^{-1}]_{i a}+\frac{1}{2}\sum_{j=1}^n  [A^{-1}]_{a j}\xi_j\text{     
   }(a=1, ... ,n)$

    and

    $\frac{\partial}{\partial \xi_a}\exp \left(\frac{1}{2}\sum_{i,j=1}^n \xi_i [A^{-1}]_{i j}\xi_j\right)=B_a(\xi ) \exp \left(\frac{1}{2}\sum
  _{i,j=1}^n \xi_i [A^{-1}]_{i j}\xi_j\right)$

    Luckily, because of the *anti-symmetry* of $A$ (and $A^{-1}$),

    $\frac{\partial B_a}{\partial \xi_b}=-\frac{1}{2}[A^{-1}]_{b a}+\frac{1}{2}[A^{-1}]_{a b}=[A^{-1}]_{a b}$

    this result still holds.

The Wick's theorem for Grassmann Gaussian integrals then states that

- Mean values of an *even* number of variables can be obtained by finding *all pairings of the variables*, calculate the product of the two-point functions, and sum over all pairings. But the term should carry a *negative* sign if the permutation needed to pair the variables has
*odd* parity.

- Mean values of an *odd* number of variables are *zero* identically.

*Example*: 4-point function

$$
\langle i j k l\rangle =\langle i j\rangle \langle k l\rangle -\langle i k\rangle \langle j l\rangle +\langle i l\rangle \langle j k\rangle
$$

The four letters *must* represent different variables (without loss of generality, we assume that $i<j<k<l$).

*Proof:*

$$
\begin{aligned}
    \langle i j k l\rangle 
    &=
    \frac{\partial}{\partial \xi_l}
    \frac{\partial}{\partial \xi_k}
    \frac{\partial}{\partial \xi_j}
    \frac{\partial}{\partial \xi_i}
    \exp ( ... )
    = 
    \frac{\partial}{\partial \xi_l}
    \frac{\partial}{\partial \xi_k}
    \frac{\partial}{\partial \xi_j}
    B_i \exp ( ... )
    \\
    &=
    \frac{\partial}{\partial \xi_l}
    \frac{\partial}{\partial \xi_k}
    (
        \langle i j\rangle \exp ( ... )
        - B_i B_j\exp ( ... )
    )
    \\
    &\text{(
        the minus sign is due to the exchange of
        $\partial /\partial \xi_j$ and $B_i$
    )}
    \\
    &= \frac{\partial}{\partial \xi_l}(
        \langle i j\rangle B_k\exp ( ... )-\langle i k\rangle B_j\exp ( ... )
        \\ &\qquad
        + B_i\langle j k\rangle \exp ( ... )
        - B_i B_j B_k\exp ( ... )
    )
    \\
    &= \langle i j\rangle \langle k l\rangle 
    -\langle i k\rangle \langle j l\rangle 
    +\langle i l\rangle \langle j k\rangle 
    +(\text{terms} \propto B)
    \\
    &\xrightarrow{\xi = 0}
    \langle i j\rangle \langle k l\rangle 
    - \langle i k\rangle \langle j l\rangle 
    + \langle i l\rangle \langle j k\rangle
    \end{aligned}
$$

## Integral over "Real" and "Imaginary" Parts

### One-Species Integral

We start from the simplest case: the Gaussian integral with one Grassmann variable and its "conjugate" (they are in fact independent; one pair of such variables are called a *species* (of *complex scalar fermions*))

$\int d\bar{\eta}d\eta  \exp \left(-\bar{\eta}a \eta \right)=\int d\bar{\eta}d\eta  \left(1-\bar{\eta}a \eta \right)$

and the with the source $\left(\bar{\xi},\xi \right)$

$Z\left(\bar{\xi},\xi \right)=\int d\bar{\eta}d\eta  \exp \left(-\bar{\eta}a \eta +\bar{\eta}\xi +\bar{\xi}\eta \right)\\
=\int d\bar{\eta}d\eta  \left(1-\bar{\eta}a \eta \right)\left(1+\bar{\eta}\xi \right)\left(1+\bar{\xi}\eta \right)$

We show that

$Z(0,0)=a,\text{       }Z\left(\bar{\xi},\xi \right)=Z(0,0) \exp \left(\bar{\xi} a^{-1}\xi \right)$

We put the result in this form to compare with the general case below.

*Proof*:

$Z\left(\bar{\xi},\xi \right)=\int d\bar{\eta}d\eta  \left(1-\bar{\eta}a \eta +\bar{\eta}\xi +\bar{\xi}\eta +\bar{\eta}\xi  \bar{\xi}\eta
-\bar{\eta}a \eta  \bar{\eta}\xi  \bar{\xi}\eta \right)$

If a term has nonzero contribution, it must contain *one* (because
integration $\Leftrightarrow$ differentiation) *and only one* (Since any
power higher than 2 vanishes) $\eta$ and $\bar{\eta}$. Then we are left
with

$Z\left(\bar{\xi},\xi \right)=\int d\bar{\eta}d\eta  \left(-\bar{\eta}a \eta +\bar{\eta}\xi  \bar{\xi}\eta \right)=\int d\bar{\eta}d\eta 
\left(\eta  a \bar{\eta}-\eta  \bar{\eta} \xi  \bar{\xi}\right)=a-\xi  \bar{\xi}\\
=a \left(1+\bar{\xi}a^{-1}\xi \right)=a \exp \left(\bar{\xi} a^{-1}\xi \right)$

### Multi-Species Integral

Now we generalize the result above to the $n$-species ($2n$-variable) case

$\int \prod_{k=1}^n  \left(d\bar{\eta}_kd\eta_k\right) \exp \left(-\sum_{i,j}  \bar{\eta}_iA_{i j}\eta_j\right)$

or more generally, the with the source $\left(\bar{\xi},\xi \right)$
terms

$Z\left(\bar{\xi},\xi \right)=\int \prod_{k=1}^n  \left(d\bar{\eta}_kd\eta_k\right) \exp \left(-\sum_{i,j=1}^n  \bar{\eta}_iA_{i j}\eta_j+\sum
_{i=1}^n \bar{\eta}_i\xi_i +\sum_{j=1}^n  \bar{\xi}_j\eta_j\right)\\
=\int \prod_{k=1}^n  \left(d\bar{\eta}_kd\eta_k\right) \exp \left(-\bar{\eta}^TA \eta +\bar{\eta}^T\xi +\bar{\xi}^T\eta \right)$

Here $A$ is an $n\times n$ *Hermitian and invertible* matrix *.* Since
the order of multiplication matters, we *define* that the product symbol
$\prod_{k=1}^n$ means multiplication from $k=1$ to $n$:

$\prod_{k=1}^n  f_k=f_1f_2 ... f_k$

We now prove that

$Z(0,0)=\det A$

$Z\left(\bar{\xi},\xi \right)=\\
Z(0,0) \exp \left(\sum_{i,j=1}^n  \bar{\xi}_i[A^{-1}]_{i j}\xi_j\right)=Z(0,0)\prod_{i,j=1}^n \left(1+\bar{\xi}_i[A^{-1}]_{i
j}\xi_j\right)$

*Proof*:

We first consider the source-free integral $Z(0,0)$. Because the
exponential function is now very simple, we choose not to diagonalize
the matrix $A$ to prove the theorem, but directly check the product
expansion of the exponential function to get the answer.

In the product expansion of the exponential function

$\prod_{i,j=1}^n  \left(1-\bar{\eta}_iA_{i j}\eta_j\right)$

the nonzero contribution comes from the terms containing *one* (because
integration $\Leftrightarrow$ differentiation) *and only one* (Since any
power higher than 2 vanishes) $\eta_i$ and $\bar{\eta}_i$ for *each*
$i$. The result is

$Z(0,0)=(-1)^n\int  \prod_{k=1}^n  \left(d\bar{\eta}_kd\eta_k\right) \sum_{\sigma}  \left(-\bar{\eta}_1A_{1\sigma (1)}\eta_{\sigma (1)}\right) ... \left(-\bar{\eta
}_nA_{n \sigma (n)}\eta_{\sigma (n)}\right)\\
=(-1)^n\sum_{\sigma} A_{1 \sigma (1)} ... A_{n \sigma (n)}\int  \prod_{k=1}^n  \left(d\bar{\eta}_kd\eta_k\right) \left(\bar{\eta}_1\eta
_{\sigma (1)} ... \bar{\eta}_n\eta_{\sigma (n)}\right)$

Reorder the product of $\eta$'s to match the order in the integration
measure:

$Z(0,0)=(-1)^n\sum_{\sigma} A_{1 \sigma (1)} ... A_{n \sigma (n)}\int  d\bar{\eta}_1d\eta_1d\bar{\eta}_2d\eta_2 ... \\
d\bar{\eta}_nd\eta_n \left(\bar{\eta}_n\eta_{\sigma (n)} ... \bar{\eta}_1\eta_{\sigma (1)}\right)\\
=\sum_{\sigma} A_{1 \sigma (1)} ... A_{n \sigma (n)}\int  d\bar{\eta}_1d\eta_1d\bar{\eta}_2d\eta_2 ... d\bar{\eta}_nd\eta_n \left(\eta
_{\sigma (n)}\bar{\eta}_n ... \eta_{\sigma (1)}\bar{\eta}_1\right)\\
=\sum_{\sigma} A_{1 \sigma (1)} ... A_{n \sigma (n)} (-1)^{p(\sigma )}\int  d\bar{\eta}_1d\eta_1d\bar{\eta}_2d\eta_2 ... \\
d\bar{\eta}_nd\eta_n\left(\eta_n\bar{\eta}_n ... \eta_1\bar{\eta}_1\right)=\sum_{\sigma}  (-1)^{p(\sigma )}A_{1 \sigma (1)} ... A_{n
\sigma (n)}$

Here $\sigma$ is a permutation of the sequence $\{1,2, ... ,n\}$
(i.e. $\sigma \in S_n$), and $p(\sigma )$ be the parity of the
permutation $\sigma$.

The last expression is just the definition of the *determinant* of $A$.
Therefore

$Z(0,0)=\det A$

Now we turn on the source $\left(\bar{\xi},\xi \right)$. This time it
is still better to diagonalize the matrix $A$. Since $A$ is Hermitian,
we can diagonalize it with a *unitary* matrix $U$ with determinant 1:

$\Lambda =U^{\dagger}A U \Longrightarrow A=U \Lambda  U^{\dagger}, A^{-1}=\left(U^{\dagger}\right)^{-1}\frac{1}{\Lambda}O^{-1}=U\frac{1}{\Lambda
}U^{\dagger}$

Here $1/\Lambda$ is the inverse of $\Lambda$. Introduce the new
variables $\theta =U^{\dagger}\eta , \bar{\theta}=U^T \bar{\eta}$
(just like a complex conjugate of $\theta$). Then

$Z\left(\bar{\xi},\xi \right)=\int \prod_{k=1}^n  \left(d\bar{\eta}_kd\eta_k\right) \exp \left(-\bar{\eta}^TA \eta +\bar{\eta}^T\xi +\bar{\xi
}^T\eta \right)\\
=\int \prod_{k=1}^n  \left(d\bar{\eta}_kd\eta_k\right) \exp \left(-\bar{\eta}^TU \Lambda  U^{\dagger} \eta +\bar{\theta}^TU^{\dagger}\xi +\bar{\xi
}^TU \theta \right)\\
=\int \prod_{k=1}^n  \left(d\bar{\theta}_kd\theta_k\right) \exp \left(-\bar{\theta}^T\Lambda  \theta +\bar{\theta}^T\zeta +\bar{\zeta}^T\theta
\right)$

Here we defined two new sources

$\zeta =U^{\dagger}\xi ,\text{          }\bar{\zeta}=U^T\bar{\xi}$

Then

$Z\left(\bar{\xi},\xi \right)=\prod_{k=1}^n \int  \left(d\bar{\theta}_kd\theta_k\right) \exp \left(-\bar{\theta}_k\Lambda_k \theta_k+\bar{\theta
}_k\zeta_k+\bar{\zeta}_k\theta_k\right)$

Now we can apply our previous result about one-species integral

$\int d\bar{\eta}d\eta  \exp \left(-\bar{\eta}a \eta +\bar{\eta}\xi +\bar{\xi}\eta \right)=a \exp \left(\bar{\xi} a^{-1}\xi \right)$

$\Longrightarrow Z\left(\bar{\xi},\xi \right)=\prod_{k=1}^n  \Lambda_k \exp \left(\bar{\zeta}_k\Lambda_k^{-1}\zeta_k\right)=\det \Lambda
 \times  \exp \left(\bar{\zeta}^T\frac{1}{\Lambda}\zeta \right)\\
=\det A \times  \exp \left(\bar{\xi}^TU\frac{1}{\Lambda}U^{\dagger}\xi \right)=\det A \times  \exp \left(\bar{\xi}^TA^{-1}\xi \right)$

### Wick's Theorem
