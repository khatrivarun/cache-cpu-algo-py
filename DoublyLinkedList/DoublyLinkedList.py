from .Node import Node


class DoublyLinkedList:
    def __init__(self, total_length):
        self.total_length = total_length
        self.counter = 0
        self.head = None

    def push(self, data):

        if self.counter < self.total_length:
            new_node = Node(data)

            if self.head is not None:
                self.head.previous = new_node
                new_node.next = self.head

            self.head = new_node

            self.counter += 1

        # TODO: LRU REPLACEMENT ALGORITHM.
        else:
            print("OVERLOAD.")

    def pop(self):

        temp_node = self.head

        if self.counter is not 0:

            temp_node.next.previous = None
            self.head = self.head.next

            self.counter -= 1

        else:

            print("NO ELEMENT PRESENT")

    def dequeue(self):

        temp_node = self.head

        if self.counter is not 0:

            while temp_node.next is not None:
                temp_node = temp_node.next

            temp_node.previous.next = None

            self.counter -= 1

        else:

            print("NO ELEMENT PRESENT.")

    def display(self):

        temp_node = self.head

        while temp_node is not None:
            print(temp_node.data)
            temp_node = temp_node.next

    def display_reverse(self):

        temp_node = self.head

        while temp_node.next is not None:
            temp_node = temp_node.next

        while temp_node is not None:
            print(temp_node.data)
            temp_node = temp_node.previous



