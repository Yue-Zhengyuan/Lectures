# Matrix Description of Rotations

PHYS1110D Supplementary Material 2   
by YUE Zhengyuan

----

*Review before Reading*:   
Change of basis

----

In most introductory courses on classical mechanics, the teachers simply tell their students the following "facts":

> For a point rotating around a fixed axis (rotation angle =
$\alpha (t)$), the **angular velocity** $\boldsymbol{\omega}(t)$ is a *vector* of
>
> - Magnitude: $\omega(t) = d\alpha (t)/dt$
> - Direction: Parallel to the axis of rotation, determined by some "**right-hand rule**"

With the above definition of $\boldsymbol{\omega}$, The linear velocity $\boldsymbol{v}(t)$ of the point can be found by some *mysterious* operation called the **cross product**, defined by

$$
\boldsymbol{v}
= \boldsymbol{\omega} \times \boldsymbol{r}
=\det \begin{bmatrix}
    e_x & e_y & e_z \\
    \omega_1 & \omega_2 & \omega_3 \\
    r_1 & r_2 & r_3 
\end{bmatrix} 
= \begin{bmatrix}
    \omega_2 r_3 - \omega_3 r_2 \\
    \omega_3 r_1 - \omega_1 r_3 \\
    \omega_1 r_2 - \omega_2 r_1
\end{bmatrix}
$$

To really understand how people "invented" the angular velocity vector and cross product, you must use the correct mathematical language (i.e. matrices) to describe rotations. After going through this material, the *most important* (and maybe surprising to you, or any starters) thing you should remember is that:

<center>

**The angular velocity is not a vector!**

</center>

## Matrix Representation of Rotations

### Rotation Around the Coordinate Axes

<center>

![image]   
*Rotation around the $z$-axis. Only xy-plane is shown.*

</center>

The matrices of rotation by an angle $\alpha$ ($\alpha >0$ for
counter-clockwise rotations) around the $x$, $y$ and $z$-axes are, respectively:

$$
R_z(\alpha)
= \begin{bmatrix}
    \cos  \alpha  & -\sin  \alpha  & 0 \\
    \sin  \alpha  & \cos  \alpha  & 0 \\
    0 & 0 & 1
\end{bmatrix}
$$

You can derive them by the meaning of the columns of the matrices. 

### EXERCISE

Please show that the rotation matrix around $x$-axis and $y$-axis are, respectively

$$
R_x(\alpha) 
= \begin{bmatrix}
    1 & 0 & 0 \\
    0 & \cos  \alpha  & -\sin  \alpha  \\
    0 & \sin  \alpha  & \cos  \alpha
\end{bmatrix}
, \quad
R_y(\alpha)
= \begin{bmatrix}
    \cos  \alpha  & 0 & \sin  \alpha  \\
    0 & 1 & 0 \\
    -\sin  \alpha  & 0 & \cos  \alpha
\end{bmatrix}
$$

### Matrix for Arbitrary 3D Rotations

Every rotation in 3D space can be determined by 3 quantities:

- **The direction** of the rotation axis, specified by the **polar angle** $\theta$ and the **azimuth angle** $\varphi$

- **The angle of rotation** $\alpha$ around the rotation axis

To obtain the general rotation matrix (denoted by $R(\theta,\varphi, \alpha$), we proceed in the following way:

1. **Change basis so that the rotation axis *coincides* with the $z$-axis**

    We first rotate the old *system* $K$ by $\varphi$ around the $z$-axis to
    get a new *system* $K'$, followed by another rotation of the *new
    system* $K'$ about $y$ by an angle $\theta$ to get another *system*
    $K^{\prime\prime}$. This change of basis is simply described by

    $$
    \mathcal{D}(\theta ,\varphi)
    = \mathcal{D}_y(\theta) \mathcal{D}_z(\varphi)
    = R_y{}^{-1}(\theta) R_z{}^{-1}(\varphi)
    $$

2. **Rotate the object around the $z$-axis in the new system**

    In the new coordinate system, the rotation is just the rotation around $z$-axis by an angle $\alpha$, simply described by

    $$ R_z(\alpha)$$

Therefore, the matrix for an arbitrary rotation can be expressed as the combination

$$
\begin{aligned}
    R(\theta ,\varphi ,\alpha)
    &= \mathcal{D}^{-1}(\theta ,\varphi)
    R_z(\alpha) \mathcal{D}(\theta ,\varphi)
    \\
    &= R_z(\varphi) R_y(\theta) R_z(\alpha)
    R_y^{-1}(\theta) R_z^{-1}(\varphi)
\end{aligned}
$$

### EXERCISE

Not all matrices represent a rotation. Recall the following twoproperties of matrices:

1. The columns of the matrices correspond to the vectors $(e_1, e_2, e_3)$ after the transformation respectively
2. The determinant of a 3 $\times$ 3 matrix is the (signed) volume of the parallelepiped formed by its three columns}

