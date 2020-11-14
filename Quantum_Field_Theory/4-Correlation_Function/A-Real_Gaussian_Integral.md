# Appendix A: <br>Gaussian Integral

## Integral of Real Variables

### The Integral and the Generating Function 

The $n$-variable Gaussian integral is

$$
\int dx_1 \cdots dx_n 
\exp \left(-\frac{1}{2}x_iA_{i j}x_j\right)
$$

Here $A_{i j}$ is a *real symmetric* $n\times n$ matrix, and Einstein summation rule is used. 

We also introduce **generating function** the with the (real) **source** $J$:

$$
\begin{aligned}
    Z(J)
    &=\int dx_1\text{...}dx_n \exp \left(-\frac{1}{2}x_iA_{i j}x_j+J_ix_i\right)
    \\
    &=\int dx_1\text{...}dx_n \exp \left(-\frac{1}{2}x^TA x+J^Tx\right)
\end{aligned}
$$

The integration results are

$$
\begin{aligned}
    Z(0) &= \frac{(2\pi)^{n/2}}{(\det A)^{1/2}}
    \\
    Z(J) &= Z(0) \exp \left(
        \frac{1}{2} J_i [A^{-1}]_{i j}J_j
    \right)
\end{aligned}
$$

*Proof*: The standard method is to *diagonalize* the matrix $A$. Since it is real symmetric, diagonalization can be done by an *orthogonal matrix* $O$ (which has *unit determinant*). Let the matrix after diagonalization be $\Lambda$:

$\Lambda =O^TA O \Longrightarrow A=O \Lambda  O^T, A^{-1}=\left(O^T\right)^{-1}\frac{1}{\Lambda }O^{-1}=O\frac{1}{\Lambda }O^T$

Here $1/\Lambda$ is the inverse of $\Lambda$. Introduce the new
variables $y=O^Tx$. The corresponding Jacobian is 1 (since we choose
$\det
 O=1$). Then

$Z(0)=\int dx_1\text{...}dx_n \exp \left(-\frac{1}{2}x^TO \Lambda  O^Tx\right)=\int dy_1\text{...}dy_n \exp \left(-\frac{1}{2}y^T\Lambda  y\right)=\int
dy_1\text{...}dy_n \prod _{k=1}^n  \exp \left(-\frac{1}{2}\Lambda _k y_k^2\right)\\
=\prod _{k=1}^n \int dy_k \exp \left(-\frac{1}{2}\Lambda _k y_k^2\right)=\prod _{k=1}^n \left(\frac{2\pi }{\Lambda _k}\right)^{1/2}=\frac{(2\pi
)^{n/2}}{(\det \Lambda)^{1/2}}=\frac{(2\pi)^{n/2}}{(\det A)^{1/2}}$

The general $Z(J)$ can be found similarly:

$Z(J)=\int dx_1\text{...}dx_n \exp \left(-\frac{1}{2}x^TO \Lambda  O^Tx+J^Tx\right)=\int dy_1\text{...}dy_n \exp \left(-\frac{1}{2}y^T\Lambda  y+J^TO
y\right)$

Define the new parameters $\mathcal{J}=O^TJ$:

$Z(J)=\int dy_1\text{...}dy_n \exp \left(-\frac{1}{2}y^T\Lambda  y+\mathcal{J}^T y\right)\\
=\int dy_1\text{...}dy_n \prod _{k=1}^n  \exp \left(-\frac{1}{2}\Lambda _k y_k^2+\mathcal{J}_k y_k\right)=\prod _{k=1}^n \int dy_k \exp \left(-\frac{1}{2}\Lambda
_k y_k^2+\mathcal{J}_k y_k\right)\\
=\prod _{k=1}^n \left(\frac{2\pi }{\Lambda _k}\right)^{1/2}\exp \left(\frac{1}{2}\mathcal{J}_k\frac{1}{\Lambda _k}\mathcal{J}_k\right)=\frac{(2\pi
)^{n/2}}{(\det A)^{1/2}}\exp \left(\frac{1}{2}\mathcal{J}^T \frac{1}{\Lambda }\mathcal{J}\right)\\
=\frac{(2\pi)^{n/2}}{(\det A)^{1/2}}\exp \left(\frac{1}{2}J O\frac{1}{\Lambda }O^TJ\right)=\frac{(2\pi)^{n/2}}{(\det A)^{1/2}}\exp \left(\frac{1}{2}J_i
[A^{-1}]_{i j}J_j\right)$

