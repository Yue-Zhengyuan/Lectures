# Transfer Matrices: <br>Construction

## Input Tensor Conventions 

In the original tensor network, the two kinds of tensors $A$ and $B$ are contracted using the following choice of Grassmann metrics (which I call the **natural convention**, since this is *naturally* used in the network of imaginary time evolution of a fermion MPS). In this choice, all arrows go downward or rightward. The numbers on the axes of each tensor is the axis order.

```
            :           :
            1           1    
            ↓           ↓
    ... 2 → A → 0...2 → B → 0 ...
            ↓           ↓
            3           3
            :           :
            1           1
            ↓           ↓
    ... 2 → B → 0...2 → A → 0 ...
            ↓           ↓
            3           3
            :           :
```

However, in program implementation, we prefer the following choice (which I call the **loop convention**, since the arrows on each square of the network form a *closed loop*). This choice makes it easier to find projectors. 

```
            :           :
            1           1    
            ↓           ↑
    ... 2 ← A → 0...2 → B ← 0 ...
            ↑           ↓
            3           3
            :           :
            1           1
            ↑           ↓
    ... 2 → B ← 0...2 ← A → 0 ...
            ↓           ↑
            3           3
            :           :
```

The conversion between these two conventions is achieved by the code

```python
a = a.flip_gSign(2, 3)
```

this reverses the Grassmann metric on all contractions involving the 2nd and the 3rd axes of `a`. Equivalently, we can use

```python
b = b.flip_gSign(0, 1)
# or
a, b = a.flip_gSign(2), b.flip_gSign(1)
# or
a, b = a.flip_gSign(3), b.flip_gSign(0)
```

## Construction of Large Transfer Matrix

The size of transfer matrix can be huge. For example, the matrix of 4 tensors' wide will have dimension $D^4 \times D^4$, where $D$ is the dimension of one axis of the tensor. Such a large matrix cannot be handled by SciPy and NumPy. 

Thus, instead of specifying every entry of the matrix, we tell the computer how the matrix act on an arbitrary *vector*. SciPy then construct a [linear operator][lo_doc] (`scipy.sparse.linalg.LinearOperator`) based on this information, which uses much less memory. Eigenvalues of this operator can be found using other functions provided in the module `scipy.sparse.linalg`. 

[lo_doc]: https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.linalg.LinearOperator.html

## The Smallest (2 $\times$ 2) Transfer Matrices

From the two tensors $A, B$ we can construct four different transfer matrices (TM, denoted by $\mathcal{T}$).

### Row (Real Space) Transfer Matrices

- With periodic boundary condition (PBC)

    ```
        Loop convention      Natural convention

            0   1                   0   1
            |   |                   |   |
        ..← A → B ←..           ..→ A → B →..
            ↑   ↓                   ↓   ↓
        ..→ B ← A →..           ..→ B → A →..
            ↓   ↑                   ↓   ↓
            2   3                   2   3
            :   :                   :   :
            0   1                   0   1
            ↓___↑                   ↓___↓
            vec                     vec
    ```

    Loop convention:

    ```python
    ab = gt.tensordot(a, b, [(0,2), (2,0), (1,1)])
    ba = gt.tensordot(b, a, [(0,2), (2,0), (-1,-1)])
    tm_pbc = gt.tensordot(ab, ba, [(1,3), (0,2), (-1,1)])
    # apply on `vec`
    gt.tensordot(tm_pbc, vec, [(2,3), (0,1), (1,-1)])
    ```

    Natural convention:

    ```python
    ab = gt.tensordot(a, b, [(0,2), (2,0), (1,-1)])
    ba = gt.tensordot(b, a, [(0,2), (2,0), (1,-1)])
    tm_pbc = gt.tensordot(ab, ba, [(1,3), (0,2), (1,1)])
    # apply on `vec`
    gt.tensordot(tm_pbc, vec, [(2,3), (0,1), (1,1)])
    ```

