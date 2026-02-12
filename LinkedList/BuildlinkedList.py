class Node():
  def __init__(self,val,next=None):
    self.val=val
    self.next=next
def build_linked_list(arr):
  if not arr:
    return None
  head=Node(arr[0])
  curr = head
  for val in arr[1:]:
    curr.next=Node(val)
    curr=curr.next
  return head
def printi(head):
  if not head:
    return None
  current=head
  while current:
    print(current.val,end="->")
    current=current.next
  print("None")
  return head
head = build_linked_list(range(12))
printi(head)
