from collections import deque
from typing import List


def can_reach(arr: List[int], start: int) -> bool:
    n = len(arr)
    visited = set()
    q = deque([start])

    while q:
        i = q.popleft()

        if i < 0 or i >= n or i in visited:
            continue

        if arr[i] == 0:
            return True

        visited.add(i)
        q.append(i + arr[i])
        q.append(i - arr[i])

    return False


print(can_reach([4, 2, 3, 0, 3, 1, 2], 5))
print(can_reach([4, 2, 3, 0, 3, 1, 2], 0))
print(can_reach([3, 0, 2, 1, 2], 2))
