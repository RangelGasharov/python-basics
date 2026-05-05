from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotate_right(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        n = 1
        curr = head

        while curr.next:
            n += 1
            curr = curr.next

        k = k % n
        if k == 0:
            return head

        curr.next = head
        limit = n - k
        new_tail = curr

        for _ in range(limit):
            new_tail = new_tail.next

        new_head = new_tail.next
        new_tail.next = None

        return new_head


solution = Solution()
listNode = ListNode(0, ListNode(1, ListNode(2)))
print(solution.rotate_right(listNode, 4).val)

