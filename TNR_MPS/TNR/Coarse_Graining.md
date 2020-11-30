# Two Methods of Coarse Graining

In this document we use the *loop convention* of tensors.

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
          ↑   ↓           ↑   ↓
          2 ← 1           2 ← 1
        ↙       ↖       ↙       ↖
    → 3           0 → 3           0 →
      ↓           ↑ B ↓           ↑
    ← 4           7 ← 4           7 ←
        ↘       ↗       ↘       ↗ 
          5 → 6           5 → 6
          ↑ A ↓           ↑ A ↓
          2 ← 1           2 ← 1
        ↙       ↖       ↙       ↖
    → 3           0 → 3           0 →
      ↓           ↑ B ↓           ↑
    ← 4           7 ← 4           7 ←
        ↘       ↗       ↘       ↗ 
          5 → 6           5 → 6
          ↑   ↓           ↑   ↓
```

In the network after RG, the tensors A, B are rotated *counter-clockwise* by 45 degrees, but the network is rotated *clockwise* by 45 degrees:

```
    1       0       1       0
      ↘   ↗           ↖   ↙
        A               B
      ↙   ↖           ↗   ↘
    2       3       2       3
```

Therefore, in the next step of RG, we prefer to rotate back the tensor network by using another combination of the tensors $S_0$ to $S_7$. 

## Clockwise Rotation

```
          ↑   ↓           ↑   ↓
          2 ← 1           2 ← 1
        ↙       ↖       ↙       ↖
    → 3           0 → 3           0 →
      ↓           ↑ A ↓           ↑
    ← 4           7 ← 4           7 ←
        ↘       ↗       ↘       ↗ 
          5 → 6           5 → 6
          ↑ B ↓           ↑ B ↓
          2 ← 1           2 ← 1
        ↙       ↖       ↙       ↖
    → 3           0 → 3           0 →
      ↓           ↑ A ↓           ↑
    ← 4           7 ← 4           7 ←
        ↘       ↗       ↘       ↗ 
          5 → 6           5 → 6
          ↑   ↓           ↑   ↓
```

In the network after RG, the tensors A, B are rotated *clockwise* by 45 degrees, but the network is rotated *counter-clockwise* by 45 degrees:

```
    2       1       2       1
      ↘   ↗           ↖   ↙
        B               A
      ↙   ↖           ↗   ↘
    3       0       3       0
```

This can be implemented by the same code as the counter-clockwise rotation, except that:

- Tensors A and B are exchanged
- After combining the S tensors, we should transpose A and B by the permutation `(3,0,1,2)`

Method 1

```
    1       0       1       0
      ↘   ↗           ↖   ↙
        A               B
      ↙   ↖           ↗   ↘
    2       3       2       3
```

Method 2

```
    2       1       2       1
      ↘   ↗           ↖   ↙
        B               A
      ↙   ↖           ↗   ↘
    3       0       3       0
```
