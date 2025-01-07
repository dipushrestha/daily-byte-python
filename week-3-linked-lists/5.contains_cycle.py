'''
This question is asked by Microsoft. Given a linked list, containing unique numbers, return whether or not it has a cycle.
Note: a cycle is a circular arrangement (i.e. one node points back to a previous node)

Ex: Given the following linked lists...

1->2->3->1 -> true (3 points back to 1)
1->2->3 -> false
1->1 true (1 points to itself)
'''

class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

def contains_cycle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            return True

    return False 

list = ListNode(1)
list.next = ListNode(2)
list.next.next = ListNode(3)
list.next.next.next = list
assert contains_cycle(list) == True

list = ListNode(1)
list.next = ListNode(2)
list.next.next = ListNode(3)
assert contains_cycle(list) == False

list = ListNode(1)
list.next = list
assert contains_cycle(list) == True
