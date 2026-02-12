class Node:
  def __init__(self,val,next=None):
    self.val = val
    self.next=next
def insert(head,val):
  newnode=Node(val)
  newnode.next=head
  return newnode # to update the new head
def print_list(head):
  current=head
  while current:
    print(current.val, end="->")
    current=current.next
  print("None")
head=Node(1)
head.next=Node(2)
head.next.next=Node(3)
head=insert(head,5)# marking the new head in head
print_list(head)
