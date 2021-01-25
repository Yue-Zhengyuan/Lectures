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

# Descriptions of Time Evolution

## Schrödinger Picture

Consider a system in state $\ket{\psi}$, with Hamiltonian $H$ (which may depends on time). In the **Schrödinger picture** (denoted by subscript $S$), the time evolution is entirely due to the evolution of the state, described by the **Schrödinger's equation**:

$$
i\hbar \frac{\partial}{\partial t} \ket{\psi_S(t)}
= H \ket{\psi_S(t)}
$$

To find a formal solution $\ket{\psi_S(t)}$, we introduce the **time evolution operator** $U(t,t_0)$ so that

$$
\ket{\psi_S(t)} = U(t,t_0) \ket{\psi_S(t_0)}
$$

with $t_0$ some reference instant. 

The operator $U(t,t_0)$ has the following properties:

## Heisenberg Picture

There is another description of time evolution which gives the same result for the expectation values of operators. 

## Interaction Picture
