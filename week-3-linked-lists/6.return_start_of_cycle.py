'''
This question is asked by Apple. Given a potentially cyclical linked list 
where each value is unique, return the node at which the cycle starts. 
If the list does not contain a cycle, return null.

Ex: Given the following linked lists...

1->2->3, return null
1->2->3->4->5->2 (5 points back to 2), return a reference to the node containing 2
1->9->3->7->7 (7 points to itself), return a reference to the node containing 7
'''

class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

def return_start_of_cycle(list):
    fast = list
    slow = list

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if fast == slow: break
    else:
        return None

    slow = list
    while slow != fast:
        slow = slow.next
        fast = fast.next
    
    return slow


list = ListNode(1)
list.next = ListNode(2)
list.next.next = ListNode(3)
assert return_start_of_cycle(list) == None

list = ListNode(1)
list.next = ListNode(2)
list.next.next = ListNode(3)
list.next.next.next = ListNode(4)
list.next.next.next.next = ListNode(5)
list.next.next.next.next.next = list.next
assert return_start_of_cycle(list) == list.next

list = ListNode(1)
list.next = ListNode(9)
list.next.next = ListNode(3)
list.next.next.next = ListNode(7)
list.next.next.next.next = list.next.next.next
assert return_start_of_cycle(list) == list.next.next.next
