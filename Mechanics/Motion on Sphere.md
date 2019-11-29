# Classical Mechanics in Curved Space

We are already vary familiar with the (classical) motion of particles in the 2-dimensional Euclidean plane $\R^2$, described by **Newton's Laws of Motion**:

- *First Law*: In an inertial frame of reference, an object either remains at rest or continues to move at a constant velocity, unless acted upon by a force.
- *Second Law*: In an inertial frame of reference, the vector sum of the forces $\boldsymbol{F}$ on an object is equal to the mass $m$ of that object multiplied by the acceleration a of the object:  
    $$
    \boldsymbol{F} 
    = m \frac{\text{d}^2\boldsymbol{x}}{{\text{d}t}^2}
    $$

However, if you have heard of the general relativity, you know that physics is more interesting if the space is *curved*. A simple example is the 2-dimensional sphere (of radius $R$):

$$
S^2=\{(x,y,z) \in \R^3 | x^2 + y^2 + z^2 =R^2\}
$$

It is better to describe the sphere using the spherical polar coordinates, which are related to the Cartesian coordinates by

$$
\begin{aligned}
    x &= r \sin{\theta} \cos{\varphi} \\
    y &= r \sin{\theta} \sin{\varphi} \\
    z &= r \cos{\theta}
\end{aligned}
$$

Then the expression of the sphere is simply

$$
S^2 = \{(r,\theta,\varphi) | 
r = R, \quad 
\theta \in [0,\pi], \quad 
\varphi \in [0,2\pi)\}
$$

In $\R^2$, according to Newton's Laws, a free particle will move in a "straight line" in the usual sense. What would happen for a particle moving in $S^2$? 

## Thinking like Ants

We are living in the 3-dimensional Euclidean space $\R^3$, so we are long accustomed to thinking using the 3D Cartesian coordinates. Mathematicians call this **embedding** the surfaces into $\R^3$. Such a way of thinking surfaces has the disadvantage that we don't know what properties are *intrinsic* to the curved surface. 

When studying the cross product, you may have a feeling of absurdity that in order to describe the linear velocity in *2D*, we have to go "out of the space" and calculate the cross product of the angular velocity $\boldsymbol{\omega}$ and the position $\boldsymbol{r}$ in *3D*. Is there a way to stay in the 2D plane and get all the things?

## Curvilinear Coordinates

To describe the motion on the sphere, it is much more convenient to use the angles $(\theta, \varphi)$, instead of the old Cartesian coordinates $(x, y, z)$. Unlike the rectangular grids in Cartesian coordinate system, lines of constant $\theta$ and of constant $\varphi$ are *curves* in $\R^3$. Therefore, the coordinates $(\theta, \varphi)$ are called **curvilinear coordinates**.

- *Remark*: In order to generalize the result, the curvilinear coordinates will also be denoted as $(u_1, u_2, ...)$, as different from the Cartesian coordinates $(x_1, x_2, ...)$. 

## Basis Vectors

As usual, there are **basis vectors** corresponding to the each of the coordinates. 

## The Metric Tensor

To measure the distance on the sphere, we need the **metric tensor** $[g_{ij}]$ (we shall use the square bracket [ ] to indicate matrices). But let us first recall 

$$
[g_{ij}] = 
\begin{pmatrix}
    R^2 & 0 \\
    0 & R^2 \sin{\theta}
\end{pmatrix}
$$

## Covariant Derivative

Since the basis vectors are changing from place to place, the change in the *components* of the position is *not* the real change. We must exclude the change of the basis vector. 

## Newton's Laws on Curved Surfaces