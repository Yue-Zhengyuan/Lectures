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

# Real Gaussian Integral

## The Integral and the Generating Function 

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

## Wick's Theorem

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

