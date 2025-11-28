def max_k_divisible_components(n: int, edges: list[list[int]], values: list[int], k: int) -> int:
    adj = [[] for _ in range(n)]
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)

    ans = 0

    def dfs(node, parent):
        nonlocal ans
        s = values[node]
        for nxt in adj[node]:
            if nxt != parent:
                s += dfs(nxt, node)
        if s % k == 0:
            ans += 1
        return s % k

    dfs(0, -1)
    return ans


print(max_k_divisible_components(5, [[0, 2], [1, 2], [1, 3], [2, 4]], [1, 8, 1, 4, 4], 6))
print(max_k_divisible_components(7, [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6]], [3, 0, 6, 1, 5, 2, 1], 3))
