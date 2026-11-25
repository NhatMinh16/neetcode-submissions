# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        firstPointer = secondPointer = head
        while secondPointer:
            secondPointer = secondPointer.next
            if secondPointer is None:
                return False
            secondPointer = secondPointer.next
            if secondPointer is None:
                return False
            firstPointer = firstPointer.next
            if secondPointer == firstPointer:
                return True
        return False
            