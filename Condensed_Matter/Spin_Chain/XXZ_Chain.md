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

# XXZ Spin Chain

## The Luttinger Liquid Phase

<center>
<img src="images/xxz_phase.png" width="300pt">
</center>

The XXZ chain is in the Luttinger liquid phase when

$$
-1 \le \frac{J_z}{J_\perp} \le 1
\quad \text{or} \quad
-1 \le \frac{V}{2t} \le 1
$$

By comparison with Bethe ansatz exact solution, the Luttinger parameter (compactified radius) $K$ and the velocity $u$ can be determined as ($0 \le g \le 1$)

$$
\frac{J_z}{J_\perp} = -\cos (\pi g)
\  \Rightarrow \  \left\{
\begin{align*}
    K &= \frac{1}{2g} \\
    u &= \frac{1}{1-g} \sin(\pi(1-g)) \frac{J_\perp}{2}
\end{align*}
\right.
$$

To recast this result, 