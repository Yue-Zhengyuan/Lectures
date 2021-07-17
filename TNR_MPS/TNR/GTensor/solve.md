# Linear Equations of Grassmann Tensors

*Program implementation: `gtensor.solve`*

Suppose that the contraction of the $a,c,...$th axes of a *known* Grassmann tensor $\mathbf{A}$ with the $b,d,...$th axes of an *unknown* Grassmann tensor $\mathbf{X}$ is equal to another *known* Grassmann tensor $\mathbf{B}$, i.e.

$$
\begin{align*}
    &[\mathbf{A}(\theta)  \mathbf{X}(\eta)]_{i_1 ... \cancel{i_a} ... \cancel{i_c} ... i_r, j_1... \cancel{j_b} ... \cancel{j_d} ... j_s}^{m_1 ... \cancel{m_a} ... \cancel{m_c} ... m_r, n_1 ... \cancel{n_b} ... \cancel{n_d} ... n_s}
    \\
    &= \sum_{m_a,n_b} \sum_{m_c,n_d} \cdots \sum_{i_a,j_b} \sum_{i_c,j_d} \cdots
    (-1)^{P(p(a,b,c,d,...) | \{m, n\})} 
    \\ &\quad \times
    g_{ab}^{m_a} g_{cd}^{m_c} \cdots
    \delta_{m_a n_b} \delta_{m_c n_d} \cdots
    \delta_{i_a j_b} \delta_{i_c j_d} \cdots
    A_{i_1 ... i_r}^{m_1 ... m_r} 
    X_{j_1 ... j_s}^{n_1 ... n_s} 
    \\ &\quad \times
    \theta_1^{m_1} \cdots \cancel{\theta_a^{m_a}} \cdots \cancel{\theta_c^{m_c}} \cdots \theta_r^{m_r} 
    \eta_1^{n_1} \cdots \cancel{\eta_b^{n_b}} \cdots \cancel{\eta_d^{m_d}} \cdots \eta_s^{n_s}
    \\
    &= \mathbf{B}(\theta, \eta)_{i_1 ... \cancel{i_a} ... \cancel{i_c} ... i_r, j_1... \cancel{j_b} ... \cancel{j_d} ... j_s}^{m_1 ... \cancel{m_a} ... \cancel{m_c} ... m_r, n_1 ... \cancel{n_b} ... \cancel{n_d} ... n_s}
\end{align*}
$$

Now we want to solve this linear equation for $\mathbf{X}$.

## Transpose $A, X$ to Simplify Contraction

To get rid of the annoying parity $P$, we first transpose both $A$ and $X$ properly:

- In $A$, transpose axes $a,c,...$ to position $r,r-1,...$
- In $X$, transpose axes $b,d,...$ to position $1,2,...$

This transposition obviously does not affect $B$. We shall then solve for this transposed $X$, and restore the correct axis order at the final stage. 

In the following, $A, X$ refer to the already transposed tensors. Suppose that there are $q$ pairs of axes to be contracted, then (omitting the Grassmann variables)

$$
\begin{align*}
    &[A  X]_{i_1 ... i_{r-q}, j_{q+1} ... j_s}^{m_1 ... m_{r-q}, n_{q+1} ... n_s}
    \\
    &= \sum_{n_1, ..., n_q} \sum_{j_1, ..., j_q}
    g_{r,1}^{n_1} g_{r-1,2}^{n_2} \cdots g_{r-q+1,q}^{n_q}
    A_{i_1 ... i_{r-q}, j_q ... j_1}^{m_1 ... m_{r-q}, n_q ... n_1} 
    X_{j_1 ... j_q, j_{q+1} ... j_s}^{n_1 ... n_q, n_{q+1} ... n_s} 
    \\
    &= \sum_{n_1, ..., n_q} \sum_{j_1, ..., j_q}
    \tilde{A}_{i_1 ... i_{r-q}, j_q ... j_1}^{m_1 ... m_{r-q}, n_q ... n_1} 
    X_{j_1 ... j_q, j_{q+1} ... j_s}^{n_1 ... n_q, n_{q+1} ... n_s} 
    \\
    &= B_{i_1 ... i_{r-q}, j_{q+1} ... j_s}^{m_1 ... m_{r-q}, n_{q+1} ... n_s}
