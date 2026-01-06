import collections
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def max_level_sum(self, root: Optional[TreeNode]) -> int:
        current_level = 0
        node_queue = collections.deque([root])
        max_sum = -float("inf")
        best_level = 0

        while node_queue:
            current_level += 1
            current_level_sum = 0
            level_size = len(node_queue)
            for _ in range(level_size):
                node = node_queue.popleft()
                if node.left:
                    node_queue.append(node.left)
                if node.right:
                    node_queue.append(node.right)
                current_level_sum += node.val
            if current_level_sum > max_sum:
                max_sum = current_level_sum
                best_level = current_level
        return best_level

sol = Solution()

root = TreeNode(989)
root.right = TreeNode(10250)
root.right.left = TreeNode(98693)
root.right.right = TreeNode(-89388)
root.right.right.right = TreeNode(-32127)
print(sol.max_level_sum(root))

root = TreeNode(1)
root.right = TreeNode(0)
root.left = TreeNode(7)
root.left.left = TreeNode(7)
root.left.right = TreeNode(-8)
print(sol.max_level_sum(root))