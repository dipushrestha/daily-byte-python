'''
This question is asked by Apple. Given two sorted linked lists, merge them 
together in ascending order and return a reference to the merged list

Ex: Given the following lists...

list1 = 1->2->3, list2 = 4->5->6->null, return 1->2->3->4->5->6->null
list1 = 1->3->5, list2 = 2->4->6->null, return 1->2->3->4->5->6->null
list1 = 4->4->7, list2 = 1->5->6->null, return 1->4->4->5->6->7->null
'''

class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def list_from_str(string=""):
    node_values = string.split("->")
    if len(node_values) == 0: return
    head = ListNode(int(node_values[0]))
    cur = head
    for value in node_values[1:]:
        cur.next = ListNode(int(value))
        cur = cur.next
    return head

def list_str(list):
    values = []
    while list:
        values.append(str(list.data))
        list = list.next
    return "->".join(values)

def merged_linked_lists(list1, list2):
    temp = ListNode(0)
    tail = temp
    while list1 and list2:
        if list1.data < list2.data:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next
    tail.next = list1 if list1 else list2
    return temp.next


assert list_str(merged_linked_lists(list_from_str("1->2->3"), list_from_str("4->5->6"))) == "1->2->3->4->5->6"
assert list_str(merged_linked_lists(list_from_str("1->3->5"), list_from_str("2->4->6"))) == "1->2->3->4->5->6"
assert list_str(merged_linked_lists(list_from_str("4->4->7"), list_from_str("1->5->6"))) == "1->4->4->5->6->7"
