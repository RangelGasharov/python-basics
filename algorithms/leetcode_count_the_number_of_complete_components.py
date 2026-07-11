from typing import List


def count_complete_components(n: int, edges: List[List[int]]) -> int:
    adj = [[] for _ in range(n)]

    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)

    visited = [False] * n

    def dfs(a, comp):
        visited[a] = True
        comp.append(a)
        for v in adj[a]:
            if not visited[v]:
                dfs(v, comp)

    result = 0

    for i in range(n):
        if not visited[i]:
            comp = []
            dfs(i, comp)
            if all(len(adj[u]) == len(comp) - 1 for u in comp):
                result += 1

    return result


print(count_complete_components(6, [[0, 1], [0, 2], [1, 2], [3, 4]]))
print(count_complete_components(6, [[0, 1], [0, 2], [1, 2], [3, 4], [3, 5]]))
