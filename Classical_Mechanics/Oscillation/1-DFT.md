# Discrete Fourier Transform

## Introduction: Oscillation on a 1D Chain

Consider $N$ small balls (all of mass $n$; neglect their size) connected
by springs (all of the same stiffness $m\Omega^{2}$ and equilibrium
length $a$). The balls are labeled from 0 to $N - 1$, and their
displacements away from the equilibrium position are denoted by
$u_{n}(t)\ \left( n = 0,\ 1,\ \ldots,\ N - 1 \right)$.

We also assume that the first ball is connected to the last ball by the
same spring (so that the balls are on a closed loop), then we can set
the counting convention (called the **periodic boundary condition**):

$$u_{n + jN} = u_{n}\text{\ \ }\left( \forall j\mathbb{\in Z} \right)$$

### The equation of motion (Newton's Second Law) 

For each ball:

$$
\begin{align*}
m{\ddot{u}}_{n}(t)
&= m\Omega^{2} [ 
    ( u_{n + 1} - u_{n} ) 
    - ( u_{n} - u_{n - 1} ) 
]
\\
&= m\Omega^{2} (
    u_{n + 1} - 2u_{n} + u_{n - 1} 
), 
\quad n = 0,1,...,N - 1 \\
\end{align*}$$

We can verify that the expression

$$
\begin{align*}
    u_{n}(t) 
    &= \left( A\cos kna + B\sin kna \right)\left( C\cos \omega t + D\sin \omega t \right),
    \\
    \omega &= 2\Omega\left| \sin\frac{ka}{2} \right|
\end{align*}
$$

is a solution of the equation of motion for arbitrary real
coefficients $A, B, C$ and $D$; the relation between $\omega$ and
$k$ is called the **dispersion relation**.
>
*Hint: You may need the **angle sum and difference identities***

$$
\begin{align*}
    \cos (\alpha \pm \beta) 
    &= \cos\alpha\cos\beta \mp \sin\alpha\sin\beta,
    \\
    \sin (\alpha \pm \beta) 
    &= \sin\alpha\cos\beta \pm \cos\alpha\sin\beta
\end{align*}
$$

Directly substituting the expression to the equation of motion, we
    get (omitting the common $C\cos \omega t + D\sin \omega t$ factor on
    both sides:

$$- m\omega^{2}\left( A\cos kna + B\sin kna \right) = m\Omega^{2}\left[ A\left( \cos{k\left( n + 1 \right)a} + \cos{k\left( n - 1 \right)a} - 2\cos kna \right) + B\left( \sin{k\left( n + 1 \right)a} + \sin{k\left( n - 1 \right)a} - 2\sin kna \right) \right]$$

To simplify the right-hand side, we notice that (using the angle sum
and difference identities)

$$\cos{k\left( n + 1 \right)a} + \cos{k\left( n - 1 \right)a} = 2\cos kna\cos ka$$

$$\sin{k\left( n + 1 \right)a} + \sin{k\left( n - 1 \right)a} = 2\sin kna\cos ka$$

Then the right-hand side equals

$$m\Omega^{2}\left( A\cos kna + B\sin kna \right)2\left( \cos ka - 1 \right)$$

$$\Longrightarrow - m\omega^{2} = 2m\Omega^{2}\left( \cos ka - 1 \right) = - 4m\Omega^{2}\sin^{2}\frac{ka}{2}$$

This is already ensured by the relation

$$\omega = 2\Omega\left| \sin\frac{ka}{2} \right|$$

1)  Use the periodic boundary condition to show that only a limited
    number of $k$ is allowed:

$$k_{l} = \frac{2\pi l}{Na},\ \ l = 0,\ 1,\ \ldots,\ N - 1$$

3)  Because of the principle of superposition, we can of course add the
    solution for all allowed $k$ to get the general form of
    $u_{n}(t)$:

$$u_{n}(t) = \sum_{l = 0}^{N - 1}{\left( A_{l}\cos{k_{l}\text{na}} + B_{l}\sin{k_{l}\text{na}} \right)\left( C_{l}\cos{\omega_{l}t} + D_{l}\sin{\omega_{l}t} \right)}$$

Now we define two time-dependent coefficients