Now, please show that, for a matrix representing a rotation:

1. $R^\top R = 1$ (A real matrix having this property is called an **orthogonal matrix**, since all of its columns are orthogonal to each other)

2. $\det R=1$ (With both properties, it will be called a **special** orthogonal matrix)

Then, finding the inverse of a rotation matrix is easy: we only need to exchange its columns and rows:

$$
R^{-1} = R^\top
$$

## Angular Velocity

To find the linear velocity of the rotating object at $\boldsymbol{r}(t)$, recall that

$$
\boldsymbol{r}(t)
= R(\theta ,\varphi ,\alpha (t))
\boldsymbol{r}(t_0)
\qquad \alpha (t_0)=0
$$

The *instantaneous* linear velocity at time $t_0$ is

$$
\boldsymbol{v}(t_0) 
\equiv 
\frac{d\boldsymbol{r}(t_0)}{dt}
= \frac{dR\left(\theta ,\varphi ,\alpha (t_0)\right)}{dt}\boldsymbol{r}(t_0)
$$

Now we *define* the time derivative of the matrix $R(\theta ,\varphi ,\alpha (t))$ at time $t_0$ is as $\omega_{i j}$, called the **angular velocity matrix**. Then

$$
\boldsymbol{v}(t_0) 
= \omega(t_0) \boldsymbol{r}(t_0)
= \omega_{i j}(t_0) r_j(t_0)
$$

Here the **Einstein summation rule** is used: if any subscript appears *twice*, then sum over it.

Now let us find the matrix $\omega_{i j}(t_0)$: since $R(\theta, \varphi, \alpha(t))$ depends on $t$ only via $\alpha$, we have

$$
\begin{aligned}
    \omega(t_0)
    &= \left[
        \frac{d R(\theta ,\varphi ,\alpha)}{dt}
    \right]_{t=t_0}
    \\
    &= R_z(\varphi) R_y(\theta) \left[
        \frac{d R_z(\alpha(t))}{dt}
    \right]_{t=t_0}
    R_y^{-1}(\theta) R_z^{-1}(\varphi)
    \\
    &= R_z(\varphi) R_y(\theta) \begin{bmatrix}
        0 & -\omega(t_0) & 0 \\
        \omega(t_0) & 0 & 0 \\
        0 & 0 & 0 
    \end{bmatrix}
    R_y(-\theta) R_z(-\varphi)
    \\
    &= \begin{bmatrix}
        0 & -\omega _3 & \omega _2 \\
        \omega _3 & 0 & -\omega _1 \\
        -\omega _2 & \omega _1 & 0
    \end{bmatrix}
\end{aligned}
$$

Here we used something we already know: the **angular speed** $\omega(t_0)$ at time $t_0$ should be (do not confuse it with the matrix $\omega$)

$$
\omega (t_0)=\frac{d\alpha (t_0)}{dt}
$$

We see that there are only 3 independent elements in the matrix $\omega_{i j}$:

$$
\begin{aligned}
    \omega_1 = \omega_{32} 
    & = \omega \sin \theta \cos \varphi 
    \\
    \omega_2 = \omega_{13} 
    & = \omega \sin \theta \sin \varphi 
    \\
    \omega_3 = \omega_{21} & = \omega  \cos \theta
\end{aligned}
$$

If you are familiar with the spherical polar coordinates, you should immediately recognize that these three elements are exactly the Cartesian components of a *vector* $\boldsymbol{\omega}$. The direction of $\boldsymbol{\omega}$ is *parallel to the rotation axis*. We then define the *combination of this three numbers* as the **angular velocity vector** (Note why I did not say "define the *vector* $\boldsymbol{\omega}$ as ..."). 

*Remark*: We see that the angular velocity matrix has one notable property

$$
\omega_{i j}=-\omega_{j i}
$$

Such matrices are said to be **anti-symmetric**.

## Cross Product

After we rewrite the matrix $dR/dt$ using the three numbers
$\omega_i (i=1,2,3)$, the linear velocity can be expressed as

