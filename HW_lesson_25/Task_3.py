#Task 3
"""
Implement a queue using a singly linked list.
"""

class Node:

    def __init__(self, element):
        self.element = element
        self.next = None

class Queue:

    def __init__(self):
        self.front = self.rear = None

    def isEmpty(self):
        return self.front == None

    def enQueue(self, item):
        temp = Node(item)

        if self.rear == None:
            self.front = self.rear = temp
            return

        self.rear.next = temp
        self.rear = temp


    def deQueue(self):
        if self.isEmpty():
            return
        temp = self.front
        self.front = temp.next

        if self.front == None:
            self.rear = None

    
    def out(self):
        iter_node = self.front
        if self.isEmpty():
            print("Queue is empty")
        else:
            while iter_node:
                print(iter_node.element, end=" ")
                iter_node = iter_node.next
            print()

if __name__ == '__main__':
    queue = Queue()

    queue.enQueue(10)
    queue.enQueue(103)
    queue.enQueue(310)
    queue.out()
    print("*"*20)
    queue.deQueue()
    queue.deQueue()
    queue.out()

    
