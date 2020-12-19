# Expectation Value on 2D Network

The expectation value of an operator $\mathcal{O}$ in a state $|\psi\rangle$ is

$$
\langle \mathcal{O} \rangle
= \frac{\langle \psi | \mathcal{O} |\psi \rangle}
{\langle \psi |\psi \rangle}
$$

When the denominator and the numerator can be expressed as a tensor network (by expressing $|\psi\rangle$ as a **tensor product state (TPS)**, and $\mathcal{O}$ as a circuit gate), we can use the TNR method to calculate them. 

In the following, we consider the special case where $\mathcal{O}$ is a two-site gate on neighboring tensors. 

- The denominator is just the ordinary uniform tensor network:
    

    
    Recall that in each RG step, we will get a normalization factor $f_i \, (i = 0,1,...)$:
    
    $$
    (\mathcal{T}_A^{(i)}, \mathcal{T}_B^{(i)})
    =\frac{1}{f_i} (T_A^{(i)}, T_B^{(i)})
    $$

    Suppose that there are $N_0$ tensors $A$ and $B$ respectively. After $a$ RG steps, we are left with the following network (i.e. $N_a = 2$):
    
    ```
            :   :
            |   |     
        ..- B - A -..
            |   |
        ..- A - B -..
            |   |
            :   :
    ```

    Then the state norm can be expressed as
    
    $$
    \begin{aligned}
        \langle \psi |\psi \rangle 
        &= \operatorname{Tr} (T_A^{(0)} T_B^{(0)})^{N_0}
        \\
        &= f_0^{2N_0} 
        \operatorname{Tr} (\mathcal{T}_A^{(0)} \mathcal{T}_B^{(0)})^{N_0}
        \\
        &= f_0^{2N_0}
        \operatorname{Tr} (f_1 \mathcal{T}_A^{(1)} f_1 \mathcal{T}_B^{(1)})^{N_1}
        \\
        &= f_0^{2N_0} f_1^{2N_1}
        \operatorname{Tr} (\mathcal{T}_A^{(1)} \mathcal{T}_B^{(1)})^{N_1}
        \\
        & \cdots \quad \text{(after } a \text{ RG steps)}
        \\
        &= f_0^{2N_0} f_1^{2N_1} \cdots f_a^{2N_a}
        \underbrace{
            \operatorname{Tr} 
            (\mathcal{T}_A^{(a)} \mathcal{T}_B^{(a)})^{N_a}
        }_{\text{normalized to 1}}
        \\
        &= f_0^{2N_0} f_1^{2N_1} \cdots f_a^{2N_a}
    \end{aligned}
    $$

- The numerator network is with impurity tensors. Suppose that in the $i$th RG step, we obtain normalization factor $f'_i \, (i = 1,2,...)$. After $a$ RG steps, the network will be reduced into four tensors

    ```
            :   :
            |   |     
        ..- D - C -..
            |   |
        ..- A'- B'-..
            |   |
            :   :
    ```

    Then the un-normalized expectation value is then

    $$
    \begin{aligned}
        \langle \psi |\mathcal{O}| \psi \rangle 
        &= \operatorname{Tr} (T_A^{(0)} T_B^{(0)})^{N_0}
        \\
        &= f_0^{2N_0} 
        \operatorname{Tr} (\mathcal{T}_A^{(0)} \mathcal{T}_B^{(0)})^{N_0}
        \\
        &= f_0^{2N_0}
        \operatorname{Tr} (f_1 \mathcal{T}_A^{(1)} f_1 \mathcal{T}_B^{(1)})^{N_1}
        \\
        &= f_0^{2N_0} f_1^{2N_1}
        \operatorname{Tr} (\mathcal{T}_A^{(1)} \mathcal{T}_B^{(1)})^{N_1}
        \\
        & \cdots \quad \text{(after } a \text{ RG steps)}
        \\
        &= f_0^{2N_0} f_1^{2N_1} \cdots f_a^{2N_a}
        \underbrace{
            \operatorname{Tr} 
            (\mathcal{T}_A^{(a)} \mathcal{T}_B^{(a)})^{N_a}
        }_{\text{normalized to 1}}
        \\
        &= f_0^{2N_0} f_1^{2N_1} \cdots f_a^{2N_a}
    \end{aligned}
    $$
