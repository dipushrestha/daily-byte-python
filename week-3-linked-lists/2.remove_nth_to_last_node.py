'''
This question is asked by Facebook. Given a linked list and a value n, remove the nth to last node and return the resulting list.

Ex: Given the following linked lists...

1->2->3->null, n = 1, return 1->2->null
1->2->3->null, n = 2, return 1->3->null
1->2->3->null, n = 3, return 2->3->null
'''

class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def list_from_str(string=""):
    dummy = ListNode(0)
    tail = dummy
    node_values = string.split("->")
    for node_value in node_values:
        tail.next = ListNode(int(node_value))
        tail = tail.next
    return dummy.next

def list_str(list):
    values = []
    while list:
        values.append(str(list.data))
        list = list.next
    return "->".join(values)

def remove_nth_to_last_node(list, n):
    dummy = ListNode(0)
    dummy.next = list
    first = last = dummy

    for _ in range(n):
        first = first.next
    
    while first.next:
        first = first.next
        last = last.next
    
    last.next = last.next.next

    return dummy.next

assert list_str(remove_nth_to_last_node(list_from_str("1->2->3"), 1)) == "1->2"
assert list_str(remove_nth_to_last_node(list_from_str("1->2->3"), 2)) == "1->3"
assert list_str(remove_nth_to_last_node(list_from_str("1->2->3"), 3)) == "2->3"