- With anti-periodic boundary condition (APBC)

    ```
        Loop convention      Natural convention

            0   1                   0   1
            |   |                   |   |
        ..→ A → B →..           ..← A → B ←..
            ↑   ↓                   ↓   ↓
        ..← B ← A ←..           ..← B → A ←..
            ↓   ↑                   ↓   ↓
            2   3                   2   3
            :   :                   :   :
            0   1                   0   1
            ↓___↑                   ↓___↓
            vec                     vec
    ```

    Loop convention:

    ```python
    ab = gt.tensordot(a, b, [(0,2), (2,0), (1,-1)])
    ba = gt.tensordot(b, a, [(0,2), (2,0), (-1,1)])
    tm_apbc2 = gt.tensordot(ab, ba, [(1,3), (0,2), (-1,1)])
    gt.tensordot(tm_apbc, vec, [(2,3), (0,1), (1,-1)])
    ```

    Natural convention:

    ```python
    ab = gt.tensordot(a, b, [(0,2), (2,0), (1,1)])
    ba = gt.tensordot(b, a, [(0,2), (2,0), (1,1)])
    tm_apbc2 = gt.tensordot(ab, ba, [(1,3), (0,2), (1,1)])
    gt.tensordot(tm_apbc, vec, [(2,3), (0,1), (1,1)])
    ```

### Column (Virtual Space) Transfer Matrix

In fact, for quantum models we should use the eigenvalues $\tilde{\lambda}_i$ in the *horizontal* direction. To save writing in the program, this is done by rotate clockwise the tensors by 90 degrees and still calculate the vertical eigenvalues:

```
        1               2    
        ↓               ↓
    2 → A → 0  -->  3 ← A ← 1
        ↓               ↓
        3               0
```

which is done by the transposition

```python
# same for tensor b
a = a.transpose(3,0,1,2)
```

i.e. we are calculating

```
    PBC:

        :   :
        ↓   ↓
    1 - A → B → 3 .. 1 →
        ↓   ↓           | vec
    0 - B → A → 2 .. 0 →
        ↓   ↓
        :   :

    Anti-PBC:

        :   :
        ↑   ↑     
    0 - A → B → 2 .. 0 →
        ↓   ↓           | vec
    1 - B → A → 3 .. 1 →
        ↑   ↑
        :   :
```

### Eigenvalues and Eigenvectors

*Note: In this section we shall use the **natural convention** to avoid complications caused by the Grassmann metrics when merging axes for contraction.*

In order to see that we are really acting on a *vector*, and which matrix does the eigenvalues belong to, we can merge the first two axes and the last two axes of the transfer tensor, to get a real *matrix*:

$$
\begin{aligned}
    \mathcal{T}_{(i_0 i_1)(i_2 i_3)}^{(n_0 n_1)(n_2 n_3)}
    v_{(i_2 i_3)}^{(n_2 n_3)}
    &\xrightarrow[\text{for contraction}]{\text{transpose}}
    \mathcal{T}_{(i_0 i_1)(i_3 i_2)}^{(n_0 n_1)(n_3 n_2)}
    v_{(i_2 i_3)}^{(n_2 n_3)}
    \\ \\ & \xrightarrow{\text{merge axes}}
    \mathcal{T}_{I J}^{M N} v_J^N
\end{aligned}
$$

This is done by (`tm2` stands for either `tm_pbc` or `tm_apbc`)

```python
tm2_ = gt.merge_axes(tm2, (2,2), (1,-1))
```

note that `order = -1` option should be used when merging the second set of axes. 

In physical applications, $\mathcal{T}$ has *even parity*, while $v$ can be either even or odd. 

- $v$ is of even parity

    $$
    \mathcal{T}_{I J}^{M N} v_J^N
    =
    \mathcal{T}_{I J}^{0 0} v_J^0
    $$

    Thus the eigenvalues and eigenvectors belong to the matrix $\mathcal{T}^{0 0}$, denoted by the labels `p0` and `a0` in the program, depending on whether $\mathcal{T}$ is constructed with PBC or anti-PBC. 

