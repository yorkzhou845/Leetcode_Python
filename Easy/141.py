# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        p1 = head
        p2 = head
        while (p2 is not None and p2.next is not None):
            p1 = p1.next#move first so that they are not automatically equal from the beginning
            p2 = p2.next.next
            if p1 == p2: return True

        return False
        

