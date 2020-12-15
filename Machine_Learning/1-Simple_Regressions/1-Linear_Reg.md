# Linear Regression

## Hypothesis Function

Suppose that we have $M$ **samples**. The $a$th sample is denoted by

$$
(x_1^a, ..., x_N^a; \, y^a) \qquad i = 1,...,M
$$

The set of $N$ numbers $(x_1^a, ..., x_N^a)$ are called **features**, and the number $y^a$ is the **label** of the example (for supervised learning). 

**Linear regression** aims to find a linear **hypothesis function** that best describes the relation between $(x_1, ..., x_N)$ and $y$. This function is denoted by

$$
\begin{aligned}
    h(x) &= \sum_{j=0}^N \theta_j x_j = \theta^\mathsf{T} x 
    \\[2em] \text{where} \quad
    \theta &= \begin{bmatrix}
        \theta_0 \\ \theta_1 \\ \vdots \\ \theta_N
    \end{bmatrix} \quad
    x = \begin{bmatrix}
        1 \\ x_1 \\ \vdots \\ x_N
    \end{bmatrix} \quad
\end{aligned}
$$

Here we introduced the auxiliary element $x_0 = 1$ (called the **bias term**) corresponding to the parameter $\theta_0$. 

In the following, we shall adopt the Einstein summation rule when no ambiguity arises and omit the summation sign.

## Cost Function

The parameters $\theta$ is determined by minimizing the **cost function**, which described how well the **prediction** of $h(x)$ matches the known examples. For linear regression, it is chosen as the average of the squared difference between the predictions and the examples (an extra factor of 1/2 is introduced for later convenience)

$$
J(\theta) 
= \frac{1}{2M} \sum_{a=1}^M [h(x^{a}) - y^{a}]^2
$$

To rewrite this in matrix notations, we introduce the $M \times (N+1)$ matrix

$$
X_{aj} \equiv x^a_j \qquad
\begin{aligned}
    a &= 1, ..., M \\
    j &= 0, ..., N
\end{aligned}
$$

Then we define the prediction based on $x^a$ as

$$
\begin{aligned}
    h^a \equiv h(x^a) &= \theta_j x_j^a = X_{aj} \theta_j
    \\[0.5em]
    \text{or} \qquad h &= X \theta
\end{aligned}
$$

Then

$$
\begin{aligned}
    J(\theta) 
    &= \frac{1}{2M} |h - y|^2
    \\[0.8em]
    &= \frac{1}{2M} (X\theta - y)^\mathsf{T} (X\theta - y)
    \\[0.8em]
    &= \frac{1}{2M} (X_{ij} \theta_j - y_i)(X_{ik} \theta_k - y_i)
\end{aligned}
$$

## Gradient Descent

One way to find the optimal $\theta$ is to start from some initial guess, and apply the **gradient descent algorithm**. It is known from calculus that for a multi-variable function like $J(\theta)$, its gradient 

$$
\nabla_\theta J(\theta_0, ..., \theta_N) = \left[
    \frac{\partial J}{\partial \theta_0}, 
    \cdots, 
    \frac{\partial J}{\partial \theta_{N}}
\right]
$$

is a vector pointing in the direction that $J(\theta)$ increases fastest. With an **learning rate** $\alpha > 0$ (a small update step size), we can update $\theta$ by

$$
\theta_n \to \theta'_n 
= \theta_n - \alpha \frac{\partial J}{\partial \theta_n}(\theta) 
\qquad n = 0, 1, ..., N
$$

The gradient for the cost function of linear regression is found to be

$$
\begin{aligned}
    \frac{\partial J}{\partial \theta_n}
    &= \frac{1}{2M} \frac{\partial J}{\partial \theta_n}
    (X_{ij} \theta_j - y_i)(X_{ik} \theta_k - y_i)
    \\
    &= \frac{1}{2M} [
        X_{in} (X_{ik} \theta_k - y_i)
        + (X_{ij} \theta_j - y_i) X_{in}
    ]
    \\
    &= \frac{1}{M} X_{in} (X_{ik} \theta_k - y_i)
\end{aligned}
$$

Using matrix notation, we have

$$
\nabla J = \frac{1}{M} X^\mathsf{T} (X \theta - y)
$$

## Normal Equation

When the sample size and feature number are not too big, we can set $\nabla J = 0$ to directly find the optimal $\theta$. This means

$$
X^\mathsf{T} (X \theta - y) = 0
$$

Solving, we obtain the **normal equation**

$$
\theta = (X^\mathsf{T} X)^{-1} X^\mathsf{T} y
$$
