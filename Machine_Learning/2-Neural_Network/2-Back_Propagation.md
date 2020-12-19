<style>
    .remark {
        border-radius: 15px;
        padding: 20px;
        background-color: SeaGreen;
        color: White;
    }
    .result {
        border-radius: 15px;
        padding: 20px;
        background-color: FireBrick;
        color: White;
    }
</style>

# Back Propagation

<div class="remark">
<center>
<i>In the following we shall NOT use Einstein summation rule. <br> All summations will be indicated explicitly.</i>
</center>
</div><br>

**Back propagation** (or shortly **backprop**) is the standard method of calculating the gradient of the cost function of a neural network in which the activation functions of all units are the sigmoid function:

$$
g(z) = \frac{1}{1 + e^{-z}}
$$

<center>
<img src="Figures/neural_network.svg" alt="neural network" width="400px">
</center>

The cost function (with regularization) is defined as (we simply write $h_i^a \equiv h_i(x^a)$ to represent the $i$th component of the $a$th prediction)

$$
\begin{aligned}
    J(\Theta) &= -\frac{1}{M} 
    \sum_{i=1}^K \sum_{a=1}^{M}\left[
        y_i^a \ln h_i^a
        + (1-y_i^a) \ln (1 - h_i^a)
    \right]
    \\[1.2em] &\quad 
    + \frac{\lambda}{2M} 
    \sum_{l=1}^L \sum_{i=1}^{N_l} \sum_{j=1}^{N_{l-1}}
    (\Theta_{ij}^{l})^2
    \\[1.2em]
    &= J_0 + J_\text{reg}
\end{aligned}
$$

The first part $J_0$ is just the sum of cost functions of each binary classification (in class $k$ or not). The second part $J_\text{reg}$ is the sum of the square of each $\Theta$ elements. Note that the $\Theta^l_{i0}$ elements (corresponding to the bias) should not be regularized. 

## The Derivative of Cost Function

We first calculate the derivative of $J_0$ with respect to *all* the parameters 

$$
\Theta_{mn}^{l} \qquad
\begin{aligned}
    l &= 1, 2, ..., L \\
    m &= 1, 2, ..., N_l \\
    n &= 0, 1, ..., N_{l-1} \\
\end{aligned}
$$

$$
\frac{\partial J_0}{\partial \Theta_{mn}^l}
= \frac{1}{M} \sum_{k=1}^K \sum_{a=1}^{M}
\frac{h_i^a - y_i^a}{h_i^a (1 - h_i^a)}
\frac{\partial h_i^a}{\partial \Theta_{mn}^l}
$$

Focus on the contribution from only one example (we suppress the example label $a$ temporarily, and use $K = N_L$):

$$
D^l_{mn} \equiv \sum_{i=1}^{N_L}
\frac{h_i - y_i}{h_i (1 - h_i)}
\frac{\partial h_i}{\partial \Theta_{mn}^l}
$$

Let us first simplify the notation a little bit:

- When calculating $\partial h_i / \partial \Theta_{mn}^{l}$we will use the following property

    $$
    g'(z) \equiv \frac{dg}{dz} = g(z) (1 - g(z))
    $$

    Then

    $$
    h_i (1 - h_i) = g'(z_i^L)
    $$

- We define
    
    $$
    b_i^L \equiv h_i - y_i \qquad
    (i = 1,...,N_L)
    $$

    The subscript $L$ means that we are using values in the $L$th layer. Other $b^l$ vectors will be introduced recursively later.

Then

