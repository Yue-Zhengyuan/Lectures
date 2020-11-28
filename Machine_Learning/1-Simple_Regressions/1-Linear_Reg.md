# Linear Regression

## Hypothesis Function

Suppose that we have $m$ **samples**. The $i$th sample is denoted by

$$
(x_1^i, ..., x_n^i; \, y^i) \qquad i = 0,1,...,m-1
$$

The set of $n$ numbers $(x_1^i, ..., x_n^i)$ are called **features**, and the number $y^i$ is the **known example**. 

**Linear regression** aims to find a linear **hypothesis function** that best describes the relation between $(x_1, ..., x_n)$ and $y$. This function is denoted by

$$
\begin{aligned}
    h(x) &= \sum_{j=0}^n \theta_j x_j = \theta^\mathsf{T} x 
    \\[2em] \text{where} \quad
    \theta &= \begin{bmatrix}
        \theta_0 \\ \theta_1 \\ \vdots \\ \theta_n
    \end{bmatrix} \quad
    x = \begin{bmatrix}
        1 \\ x_1 \\ \vdots \\ x_n
    \end{bmatrix} \quad
\end{aligned}
$$

Here we introduced the auxiliary element $x_0 = 1$ (called the **bias term**) corresponding to the parameter $\theta_0$. 

In the following, we shall adopt the Einstein summation rule when no ambiguity arises and omit the summation sign.

## Cost Function

The parameters $\theta$ is determined by minimizing the **cost function**, which described how well the **prediction** of $h(x)$ matches the known examples. For linear regression, it is chosen as the average of the squared difference between the predictions and the examples (an extra factor of 1/2 is introduced for later convenience)

$$
J(\theta) 
= \frac{1}{2m} \sum_{i=1}^m [h(x^{i}) - y^{i}]^2
$$

To rewrite this in matrix notations, we introduce the $m \times (n+1)$ matrix

$$
X_{ij} \equiv x^i_j \qquad
\begin{aligned}
    i &= 0, ..., m-1 \\
    j &= 0, ..., n
\end{aligned}
$$

Then we define the prediction based on $x^i$ as

$$
\begin{aligned}
    h^i \equiv h(x^i) &= \theta_j x_j^i = X_{ij} \theta_j
    \\[0.5em]
    \text{or} \qquad h &= X \theta
\end{aligned}
$$

Then

$$
\begin{aligned}
    J(\theta) 
    &= \frac{1}{2m} |h - y|^2
    \\[0.8em]
    &= \frac{1}{2m} (X\theta - y)^\mathsf{T} (X\theta - y)
    \\[0.8em]
    &= \frac{1}{2m} (X_{ij} \theta_j - y_i)(X_{ik} \theta_k - y_i)
\end{aligned}
$$

## Gradient Descent

One way to find the optimal $\theta$ is to start from some initial guess, and apply the **gradient descent algorithm**. It is known from calculus that for a multi-variable function like $J(\theta)$, its gradient 

$$
\nabla_\theta J(\theta_0, ..., \theta_n) = \left[
    \frac{\partial J}{\partial \theta_0}, 
    \cdots, 
    \frac{\partial J}{\partial \theta_{n}}
\right]
$$

is a vector pointing in the direction that $J(\theta)$ increases fastest. With an **learning rate** $\alpha > 0$ (a small update step size), we can update $\theta$ by

$$
\theta_a \to \theta'_a 
= \theta_a - \alpha \frac{\partial J}{\partial \theta_a}(\theta) 
\qquad a = 0, 1, ..., n
$$

The gradient for the cost function of linear regression is found to be

$$
\begin{aligned}
    \frac{\partial J}{\partial \theta_a}
    &= \frac{1}{2m} \frac{\partial J}{\partial \theta_a}
    (X_{ij} \theta_j - y_i)(X_{ik} \theta_k - y_i)
    \\
    &= \frac{1}{2m} [
        X_{ia} (X_{ik} \theta_k - y_i)
        + (X_{ij} \theta_j - y_i) X_{ia}
    ]
    \\
    &= \frac{1}{m} X_{ia} (X_{ik} \theta_k - y_i)
\end{aligned}
$$

Using matrix notation, we have

$$
\nabla J = \frac{1}{m} X^\mathsf{T} (X \theta - y)
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
