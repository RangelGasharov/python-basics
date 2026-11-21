from typing import List


def find_subtree_sizes(parent: List[int], s: str) -> List[int]:
    n = len(parent)
    result = [0] * n
    adj = [[] for _ in range(n)]
    tree = [[] for _ in range(n)]
    last = [-1] * 26

    for i in range(1, n):
        adj[parent[i]].append(i)

    def dfs(u):
        c = ord(s[u]) - 97
        old = last[c]

        if u and old != -1:
            parent[u] = old
        last[c] = u

        for v in adj[u]:
            dfs(v)

        last[c] = old

    def calc(u):
        result[u] = 1
        for v in tree[u]:
            result[u] += calc(v)
        return result[u]

    dfs(0)

    for i in range(1, n):
        tree[parent[i]].append(i)

    calc(0)
    return result


print(find_subtree_sizes([-1, 0, 0, 1, 1, 1], "abaabc"))
print(find_subtree_sizes([-1, 0, 4, 0, 1], "abbba"))
