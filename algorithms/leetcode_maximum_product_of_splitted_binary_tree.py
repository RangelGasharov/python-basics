from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def max_product(self, root: Optional[TreeNode]) -> int:
        all_sums = []

        def dfs(node):
            if not node:
                return 0
            current_sum = node.val + dfs(node.left) + dfs(node.right)
            all_sums.append(current_sum)
            return current_sum

        total_sum = dfs(root)

        max_product = 0
        for s in all_sums:
            product = s * (total_sum - s)
            max_product = max(max_product, product)
        return max_product % (10 ** 9 + 7)


sol = Solution()

root = TreeNode(989)
root.right = TreeNode(10250)
root.right.left = TreeNode(98693)
root.right.right = TreeNode(89388)
root.right.right.right = TreeNode(32127)
print(sol.max_product(root))

root = TreeNode(1)
root.right = TreeNode(0)
root.left = TreeNode(7)
root.left.left = TreeNode(7)
root.left.right = TreeNode(-8)
print(sol.max_product(root))
