from typing import List


def assign_edge_weights(edges: List[List[int]]) -> int:
    mod = 1_000_000_007
    n = len(edges) + 1
    graph = [[] for _ in range(n + 1)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    def dfs(node: int, prev: int) -> int:
        d = 0
        for c in graph[node]:
            if c != prev:
                d = max(d, dfs(c, node) + 1)
        return d

    return pow(2, dfs(1, 0) - 1, mod)


print(assign_edge_weights([[1, 2]]))
print(assign_edge_weights([[1, 2], [1, 3], [3, 4], [3, 5]]))
print(assign_edge_weights([[0, 1], [0, 2], [0, 3], [0, 4]]))