$$
D^l_{mn} \equiv \sum_{i=1}^{N_L} 
\frac{b_i^L}{g'(z_i^L)}
\frac{\partial h_i}{\partial \Theta_{mn}^l}
$$

Below we calculate the $\Theta$ derivatives of $D^l_{mn}$ from outer (larger $l$) to inner (smaller $l$) layers. 

- Layer $L$ (output)

    First, $h_i$ depends on $\Theta_{mn}^L$ via

    $$
    \begin{aligned}
        h_i \equiv a_i^L = g(z_i^L) \qquad
        z_i^L = \sum_{j=0}^{N_{L-1}} \Theta_{ij}^L a_j^{L-1}
    \end{aligned}
    $$

    Apply chain rule:

    $$
    \begin{aligned}
        \frac{\partial h_i}{\partial \Theta_{mn}^L}
        &= g'(z_i^L)
        \frac{\partial z_i^L}{\partial \Theta_{mn}^L}
        \\
        &= g'(z_i^L) \delta_{im} a_n^{L-1}
    \end{aligned}
    $$

    Then

    $$
    \begin{aligned}
        D^L_{mn} &= \sum_{i=1}^{N_L} 
        b_i^L \delta_{im} a_n^{L-1}
        \\
        &= b_m^L a_n^{L-1}
    \end{aligned}
    $$

- Layer $L-1$
    
    $h_i$ depends on $\Theta_{mn}^{L-1}$ via $a^{L-1}$:

    $$
    a_j^{L-1} = g(z_j^{L-1}) \qquad
    z_j^{L-1} = \sum_{k=0}^{N_{L-2}} \Theta_{jk}^{L-1} a_k^{L-2}
    $$

    We should be careful that only $a_j^{L-1}$ with $j \ne 0$ depend on $\Theta^{L-1}$ (while $a_0^{L-1} = 1$ is the bias term). Therefore

    $$
    \begin{aligned}
        \frac{\partial h_i}{\partial \Theta_{mn}^{L-1}}
        &= g'(z_i^L) \sum_{j=1}^{N_{L-1}}
        \frac{\partial z_i^L}{\partial a_j^{L-1}}
        g'(z_j^{L-1})
        \frac{\partial z_j^{L-1}}{\partial \Theta_{mn}^{L-1}}
        \\
        &= \Theta_{ij}^L \sum_{j=1}^{N_{L-1}} g'(z_i^L)
        g'(z_j^{L-1}) \delta_{jm} a_n^{L-2}
        \\
        &= g'(z_i^L) \Theta_{im}^L
        g'(z_m^{L-1}) a_n^{L-2}
    \end{aligned}
    $$

    and

    $$
    \begin{aligned}
        D^{L-1}_{mn} &= \sum_{i=1}^{N_L} 
        b_i^L \Theta_{im}^L g'(z_m^{L-1}) a_n^{L-2}
        \\
        &= b_m^{L-1} a_n^{L-2}
    \end{aligned}
    $$

    Here we defined

    $$
    b_m^{L-1} \equiv \sum_{i=1}^{N_L} 
    b_i^L \Theta_{im}^L g'(z_m^{L-1}) \quad
    (m = 1,...,N_{L-1})
    $$

    We can now see a pattern as we go into deeper layers. Let us calculate one more to see it more clearly.

- Layer $L-2$
    
    $h_i$ depends on $\Theta_{mn}^{L-2}$ via $a^{L-2}$:

    $$
    a_k^{L-2} = g(z_k^{L-2}) \qquad
    z_k^{L-2} = \sum_{l=0}^{N_{L-3}} \Theta_{kl}^{L-2} a_l^{L-3}
    $$

    Apply chain rule:

    $$
    \begin{aligned}
        \frac{\partial h_i}{\partial \Theta_{mn}^{L-2}}
        &= g'(z_i^L) \sum_{j=1}^{N_{L-1}}
        \frac{\partial z_i^L}{\partial a_j^{L-1}}
        g'(z_j^{L-1})
        \\ &\qquad \qquad
        \sum_{k=1}^{N_{L-2}}
        \frac{\partial z_j^{L-1}}{\partial a_k^{L-2}}
        g'(z_k^{L-2})
        \frac{\partial z_k^{L-2}}{\partial \Theta_{mn}^{L-2}}
        \\[2em]
        &= g'(z_i^L) \sum_{j=1}^{N_{L-1}}
        \Theta_{ij}^L g'(z_j^{L-1})
        \\ &\qquad \qquad
        \sum_{k=1}^{N_{L-2}}
        \Theta_{jk}^{L-1} g'(z_k^{L-2})
        \delta_{km} a_n^{L-3}
        \\[2em]
        &= g'(z_i^L) \sum_{j=1}^{N_{L-1}}
        \Theta_{ij}^L g'(z_j^{L-1})
        \\ &\qquad \qquad \qquad \times 
        \Theta_{jm}^{L-1} 
        g'(z_m^{L-2}) a_n^{L-3}
    \end{aligned}
    $$

    and

    $$
    \begin{aligned}
        D^{L-1}_{mn} 
        &= \sum_{i=1}^{N_L} \sum_{j=1}^{N_{L-1}}
        b_i^L \Theta_{ij}^L g'(z_j^{L-1})
        \\ &\qquad \qquad \times 
        \Theta_{jm}^{L-1} 
        g'(z_m^{L-2}) a_n^{L-3}
        \\
        &= \sum_{j=1}^{N_{L-1}} b^{L-1}_j
        \Theta_{jm}^{L-1} 
        g'(z_m^{L-2}) a_n^{L-3}
        \\
        &= b_m^{L-2} a_n^{L-3}
    \end{aligned}
    $$

    Here we defined

    $$
    b_m^{L-2} \equiv \sum_{j=1}^{N_{L-1}} 
    b_j^{L-1} \Theta_{jm}^{L-1} g'(z_m^{L-2}) \quad
    (m = 1,...,N_{L-2})
    $$

Now the recursive pattern of the definition of $b^l$ is quite clear:

$$
b_m^{l-1} = \sum_{i=1}^{N_l} 
b_i^l \Theta_{im}^l g'(z_m^{l-1}) 
\quad (l = 2,...,L)
$$

Finally we turn to the regularization:

$$
\begin{aligned}
    \frac{\partial J_\text{reg}}{\partial \Theta^l_{mn}}
    &= \frac{\lambda}{2M} 
    \frac{\partial}{\partial \Theta^l_{mn}}
    \sum_{\ell=1}^L \sum_{i=1}^{N_\ell} 
    \sum_{j=1}^{N_{\ell-1}} (\Theta_{ij}^{\ell})^2
    \\
    &= \frac{\lambda}{M} \times \begin{cases}
        \Theta^l_{mn} & n \ne 0
        \\
        0 & n = 0
    \end{cases}
\end{aligned}
$$

## Summary of Back Propagation Algorithm

<div class="result">

**Back Propagation Algorithm (with Regularization)**

*Below we treat vectors as columns.*

- From *one* example feature $a^0 \equiv x$ (with the bias term), Use forward propagation to obtain the activations (output) of each neuron
    
    $$
    \begin{aligned}
        \text{Input} \quad
        z_j^l &\equiv \sum_{k=0}^{N_{l-1}}
        \Theta^{l}_{jk} a_k^{l-1}
        = \Theta^l a^{l-1}
        \\
        \text{Act.} \quad 
        a_j^{l} &=
        \begin{cases}
            g(z_j^l) & j \ne 0 \\
            1 & j = 0 \, \text{(bias)}
        \end{cases}
    \end{aligned}
    $$

- Given the parameters $\Theta^l \in \mathbb{R}^{N_l\times (N_{l-1}+1)}$, recursively calculate the vector $b^l \in \mathbb{R}^{N_l}$
    
    $$
    \begin{aligned}
        b^L_m &\equiv h_m - y_m
        \\
        b_m^{l-1} &= \sum_{i=1}^{N_l} 
        b_i^l \Theta_{im}^l g'(z_m^{l-1}) 
    \end{aligned}
    $$

    In matrix notation:

    $$
    \begin{aligned}
        b^L &= h - y \\
        b^{l-1} &= [(\Theta^l)^\mathsf{T} b^l] * g'(z^{l-1})
    \end{aligned}
    $$

    The symbol $*$ means element-wise multiplication.

- Do the above calculation for each example. The derivative $\partial J/\partial \Theta^l_{mn}$ at the given values of $\Theta$ is then the sum of the following two parts:
    
    $$
    \begin{aligned}
        \frac{\partial J_0}{\partial \Theta^l_{mn}}
        &= \frac{1}{M} \sum_{\text{examples}} 
        b_m^{l} a_n^{l-1} 
        \\
        \frac{\partial J_\text{reg}}{\partial \Theta^l_{mn}}
        &= \frac{\lambda}{M} \Theta^l_{mj} \delta_{jn}
    \end{aligned}
    $$

    The summation sign adds up the contribution of all examples. In matrix notation:

    $$
    \frac{\partial J_0}{\partial \Theta^l}
    = \frac{1}{M} \sum_{\text{examples}} 
    b^{l} (a^{l-1})^\mathsf{T} 
    \in \mathbb{R}^{N_l\times (N_{l-1}+1)}
    $$

- After getting the derivatives, use optimization algorithms (e.g. gradient descent) to update $\Theta$ until we reached the optimal values. 

</div><br>

## Initialization of Parameters

We said above *given the parameters $\Theta_{mn}^l$*, but how should we initialize them?

A naive thinking is to initialize all of them to be the same value, say 0. 