$$\mathcal{A}_{l}(t) = A_{l}\left( C_{l}\cos{\omega_{l}t} + D_{l}\sin{\omega_{l}t} \right),\ \ \mathcal{B}_{l}(t) = B_{l}\left( C_{l}\cos{\omega_{l}t} + D_{l}\sin{\omega_{l}t} \right)$$

Then (substituting in the expression of $k_{l}$)

$$u_{n}(t) = \sum_{l = 0}^{N - 1}{\mathcal{A}_{l}(t)\cos\frac{2\pi nl}{N} + \mathcal{B}_{l}(t)\sin\frac{2\pi nl}{N}}$$

The procedure of finding $A_{l}(t)$ and
$B_{l}(t)$ is called the **real discrete Fourier
transform (DFT)**.
>
Please show that

$$\mathcal{A}_{l}(t) = \frac{2}{N}\sum_{n = 0}^{N - 1}{u_{n}(t)\cos\frac{2\pi nl}{N}},\ \ \mathcal{B}_{l}(t) = \frac{2}{N}\sum_{n = 0}^{N - 1}{u_{n}(t)\sin\frac{2\pi nl}{N}}$$

*Hint: You need the following set of **orthogonal relations** of
trigonometric functions*

$$\sum_{n = 0}^{N - 1}{\sin\frac{2\pi ln}{N}\sin\frac{2\pi l^{'}n}{N}} = \ \sum_{n = 0}^{N - 1}{\cos\frac{2\pi ln}{N}\cos\frac{2\pi l^{'}n}{N}} = \frac{N}{2}\delta_{ll^{'}},\ \ \sum_{n = 0}^{N - 1}{\sin\frac{2\pi ln}{N}\cos\frac{2\pi l^{'}n}{N}} = 0$$

4)  The coefficients $\mathcal{A}_{l}(t)$ and
    $\mathcal{B}_{l}(t)$ are called the **Fourier
    coefficients**, or **normal modes** of the system. To see the origin
    of the latter name, please verify that:

    a.  The equations of motion of $A_{l}(t)$ and
        $B_{l}(t)$ are:

$$m{\ddot{\mathcal{A}}}_{l}(t) = - m\omega_{l}^{2}\mathcal{A}_{l}(t),\ \ m{\ddot{\mathcal{B}}}_{l}(t) = - m\omega_{l}^{2}\mathcal{B}_{l}(t)\text{\ \ \ \ }\left( l = 0,\ 1,\ \ldots,\ N - 1 \right)$$

They are much simpler than the original $u_{n}(t)$: just
like the motion of a single particle of mass $m$ connected to a spring
of stiffness $m\omega_{l}^{2}$;

b.  \* The energy (K.E. of the balls + P.E. in the springs) of the
    system can be put in a "diagonal" form:

$$E = \frac{N}{2}\sum_{l = 0}^{N - 1}\left[ \frac{1}{2}m\left( {\dot{\mathcal{A}}}_{l}^{2}(t) + \omega_{l}^{2}\mathcal{A}_{l}(t)^{2} \right) + \frac{1}{2}m\left( {\dot{\mathcal{B}}}_{l}^{2}(t) + \omega_{l}^{2}\mathcal{B}_{l}(t)^{2} \right) \right],\ \ \omega_{l} = 2\Omega\left| \sin\frac{k_{l}a}{2} \right|$$

just like the sum of many simple oscillators, without any "cross
terms".
>
*Hint: You will need (usually used in **discrete sine/cosine
transforms \[DST/DCT\])**:*