$$
\begin{aligned}
    \boldsymbol{v}
    = \omega_{i j} r_j 
    &= \begin{bmatrix}
        0 & -\omega_3 & \omega_2 \\
        \omega_3 & 0 & -\omega_1 \\
        -\omega_2 & \omega_1 & 0
    \end{bmatrix} \begin{bmatrix}
        r_1 \\
        r_2 \\
        r_3
    \end{bmatrix}
    \\
    &= \begin{bmatrix}
        \omega_2 r_3 - \omega_3 r_2 \\
        \omega_3 r_1 - \omega_1 r_3 \\
        \omega_1 r_2 - \omega_2 r_1
    \end{bmatrix}
\end{aligned}
$$

This *defines* the formula of **cross product**:

$$
\boldsymbol{\omega} \times \boldsymbol{r}
= \begin{bmatrix}
    \omega_2 r_3 - \omega_3 r_2 \\
    \omega_3 r_1 - \omega_1 r_3 \\
    \omega_1 r_2 - \omega_2 r_1
\end{bmatrix}
$$

### EXERCISE

Please verify that

$$
M = \begin{bmatrix}
    a_1 & a_2 & a_3 \\
    b_1 & b_2 & b_3 \\
    c_1 & c_2 & c_3
\end{bmatrix}
\Rightarrow 
\det M = \boldsymbol{a}\cdot (\boldsymbol{b}\times \boldsymbol{c})
$$

## The Angular Velocity is NOT a Vector

Now you should know that the angular velocity *matrix* is the more
natural quantity, and the angular velocity *vector* is just some derived
object. But there must be some reason why people treat it as a vector
under most cases.

In fact, under *rotations* of the object, the angular velocity vector
behaves exactly the same as the position vector (which is, *by
definition*, a *true* vector). However, it will betray itself under
*reflections*. Let us see what happens in the latter case.

Consider for simplicity the reflection about the $x z$-plane. The transformation matrix of the position vector is

$$
P_y = \begin{bmatrix}
    1 & 0 & 0 \\
    0 & -1 & 0 \\
    0 & 0 & 1
\end{bmatrix}
$$

You should be able to write it down quickly using the meaning of the three columns of the matrix. Its inverse is itself (please verify this by direct calculation).

In the mirror (reflected world), since $\boldsymbol{v}$ and $\boldsymbol{r}$ are both
"true" vectors, we have

$$
\begin{aligned}
    &\boldsymbol{r}' = P_y\boldsymbol{r}, \quad
    \boldsymbol{v}' = P_y\boldsymbol{v}
    \\
    &\Rightarrow 
    \begin{bmatrix}
        x' \\
        y' \\
        z'
    \end{bmatrix}
    = \begin{bmatrix}
        x \\
        -y \\
        z
    \end{bmatrix}, \quad
    \begin{bmatrix}
        v_x' \\
        v_y' \\
        v_z'
    \end{bmatrix}
    = \begin{bmatrix}
        v_x \\
        -v_y \\
        v_z
    \end{bmatrix}
\end{aligned}
$$

However, the new $\boldsymbol{\omega}'$ vector must be extracted from the new $\omega'$ matrix, instead of applying $\boldsymbol{\omega}' = P_y\boldsymbol{\omega}$ (wrong). By definition

$$
\boldsymbol{v} = \omega \boldsymbol{r}
\Rightarrow 
\boldsymbol{v}' = \omega' \boldsymbol{r}'
$$

Note that here $\omega$ and $\omega'$ are both angular velocity matrices, not angular speed. Then

$$
P_y\boldsymbol{v}=\omega' P_y\boldsymbol{r}
$$

The left-hand side is again equal to $P_y\omega  \boldsymbol{r}$. Therefore, 

$$
P_y\omega \boldsymbol{r} = \omega'P_y \boldsymbol{r}
$$

Since this is true for *any* position $\boldsymbol{r}$, we obtain the following rule:

$$
\begin{aligned}
    &P_y \omega = \omega' P_y
    \\
    &\Rightarrow  \omega'
    = P_y \omega  P_y^{-1}
    = \begin{bmatrix}
        0 & \omega_3 & \omega_2 \\
        -\omega_3 & 0 & \omega_1 \\
        -\omega_2 & -\omega_1 & 0
    \end{bmatrix}
\end{aligned}
$$

We remark that $\omega$ and $\omega'$ are related by a similarity transformation. Now we can read off the new angular velocity *vector*:

$$
\boldsymbol{\omega}' 
= \begin{bmatrix}
    -\omega_1 \\
    \omega_2 \\
    -\omega_3
\end{bmatrix}
$$

This behavior is quite different from that of the position vector. Thus in mathematics, objects like the angular velocity vector are called **pseudo-vectors**.

### EXERCISE

Show that the angular velocity vector behaves in the same way as the position vector under rotations.
