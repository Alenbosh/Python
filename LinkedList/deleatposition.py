def delete(head,k):
  if not head or k<1://checking if head is empty or position is invalid
    return head //returns None
  dummy=node(0) //creating 0 node
  dummy.next=head // linking dummy to the actual node
  current= dummy // assing current the pointer of dummy
  for _ in range(k-1):// Runs until the position it needs to be deleted
    if not current.next:// to check if Linkedlist turns out to only have one element
      return dummy.next // returning the postion of head to not lose track of it
    current=current.next //passing the traversal pointer if the node exists
    if current.next: // if the next node exists
      current.next=current.next.next //skipping over the node to be deleted un linking the particular node from the actua linkedlist
    return dummy.next //returning head