\end{align*}
$$

Here we have absorbed the Grassmann metrics $g$ into $\tilde{A}$. 

## Reshape Tensor to Matrix

Next we merge the axes of $\tilde{A}, X, B$ (note that the last $q$ axes of $\tilde{A}$ should be merged in *reversed order*, i.e. using the `order = -1` option):

$$
\begin{align*}
    \sum_{n_1, ..., n_q} &\sum_{j_1, ..., j_q}
    \tilde{A}_{(i_1 ... i_{r-q})(j_q ... j_1)}^{(m_1 ... m_{r-q})(n_q ... n_1)} 
    X_{(j_1 ... j_q)(j_{q+1} ... j_s)}^{(n_1 ... n_q)(n_{q+1} ... n_s)} \\
    &= B_{(i_1 ... i_{r-q})(j_{q+1} ... j_s)}^{(m_1 ... m_{r-q})(n_{q+1} ... n_s)}
    \Rightarrow \sum_{Q,J}
    \tilde{A}_{I J}^{M Q} X_{J K}^{Q N} = B_{I K}^{M N}    
\end{align*}
$$

Now we have reduced the Grassmann tensor equation to several ordinary linear equations.

## Solve the Linear Equations

### Case 1: Both $A,B$ are of Even Parity

This case is most common in physical applications. We explicitly write down the four sets of linear equations:

$$
\begin{cases}
    \tilde{A}_{I J}^{0 Q} X_{J K}^{Q 0} 
    = \tilde{A}_{I J}^{0 0} X_{J K}^{0 0} = B_{I K}^{0 0} \\
    \tilde{A}_{I J}^{0 Q} X_{J K}^{Q 1} 
    = \tilde{A}_{I J}^{0 0} X_{J K}^{0 1} = B_{I K}^{0 1} \equiv 0 \\
    \tilde{A}_{I J}^{1 Q} X_{J K}^{Q 0} 
    = \tilde{A}_{I J}^{1 1} X_{J K}^{1 0} = B_{I K}^{1 0} \equiv 0\\
    \tilde{A}_{I J}^{1 Q} X_{J K}^{Q 1} 
    = \tilde{A}_{I J}^{1 1} X_{J K}^{1 1} = B_{I K}^{1 1} \\
\end{cases}
$$

Thus we obtain (when the required inverse matrices exist)

$$
\begin{cases}
    X^{0 0} = (\tilde{A}^{0 0})^{-1} B^{0 0}, 
    X^{1 1} = (\tilde{A}^{1 1})^{-1} B^{1 1} \\
    X^{0 1} = 0, 
    X^{1 0} = 0
\end{cases}
\text{(Even parity)}
$$

### Case 2: Both $A,B$ are of Odd Parity

$$
\begin{cases}
    \tilde{A}_{I J}^{0 Q} X_{J K}^{Q 0} 
    = \tilde{A}_{I J}^{0 1} X_{J K}^{1 0} = B_{I K}^{0 0} \equiv 0 \\
    \tilde{A}_{I J}^{0 Q} X_{J K}^{Q 1} 
    = \tilde{A}_{I J}^{0 1} X_{J K}^{1 1} = B_{I K}^{0 1} \\
    \tilde{A}_{I J}^{1 Q} X_{J K}^{Q 0} 
    = \tilde{A}_{I J}^{1 0} X_{J K}^{0 0} = B_{I K}^{1 0} \\
    \tilde{A}_{I J}^{1 Q} X_{J K}^{Q 1} 
    = \tilde{A}_{I J}^{1 0} X_{J K}^{0 1} = B_{I K}^{1 1} \equiv 0\\
