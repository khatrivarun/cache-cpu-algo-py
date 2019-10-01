from .Node import Node


# ADT For Doubly Linked List.
class List:

    # Constructor for length and counter of the list
    # with head of the list.
    def __init__(self, total_length=1000):
        self.total_length = total_length
        self.counter = 0
        self.head = None

    # STACK OPERATION: Insert new element at the beginning of the list.
    def push(self, data, key=None, arrival_time=None, burst_time=None, completion_time=None, turn_around_time=None,
             waiting_time=None, service_time=None):

        if self.counter is not self.total_length:
            new_node = Node(data=data,
                            key=key,
                            arrival_time=arrival_time,
                            burst_time=burst_time,
                            completion_time=completion_time,
                            turn_around_time=turn_around_time,
                            waiting_time=waiting_time,
                            service_time=service_time)

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

            if temp_node.next is None:
                self.head = None
            else:
                temp_node.next.previous = None
                self.head = self.head.next

            self.counter -= 1

        else:

            print("NO ELEMENT PRESENT")

    # Add element to the back of the list.
    def enqueue(self, data, key=None, arrival_time=None, burst_time=None, completion_time=None, turn_around_time=None,
                waiting_time=None, service_time=None):

        temp_node = self.head
        new_node = Node(data=data,
                        key=key,
                        arrival_time=arrival_time,
                        burst_time=burst_time,
                        completion_time=completion_time,
                        turn_around_time=turn_around_time,
                        waiting_time=waiting_time,
                        service_time=service_time)
        new_node.next = None

        if temp_node:

            while temp_node.next is not None:
                temp_node = temp_node.next

            temp_node.next = new_node
            new_node.previous = temp_node

        else:

            new_node.previous = None
            self.head = new_node

        self.counter += 1

    # QUEUE OPERATION: Remove the last element.
    def remove_last(self):

        temp_node = self.head

        if self.counter is not 0:

            while temp_node.next is not None:
                temp_node = temp_node.next

            temp_node.previous.next = None

            self.counter -= 1

        else:

            print("NO ELEMENT PRESENT.")

    # Search for a particular value in the list using linear search.
    # and returning the node if found.
    def search(self, data):

        temp_node = self.head

        while temp_node is not None and temp_node.data is not data:
            if temp_node.data == data:
                break
            else:
                temp_node = temp_node.next

        # Returning the node found else null.
        if temp_node is not None:
            return temp_node
        else:
            return None

    # Check if linked list is full.
    def is_full(self):
        if self.counter is self.total_length:
            return True
        else:
            return False

    # To check if a particular value is present in the list or not.
    def is_present(self, data):

        temp_node = self.head
        while temp_node and temp_node.data is not data:
            temp_node = temp_node.next

        # If value found then return true else false.
        if temp_node:

            # If value found then return true else false.
            if temp_node.data is data:
                return True
            else:
                return False
        else:
            return False

    # Display the linked List.
    def display(self):

        temp_node = self.head
        while temp_node is not None:
            print(temp_node.data)
            temp_node = temp_node.next

