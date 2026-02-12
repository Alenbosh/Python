class Node:
  def __init__(self,val,next=None):
    self.val=val
    self.next=next
def delete(head):
  if not head:
    return None
  if not head.next:
    return none
  current=head
  while current.next.next:
    current=current.next
  current.next = None
  return head



