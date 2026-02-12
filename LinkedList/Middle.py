class Node():
  def __init__(self,val,next=None):
    self.val=val
    self.next=next
def find_middle(head):
  slow=fast=head
  while fast and fast.next:
    slow = slow.next
    fast=fast.next.next
  return slow
head=Node(0)
head.next=Node(1)
head.next.next=Node(2)
head.next.next.next=Node(3)
head.next.next.next.next=Node(4)
head.next.next.next.next.next=Node(5)
head.next.next.next.next.next.next=Node(6)
head.next.next.next.next.next.next.next=Node(7)
head.next.next.next.next.next.next.next.next=Node(8)
head.next.next.next.next.next.next.next.next.next=Node(9)
head.next.next.next.next.next.next.next.next.next.next=Node(10)
head.next.next.next.next.next.next.next.next.next.next.next=Node(11)
d=find_middle(head)
print(d.val)
