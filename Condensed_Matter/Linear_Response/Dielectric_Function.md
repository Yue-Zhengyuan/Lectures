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

# The Density Self-Correlation Function

Consider the free electron gas

$$
H = \sum_\mathbf{k} \frac{k^2}{2m}
c_{\mathbf{k}\sigma}^\dagger c_{\mathbf{k}\sigma}
$$

We may also add a Coulomb interaction

$$
V_c = \frac{1}{2} 
\sum_{\mathbf{k},\mathbf{k}',\mathbf{q}} 
\frac{4\pi e^2}{q^2}
c_{\mathbf{k+q},\sigma}^\dagger
c_{\mathbf{k'-q},\sigma'}^\dagger
c_{\mathbf{k'},\sigma'}
c_{\mathbf{k},\sigma}
$$

Now we consider a perturbation (like adding a scalar potential to a group of charged)

$$
V = \int d^3x \, \phi(\mathbf{x}',t) \rho(\mathbf{x})
$$

The density-density correlation function is defined as

$$
\chi^R(\mathbf{x} - \mathbf{x}', t - t')
= -i\theta(t - t') \expect{[
    \rho(\mathbf{x}, t), 
    \rho(\mathbf{x}', t')
]}_0
$$
