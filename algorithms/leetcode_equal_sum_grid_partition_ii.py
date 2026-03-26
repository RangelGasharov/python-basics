from collections import defaultdict
from typing import List


class Solution:
    def can_partition_grid(self, grid: List[List[int]]) -> bool:
        rows = len(grid)
        cols = len(grid[0])

        total = 0
        bottom = defaultdict(int)
        top = defaultdict(int)
        left = defaultdict(int)
        right = defaultdict(int)

        for row in grid:
            for x in row:
                total += x
                bottom[x] += 1
                right[x] += 1

        sum_top = 0

        for i in range(rows - 1):
            for j in range(cols):
                val = grid[i][j]
                sum_top += val

                top[val] += 1
                bottom[val] -= 1

            sum_bottom = total - sum_top

            if sum_top == sum_bottom:
                return True

            diff = abs(sum_top - sum_bottom)

            if sum_top > sum_bottom:
                if self.check(top, grid, 0, i, 0, cols - 1, diff):
                    return True
            else:
                if self.check(bottom, grid, i + 1, rows - 1, 0, cols - 1, diff):
                    return True

        sum_left = 0


        for j in range(cols - 1):
            for i in range(rows):
                val = grid[i][j]
                sum_left += val

                left[val] += 1
                right[val] -= 1

            sum_right = total - sum_left

            if sum_left == sum_right:
                return True

            diff = abs(sum_left - sum_right)

            if sum_left > sum_right:
                if self.check(left, grid, 0, rows - 1, 0, j, diff):
                    return True
            else:
                if self.check(right, grid, 0, rows - 1, j + 1, cols - 1, diff):
                    return True

        return False

    def check(self, mp, grid, r1, r2, c1, c2, diff):
        rows = r2 - r1 + 1
        cols = c2 - c1 + 1

        if rows * cols == 1:
            return False

        if rows == 1:
            return grid[r1][c1] == diff or grid[r1][c2] == diff

        if cols == 1:
            return grid[r1][c1] == diff or grid[r2][c1] == diff

        return mp.get(diff, 0) > 0


solution = Solution()
print(solution.can_partition_grid([[1, 1, 1], [2, 1, 1], [3, 1, 2], [4, 1, 2]]))
print(solution.can_partition_grid([[1, 4], [2, 3]]))
print(solution.can_partition_grid([[1, 3], [2, 4]]))
