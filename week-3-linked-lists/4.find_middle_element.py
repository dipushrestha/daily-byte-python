'''
This question is asked by Amazon. Given a non-empty linked list, return the middle node of the list. If the linked list contains an even number of elements, return the node closer to the end.
Ex: Given the following linked lists...

1->2->3->null, return 2
1->2->3->4->null, return 3
1->null, return 1
'''

class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def list_from_str(string=""):
    node_values = string.split("->")
    dummy = ListNode(0)
    cur = dummy

    for node_value in node_values:
        cur.next = ListNode(int(node_value))
        cur = cur.next

    return dummy.next

def list_str(list):
    values = []

    while list:
        values.append(str(list.data))
        list = list.next
    
    return "->".join(values)

def find_middle_element(list):
    slow = list
    fast = list

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow.data

assert find_middle_element(list_from_str("1->2->3")) == 2
assert find_middle_element(list_from_str("1->2->3->4")) == 3
assert find_middle_element(list_from_str("1")) == 1
