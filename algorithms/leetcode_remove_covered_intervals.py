from typing import List


def remove_covered_intervals(intervals: List[List[int]]) -> int:
    intervals.sort(key=lambda k: (k[0], -k[1]))

    result = 0
    max_end = 0

    for start, end in intervals:
        result += end > max_end
        max_end = max(max_end, end)

    return result


print(remove_covered_intervals([[1, 4], [3, 6], [2, 8]]))
print(remove_covered_intervals([[1, 4], [2, 3]]))
