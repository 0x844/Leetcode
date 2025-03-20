# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        odds = head
        evens = head.next
        output = evens

        while evens and evens.next:
            odds.next = evens.next
            odds = odds.next
            evens.next = evens.next.next
            evens = evens.next
        odds.next = output
        return head
