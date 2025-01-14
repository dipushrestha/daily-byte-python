'''
Design a class to implement a stack using only a single queue. Your class, 
QueueStack, should support the following stack methods: push() (adding an item), 
pop() (removing an item), peek() (returning the top value without removing it), 
and empty() (whether or not the stack is empty).
'''

from collections import deque

class QueueStack:
    def __init__(self):
        self.queue = deque()

    def push(self, val):
        self.queue.append(val)
        
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())

    def pop(self):
        return None if self.empty() else self.queue.popleft()
    
    def peek(self):
        return self.queue[0]
    
    def empty(self):
        return len(self.queue) == 0


qs = QueueStack()
qs.push(1)
assert qs.pop() == 1
qs.push(2)
assert qs.peek() == 2
qs.push(3)
assert qs.pop() == 3
assert qs.empty() == False
assert qs.pop() == 2
assert qs.empty() == True
