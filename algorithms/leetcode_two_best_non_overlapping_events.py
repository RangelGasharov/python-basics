from collections import deque
from operator import itemgetter


def max_two_events(events: list[list[int]]) -> int:
    start_sorted = sorted(events, key=itemgetter(0))
    end_sorted = deque(sorted(events, key=itemgetter(1)))

    max_sum = max(value for _, _, value in events)
    end_max = 0

    for start, end, value in start_sorted:
        while end_sorted and end_sorted[0][1] < start:
            _, _, v = end_sorted.popleft()
            end_max = max(end_max, v)
        max_sum = max(max_sum, value + end_max)

    return max_sum


print(max_two_events([[1, 3, 2], [4, 5, 2], [2, 4, 3]]))
print(max_two_events([[1, 3, 2], [4, 5, 2], [1, 5, 5]]))
print(max_two_events([[1, 5, 3], [1, 5, 1], [6, 6, 5]]))
