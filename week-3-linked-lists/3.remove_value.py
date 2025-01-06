'''
This question is asked by Google. Given a linked list and a value, remove all 
nodes containing the provided value, and return the resulting list.

Ex: Given the following linked lists and values...

1->2->3->null, value = 3, return 1->2->null
8->1->1->4->12->null, value = 1, return 8->4->12->null
7->12->2->9->null, value = 7, return 12->2->9->null
'''

class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def list_from_str(string=""):
    dummy = ListNode(0)
    cur = dummy
    node_values = string.split("->")
    
    for node_value in node_values:
        cur.next = ListNode(int(node_value))
        cur = cur.next
    
    return dummy.next

def list_str(list):
    node_values = []

    while list:
        node_values.append(str(list.data))
        list = list.next
    
    return "->".join(node_values)

def remove_value(list, value):
    dummy = ListNode(0)
    dummy.next = list
    cur = dummy
    
    while cur.next:
        if cur.next.data == value:
            cur.next = cur.next.next
        else:
            cur = cur.next
    return dummy.next


assert list_str(remove_value(list_from_str("1->2->3"), 3)) == "1->2"
assert list_str(remove_value(list_from_str("8->1->1->4->12"), 1)) == "8->4->12"
assert list_str(remove_value(list_from_str("7->12->2->9"), 7)) == "12->2->9"
