
Linked Lists in Python
A Linked List is a linear data structure where elements (called nodes) are stored in a sequence, but not in contiguous memory locations. Each node contains:

Data: The actual value or data of the node.
Pointer: A reference (or link) to the next node in the list.
There are two main types of linked lists:

Singly Linked List
Doubly Linked List
1. Singly Linked List
In a Singly Linked List, each node contains a reference to the next node in the sequence, forming a unidirectional chain.


Node Structure
Each node consists of:

Data: Holds the value.
Next: Points to the next node in the list (or None if it's the last node).
Basic Operations:
Traversal: Visiting each node in the list from the head (start) to the tail (end).

def traverse(head):
    current = head
    while current:
        print(current.data)
        current = current.next


Insertion:

At the beginning:
def insert_at_beginning(head, data):
    new_node = Node(data)
    new_node.next = head
    return new_node



 
  At the end:
def insert_at_end(head, data):
    new_node = Node(data)
    if not head:
        return new_node
    current = head
    while current.next:
        current = current.next
    current.next = new_node
    return head


      3.Deletion:

    From the beginning:

def delete_from_beginning(head):
    if head:
        return head.next
    return None


From the end:
def delete_from_end(head):
    if not head or not head.next:
        return None
    current = head
    while current.next.next:
        current = current.next
    current.next = None
    return head


2. Doubly Linked List
In a Doubly Linked List, each node contains two references: one to the next node and one to the previous node. This allows traversal in both directions (forward and backward).

Node Structure
Each node consists of:

Data: Holds the value.
Next: Points to the next node.
Prev: Points to the previous node.




Basic Operations:
Traversal:

          Forward:

def traverse_forward(head):
    current = head
    while current:
        print(current.data)
        current = current.next


Backward:
def traverse_backward(tail):
    current = tail
    while current:
        print(current.data)
        current = current.prev

2.Insertion:

At the beginning:
def insert_at_beginning(head, data):
    new_node = Node(data)
    if head:
        head.prev = new_node
    new_node.next = head
    return new_node


At the end:
def insert_at_end(head, data):
    new_node = Node(data)
    if not head:
        return new_node
    current = head
    while current.next:
        current = current.next
    current.next = new_node
    new_node.prev = current
    return head

Deletion:

From the beginning:
def delete_from_beginning(head):
    if head:
        head = head.next
        if head:
            head.prev = None
    return head


From the end:
def delete_from_end(head):
    if not head or not head.next:
        return None
    current = head
    while current.next:
        current = current.next
    current.prev.next = None
    return head




Use Cases of Linked Lists
1.Dynamic Memory Allocation: Linked lists grow or shrink as needed, unlike arrays with fixed size, making them suitable when the size of the data structure is unknown.
2.Efficient Insertion/Deletion: Insertions and deletions (especially at the beginning or in the middle) are more efficient compared to arrays, as there’s no need to shift elements.
3.Implementing Stacks and Queues: Linked lists are often used to implement stacks and queues due to their flexible memory usage.
4.Navigation Systems: Doubly linked lists are used in software systems that require back-and-forth navigation, like undo/redo functionality in text editors or browsers.


  
Example: Singly Linked List in Python

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def traverse(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


Example: Doubly Linked List in Python


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current

    def traverse_forward(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def traverse_backward(self):
        current = self.head
        while current.next:
            current = current.next
        while current:
            print(current.data, end=" -> ")
            current = current.prev
        print("None")




Conclusion
Linked lists, though not as commonly used in Python due to the existence of lists, are powerful data structures for scenarios where dynamic size management and frequent insertions or deletions are required.

















