*Remark*:

More often, people use the *normalized* generating function

$\mathcal{Z}(J)\equiv \frac{Z(J)}{Z(0)}=\exp \left(\frac{1}{2}J_i[A^{-1}]_{i j}J_j\right)$

### Wick's Theorem

By differentiating the normalized generating function with respect to the sources $J$, we can obtain the **$n$-point function** (this name comes from quantum field theory and statistical physics):

$\left\langle x_{a(1)}\text{...}x_{a(m)}\right\rangle \equiv \frac{\int dx_1\text{...}dx_n x_{a(1)}\text{...}x_{a(m)}\exp \left(-\frac{1}{2}x_iA_{i
j}x_j\right)}{\int dx_1\text{...}dx_n \exp \left(-\frac{1}{2}x_iA_{i j}x_j\right)}=\left[\frac{\partial }{\partial J_{a(m)}}\text{...}\frac{\partial
}{\partial J_{a(1)}}\mathcal{Z}(J)\right]_{J=0}$

Sometimes we simply write $\langle a(1)\text{...}a(m)\rangle$. 

Although it does not matter here, we note that the differentiation order
is the *reverse* of the order of variables in the $m$-point function.

Now we prove some of its properties.

*Remark*: To save writing in the proofs in the following, we define the
structure linear in the $J$'s

$B_a[J]=\frac{1}{2}\sum _{i=1}^n  J_i [A^{-1}]_{i a}+\frac{1}{2}\sum _{j=1}^n  [A^{-1}]_{a j}J_j\text{      }(a=1,\text{...},n)$

Obviously $B_a(0)=0$. Then

$\frac{\partial }{\partial J_a}\exp \left(\frac{1}{2}J_i [A^{-1}]_{i j}J_j\right)=B_a(J)\exp \left(\frac{1}{2}J_i[A^{-1}]_{i
j}J_j\right)$

Because of the symmetry of $A$ (and $A^{-1}$), its derivative with
respect to $J$ is

$\frac{\partial B_a}{\partial J_k}=\frac{1}{2}[A^{-1}]_{k a}+\frac{1}{2}[A^{-1}]_{a k}=[A^{-1}]_{a k}$

1\. The is

$\left\langle x_ax_b\right\rangle =[A^{-1}]_{a b}$

*Proof*:

$\langle a b\rangle =\frac{\partial }{\partial J_b}\frac{\partial }{\partial J_a}\exp (\text{...})=\frac{\partial }{\partial J_b}\left(B_a\exp (\text{...})\right)=[A^{-1}]_{a
b}\exp (\text{...})+B_aB_b\exp (\text{...})\overset{J=0}{\rightarrow }[A^{-1}]_{a b}$

2\. ()

Mean values of an *even* number of variables can be obtained by finding
*all pairings of the variables*, calculate the product of the two-point
functions, and sum over all pairings.

Mean values of an *odd* number of variables are *zero* identically.

*Example*: 4-point function

$\langle i j k l\rangle =\langle i j\rangle \langle k l\rangle +\langle i k\rangle \langle j l\rangle +\langle i l\rangle \langle j k\rangle$

The four letters $i,j,k,l$ need *not* represent different variables.

*Proof*:

$\langle i j k l\rangle =\frac{\partial }{\partial J_l}\frac{\partial }{\partial J_k}\frac{\partial }{\partial J_j}\frac{\partial }{\partial J_i}\exp
(\text{...})=\frac{\partial }{\partial J_l}\frac{\partial }{\partial J_k}\frac{\partial }{\partial J_j}\left[B_i\exp (\text{...})\right]\\
=\frac{\partial }{\partial J_l}\frac{\partial }{\partial J_k}\left(\langle i j\rangle \exp (\text{...})+B_iB_j\exp (\text{...})\right)\\
=\frac{\partial }{\partial J_l}\left(\langle i j\rangle B_k\exp (\text{...})+\langle i k\rangle B_j\exp (\text{...})+B_i\langle j k\rangle \exp (\text{...})+B_iB_jB_k\exp
(\text{...})\right)$

