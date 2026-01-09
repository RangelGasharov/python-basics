from collections import deque
from typing import Optional

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def subtree_with_all_deepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        parent = {root: None}
        queue = deque([root])

        last_level = []

        while queue:
            size = len(queue)
            last_level = []
            for _ in range(size):
                node = queue.popleft()
                last_level.append(node)

                if node.left:
                    parent[node.left] = node
                    queue.append(node.left)
                if node.right:
                    parent[node.right] = node
                    queue.append(node.right)

        deepest = set(last_level)

        while len(deepest) > 1:
            deepest = {parent[node] for node in deepest}

        return deepest.pop()