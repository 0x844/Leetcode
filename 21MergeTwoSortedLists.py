def mergeTwoLists(list1, list2):
  head1 = list1
  head2 = list2
  new = ListNode(0) #dummmy node
  curr = new

  while head1 and head2:
    if head1.val <= head2.val:
      curr.next = head1
      head1 = head1.next
    else:
      curr.next = head2
      head2 = head2.next
    curr = curr.next

  # add remaining nodes if present
  if head1:
    curr.next = head1
  if head2:
    curr.next = head2
  return new.next #'next' to skip dummy node