If we stop differentiation here, we are evaluating
$\langle i j k\rangle$, containing 3 variables; it is obviously zero
because of the $B$'s in each term.

Now we continue:

$\langle i j k l\rangle =\langle i j\rangle \langle k l\rangle \exp (\text{...})+\langle i k\rangle \langle j l\rangle \exp (\text{...})+\langle
i l\rangle \langle j k\rangle \exp (\text{...})+(\text{terms} \text{proportional} \text{to} B)$

Setting $J=0$, and we are left with the desired result:

$\langle i j k l\rangle =\langle i j\rangle \langle k l\rangle +\langle i k\rangle \langle j l\rangle +\langle i l\rangle \langle j k\rangle$

## Integral over Real and Imaginary Parts of Complex Variables

Sometimes (when considering complex valued fields) we need to consider the following kinds of Gaussian integrals:

### "One"-Variable Case

$$
\int d\bar{z} dz \exp \left(-\bar{z}a z\right)
$$

Here we don't have the additional factor 1/2 here to account for the repeated counting. It should be emphasized that the variables $\bar{z}$ is *not* the complex conjugate of each other. They are *independent* variables constructed as

$$
z=x+i y \qquad \bar{z}=x-i y
$$

Therefore, the integration measure means

$d\bar{z}dz=\frac{\partial \left(\bar{z},z\right)}{\partial (x,y)}dxdy=2i dxdy$

The polar coordinates are also often used
($z=r e^{i \theta },\bar{z}=r e^{-i \theta }$):

$d\bar{z}dz=\frac{\partial \left(\bar{z},z\right)}{\partial (r,\theta)}drd\theta =\det \left(
\begin{array}{cc}
 e^{-i \theta } & -i r e^{-i \theta } \\
 e^{i \theta } & i r e^{i \theta } \\
\end{array}
\right)drd\theta =2i r drd\theta$

as expected. Therefore, we usually define the Gaussian integral with the
numerical factor $1/\pi$

$Z(0,0)=\int \frac{d\bar{z}dz}{2\pi i} \exp \left(-\bar{z}a z\right)=\int \frac{dxdy}{\pi } \exp \left(-a\left(x^2+y^2\right)\right)$

And the generating function with source $\left(\bar{J},J\right)$ is

$Z\left(\bar{J},J\right)=\int \frac{d\bar{z}dz }{2\pi i}\exp \left(-\bar{z}a z+\bar{z}J+\bar{J} z\right)$

The two sources are *not* complex conjugate of each other; they are two
independent quantities. We first prove that

$Z(0,0)=\frac{1}{a},\text{           }Z\left(\bar{J},J\right)=Z(0,0)\exp \left(\bar{J} \frac{1}{a}J\right)$

*Proof*:

To evaluate the integral we have to use the real variables. Cartesian
coordinates are better:

$Z\left(\bar{J},J\right)=\frac{1}{\pi }\int dxdy \exp \left(-a \left(x^2+y^2\right)+(x-i y)J+\bar{J} (x+i y)\right)\\
=\frac{1}{\pi }\int dx \exp \left[-a x^2+\left(J+\bar{J}\right)x\right] \int dy \exp \left[-a y^2+i \left(-J+\bar{J}\right)y\right]\\
=\frac{1}{a}\exp \left(\frac{\left(J+\bar{J}\right)^2+\left[i \left(-J+\bar{J}\right)\right]^2}{4a}\right)=\frac{1}{a}\exp \left(\bar{J} \frac{1}{a}J\right)$

### Multi-Variable Case

The generalization to multi-variable case is straightforward:

$$
Z(0,0)
=\int \frac{d\bar{z}_1dz_1}{2\pi i} \cdots 
\frac{d\bar{z}_ndz_n}{2\pi i} 
\exp \left(-\bar{z}_iA_{i j}z_j\right)
$$

The complex matrix $A$ is now assumed to be *Hermitian*. We also have the generating
function

