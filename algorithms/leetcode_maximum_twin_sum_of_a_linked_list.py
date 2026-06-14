from collections import deque
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        current = head
        values = deque()

        while current is not None:
            values.append(current.val)
            current = current.next

        result = 0

        while values:
            front = values.popleft()
            back = values.pop()
            result = max(result, front + back)

        return result
