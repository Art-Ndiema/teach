class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)

    def is_empty(self):
        return len(self.queue) == 0

# Create empty data structures
stack = []
linked_list = LinkedList()
queue = Queue()

# Prompt the user to enter 5 names and add them to the data structures
for i in range(5):
    name = input(f"Enter name {i+1}: ")
    stack.append(name)
    linked_list.append(name)
    queue.enqueue(name)

# Display names in stack
print("Names in Stack (Last In, First Out):")
while stack:
    print(stack.pop())

# Display names in linked list
print("\nNames in Linked List:")
linked_list.display()

# Display names in queue
print("\nNames in Queue (First In, First Out):")
while not queue.is_empty():
    print(queue.dequeue())
