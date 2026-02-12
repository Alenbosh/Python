class Node:
  def __init__(self,val=0,next=None):
    self.val= val
    self.next = next

def print_list(head):
    current=head# storing the pointer of first node in current for traversing the LL
    while current:# initiating traversion
      print(current.val, end="->")#Printing the value of Node
      current = current.next# Moving the pointer to the next node
    print("None")# prints none for the last node
head=Node(1) #Creating first node
head.next=Node(2)#Creating Second node
head.next.next=Node(3)#Creating Third Node
print_list(head)
