from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def modified_list(nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
    nums = set(nums)
    while head and head.val in nums:
        head = head.next

    current = head
    while current and current.next:
        if current.next.val in nums:
            current.next = current.next.next
        else:
            current = current.next
    return head