- $v$ is of odd parity

    $$
    \mathcal{T}_{I J}^{M N} v_J^N
    =
    \mathcal{T}_{I J}^{1 1} v_J^1
    $$

    Thus the eigenvalues and eigenvectors belong to the matrix $\mathcal{T}^{1 1}$, denoted by the labels `p1` and `a1` in the program. 

## The 4 $\times$ 2 Row Transfer Matrix

*Note: In this section we use the **natural convention**.*

### Eigenvalues and Eigenvectors

```
    Natural convention

        0   1   2   3
        |   |   |   |
    ..→ A → B → A → B →..
        ↓   ↓   ↓   ↓
    ..→ B → A → B → A →..
        ↓   ↓   ↓   ↓
        4   5   6   7
        :   :   :   :
        0   1   2   3
        ↓___↓___↓___↓
            vec
```

Similar to the 2 $\times$ 2 case, we can merge the first four axes and the last four axes of the transfer tensor, to get a real *matrix*:

$$
\begin{aligned}
    &\mathcal{T}_{(i_0 ... i_3)(i_4 ... i_7)}^{(n_0 ... n_3)(n_4 ... n_7)}
    v_{(i_4 ... i_7)}^{(n_4 ... n_7)}
    \\ \\
    &\xrightarrow[\text{for contraction}]{\text{transpose}}
    \mathcal{T}_{(i_0 ... i_3)(i_7 ... i_4)}^{(n_0 ... n_3)(n_7 ... n_4)}
    v_{(i_4 ... i_7)}^{(n_4 ... n_7)}
    \\ \\
    & \xrightarrow{\text{merge axes}}
    \mathcal{T}_{I J}^{M N} v_J^N
\end{aligned}
$$

This is done by

```python
tm4_ = gt.merge_axes(tm4, (4,4), (1,-1))
```

Thus:

- $v$ is of even parity

    $$
    \mathcal{T}_{I J}^{M N} v_J^N
    =
    \mathcal{T}_{I J}^{0 0} v_J^0
    $$

    The eigenvalues and eigenvectors belong to the matrix $\mathcal{T}^{0 0}$, denoted by the labels `p0` and `a0`. 

- $v$ is of odd parity

    $$
    \mathcal{T}_{I J}^{M N} v_J^N
    =
    \mathcal{T}_{I J}^{1 1} v_J^1
    $$

    The eigenvalues and eigenvectors belong to the matrix $\mathcal{T}^{1 1}$, denoted by the labels `p1` and `a1`. 

However, under some cases (e.g. [computing on the Klein bottle](trsf_mat_on_klein_bottle.md)), we do not want to merge the axes of $\mathcal{T}$ so completely. Suppose we only merge two axes together:

$$
\begin{aligned}
    &\mathcal{T}_{(i_0 i_1)(i_2 i_3)(i_4 i_5)(i_6 i_7)}^{(n_0 n_1)(n_2 n_3)(n_4 n_5)(n_6 n_7)}
    v_{(i_4 i_5)(i_6 i_7)}^{(n_4 n_5)(n_6 n_7)}
    \\ \\
    &\xrightarrow[\text{for contraction}]{\text{transpose}}
    \mathcal{T}_{(i_0 i_1)(i_2 i_3)(i_5 i_4)(i_7 i_6)}^{(n_0 n_1)(n_2 n_3)(n_5 n_4)(n_7 n_6)}
    v_{(i_4 i_5)(i_6 i_7)}^{(n_4 n_5)(n_6 n_7)}
    \\ \\
    & \xrightarrow{\text{merge axes}}
    \mathcal{T}_{I J K L}^{M N P Q} v_{K L}^{P Q}
\end{aligned}
$$

This is done by

```python
tm4_ = gt.merge_axes(tm4, (2,)*4, (1,1,-1,-1))
```

which can further be reduced to matrix form by the same code used for the 2 $\times$ 2 transfer matrix:

```python
tm4__ = gt.merge_axes(tm4_, (2,2), (1,-1))
```

### Approximation Method

The 4 $\times$ 2 row transfer matrix at RG step $i$ can be approximated by the following transfer matrix at RG step $i+1$ (before normalizing the tensors using the 2 $\times$ 2 norm)
