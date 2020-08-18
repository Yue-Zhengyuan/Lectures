## Radial Ordering

After the mapping from cylinder to complex plane, the time ordering (later time to earlier time) becomes a **radial ordering** (farther to closer to the origin). Explicitly

$$
\mathcal{R} \phi_1(z)\phi_2(w)=
\begin{cases}
    \phi_1(z)\phi_2(w), & |z|>|w| \\
    \pm \phi_2(w)\phi_1(z), & |z|<|w| \\
\end{cases}
$$

Here the $+$ sign is for bosons, and the $-$ sign is for fermions.

Let $a(z), b(z)$ be two holomorphic fields, and define two operators

$$
A=\oint dz \, a(z), \quad
B=\oint dz \, b(z)
$$

the integration path being any circle around the origin. Now we **claim** that

$$
\oint_0 dz [a(z),b(w)]=\oint_w dz [\mathcal{R} a(z)b(w)]
$$

Then we can integrate over $w$ to obtain

$$
[A,B] = \oint_0 dw \oint_w dz \, [\mathcal{R} a(z)b(w)]
$$

the subscript $0,w$ means circular paths centered at $0,w$. In the
following, we shall always assume radial ordering and omit the
$\mathcal{R}$ notation.

*Proof*:

We first evaluate the integral over $z$.

<center>

![image](Fig-6_2.png)   
*Deformation of integration path*

</center>

$$
\begin{aligned}
    \oint_w dz a(z)b(w)
    &=\oint_{|z|>|w|} dz a(z)b(w)-\oint_{|z|<|w|} dz b(w) a(z)
    \\
    &=\oint_0 dz [a(z),b(w)]
\end{aligned}
$$

Then, after integration over $w$, we immediately obtain

$$
\begin{aligned}
    \oint_0 dw \oint_0 dz [a(z),b(w)]
    &= \left[\oint_0 dz a(z), \oint_0 dw b(w)\right]
    \\
    & = [A,B] 
    \qquad \blacksquare
\end{aligned}
$$