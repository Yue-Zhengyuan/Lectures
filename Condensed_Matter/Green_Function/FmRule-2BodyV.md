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

# Feynman Rules

<font size=5>

**Example: Two-Body Interactions**

</font>

In the following we illustrate the perturbative expansion of 2-point functions (Green's function, $n = 2$) 

$$
iG_{\alpha \beta}(t - t')
\equiv \amp{\Psi_0}{T[a_\alpha(t) a^\dagger_\beta(t')]}{\Psi_0}
$$

using a Hamiltonian with two-body interactions (in interaction picture):

$$
\begin{aligned}
    V(t) = \frac{1}{2} V_{\gamma \delta, \epsilon \theta} 
    a_\gamma^\dagger(t) a_\delta^\dagger(t)
    a_\theta(t) a_\epsilon(t)
\end{aligned}
$$

## Zeroth Order

The zeroth order term is just the Green's function in free system:

$$
iG_{\alpha \beta}^{(0)} (t - t')
\equiv \amp{0}{T[a_\alpha(t) a^\dagger_\beta(t')]}{0}
$$

We note that since $a_\alpha a^\dagger_\beta$ is already in normal order, the zeroth term is the same as the contraction:

$$
a^\bullet_\alpha(t) a^{\dagger \bullet}_\beta(t')
= iG_{\alpha \beta}^{(0)} (t - t')
$$

The application of Wick's theorem is then made simple.

## First Order Terms

$$
i G^{(1)}_{\alpha \beta}(t - t')
= (-i) \int_{-T}^T dt_1 \,
\amp{0}{T[V(t_1) a_\alpha(t) a^\dagger_\beta(t')]}{0}
$$

## Second Order Terms

$$

$$

## Summary: The Feynman Rules