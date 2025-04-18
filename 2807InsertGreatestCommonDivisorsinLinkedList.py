import math
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = head
        final = res
        while res.next:
            temp = res.next
            gcdv = gcd(res.val, temp.val)
            res.next = ListNode(gcdv,temp)
            res = res.next.next # skip node that just got added
        return final
