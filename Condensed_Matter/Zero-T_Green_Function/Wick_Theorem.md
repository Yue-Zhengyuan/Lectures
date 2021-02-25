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

# Wick's Theorem

## Normal Ordering

Under most cases, the **normal ordering** means that we put the creation operators in front of the annihilation operators, so that the normal-ordered product will have zero vacuum expectation value. For example

$$
N[a_\alpha a^\dagger_\beta]
= \pm a^\dagger_\beta a_\alpha
\qquad \begin{aligned}
    \text{boson} &: + \\
    \text{fermion} &: -
\end{aligned}
$$

In general, the normal ordering shares the following property with time ordering when permuting the operators:

$$
N[A_1 A_2 \cdots]
= (\pm 1)^\sigma N[A_{\sigma(1)} A_{\sigma(2)} \cdots]
\qquad \begin{aligned}
    \text{boson} &: + \\
    \text{fermion} &: -
\end{aligned}
$$

## Contraction

<div class="result">

**Contraction of two operators:**

$$
A^\bullet B^\bullet = T[AB] - N[AB]
$$

</div><br>

## Wick's Theorem

<div class="result">

**Wick's theorem:**

$$
T[AB...] = N[AB ... + \text{sum of all possible contractions}]
$$

</div><br>

*Proof (by induction)*:

First, the case with only 2 operators is just a repetition of the definition of contraction:

$$
T[AB] = N[AB] + A^\bullet B^\bullet
$$

