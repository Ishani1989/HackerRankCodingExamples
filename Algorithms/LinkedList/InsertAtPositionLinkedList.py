"""
 Insert Node at a specific position in a linked list
 head input could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""


# This is a "method-only" submission.
# You only need to complete this method.
def InsertNth(head, data, position):
    temp = Node()
    current = Node()
    temp.data = data
    current = head

    if head is None:
        head = temp
        return head
    elif position == 0:
        temp.next = current
        head = temp
        return head
    else:
        count = 1
        while (current.next and count < position):
            current = current.next
            count += 1
        pos = current.next
        current.next = temp
        temp.next = pos
        return head












