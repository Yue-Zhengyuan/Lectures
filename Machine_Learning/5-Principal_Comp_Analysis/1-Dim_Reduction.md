# Dimensionality Reduction

In machine learning problems, some features are highly correlated that they approximately lie in a *lower-dimensional flat surface* in the feature space. For example, in the figure below, the feature space is 2-dimensional (i.e. there are 2 features), while the examples approximately lie on a 1-dimensional straight line (not a curve: we said "flat" surface). 

<center>
<img src="Figures/feat_original.png" width="300px">
<br><i>The original examples</i>
</center>

In order to speed up model training or reduce memory usage, we may *orthogonally* (the meaning of this word will be made clear later) project them into that lower-dimensional surface (see the figure below). The number of features is then reduces to the dimension of the surface). This process is called the **dimensionality reduction**. 

<center>
<img src="Figures/feat_approx.png" width="300px">
<br><i>The approximated examples</i>
</center>

The mostly used *linear* algorithm to do this is called the **Principal Component Analysis**, which we describe below. 

## Reformulation of the Problem

Let us now convert what is said above to mathematical expressions. Suppose we have $M$ examples of $N$-dimensional features; the $i$th example is denoted by

$$
x^a = (x^a_1, x^a_2, ..., x^a_n)^\mathsf{T} \in \mathbb{R}^N \qquad
i = 1,2,...,M
$$

What we want to find is a *flat* surface of $K$ dimensions ($K \le N$) that minimizes the sum of the *(squared) distance* to each feature point. In other words, the optimization cost function is

$$
J = \sum_{a=1}^M (\text{distance of } x^a \text{ to the flat surface})^2
$$

## Explicit Expression of the Cost Function

To simplify things, we shall perform feature scaling so that the average of each feature is moved to 0; then it is reasonable that the origin $(0,...,0)$ will be included in this surface. The surface can then be described by $K$ orthonormal basis vectors

$$
u_1, u_2, ..., u_k \in \mathbb{R}^N
\qquad u_i \cdot u_j = \delta_{ij}
$$ 

so that every point $z$ in that surface can be expressed as ($z_j$ are the components of $z$ under the basis $\{u_j\}$)

$$
z = z_j u_j
$$

For computational convenience, we shall reexpress it under the standard basis $\{e_j\}$: the two sets of basis vectors are related by a linear map

$$
\left. \begin{aligned}
    e_1 &= (1,0,...,0)^\mathsf{T} \\
    &\vdots \\
    e_n &= (0,0,...,1)^\mathsf{T}
\end{aligned} \right\}
\, \Rightarrow \,
u_j = u_{ij} e_i
$$

Then $z$ in the standard basis is

$$
z = (u_{ij} z_j) e_i
$$

Since the $\{u_j\}$ basis is orthonormal, the components $u_{ij}$ should satisfy

$$
\begin{aligned}
    u_i \cdot u_j
    &= (u_{ki} e_k) \cdot (u_{lj} e_l)
    \\
    &= u_{ki} u_{lj} \delta_{kl}
    \\
    &= u_{ki} u_{kj} = \delta_{ij}
\end{aligned}
$$

Each example $x$ will be *orthogonally* projected onto a point $z$ of this plane (we temporarily suppress the example label):

$$
\begin{aligned}
    x \mapsto z = z_j u_j
    = (u_{ij} z_j) e_i
\end{aligned}
$$

Now we can explain what *orthogonally* means: the vector $x - z$ is *orthogonal* to the surface, or equivalently $z$. Mathematically

$$
\begin{aligned}
    (x - z) \cdot z 
    &= (x_i - u_{ij} z_j) u_{ik} z_k
    \\
    &= x_i u_{ij} z_j - z_j z_j 
    \\
    &= (x_i u_{ij} - z_j) z_j= 0
\end{aligned}
$$

This allows us to express $z$ in terms of $x$ and the basis $\{u_j\}$:

The distance between $x$ and $z$ is now the same as the distance $s$ between $x$ and the plane:

$$
\begin{aligned}
    s^2 &= (x - z)^2
    \\
    &= (x - z) \cdot x \qquad ((x - z) \cdot z = 0)
    \\
    &= (x_i - u_{ij} z_j) x_i
\end{aligned}
$$

## Minimizing the Cost Function

## Approximated Features

## Matrix Notation for the Algorithm