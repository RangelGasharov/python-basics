from typing import List, Tuple


class Solution:
    def decompose(self, nums: List[int]) -> List[Tuple[int, int, int]]:
        n = len(nums)
        subarrays: List[Tuple[int, int, int]] = []

        l = 0
        s = nums[0]

        for i in range(1, n):
            if nums[i - 1] <= nums[i]:
                subarrays.append((l, i - 1, s))
                l = i
                s = 0
            s += nums[i]

        subarrays.append((l, n - 1, s))
        return subarrays


    def max_sum_trionic(self, nums: List[int]) -> int:
        n = len(nums)

        max_ending_at = [0] * n
        for i in range(n):
            max_ending_at[i] = nums[i]
            if i > 0 and nums[i - 1] < nums[i]:
                if max_ending_at[i - 1] > 0:
                    max_ending_at[i] += max_ending_at[i - 1]

        max_starting_at = [0] * n
        for i in range(n - 1, -1, -1):
            max_starting_at[i] = nums[i]
            if i < n - 1 and nums[i] < nums[i + 1]:
                if max_starting_at[i + 1] > 0:
                    max_starting_at[i] += max_starting_at[i + 1]

        PQS = self.decompose(nums)
        result = -10 ** 30
        for (p, q, s) in PQS:
            if (p > 0 and nums[p - 1] < nums[p] and
                    q < n - 1 and nums[q] < nums[q + 1] and
                    p < q):
                cand = max_ending_at[p - 1] + s + max_starting_at[q + 1]
                if cand > result:
                    result = cand

        return result
