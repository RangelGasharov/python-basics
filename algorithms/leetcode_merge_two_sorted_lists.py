from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_two_lists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode(-1)
    current = dummy

    while list1 and list2:
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next

    if list1:
        current.next = list1
    elif list2:
        current.next = list2

    return dummy.next


def list_to_linkedlist(lst):
    dummy = ListNode(0)
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next


def linkedlist_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


print(linkedlist_to_list(merge_two_lists(list_to_linkedlist([1, 2, 4]), list_to_linkedlist([1, 2, 4]))))
print(linkedlist_to_list(merge_two_lists(list_to_linkedlist([]), list_to_linkedlist([]))))
print(linkedlist_to_list(merge_two_lists(list_to_linkedlist([]), list_to_linkedlist([0]))))