\end{cases}
$$

$$
\Longrightarrow
\begin{cases}
    X^{0 0} = (\tilde{A}^{1 0})^{-1} B^{1 0}, 
    X^{1 1} = (\tilde{A}^{0 1})^{-1} B^{0 1} \\
    X^{0 1} = 0, 
    X^{1 0} = 0
\end{cases}
\text{(Even parity)}
$$

### Case 3: $A$ is of Even Parity, $B$ is of Odd Parity

$$
\begin{cases}
    \tilde{A}_{I J}^{0 Q} X_{J K}^{Q 0} 
    = \tilde{A}_{I J}^{0 0} X_{J K}^{0 0} = B_{I K}^{0 0} \equiv 0 \\
    \tilde{A}_{I J}^{0 Q} X_{J K}^{Q 1} 
    = \tilde{A}_{I J}^{0 0} X_{J K}^{0 1} = B_{I K}^{0 1} \\
    \tilde{A}_{I J}^{1 Q} X_{J K}^{Q 0} 
    = \tilde{A}_{I J}^{1 1} X_{J K}^{1 0} = B_{I K}^{1 0} \\
    \tilde{A}_{I J}^{1 Q} X_{J K}^{Q 1} 
    = \tilde{A}_{I J}^{1 1} X_{J K}^{1 1} = B_{I K}^{1 1} \equiv 0\\
\end{cases}
$$

$$
\Longrightarrow
\begin{cases}
    X^{0 0} = 0, 
    X^{1 1} = 0 \\
    X^{0 1} = (\tilde{A}^{0 0})^{-1} B^{0 1}, 
    X^{1 0} = (\tilde{A}^{1 1})^{-1} B^{1 0}
\end{cases}
\text{(Odd parity)}
$$

### Case 4: $A$ is of Odd Parity, $B$ is of Even Parity

$$
\begin{cases}
    \tilde{A}_{I J}^{0 Q} X_{J K}^{Q 0} 
    = \tilde{A}_{I J}^{0 1} X_{J K}^{1 0} = B_{I K}^{0 0} \\
    \tilde{A}_{I J}^{0 Q} X_{J K}^{Q 1} 
    = \tilde{A}_{I J}^{0 1} X_{J K}^{1 1} = B_{I K}^{0 1} \equiv 0\\
    \tilde{A}_{I J}^{1 Q} X_{J K}^{Q 0} 
    = \tilde{A}_{I J}^{1 0} X_{J K}^{0 0} = B_{I K}^{1 0} \equiv 0\\
    \tilde{A}_{I J}^{1 Q} X_{J K}^{Q 1} 
    = \tilde{A}_{I J}^{1 0} X_{J K}^{0 1} = B_{I K}^{1 1} \\
\end{cases}
$$

$$
\Longrightarrow
\begin{cases}
    X^{0 0} = 0, 
    X^{1 1} = 0 \\
    X^{0 1} = (\tilde{A}^{1 0})^{-1} B^{1 1}, 
    X^{1 0} = (\tilde{A}^{0 1})^{-1} B^{0 0}
\end{cases}
\text{(Odd parity)}
$$

## Parity of the Solution $X$

From properties of Grassmann tensor contraction, $P(A) + P(X) = P(B) \pmod{2}$. Therefore

$$
P(X) = P(A) + P(B) \pmod{2}
$$

This is verified in the four cases above. 

## Recover Tensor Shape and Axes Order of $X$

After finding the solution $X_{J K}^{Q N}$, we split the two big axes to recover the tensor shape of $X$: 

$$
X_{J K}^{Q N}
\xrightarrow{\text{split axes}}
X_{(j_1 ... j_q)(j_{q+1} ... j_s)}^{(n_1 ... n_q)(n_{q+1} ... n_s)}
$$

Finally, transpose $X$ to recover the original order of axes. Now we have finished solving the equation $\mathbf{A}  \mathbf{X} = \mathbf{B}$.