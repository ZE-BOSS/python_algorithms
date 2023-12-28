from collections import deque

class stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]
    
    def is_empty(self):
        return len(self.container) == 0
    
    def size(self):
        return len(self.container)
    
if __name__ == '__main__':
    s = stack()
    s.push(5)
    s.peek()
    s.pop()
    s.is_empty()
    s.push(7)
    s.push(5)
    s.push(73)
    s.size()