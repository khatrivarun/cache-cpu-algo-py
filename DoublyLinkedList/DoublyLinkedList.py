from .Node import Node


# ADT For Doubly Linked List.
class DoublyLinkedList:

    # Constructor for length and counter of the list
    # with head of the list.
    def __init__(self, total_length):
        self.total_length = total_length
        self.counter = 0
        self.head = None

    # STACK OPERATION: Insert new element at the beginning of the list.
    def push(self, data):

        if self.counter is not self.total_length:
            new_node = Node(data)

            if self.head is not None:
                self.head.previous = new_node
            new_node.next = self.head

            self.head = new_node

            self.counter += 1

        else:
            print("OVERLOAD.")

    # STACK OPERATION: Remove the first element.
    def pop(self):

        temp_node = self.head

        if self.counter is not 0:

            temp_node.next.previous = None
            self.head = self.head.next

            self.counter -= 1

        else:

            print("NO ELEMENT PRESENT")

    # QUEUE OPERATION: Remove the last element.
    def dequeue(self):

        temp_node = self.head

        if self.counter is not 0:

            while temp_node.next is not None:
                temp_node = temp_node.next

            temp_node.previous.next = None

            self.counter -= 1

        else:

            print("NO ELEMENT PRESENT.")

    # Display the linked List.
    def display(self):

        temp_node = self.head

        while temp_node is not None:
            print(temp_node.data)
            temp_node = temp_node.next

    # Check if linked list is full.
    def is_full(self):
        if self.counter is self.total_length:
            return True
        else:
            return False

    def is_present(self, data):

        temp_node = self.head
        while temp_node and temp_node.data is not data:
            temp_node = temp_node.next

        if temp_node:

            if temp_node.data is data:
                return True
            else:
                return False
        else:
            return False

    # Display in reverse manner.
    # (Used for checking the stability of the double linked list.)
    def display_reverse(self):

        temp_node = self.head

        while temp_node.next is not None:
            temp_node = temp_node.next

        while temp_node is not None:
            print(temp_node.data)
            temp_node = temp_node.previous
