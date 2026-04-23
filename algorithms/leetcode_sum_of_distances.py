from collections import defaultdict
from typing import List


def distance(nums: List[int]) -> List[int]:
    n = len(nums)
    result = [0] * n

    mp = defaultdict(list)

    for i in range(n):
        mp[nums[i]].append(i)

    for arr in mp.values():
        siz = len(arr)

        pref = [0] * siz
        pref[0] = arr[0]

        for i in range(1, siz):
            pref[i] = pref[i - 1] + arr[i]

        for i in range(siz):
            left = 0
            right = 0

            if i > 0:
                left = i * arr[i] - pref[i - 1]

            if i < siz - 1:
                right = (pref[siz - 1] - pref[i]) - (siz - i - 1) * arr[i]

            result[arr[i]] = left + right

    return result


print(distance([1, 3, 1, 1, 2]))
print(distance([0, 5, 3]))
