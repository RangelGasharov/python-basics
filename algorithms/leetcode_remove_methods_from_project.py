import collections


def remaining_methods(n: int, k: int, invocations: list[list[int]]) -> list[int]:
    in_deg = [0] * n
    edges = [[] for _ in range(n)]

    for u, v in invocations:
        edges[u].append(v)
        in_deg[v] += 1

    queue = collections.deque([k])
    suspicious = bytearray(n)
    suspicious[k] = 1

    while queue:
        u = queue.popleft()
        for v in edges[u]:
            in_deg[v] -= 1

            if suspicious[v] == 0:
                queue.append(v)
                suspicious[v] = 1

    can_remove_all = True
    for i in range(n):
        if suspicious[i] == 1 and in_deg[i] > 0:
            can_remove_all = False
            break

    if not can_remove_all:
        return list(range(n))

    return [i for i in range(n) if suspicious[i] == 0]


print(remaining_methods(4, 1, [[1, 2], [0, 1], [3, 2]]))
print(remaining_methods(5, 0, [[1, 2], [0, 2], [0, 1], [3, 4]]))
print(remaining_methods(3, 2, [[1, 2], [0, 1], [2, 0]]))
