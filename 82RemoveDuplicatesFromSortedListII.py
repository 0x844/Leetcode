def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
  if not head:
    return head
  hmap = {}
  curr = head
  while curr:
    if curr.val in hmap:
      hmap[curr.val] += 1
    else:
      hmap[curr.val] = 1
    curr = curr.next
  dummy = ListNode()
  final = dummy
  curr = head
  while curr:
    if hmap[curr.val] == 1:
      dummy.next = curr
      dummy = dummy.next
      curr = curr.next
    else:
      curr = curr.next
  dummy.next = None # terminate tail 
  return final.next
