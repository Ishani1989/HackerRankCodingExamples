"""
 Delete Node at a given position in a linked list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""


def Delete(head, position):
    temp = Node()
    current = head
    count = 0
    if head is None:
        return "nothing to delete"

    if position == 0 and head.next is None:
        head = None
    elif position == 0 and head.next is not None:
        temp = head
        head = head.next
        temp = None
    while (head.next and count < position):
        current = current.next
        count += 1
    print "count", count, "position", position
    pos = current.next
    current = pos.next
    pos = None
    return head






