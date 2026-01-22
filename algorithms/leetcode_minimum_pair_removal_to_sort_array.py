class Solution:
    def minimumPairRemoval(self, nums: list[int]) -> int:
        def is_sorted(nums, n) -> bool:
            for i in range(1,n):
                if nums[i] < nums[i - 1]:
                    return False
            return True
        res, n = 0, len(nums)
        while not is_sorted(nums, n):
            res += 1
            min_sum, pos = float('inf'), -1
            for i in range(1,n):
                current_sum = nums[i - 1] + nums[i]
                if current_sum < min_sum:
                    min_sum = current_sum
                    pos = i
            nums[pos - 1] = min_sum
            for i in range(pos, n-1): nums[i] = nums[i + 1]
            n -= 1
        return res


s = Solution()
print(s.minimumPairRemoval([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(s.minimumPairRemoval([5, 2, 3, 1]))
print(s.minimumPairRemoval([1, 2, 2]))
