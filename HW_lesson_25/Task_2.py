#Task 2
"""
Implement a stack using a singly linked list.
"""

class Node:

    def __init__(self, element):
        self.element = element
        self.next = None

        
class Stack:
    def __init__(self):
        self.head = None


    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False
        

    def push(self, element):
        if self.head == None:
            self.head = Node(element)
        else:
            new_node = Node(element)
            new_node.next = self.head
            self.head = new_node


    def pop(self):
        if self.isEmpty():
            return None
        else:
            popped_node = self.head
            self.head = self.head.next
            popped_node.next = None
            return popped_node.element


    def peek(self):
        if self.isEmpty():
            return None                                                                             
        else:                                                                                                                                                                     
            return self.head.element

        

    def out(self):
        iter_node = self.head
        if self.isEmpty():
            print("Stack Underflow")
        else:
            while iter_node:
                print(iter_node.element)
                iter_node = iter_node.next

            
    
if __name__ == "__main__":
    stack = Stack()

    stack.push(1)
    stack.push(15)
    stack.push(165)
    stack.push(81)
    stack.out()

    print("*"*20)

    print("\nTop element is ", stack.peek())
    stack.pop()
    
    print("*"*20)
    print("\nTop element is ", stack.peek())    
    stack.out()
     
