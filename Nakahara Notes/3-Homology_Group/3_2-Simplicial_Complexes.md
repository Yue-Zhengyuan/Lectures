## Simplexes and Simplicial Complexes

### Simplexes

*Definition*:

- **Geometrically independent**: A set of $r+1$ points in $\mathbb{R}^m (m \ge r)$is said to be *geometrically independent* if there is no $r-1$ dimensional hyperplane containing all of them, i.e. the points can form an $r$-dimensional object

- **$r$-Simplex (单纯形) $\sigma_r$**: An object containing an $r$-dimensional region determined by $r+1$ *geometrically independent* points $p_0, ..., p_r$ in $\mathbb{R}^m (m \ge r)$

    $$
    \begin{aligned}
        \sigma_r &\equiv
        \langle p_0 p_1 ... p_r \rangle
        \\ &= 
        \left\{
            x \in \mathbb{R}^m \mid
            x = \sum_{i=0}^r c_i p_i, \quad
            (c_i \ge 0) \land \left(
                \sum_{i=0}^r c_i = 1
            \right)
        \right\}
    \end{aligned}
    $$

    - **Barycentric coordinate**: $(c_0, ..., c_r)$
    
    *Remark*: Since $\sigma_r$ is bounded and closed, it is *compact*.
    
    *Example*:

    - 2-simplex: triangle
    - 3-simplex: tetrahedron

- **$q$-Face of a simplex**
    - **Proper face**

### Simplicial Complexes and Polyhedra

*Definition*:

- **Simplicial complex (单纯复形)**: a set $K$ of simplexes satisfying the following requirements:   
    
> 1. Any face of any simplex in $K$ is still in $K$;
>
> 2. The intersection of any two simplexes in $K$ is either *empty* or *a common face of the two simplexes*.

- **Polyhedron**

- **Triangulable topological space**

    - **Triangulation (三角剖分) of topological space**