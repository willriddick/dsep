# https://web.mit.edu/jmn/www/6.034/d-separation.pdf


import copy


type AdjMatrix = list[list[int]]


def get_ancestors(adj_matrix: AdjMatrix, x: int) -> set[int]:
    """Get the ancestors of a node in a DAG."""
    ancestors = set()
    length = len(adj_matrix)
    for i in range(length):
        if adj_matrix[i][x] == 1:
            ancestors.add(i)
    return ancestors


def ancestorize(adj_matrix: AdjMatrix, x: int, y: int, z: list[int]) -> AdjMatrix:
    """Remove non ancestral nodes from the DAG."""
    check = [x, y] + z if z else [x, y]

    ancestors = set()
    for i in check:
        ancestors.update(get_ancestors(adj_matrix, i))
    ancestors.update(check)

    new_matrix = copy.deepcopy(adj_matrix)
    length = len(adj_matrix)
    for i in range(length):
        for j in range(length):
            if j not in ancestors:
                new_matrix[i][j] = 0

    return new_matrix


def moralize(adj_matrix: AdjMatrix) -> AdjMatrix:
    """Add edges between parents of a node in a DAG."""
    new_matrix = copy.deepcopy(adj_matrix)
    length = len(adj_matrix)

    for child in range(length):  
        parents = [parent for parent in range(length) if adj_matrix[parent][child] == 1]
        
        for i in range(len(parents)):
            for j in range(i + 1, len(parents)):
                p1, p2 = parents[i], parents[j]
                new_matrix[p1][p2] = 1
                new_matrix[p2][p1] = 1

    return new_matrix


def disorient(adj_matrix: AdjMatrix) -> AdjMatrix:
    """Replaces directed edges with undirected edges."""
    new_matrix = copy.deepcopy(adj_matrix)
    length = len(adj_matrix)
    for i in range(length):
        for j in range(length):
            if new_matrix[i][j] == 1:
                new_matrix[j][i] = 1
    return new_matrix


def delete_givens(adj_matrix: AdjMatrix, z: list[int]) -> AdjMatrix:
    """Delete nodes in Z from the DAG."""
    new_matrix = copy.deepcopy(adj_matrix)
    length = len(adj_matrix)
    for node in z:
        for i in range(length):
            new_matrix[node][i] = 0
            new_matrix[i][node] = 0
    return new_matrix


def bfs(adj_matrix: AdjMatrix, x: int, y: int) -> bool:
    """Check if there exists a path between x and y."""
    length = len(adj_matrix)
    visited = [False] * length
    visited[x] = True

    queue = [x]

    while queue:
        cur = queue.pop(0)

        if cur == y:
            return True

        for i in range(length):
            if adj_matrix[cur][i] == 1 and not visited[i]:
                visited[i] = True
                queue.append(i)
    
    return False


def dsep(adj_matrix: AdjMatrix, x: int, y: int, z: list[int]) -> bool:
    """
    Check if X is d-separated from Y given Z in a DAG.

    Parameters:
    adj_matrix (AdjMatrix): Adjacency matrix of the DAG.
    x (int): Node X.
    y (int): Node Y.
    z (list[int]): List of nodes in Z.

    Returns:
    bool: True if X is d-separated from Y given Z, False otherwise.
    """
    adj_matrix = ancestorize(adj_matrix, x, y, z)
    adj_matrix = moralize(adj_matrix)
    adj_matrix = disorient(adj_matrix)
    adj_matrix = delete_givens(adj_matrix, z)

    # If a path between X and Y exists, then X is not d-separated from Y.
    result = not bfs(adj_matrix, x, y)
    print(f'Nodes {x} and {y} are {'' if result else 'not '}d-separated conditional on {z}.')
    return result


def pretty_print(adj_matrix: AdjMatrix) -> None:
    """Pretty print the adjacency matrix."""
    for i in range(len(adj_matrix)):
        for j in range(len(adj_matrix[i])):
            print(adj_matrix[i][j], end=" ")
        print()


def main():
    """Run our tests."""
    test_adj_matrix = [
        [0, 0, 1, 0, 0, 0, 0], # Node A 
        [0, 0, 1, 0, 0, 0, 0], # Node B
        [0, 0, 0, 1, 1, 0, 0], # Node C
        [0, 0, 0, 0, 0, 1, 0], # Node D
        [0, 0, 0, 0, 0, 0, 0], # Node E
        [0, 0, 0, 0, 0, 0, 1], # Node F
        [0, 0, 0, 0, 0, 0, 0], # Node G
    #    A  B  C  D  E  F  G
    ]
    dsep(test_adj_matrix, 3, 4, [2])
   

if __name__ == "__main__":
    main()
