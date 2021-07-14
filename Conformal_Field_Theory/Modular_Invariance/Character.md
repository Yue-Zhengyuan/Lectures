# Virasoro Character

## Virasoro Characters

For a Verma module $V(c,h)$, we define its **character** as

$$
\chi_{(c,h)}(\tau)
= \text{Tr } q^{L_0-c/24}
= \sum_{n=0}^{\infty} \dim (h+n) \times q^{n+h-c/24}
$$

Here $q\equiv \exp (2 \pi i \tau) \, (\tau \in \mathbb{C})$, and $\dim (h+n)$ is the number of linearly independent states at level $n$, which is equal to $p(n)$. Hence

$$
\chi_{(c,h)}(\tau)
= q^{h-c/24} \sum_{n=0}^{\infty} p(n) q^n
=\frac{q^{h-c/24}}{\varphi (q)}
$$

*Remark*:

- The complex variable $\tau$ is in fact the **modular parameter** to be introduced later when we consider CFT on a torus.

- Introducing the **Dedekind function**

    $$
    \eta (\tau)\equiv q^{1/24} \varphi (q)=q^{1/24} \prod_{n=1}^{\infty}  \left(1-q^n\right)
    $$

    then we can express the character as

    $$
    \chi_{(c,h)}(\tau)
    =\frac{q^{h+(1-c)/24}}{\eta (\tau)}
    $$