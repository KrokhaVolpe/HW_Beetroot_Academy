#Task 2
"""
Write a program that reads in a sequence of characters,
and determines whether it's parentheses, braces, and curly brackets are "balanced."
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
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

def balance(sequence):
    s = Stack()
    open_brackets = ["[", "{", "("]
    close_brackets = ["]", "}", ")"]

    for i in sequence:
        if i in open_brackets:
            s.push(i)
        elif i in close_brackets:
            pos = close_brackets.index(i)
            if s.size() > 0 and open_brackets[pos] == s.peek():
                s.pop()
            else:
                return "Unbalanced"

            
    if s.isEmpty():
        return "Balanced"
    else:
        return "Unbalanced"
                

                
if __name__ == '__main__':

    input_user = input("Enter a sequence of characters: ")
    result = balance(input_user)
    print(result)

