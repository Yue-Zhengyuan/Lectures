# GTNR Coarse-Graining on Square Lattice

In this document we use the *loop convention* of tensors in Grassmann TNR. The coarse-graining in ordinary TNR is very similar. 

## Counter-Clockwise Rotation (Default Choice)

After SVD of the A, B tensors, the original network

```
      ↑   ↓   ↑   ↓
    → B ← A → B ← A →
      ↓   ↑   ↓   ↑
    ← A → B ← A → B ←
      ↑   ↓   ↑   ↓
    → B ← A → B ← A →
      ↓   ↑   ↓   ↑
    ← A → B ← A → B ←
      ↑   ↓   ↑   ↓
```

becomes to

```
          ↑ A ↓           ↑ A ↓
          2 ← 1           2 ← 1
        ↙       ↖       ↙       ↖
    → 3           0 → 3           0 →
    B ↓           ↑ B ↓           ↑ B
    ← 4           7 ← 4           7 ←
        ↘       ↗       ↘       ↗ 
          5 → 6           5 → 6
          ↑ A ↓           ↑ A ↓
          2 ← 1           2 ← 1
        ↙       ↖       ↙       ↖
    → 3           0 → 3           0 →
    B ↓           ↑ B ↓           ↑ B
    ← 4           7 ← 4           7 ←
        ↘       ↗       ↘       ↗ 
          5 → 6           5 → 6
          ↑ A ↓           ↑ A ↓
```

In the network after RG, the tensors A, B are rotated *counter-clockwise* by 45 degrees, but the network is rotated *clockwise* by 45 degrees: (however, in ordinary TNR where there is no Grassmann metric issue, we shall rotate the tensors in the same way as the network)

```
    1       0       1       0
    ↘       ↗       ↖       ↙ 
      5 → 6           0 → 3
      ↑ A ↓           ↑ B ↓
      2 ← 1           7 ← 4
    ↙       ↖       ↗       ↘
    2       3       2       3
```

In the program, these are done by

```python
A = combineA(S[6], S[5], S[2], S[1])
B = combineB(S[3], S[0], S[7], S[4])
```

Therefore, in the next step of RG, we prefer to rotate back the tensor network by using another combination of the tensors `S[0]` to `S[7]`. 

## Clockwise Rotation

In the other coarse-graining method, the tensors A, B are rotated *clockwise* by 45 degrees, but the network is rotated *counter-clockwise* by 45 degrees:

```
          ↑ B ↓           ↑ B ↓
          2 ← 1           2 ← 1
        ↙       ↖       ↙       ↖
    → 3           0 → 3           0 →
    A ↓           ↑ A ↓           ↑ A
    ← 4           7 ← 4           7 ←
        ↘       ↗       ↘       ↗ 
          5 → 6           5 → 6
          ↑ B ↓           ↑ B ↓
          2 ← 1           2 ← 1
        ↙       ↖       ↙       ↖
    → 3           0 → 3           0 →
    A ↓           ↑ A ↓           ↑ A
    ← 4           7 ← 4           7 ←
        ↘       ↗       ↘       ↗ 
          5 → 6           5 → 6
          ↑ B ↓           ↑ B ↓
```

In the network after RG, the tensors A, B are rotated *clockwise* by 45 degrees, but the network is rotated *counter-clockwise* by 45 degrees:

```
    2       1       2       1
    ↘       ↗       ↖       ↙ 
      5 → 6           0 → 3
      ↑ B ↓           ↑ A ↓
      2 ← 1           7 ← 4
    ↙       ↖       ↗       ↘
    3       0       3       0
```

This can be implemented by the same code as the counter-clockwise rotation, with the following additional step:

```python
Ta, Tb = Tb.transpose(3,0,1,2), Ta.transpose(3,0,1,2)
```

## Network with Impurity Center

For the following network:

```
      ↑   ↓   ↑   ↓
    → B ← A → B ← A →
      ↓   ↑   ↓   ↑
    ← A → D ← C → B ←
      ↑   ↓   ↑   ↓
    → B ← A'→ B'← A →
      ↓   ↑   ↓   ↑
    ← A → B ← A → B ←
      ↑   ↓   ↑   ↓
```

After one RG step: (the primed tensors are from the SVD of the DCA'B' network in the center)

