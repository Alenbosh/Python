class Node():
  def __init__(self,val,next=None):
    self.val=val
    self.next=next
def Make(arr):
  if not arr:
    return None
  head=Node(arr[0])
  current= head
  for val in arr[1:]:
    current.next=Node(val)
    current=current.next
  return head
def RLL(head):
 fast=head
 curr=head
 prev=None
 if not head:
  return None
 while curr:
  fast=head.next.next
#  return head
 head=fast
 curr.prev=None
#  while slow:
#   slo=slow.prev
#   slow.prev=slow
#   slow=slo
 return head
# def printi(head):
#   if not head:
#     return None
#   curr=head
#   while curr:
#     print(curr.val,end="->")
#     curr=curr.next
#   return head
head=Make(range(12))
# print(head)
head=RLL(head)
print(head)


