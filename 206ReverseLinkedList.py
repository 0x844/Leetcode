def reverseList(head):
  curr = head
  new = None

  while curr:
    next_node = curr.next
    curr.next = new
    new = curr
    curr = next_node
  return new