```
          ↑ A ↓           ↑ A ↓
          2 ← 1           2 ← 1
        ↙       ↖       ↙       ↖
    → 3           0 → 3           0 →
    B ↓           ↑ D ↓           ↑ B
    ← 4           7'← 4'          7 ←
        ↘       ↗       ↘       ↗ 
          5 → 6'          5'→ 6
          ↑ A'↓           ↑ C ↓
          2 ← 1'          2'← 1
        ↙       ↖       ↙       ↖
    → 3           0'→ 3'          0 →
    B ↓           ↑ B'↓           ↑ B
    ← 4           7 ← 4           7 ←
        ↘       ↗       ↘       ↗ 
          5 → 6           5 → 6
          ↑ A ↓           ↑ A ↓
```

In the network after RG, the tensors are rotated *counter-clockwise* by 45 degrees, but the network is rotated *clockwise* by 45 degrees.

- Impurity tensors `A', B, C, D`

    ```
        The impurity tensors A', B', C, D

            1       0       1       0
            ↘       ↗       ↘       ↗ 
              5 → 6'          5'→ 6
              ↑ A'↓           ↑ C ↓
              2 ← 1'          2'← 1
            ↙       ↖       ↙       ↖
            2       3       2       3

            1       0       1       0
            ↖       ↙       ↖       ↙
              0'→ 3'          0 → 3
              ↑ B'↓           ↑ D ↓
              7 ← 4           7'← 4'
            ↗       ↘       ↗       ↘
            2       3       2       3
    ```
    ```python
    # 'u' means the S matrices from uniform part 
    A = combineA(S[6], Su[5], Su[2], S[1])
    B = combineB(S[3], S[0], Su[7], Su[4])
    C = combineA(Su[6], S[5], S[2], Su[1])
    D = combineB(Su[3], Su[0], S[7], S[4])
    ```

- Uniform tensors `A, B`

    ```
        The uniform tensors A, B

            1       0       1       0
            ↘       ↗       ↖       ↙ 
              5 → 6           0 → 3
              ↑ A ↓           ↑ B ↓
              2 ← 1           7 ← 4
            ↙       ↖       ↗       ↘
            2       3       2       3
    ```
    ```python
    Au = combineA(Su[6], Su[5], Su[2], Su[1])
    Bu = combineB(Su[3], Su[0], Su[7], Su[4])
    ```

In another way to obtain the coarse-grained tensors, the tensors are rotated *counter-clockwise* by 45 degrees, but the network is rotated *clockwise* by 45 degrees.

```
          ↑ B ↓           ↑ B ↓
          2 ← 1           2 ← 1
        ↙       ↖       ↙       ↖
    → 3           0 → 3           0 →
    A ↓           ↑ C ↓           ↑ A
    ← 4           7'← 4'          7 ←
        ↘       ↗       ↘       ↗ 
          5 → 6'          5'→ 6
          ↑ D ↓           ↑ B'↓
          2 ← 1'          2'← 1
        ↙       ↖       ↙       ↖
    → 3           0'→ 3'          0 →
    A ↓           ↑ A'↓           ↑ A
    ← 4           7 ← 4           7 ←
        ↘       ↗       ↘       ↗ 
          5 → 6           5 → 6
          ↑ B ↓           ↑ B ↓
```

The tensors are obtained through

```
    The impurity tensors A', B', C, D

        2       1       2       1
        ↘       ↗       ↘       ↗ 
          5 → 6'          5'→ 6
          ↑ D ↓           ↑ B'↓
          2 ← 1'          2'← 1
        ↙       ↖       ↙       ↖
        3       0       3       0

        2       1       2       1
        ↖       ↙       ↖       ↙
          0'→ 3'          0 → 3
          ↑ A'↓           ↑ C ↓
          7 ← 4           7'← 4'
        ↗       ↘       ↗       ↘
        3       0       3       0

    The uniform tensors A, B

        2       1       2       1
        ↘       ↗       ↖       ↙ 
          5 → 6           0 → 3
          ↑ B ↓           ↑ A ↓
          2 ← 1           7 ← 4
        ↙       ↖       ↗       ↘
        3       0       3       0
```

These tensors can be obtained from the previous method with appropriate transpositions:

```python
Au, Bu = Bu.transpose(3,0,1,2), Au.transpose(3,0,1,2)

A, B, C, D = B.transpose(3,0,1,2), C.transpose(3,0,1,2), D.transpose(3,0,1,2), A.transpose(3,0,1,2)
```