#Task 3
"""
Extend the Stack to include a method called get_from_stack that searches and returns an element e from a stack.
Any other element must remain on the stack respecting their order. Consider the case in which the element is not found - raise ValueError with proper info Message
"""

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
        if not self.isEmpty():
            return self.items[len(self.items) - 1]
        else:
            raise IndexError("Empty stack")

    def size(self):
        return len(self.items)

    def get_from_stack(self, element):
        s = Stack()
        found = False

       
        while not self.isEmpty():
            current = self.pop()
            if current == element:
                found = True
                break
            else:
                s.push(current)

        
        while not s.isEmpty():
            self.push(s.pop())

        if found:
            return element
        else:
            raise ValueError(f"Element '{element}' not found in the stack")


if __name__ == '__main__':
    
    my_stack = Stack()
    my_stack.push(1)
    my_stack.push(2)
    my_stack.push(3)

    try:
        result = my_stack.get_from_stack(3)
        print(f"Element found: {result}")
    except ValueError as e:
        print(e)
