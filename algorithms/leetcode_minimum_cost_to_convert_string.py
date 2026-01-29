from typing import List


def minimum_cost(source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
    inf = float('inf')
    dist = [[inf] * 26 for _ in range(26)]

    for i in range(26):
        dist[i][i] = 0

    for o, c, z in zip(original, changed, cost):
        u = ord(o) - 97
        v = ord(c) - 97
        dist[u][v] = min(dist[u][v], z)

    for k in range(26):
        for i in range(26):
            if dist[i][k] == inf:
                continue
            for j in range(26):
                if dist[k][j] != inf:
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    total_cost = 0
    for s_char, t_char in zip(source, target):
        u = ord(s_char) - 97
        v = ord(t_char) - 97
        if u == v:
            continue
        if dist[u][v] == inf:
            return -1
        total_cost += dist[u][v]

    return total_cost


print(minimum_cost("abcd", "acbe", ["a", "b", "c", "c", "e", "d"], ["b", "c", "b", "e", "b", "e"], [2, 5, 5, 1, 2, 20]))
print(minimum_cost("aaaa", "bbbb", ["a", "c"], ["c", "b"], [1, 2]))
print(minimum_cost("abcd", "abce", ["a"], ["e"], [10000]))
