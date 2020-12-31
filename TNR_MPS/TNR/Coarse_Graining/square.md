# Coarse-Graining on Square Lattice

In this document we use the *loop convention* of tensors in Grassmann TNR. The coarse-graining in ordinary TNR is very similar. 

## Uniform Network

### Counter-Clockwise Rotation (Default Choice)

After SVD of the A, B tensors, the original network

```
    ● ↑   ↓ ● ↑   ↓ ●
    → B ← A → B ← A →
      ↓   ↑   ↓   ↑
    ← A → B ← A → B ←
    ● ↑   ↓ ● ↑   ↓ ●
    → B ← A → B ← A →
      ↓   ↑   ↓   ↑
    ← A → B ← A → B ←
    ● ↑   ↓ ● ↑   ↓ ●
```

becomes to (the squares labelled with ● is transformed into octagons)

```
    ●     ↑ B ↓     ●     ↑ B ↓     ●
          7 ← 4           7 ← 4
        ↗       ↘       ↗       ↘
    → 6           5 → 6           5 →
    A ↓           ↑ A ↓           ↑ A
    ← 1           2 ← 1           2 ←
        ↖       ↙       ↖       ↙ 
          0 → 3           0 → 3
    ●     ↑ B ↓     ●     ↑ B ↓     ●
          7 ← 4           7 ← 4
        ↗       ↘       ↗       ↘
    → 6           5 → 6           5 →
    A ↓           ↑ A ↓           ↑ A
    ← 1           2 ← 1           2 ←
        ↖       ↙       ↖       ↙ 
          0 → 3           0 → 3
    ●     ↑ B ↓     ●     ↑ B ↓     ●
```

In the network after RG, the network is rotated *counter-clockwise* by 45 degrees. We obtain the new A and B from

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

### Clockwise Rotation

In the other coarse-graining method, the network is rotated *clockwise* by 45 degrees:

```
    ●     ↑ A ↓     ●     ↑ A ↓     ●
          7 ← 4           7 ← 4
        ↗       ↘       ↗       ↘
    → 6           5 → 6           5 →
    B ↓           ↑ B ↓           ↑ B
    ← 1           2 ← 1           2 ←
        ↖       ↙       ↖       ↙ 
          0 → 3           0 → 3
    ●     ↑ A ↓     ●     ↑ A ↓     ●
          7 ← 4           7 ← 4
        ↗       ↘       ↗       ↘
    → 6           5 → 6           5 →
    B ↓           ↑ B ↓           ↑ B
    ← 1           2 ← 1           2 ←
        ↖       ↙       ↖       ↙ 
          0 → 3           0 → 3
    ●     ↑ A ↓     ●     ↑ A ↓     ●
```

The new tensors A, B are:

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
B, A = A.transpose(3,0,1,2), B.transpose(3,0,1,2)
```

## Network with Impurity Center

For the following network:

```
    ● ↑   ↓ ● ↑   ↓ ●
    → B ← A → B ← A →
      ↓   ↑   ↓   ↑
    ← A → D ← C → B ←
    ● ↑   ↓ ● ↑   ↓ ●
    → B ← A'→ B'← A →
      ↓   ↑   ↓   ↑
    ← A → B ← A → B ←
    ● ↑   ↓ ● ↑   ↓ ●
```

### Counter-Clockwise Rotation (Default Choice)

After one RG step: (the primed tensors are from the SVD of the DCA'B' network in the center)

```
    ●     ↑ B ↓     ●     ↑ B ↓     ●
          7 ← 4           7 ← 4
        ↗       ↘       ↗       ↘
    → 6           5 → 6           5 →
    A ↓           ↑ C ↓           ↑ A
    ← 1           2'← 1'          2 ←
        ↖       ↙       ↖       ↙ 
          0 → 3'          0'→ 3
    ●     ↑ D ↓     ●     ↑ B'↓     ●
          7 ← 4'          7'← 4
        ↗       ↘       ↗       ↘
    → 6           5'→ 6'          5 →
    A ↓           ↑ A'↓           ↑ A
    ← 1           2 ← 1           2 ←
        ↖       ↙       ↖       ↙ 
          0 → 3           0 → 3
    ●     ↑ B ↓     ●     ↑ B ↓     ●
```

In the network after RG, the tensors are rotated *counter-clockwise* by 45 degrees, but the network is rotated *clockwise* by 45 degrees.

Impurity tensors `A', B, C, D` are obtained from:

```
        1       0       1       0
        ↘       ↗       ↘       ↗ 
          5'→ 6'          5 → 6
          ↑ A'↓           ↑ C ↓
          2 ← 1           2'← 1'
        ↙       ↖       ↙       ↖
        2       3       2       3

        1       0       1       0
        ↖       ↙       ↖       ↙
          0'→ 3           0 → 3'
          ↑ B'↓           ↑ D ↓
          7'← 4           7 ← 4'
        ↗       ↘       ↗       ↘
        2       3       2       3
```
```python
# 'u' means the S matrices from uniform part 
A = combineA(S[6], S[5], Su[2], Su[1])
B = combineB(Su[3], S[0], S[7], Su[4])
C = combineA(Su[6], Su[5], S[2], S[1])
D = combineB(S[3], Su[0], Su[7], S[4])
```

Uniform tensors `A, B` are not affected by the impurity center:

```
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

### Clockwise Rotation

In another way to obtain the coarse-grained tensors, the network is rotated *clockwise* by 45 degrees:

```
    ●     ↑ A ↓     ●     ↑ A ↓     ●
          7 ← 4           7 ← 4
        ↗       ↘       ↗       ↘
    → 6           5 → 6           5 →
    B ↓           ↑ D ↓           ↑ B
    ← 1           2'← 1'          2 ←
        ↖       ↙       ↖       ↙ 
          0 → 3'          0'→ 3
    ●     ↑ A'↓     ●     ↑ C ↓     ●
          7 ← 4'          7'← 4
        ↗       ↘       ↗       ↘
    → 6           5'→ 6'          5 →
    B ↓           ↑ B'↓           ↑ B
    ← 1           2 ← 1           2 ←
        ↖       ↙       ↖       ↙ 
          0 → 3           0 → 3
    ●     ↑ A ↓     ●     ↑ A ↓     ●
```

The tensors are obtained through

```
    The impurity tensors A', B', C, D

        2       1       2       1
        ↘       ↗       ↘       ↗ 
          5'→ 6'          5 → 6
          ↑ B'↓           ↑ D ↓
          2 ← 1           2'← 1'
        ↙       ↖       ↙       ↖
        3       0       3       0

        2       1       2       1
        ↖       ↙       ↖       ↙
          0'→ 3           0 → 3'
          ↑ C ↓           ↑ A'↓
          7'← 4           7 ← 4'
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
Bu, Au = Au.transpose(3,0,1,2), Bu.transpose(3,0,1,2)

B, C, D, A = A.transpose(3,0,1,2), B.transpose(3,0,1,2), C.transpose(3,0,1,2), D.transpose(3,0,1,2)
```