$Z\left(\bar{J},J\right)=\int \prod _{k=1}^n  \left(\frac{d\bar{z}_kdz_k}{2\pi i}\right) \exp \left(- \bar{z}_iA_{i j}z_j+J_i\bar{z}_i +z_j \bar{J}_j\right)\\
=\int \prod _{k=1}^n  \left(\frac{d\bar{z}_kdz_k}{2\pi i}\right) \exp \left(- \bar{z}^TA z+J^T\bar{z} +z^T \bar{J}\right)$

Again, by diagonalizing the matrix $A$, we can prove that

$$
\begin{aligned}
    Z(0,0) &= \frac{1}{\det A}
    \\ \\
    Z\left(\bar{J},J\right)
    &= Z(0,0) \exp [
        \bar{J}_i (A^{-1})_{i j} J_j
    ]
\end{aligned}
$$

*Proof*:

Since $A$ is Hermitian, we can diagonalize it with a *unitary* matrix
$U$ with determinant 1:

$\Lambda =U^{\dagger }A U \Longrightarrow A=U \Lambda  U^{\dagger }, A^{-1}=\left(U^{\dagger }\right)^{-1}\frac{1}{\Lambda }O^{-1}=U\frac{1}{\Lambda
}U^{\dagger }$

Introduce the new variables $w=U^{\dagger }z, \bar{w}=U^T \bar{z}$ (just like a complex conjugate of $\mathcal{J}$). Then

$Z\left(\bar{J},J\right)=\int \prod _{k=1}^n  \left(\frac{d\bar{z}_kdz_k}{2\pi i}\right) \exp \left(-\bar{z}^TA z+\bar{z}^TJ+\bar{J}^Tz\right)\\
=\int \prod _{k=1}^n  \left(\frac{d\bar{z}_kdz_k}{2\pi i}\right) \exp \left(-\bar{z}^TU \Lambda  U^{\dagger } z+\bar{w}^TU^{\dagger }J+\bar{J}^TU
w\right)\\
=\int \prod _{k=1}^n  \left(\frac{d\bar{w}_kdw_k}{2\pi i}\right) \exp \left(-\bar{w}^T\Lambda  w+\bar{w}^T\mathcal{J}+\bar{\mathcal{J}}^Tw\right)$

Here we defined two new sources

$\mathcal{J}=U^{\dagger }J,\text{           }\bar{\mathcal{J}}=U^T\bar{J}$

Then

$Z\left(\bar{J},J\right)=\prod _{k=1}^n \int  \left(\frac{d\bar{w}_kdw_k}{2\pi i}\right) \exp \left(-\bar{w}_k\Lambda _k w_k+\bar{w}_k\mathcal{J}_k+\bar{\mathcal{J}}_kw_k\right)$

Now we can apply our previous result about one-species integral

$\int \frac{d\bar{z}dz }{2\pi i}\exp \left(-\bar{z}a z+\bar{z}J+\bar{J}z\right)=\frac{1}{a} \exp \left(\bar{J} a^{-1}J\right)$

$\Longrightarrow Z\left(\bar{J},J\right)=\prod _{k=1}^n  \frac{1}{\Lambda _k} \exp \left(\bar{\mathcal{J}}_k\Lambda _k^{-1}\mathcal{J}_k\right)=\frac{1}{\det
 A} \exp \left(\bar{\mathcal{J}}^T\frac{1}{\Lambda }\mathcal{J}\right)\\
=\frac{1}{\det A}\exp \left(\bar{J}^TU\frac{1}{\Lambda }U^{\dagger }J\right)=\frac{1}{\det A} \exp \left(\bar{J}^TA^{-1}J\right)$

### Wick's Theorem

With the generating function, we can take the $J$ (or $\bar{J}$)
derivative to get various mean values and derive Wick's Theorem.

To see the difference from the case of real integrals, we first
calculate the possible two-point functions. They are

$\left\langle z_a z_b\right\rangle =0, \left\langle \bar{z}_a \bar{z}_b\right\rangle =0, \left\langle \bar{z}_a z_b\right\rangle =\left\langle z_b\bar{z}_a\right\rangle
=(A^{-1})_{a b}$

They are also denoted by
$\langle a b\rangle ,\left\langle \bar{a} \bar{b}\right\rangle ,\left\langle \bar{a} b\right\rangle /\left\langle b \bar{a}\right\rangle$.
We see that a nonzero pair must include one variable and one "conjugate"
variable.

