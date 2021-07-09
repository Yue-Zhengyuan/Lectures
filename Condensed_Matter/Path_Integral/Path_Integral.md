<style>
    .katex {
        font-size: 1.1em;
    }
    .remark {
        border-radius: 15px;
        padding: 20px;
        background-color: SeaGreen;
        color: White;
    }
    .result {
        border-radius: 15px;
        padding: 20px;
        background-color: DarkSlateBlue;
        color: White;
    }
</style>

# Path Integral in Real Time

## Path Integral in Phase Space 

The **path integral** form of propagators is introduced in the (in position space) by inserting a series of identity at time $t_k=k\epsilon \, (k = 1,2,...,N-1)$ in the **propagator**:

$$
\begin{aligned}
    &\langle q_f|e^{-i H(p,q) T}|q_i\rangle
    \\
    &= \int dq_{N-1} \cdots dq_1
    \langle q_N|e^{-i H \epsilon}|q_{N-1}\rangle
    \cdots 
    \langle q_1|e^{-i H \epsilon}|q_0\rangle 
    \\
    &=\int \prod_{k=1}^{N-1} dq_k
    \prod_{j=0}^{N-1} 
    \langle q_{j+1}|1-i H \epsilon |q_j\rangle
\end{aligned}
$$

Here 

$$
|q_0\rangle =|q_i\rangle ,\, |q_N\rangle =|q_f\rangle ,
\quad 
\epsilon = T/N \, (N \to \infty)
$$

When the Hamiltonian has the classical form

$$
H(p,q) = \frac{1}{2m}p^2 + V(q)
$$

The propagator in each time step is

$$
\begin{aligned}
    &\langle q_{k+1}|1-i H(p,q) \epsilon |q_k\rangle 
    \\
    &= \int \frac{dp_k}{2\pi}
    \langle q_{k+1}|1-i H(p,q) \epsilon |p_k\rangle 
    \langle p_k|q_k \rangle 
    \\
    &= \int \frac{dp_k}{2\pi}
    (1-i H(p_k,q_k) \epsilon)
    \langle q_{k+1}|p_k \rangle \langle p_k|q_k \rangle 
    \\
    &= \int \frac{dp_k}{2\pi}
    (1-i H(p_k,q_k) \epsilon) e^{i p_k(q_{k+1}-q_k)}
    \\
    &= \int \frac{dp_k}{2\pi}
    (1-i H(p_k,q_k) \epsilon) e^{i p_k\dot{q}_k \epsilon}
    \\
    &= \int \frac{dp_k}{2\pi} 
    \exp \left[i \epsilon (
        p_k \dot{q}_k - H(p_k,q_k)
    ) \right]
\end{aligned}
$$

Now we have expressed the propagator as a **path integral in phase space**:

$$
\begin{aligned}
    &\langle q_f|e^{-i H(p,q) T}|q_i\rangle 
    \\
    &= \int \prod_{k=1}^{N-1} dq_k
    \prod_{k=0}^{N-1} \frac{dp_k}{2\pi}
    \prod_{j=0}^{N-1} \exp [
        i \epsilon  (p_j \dot{q}_j - H(p_j,q_j))
    ]
    \\
    &= \int [dq][dp] \exp \left[
        i \int_0^T dt \, (p \dot{q} - H(p,q))
    \right]
\end{aligned}
$$
