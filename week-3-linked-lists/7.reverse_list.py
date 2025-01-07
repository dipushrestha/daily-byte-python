'''
This question is asked by Facebook. Given a linked list, containing unique values, reverse it, and return the result.

Ex: Given the following linked lists...

1->2->3->null, return a reference to the node that contains 3 which points to a list that looks like the following: 3->2->1->null
7->15->9->2->null, return a reference to the node that contains 2 which points to a list that looks like the following: 2->9->15->7->null
1->null, return a reference to the node that contains 1 which points to a list that looks like the following: 1->null
'''

class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def from_list(nodes):
    dummy = ListNode(0)
    cur = dummy

    for node in nodes:
        cur.next = ListNode(node)
        cur = cur.next
    
    return dummy.next

def to_list(head):
    list = []

    while head:
        list.append(head.value)
        head = head.next

    return list

def reverse_list(head):    
    cur = head
    head = None 

    while cur:
        temp = cur
        cur = cur.next
        temp.next = head
        head = temp
    
    return head;

assert to_list(reverse_list(from_list([1, 2, 3]))) == [3, 2, 1]
assert to_list(reverse_list(from_list([7, 15, 9, 2]))) == [2, 9, 15, 7]
assert to_list(reverse_list(from_list([1]))) == [1]
