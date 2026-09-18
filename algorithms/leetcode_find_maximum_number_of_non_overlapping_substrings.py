from cmath import inf
from collections import deque
from typing import Counter


def max_num_of_substrings(s: str) -> list[str]:
    counts = Counter(s)
    first = {c: s.find(c) for c in counts}
    last = {c: s.rfind(c) for c in counts}

    result = []
    queue = deque()

    for count in counts:
        queue.appendleft([first[count], last[count], counts[count]])

        left = inf
        right = -inf
        total = 0

        for x, y, z in queue:
            total += z
            left = min(left, x)
            right = max(right, y)

            if total == right - left + 1:
                break

        if total == right - left + 1:
            result.append(s[left:right + 1])
            queue.clear()

    return result


print(max_num_of_substrings("adefaddaccc"))
print(max_num_of_substrings("abbaccd"))
