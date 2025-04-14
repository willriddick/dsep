# D-Separation in DAGs (Directed Acyclic Graphs)
This Python module implements d-separation testing for Directed Acyclic Graphs (DAGs) based on adjacency matrices. It allows you to check if two nodes are d-separated given a set of observed variables.

Inspired by [MIT 6.034](https://web.mit.edu/jmn/www/6.034/d-separation.pdf) materials on d-separation.

## What is D-Separation?
D-separation is a graphical criterion used in Bayesian networks to determine whether a set of variables is conditionally independent from another set, given a third set.

If set Z blocks every path between two nodes X and Y, then X and Y are d-separated (𝑋⫫_𝑑 𝑌|𝑍) conditional on Z and thus are also independent conditional on Z.

## Example Use
To test a DAG we must encode it as a matrix where each row in the matrix is a node, and each column denotes a directed edge to the node at that index. Per the example below, we place a *1* at index 2 in the first row because `A` has a directed edge to `C`. `B` also has a directed edge to `C`, so we similarly place a *1* in the second row at index 2.

![image](https://github.com/user-attachments/assets/9a9dee7e-d066-4340-bfc4-07f7b30806a4)

### Matrix Encoding
```
test_adj_matrix = [
    [0, 0, 1, 0, 0, 0, 0], # A
    [0, 0, 1, 0, 0, 0, 0], # B
    [0, 0, 0, 1, 1, 0, 0], # C
    [0, 0, 0, 0, 0, 1, 0], # D
    [0, 0, 0, 0, 0, 0, 0], # E
    [0, 0, 0, 0, 0, 0, 1], # F
    [0, 0, 0, 0, 0, 0, 0], # G
]
```

### Check if D and E are d-separated given C
`dsep(test_adj_matrix, 3, 4, [2])  # outputs: True`
