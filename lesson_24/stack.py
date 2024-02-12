class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            raise IndexError("Empty stack")

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

    def push_revers(self, item):
        return self.items.append(str(item)[::-1])



if __name__ == '__main__':
    s = Stack()
    s.push('Hello')
    s.push_revers(123)
    s.push(2)
    s.push(3)
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.isEmpty())
    
