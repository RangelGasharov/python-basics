from typing import List


class SegmentTree:
    def __init__(self, n: int):
        self.n = n
        self.size = 4 * n
        self.sum = [0] * self.size
        self.min = [0] * self.size
        self.max = [0] * self.size

    def _pull(self, node: int):
        l, r = node * 2, node * 2 + 1

        self.sum[node] = self.sum[l] + self.sum[r]
        self.min[node] = min(self.min[l], self.sum[l] + self.min[r])
        self.max[node] = max(self.max[l], self.sum[l] + self.max[r])

    def update(self, idx: int, val: int):
        node, l, r = 1, 0, self.n - 1
        path = []

        while l != r:
            path.append(node)
            m = l + (r - l) // 2
            if idx <= m:
                node = node * 2
                r = m
            else:
                node = node * 2 + 1
                l = m + 1

        self.sum[node] = val
        self.min[node] = val
        self.max[node] = val

        while path:
            self._pull(path.pop())

    def find_rightmost_prefix(self, target: int = 0) -> int:
        node, l, r, sum_before = 1, 0, self.n - 1, 0

        def _exist(node: int, sum_before: int):
            return self.min[node] <= target - sum_before <= self.max[node]

        if not _exist(node, sum_before):
            return -1

        while l != r:
            m = l + (r - l) // 2
            l_child, r_child = node * 2, node * 2 + 1

            sum_before_right = self.sum[l_child] + sum_before
            if _exist(r_child, sum_before_right):
                node = r_child
                l = m + 1
                sum_before = sum_before_right
            else:
                node = l_child
                r = m

        return l


class Solution:
    def longest_balanced(self, nums: List[int]) -> int:
        n = len(nums)

        stree = SegmentTree(n)
        first = dict()

        result = 0
        for l in reversed(range(n)):
            num = nums[l]

            if num in first:
                stree.update(first[num], 0)

            first[num] = l
            stree.update(l, 1 if num % 2 == 0 else -1)

            r = stree.find_rightmost_prefix(target=0)
            if r >= l:
                result = max(result, r - l + 1)

        return result