*Proof*: We reproduce the (normalized) generating function here for
convenience

$\mathcal{Z}\left(\bar{J},J\right)=\frac{1}{Z(0,0)}\int \prod _{k=1}^n  \left(\frac{d\bar{z}_kdz_k}{2\pi i}\right) \exp \left(- \bar{z}_iA_{i j}z_j+J_i\bar{z}_i
+z_j \bar{J}_j\right)=\exp \left(\bar{J}_i(A^{-1})_{i j}J_j\right)$

First take the derivative of $J_a$ and

$\frac{\partial }{\partial J_a}\mathcal{Z}\left(\bar{J},J\right)=\left(\sum _{i=1}^n \bar{J}_i(A^{-1})_{i a}\right)\exp (\text{...})\equiv
\bar{B}_a\left(\bar{J}\right)\exp (\text{...})$

Since the structure $\bar{B}_a$ does not contain $J$, the two point
function $\langle a b\rangle$ must vanish. But

$\frac{\partial \bar{B}_a}{\partial \bar{J}_b}=(A^{-1})_{b a}$

Similarly,

$\frac{\partial }{\partial \bar{J}_a}\mathcal{Z}\left(\bar{J},J\right)=\left(\sum _{i=1}^n (A^{-1})_{a i}J_i\right)\exp (\text{...})\equiv
B_a(J)\exp (\text{...})$

the structure $B_a$ does not contain $\bar{J}$, and
$\left\langle \bar{a} \bar{b}\right\rangle$ vanishes. And

$\frac{\partial B_a}{\partial J_b}=(A^{-1})_{a b}$

Only the pairs with both kinds of variables survive:

$\left\langle \bar{z}_a z_b\right\rangle =\frac{\partial }{\partial J_b}\frac{\partial }{\partial \bar{J}_a}\exp (\text{...})=\frac{\partial }{\partial
J_b}B_a(J)\exp (\text{...})=(A^{-1})_{a b}\exp (\text{...})+B_a(J)\bar{B}_b\left(\bar{J}\right)\overset{J=0}{\rightarrow }(A^{-1})_{a
b}$

Now we know how to generalize the real integral Wick's Theorem. For
example, the 4-point function

$\left\langle \bar{i} j \bar{k}l\right\rangle =\left\langle \bar{i} j\right\rangle \left\langle \bar{k}l\right\rangle +\left\langle \bar{i} l\right\rangle
\left\langle \bar{k} j\right\rangle$

*Proof*:

$\text{LHS}=\frac{\partial }{\partial J_l}\frac{\partial }{\partial \bar{J}_k}\frac{\partial }{\partial J_j}\frac{\partial }{\partial \bar{J}_i}\exp
(\text{...})=\frac{\partial }{\partial J_l}\frac{\partial }{\partial \bar{J}_k}\frac{\partial }{\partial J_j}\left(B_i\exp (\text{...})\right)\\
=\frac{\partial }{\partial J_l}\frac{\partial }{\partial \bar{J}_k}\left((A^{-1})_{i j}\exp (\text{...})+B_i\bar{B}_j\exp (\text{...})\right)\\
=\frac{\partial }{\partial J_l}\left((A^{-1})_{i j}B_k\exp (\text{...})+B_i(A^{-1})_{k j}\exp (\text{...})+B_i\bar{B}_jB_k\exp
(\text{...})\right)\\
=(A^{-1})_{i j}(A^{-1})_{k l}\exp (\text{...})+(A^{-1})_{i j}B_k\bar{B}_l\exp (\text{...})+(A^{-1})_{i
l}(A^{-1})_{k j}\exp (\text{...})+\left(\text{terms} \propto B,\bar{B}\right)\\
\overset{J=0}{\rightarrow }(A^{-1})_{i j}(A^{-1})_{k l}+(A^{-1})_{i l}(A^{-1})_{k j}=\left\langle
\bar{i} j\right\rangle \left\langle \bar{k}l\right\rangle +\left\langle \bar{i} l\right\rangle \left\langle \bar{k} j\right\rangle$

## Fourier Transform of Integration Variables

