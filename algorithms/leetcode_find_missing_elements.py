from typing import List


def find_missing_elements(nums: List[int]) -> List[int]:
    seen = set(nums)
    result = []

    min_num = min(nums)
    max_num = max(nums)

    for i in range(min_num, max_num + 1):
        if i not in seen:
            result.append(i)

    return result


print(find_missing_elements([1, 4, 2, 5]))
print(find_missing_elements([7, 8, 6, 9]))
print(find_missing_elements([5, 1]))
