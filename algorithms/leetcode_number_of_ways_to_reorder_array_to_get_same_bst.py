from math import factorial
from typing import List


def num_of_ways(nums: List[int]) -> int:
    n = len(nums)
    born = [-1] * (n + 2)

    for t, x in enumerate(nums):
        born[x] = t

    sizes, stack = 1, [0]
    for v in range(1, n + 2):
        while born[stack[-1]] > born[v]:
            stack.pop()
            sizes *= v - stack[-1] - 1
        stack.append(v)

    return (factorial(n) // sizes - 1) % (10 ** 9 + 7)


print(num_of_ways([2, 1, 3]))
print(num_of_ways([3, 4, 5, 1, 2]))
print(num_of_ways([1, 2, 3]))
