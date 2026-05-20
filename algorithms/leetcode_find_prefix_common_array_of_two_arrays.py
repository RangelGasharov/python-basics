from typing import List


def find_the_prefix_common_array(A: List[int], B: List[int]) -> List[int]:
    n = len(A)
    result = [0] * n
    seen = [0] * (n + 1)

    for i in range(n):
        seen[0] += seen[A[i]]
        seen[A[i]] = 1

        seen[0] += seen[B[i]]
        seen[B[i]] = 1

        result[i] = seen[0]

    return result


print(find_the_prefix_common_array([1, 3, 2, 4], [3, 1, 2, 4]))
print(find_the_prefix_common_array([2, 3, 1], [3, 1, 2]))
