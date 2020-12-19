# $Z_q$ Symmetry in Statistical Models

## 

We use a tensor with 4 axes (i.e. square tensor network) to demonstrate the idea. 

```
                 D
                 |
                 u
                 |
    l' --D-- l --T-- r --D-- r'
                 d
```

## Examples

### Classical 2D Ising Model

$$
H = -J \sum_{\langle i, j \rangle} s_i s_j
$$

where $s_i$ is the spin direction at site $i$, which can only be one of the following:

$$
s_i = \begin{cases}
    0, &\text{spin up} \\
    1, &\text{spin down}
\end{cases}
$$

The phase transition temperature is $\beta = \ln(1 + \sqrt{2}) / 2$.

The tensor network represents the partition function

$$
Z = e^{-\beta H}
$$

### Quantum (1+1)D Transverse Field Ising Model (TFIM)

$$
H = -J \sum_{i} \sigma_i^z \sigma_{i+1}^z + h \sum_i \sigma_i^x
$$

The critical point is $h / J = 1$.

### Classical 2D $q$-State Clock Model

$$
H = -J \sum_{\langle i, j \rangle} \cos(\theta_i - \theta_j)
$$

where $\theta_i$ is the spin direction at site $i$, taking only the following values:

$$
\theta_i = 2 \pi n_i / q \quad
n_i = 0,1,2,..., q-1
$$