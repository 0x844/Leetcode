# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = l1
        string1 = ""
        while (head):
            string1 += str(head.val)
            head = head.next
        
        head = l2
        string2 = ""
        while(head):
            string2 += str(head.val)
            head = head.next

        combined = str(int(string1[::-1]) + int(string2[::-1]))
        
        head = None

        for i in range(len(combined)):
            newNode = ListNode(int(combined[i]), head)
            head = newNode     
        return head
