# Logistic Regression (Classification)

## Hypothesis Function

In (binary) **logistic regression**, the examples $y^a \, (a = 1, ..., M)$ can only take a *discrete* set of values, usually chosen as 0 and 1.

The logistic regression hypothesis is defined as:

$$ h(x) = g(\theta^\mathsf{T} x)$$

where function $g$ is the **sigmoid function** defined as: 

$$
g(z) = \frac{1}{1+e^{-z}}
$$

which looks like this:

<center>
<img src="Figures/sigmoid.svg" alt="sigmoid function" width="300px">
</center>

The function $h(x)$ is interpreted as the *probability* that the outcome $y$ will be equal to 1, given the values of the features $x$:

$$
h(x) = P(\, y = 1 \mid x \,)
$$

The final output $\bar{h}$ is determined by

$$
\tilde{h} = \begin{cases}
    1 & h > 0.5 \\
    0 & h \le 0.5
\end{cases}
$$

The number 0.5 here is called the **threshold**, and can be set to other values between 0 and 1 according to the concrete situations.

## Cost Function and Its Gradient 

The cost function in logistic regression is defined differently from linear regression (summation over $i$ is implied by Einstein rule):

$$
\begin{aligned}
    J(\theta) 
    &= - \frac{1}{M} \sum_{a=1}^{M} \left[
        y^a \ln h^a
        + ( 1 - y^a) \ln (1 - h^a) 
    \right]
    \\
    &= - \frac{1}{M} \left[
        y^\mathsf{T} \ln h 
        + (1 - y)^\mathsf{T} \ln (1 - h)
    \right]
\end{aligned}
$$

Here $h^a \equiv h(x^a)$. In the last line, the number 1 in the second line stands for the $M$-dimensional vector

$$
1 = (1, 1, ..., 1)^\mathsf{T}
$$

The gradient of the cost function is found to be:

$$ 
\begin{aligned}
    \frac{\partial J}{\partial \theta_n} 
    &= - \frac{1}{M} \sum_{a=1}^{M}
    \frac{\partial}{\partial \theta_n} \left[
        y^a \ln h^a
        + (1 - y^a) \ln (1 - h^a) 
    \right]
    \\
    &= - \frac{1}{M} \sum_{a=1}^{M} \left[
        y^a \frac{\partial}{\partial \theta_n} 
        \ln h^a
        + (1 - y^a) \frac{\partial}{\partial \theta_n} 
        \ln (1 - h^a) 
    \right]
    \\
    &= - \frac{1}{M} \sum_{a=1}^{M} \left[
        \frac{y^a}{h^a}
        + \frac{-(1 - y^a)}{1 - h^a}
    \right] \frac{\partial h^a}{\partial \theta_n} 
    \\
    &= \frac{1}{M} \sum_{a=1}^{M} 
    \frac{h^a - y^a}{h^a (1 - h^a)}
    \frac{\partial h^a}{\partial \theta_n} 
\end{aligned}
$$

Using the following property of the sigmoid function

$$
\frac{dg}{dz} = g(z) (1 - g(z))
$$

the derivative $\partial h^a / \partial \theta_n$ is found to be

$$
\begin{aligned}
    \frac{\partial h^a}{\partial \theta_n} 
    &= g'(z^a)
    \frac{\partial z}{\partial \theta_n} 
    \qquad (z^a \equiv X_{aj} \theta_j)
    \\
    &= g(z^a) (1 - g(z^a)) X_{an}
    \\
    &= h^a (1 - h^a) X_{an}
\end{aligned}
$$

Therefore

$$
\frac{\partial J}{\partial \theta_n} 
= \frac{1}{M} \sum_{a=1}^{M} 
(h^a - y^a) X_{an}
$$

In matrix form (as column vector):

$$
\nabla J = \frac{1}{M} X^\mathsf{T} (h - y)
$$

which happens to be similar to that in linear regression. We then apply gradient descent to minimize $J(\theta)$, and thus find the optimal parameters $\theta$.

## Multi-Class Classification

In a classification problem with $K > 3$ classes, the labels $y^a$ are $K$-dimensional standard basis vectors: if the $a$'th example belong to the $k$th class, then

$$
y^a_i = \delta_{ik} = \begin{cases}
    1 & i = k \\
    0 & i \ne k
\end{cases}
$$

To perform the classification, we will in fact do $K$ binary classification problem: whether the input belongs to the $i$th class or not. This method is called the **one-vs-all (one-vs-rest) algorithm**.

After these $K$ classification, we shall obtain a $K$-dimension vector $(h_1, ..., h_K)$ containing the "probabilities" that the input belongs to each class. The final output $\tilde{h}$ is then a $K$-dimensional vector with components determined by

$$
\tilde{h}_i = \begin{cases}
    1 & h_i = \max (h_1, ..., h_K) \\
    0 & \text{otherwise}
\end{cases}
$$
