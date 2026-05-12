from typing import List


def minimum_effort(tasks: List[List[int]]) -> int:
    tasks.sort(key=lambda x: x[1] - x[0])
    result = 0
    for task in tasks:
        result = max(result + task[0], task[1])
    return result


print(minimum_effort([[1, 2], [2, 4], [4, 8]]))
print(minimum_effort([[1, 3], [2, 4], [10, 11], [10, 12], [8, 9]]))
print(minimum_effort([[1, 7], [2, 8], [3, 9], [4, 10], [5, 11], [6, 12]]))