$$\sum_{n = 0}^{N - 1}{\sin\left[ \frac{2\pi l}{N}\left( n + \frac{1}{2} \right) \right]\sin\left[ \frac{2\pi l^{'}}{N}\left( n + \frac{1}{2} \right) \right]} = \sum_{n = 0}^{N - 1}{\cos\left[ \frac{2\pi l}{N}\left( n + \frac{1}{2} \right) \right]\cos\left[ \frac{2\pi l^{'}}{N}\left( n + \frac{1}{2} \right) \right]} = \frac{N}{2}\delta_{ll^{'}}$$

$$\sum_{n = 0}^{N - 1}{\sin{\frac{2\pi l}{N}\left( n + \frac{1}{2} \right)}\cos\frac{2\pi l^{'}}{N}\left( n + \frac{1}{2} \right)} = 0$$

*And the sum-to-product identities:*

$$\cos\alpha - \cos\beta = - 2\sin\frac{\alpha - \beta}{2}\sin\frac{\alpha + \beta}{2},\ \ \sin\alpha - \sin\beta = 2\sin\frac{\alpha - \beta}{2}\cos\frac{\alpha + \beta}{2}$$

**Solution:**

1)  

2)  Since $u_{n} = u_{n + jN}$ for all integers $j$, we must have

$$kNa = 2\pi l \Longrightarrow k_{l} = \frac{2\pi l}{Na},\ \ l = 0,\ 1,\ \ldots N - 1$$

Other integer values of $l$ are not necessary. Can you see why?

3)  To get the coefficient $\mathcal{A}_{l}$, we multiply
    $u_{n}(t)$ by $\cos\left( \frac{2\pi nl}{N} \right)$:

$$\begin{matrix}
u_{n}(t)\cos\frac{2\pi nl}{N} = \sum_{l^{'} = 0}^{N - 1}{\mathcal{A}_{l^{'}}\cos\frac{2\pi nl^{'}}{N}\cos\frac{2\pi nl}{N} + \mathcal{B}_{l^{'}}\sin\frac{2\pi nl^{'}}{N}\cos\frac{2\pi nl}{2}} \\
 = \sum_{l' = 0}^{N - 1}{\mathcal{A}_{l'} \times \frac{N}{2}\delta_{ll'}} = \frac{N}{2}\mathcal{A}_{l} \\
\end{matrix}$$

Similarly

$$\begin{matrix}
u_{n}(t)\sin\frac{2\pi nl}{N} = \sum_{l^{'} = 0}^{N - 1}{\mathcal{A}_{l^{'}}\cos\frac{2\pi nl^{'}}{N}\sin\frac{2\pi nl}{N} + \mathcal{B}_{l^{'}}\sin\frac{2\pi nl^{'}}{N}\sin\frac{2\pi nl}{2}} \\
 = \sum_{l' = 0}^{N - 1}{\mathcal{B}_{l'} \times \frac{N}{2}\delta_{ll'}} = \frac{N}{2}\mathcal{B}_{l} \\
\end{matrix}$$

The desired results follow immediately.

4)  a.  Recall that the definition of $\mathcal{A}_{l}(t)$
        and that of $\mathcal{B}_{l}(t)$ are respectively

$$\mathcal{A}_{l}(t) = A_{l}\left( C_{l}\cos{\omega_{l}t} + D_{l}\sin{\omega_{l}t} \right),\ \ \mathcal{B}_{l}(t) = B_{l}\left( C_{l}\cos{\omega_{l}t} + D_{l}\sin{\omega_{l}t} \right)$$

Note that $A_{l},\ B_{l},\ C_{l}$ and $D_{l}$ are constants. Then the
equation of motions can be directly verified.

b.  We first write down the energy expression using the original
    variables $u_{n}(t)$:

$$E = \sum_{n = 0}^{N - 1}\left[ \frac{1}{2}m{\dot{u}}_{n}(t)^{2} + \frac{1}{2}m\Omega^{2}\left( u_{n + 1}(t) - u_{n}(t) \right)^{2} \right]$$

This expression involves "cross terms" resulted from

$$\begin{matrix}
u_{n + 1} - u_{n} = \sum_{l}^{}{\mathcal{A}_{l}\left( \cos\frac{2\pi\left( n + 1 \right)l}{N} - \cos\frac{2\pi nl}{N} \right) + \mathcal{B}_{l}\left( \sin\frac{2\pi\left( n + 1 \right)l}{N} - \sin\frac{2\pi nl}{N} \right)} \\
 = 2\sum_{l}^{}{\sin\frac{\pi l}{N}\left\{ - \mathcal{A}_{l}\sin\left[ \frac{2\pi l}{N}\left( n + \frac{1}{2} \right) \right] + \mathcal{B}_{l}\cos\left[ \frac{2\pi l}{N}\left( n + \frac{1}{2} \right) \right] \right\}} \\
\end{matrix}$$

In the second equality we used the sum-to-product identities. Then

$$\sum_{n}^{}{\dot{u}}_{n}^{2} = \sum_{n}^{}{\sum_{l}^{}{\sum_{l^{'}}^{}\left( {\dot{\mathcal{A}}}_{l}{\dot{\mathcal{A}}}_{l^{'}}\cos\frac{2\pi nl}{N}\cos\frac{2\pi nl^{'}}{N} + 2{\dot{\mathcal{A}}}_{l}{\dot{\mathcal{B}}}_{l^{'}}\cos\frac{2\pi nl}{N}\sin\frac{2\pi nl^{'}}{N} + {\dot{\mathcal{B}}}_{l}{\dot{\mathcal{B}}}_{l^{'}}\sin\frac{2\pi nl}{N}\sin\frac{2\pi nl^{'}}{N} \right)}} = \sum_{l}^{}{\sum_{l^{'}}^{}{\frac{N}{2}\delta_{ll^{'}}\left( {\dot{\mathcal{A}}}_{l}{\dot{\mathcal{A}}}_{l^{'}} + {\dot{\mathcal{B}}}_{l}{\dot{\mathcal{B}}}_{l^{'}} \right)}} = \frac{N}{2}\sum_{l = 0}^{N - 1}\left( {\dot{\mathcal{A}}}_{l}^{2} + {\dot{\mathcal{B}}}_{l}^{2} \right)$$

Now you should have some feeling about the power of orthogonal
relations. Besides, we also have for the potential energy:

$$\sum_{n}^{}\left( u_{n + 1} - u_{n} \right)^{2} = 4\sum_{n}^{}{\sum_{l}^{}{\sum_{l^{'}}^{}{\sin\frac{\pi l}{N}\sin\frac{\pi l^{'}}{N}\left( {\dot{\mathcal{A}}}_{l}{\dot{\mathcal{A}}}_{l^{'}}\sin\left[ \frac{2\pi l}{N}\left( n + \frac{1}{2} \right) \right]\sin\left[ \frac{2\pi l^{'}}{N}\left( n + \frac{1}{2} \right) \right] - 2{\dot{\mathcal{A}}}_{l}{\dot{\mathcal{B}}}_{l^{'}}\sin{\frac{2\pi l}{N}\left( n + \frac{1}{2} \right)}\cos\frac{2\pi l^{'}}{N}\left( n + \frac{1}{2} \right) + {\dot{\mathcal{B}}}_{l}{\dot{\mathcal{B}}}_{l^{'}}\cos{\frac{2\pi l}{N}\left( n + \frac{1}{2} \right)}\cos\frac{2\pi l^{'}}{N}\left( n + \frac{1}{2} \right) \right)}}} = \sum_{l}^{}{\sum_{l^{'}}^{}{\frac{N}{2}\delta_{ll^{'}}4\sin\frac{\pi l}{N}\sin\frac{\pi l^{'}}{N}\left( {\dot{\mathcal{A}}}_{l}{\dot{\mathcal{A}}}_{l^{'}} + {\dot{\mathcal{B}}}_{l}{\dot{\mathcal{B}}}_{l^{'}} \right)}} = \frac{N}{2}\sum_{l = 0}^{N - 1}{4\sin^{2}\frac{\pi l}{N}\left( {\dot{\mathcal{A}}}_{l}^{2} + {\dot{\mathcal{B}}}_{l}^{2} \right)}$$

Don't forget that

$$\sin\frac{\pi l}{N} = \sin\frac{k_{l}a}{2}$$

Therefore

$$\begin{matrix}
E = \frac{N}{2}\sum_{l = 0}^{N - 1}\left[ \frac{1}{2}m\left( {\dot{\mathcal{A}}}_{l}^{2} + {\dot{\mathcal{B}}}_{l}^{2} \right) \right] + \frac{N}{2}\sum_{l = 0}^{N - 1}\left[ \frac{1}{2}m \cdot 4\Omega^{2}\sin^{2}\frac{k_{l}a}{2}\left( {\dot{\mathcal{A}}}_{l}^{2} + {\dot{\mathcal{B}}}_{l}^{2} \right) \right] \\
 = \frac{N}{2}\sum_{l = 0}^{N - 1}\left[ \frac{1}{2}m\left( {\dot{\mathcal{A}}}_{l}^{2}(t) + {\dot{\mathcal{B}}}_{l}^{2}(t) \right) + \frac{1}{2}m\omega_{l}^{2}\left( \mathcal{A}_{l}^{2}(t) + \mathcal{B}_{l}^{2}(t) \right) \right] \\
\end{matrix}$$