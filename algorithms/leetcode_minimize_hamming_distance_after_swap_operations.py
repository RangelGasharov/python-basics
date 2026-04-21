from collections import defaultdict, Counter


def minimum_hamming_distance(source: list[int], target: list[int], allowed_swaps: list[list[int]]) -> int:
    n = len(source)
    parent = list(range(n))

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def unite(a, b):
        parent[find(a)] = find(b)

    for a, b in allowed_swaps:
        unite(a, b)

    groups = defaultdict(list)
    for i in range(n):
        groups[find(i)].append(source[i])
    groups = {root: Counter(vals) for root, vals in groups.items()}

    hamming_dist = 0
    for i in range(n):
        root = find(i)
        freq = groups[root]
        if freq[target[i]] > 0:
            freq[target[i]] -= 1
        else:
            hamming_dist += 1

    return hamming_dist


print(minimum_hamming_distance([1, 2, 3, 4], [2, 1, 4, 5], [[0, 1], [2, 3]]))
print(minimum_hamming_distance([1, 2, 3, 4], [1, 3, 2, 4], []))
print(minimum_hamming_distance([5, 1, 2, 4, 3], [1, 5, 4, 2, 3], [[0, 4], [4, 2], [1, 3], [1, 4]]))
