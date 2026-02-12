class Node:
  def __init__(self,val,next=None):
    self.val= val
    self.next=next
def inserte(head,val):
  current=head
  while current.next:
    current=current.next
  newNode=Node(val)
  current.next=newNode
  newNode.next=None
def printi(head):
  current=head
  while current:
    print(current.val,end="->")
    current=current.next
  print("None")
head=Node(1)
head.next=Node(3)
head.next.next=Node(2)
p=int(input("Enter your Node data"))
inserte(head,p)
printi(head)
