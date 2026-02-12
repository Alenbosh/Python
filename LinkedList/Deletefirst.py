class Node:
  def __init__(self,val,next=None):
    self.val=val
    self.next=next
def delete(head):
  head=head.next
  return head
def rp(head):
  current=head
  while current:
    print(current.val,end="->")
    current=current.next
  print("None")
head=Node(1)
head.next=Node(2)
head.next.next=Node(3)
rp(head)
head=delete(head)
rp(head)

#Miles

def delete(head):
  if not head:
    return None
  return head.next
