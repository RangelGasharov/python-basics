from cmath import inf
from typing import List


def minMirrorPairDistance(nums: List[int]) -> int:
    def reverse_num(x):
        ans = 0
        while x > 0:
            x, d = divmod(x, 10)
            ans = 10 * ans + d
        return ans

    num_map = {}
    dist = inf
    for i, x in enumerate(nums):
        reverse = reverse_num(x)
        if x in num_map:
            dist = min(dist, i - num_map[x])
        num_map[reverse] = i
    return -1 if dist == inf else dist


print(minMirrorPairDistance([12, 21, 45, 33, 54]))
print(minMirrorPairDistance([120, 21]))
print(minMirrorPairDistance([21, 120]))
