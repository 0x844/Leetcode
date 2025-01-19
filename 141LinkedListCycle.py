# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head
        seen = []

        while curr:
            if curr.next and curr.next in seen:
                return True
            else:
                seen.append(curr)
            curr = curr.next
        return False