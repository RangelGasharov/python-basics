from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def nodes_between_critical_points(self, head: Optional[ListNode]) -> List[int]:
    last = None
    current = head
    index = 0

    first_critical = -1
    prev_critical = -1
    min_distance = float("inf")

    while current and current.next:
        if last and (last.val < current.val > current.next.val or last.val > current.val < current.next.val):
            if first_critical == -1:
                first_critical = index
            else:
                min_distance = min(min_distance, index - prev_critical)
            prev_critical = index

        last = current
        current = current.next
        index += 1

    if first_critical == prev_critical:
        return [-1, -1]
    return [min_distance, prev_critical - first_critical]



