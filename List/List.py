from .Node import Node


# ADT For Doubly Linked List.
class List:

    # Constructor for length and counter of the list
    # with head of the list.
    def __init__(self, total_length=1000):
        self.total_length = total_length
        self.counter = 0
        self.head = None
        self.template = "PROCESS ID: {}\n" \
                        "ARRIVAL TIME: {}\n" \
                        "BURST TIME: {}\n" \
                        "COMPLETION TIME: {}\n" \
                        "TURN AROUND TIME: {}\n" \
                        "WAITING TIME: {}\n\n"

    # STACK OPERATION: Insert new element at the beginning of the list.
    def push(self, data, key=None, arrival_time=None, burst_time=None, completion_time=None, turn_around_time=None,
             waiting_time=None):

        if self.counter is not self.total_length:
            new_node = Node(data=data, key=key,
                            arrival_time=arrival_time,
                            burst_time=burst_time,
                            completion_time=completion_time,
                            turn_around_time=turn_around_time,
                            waiting_time=waiting_time)

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

    # Add element to the back of the list.
    def add_last(self, data, key=None, arrival_time=None, burst_time=None, completion_time=None,turn_around_time=None,
                 waiting_time=None):

        temp_node = self.head
        new_node = Node(data=data,
                        key=key,
                        arrival_time=arrival_time,
                        burst_time=burst_time,
                        completion_time=completion_time,
                        turn_around_time=turn_around_time,
                        waiting_time=waiting_time)
        new_node.next = None

        if temp_node:

            while temp_node.next is not None:
                temp_node = temp_node.next

            temp_node.next = new_node
            new_node.previous = temp_node

        else:

            new_node.previous = None
            self.head = new_node

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

    def search(self, key):

        temp_node = self.head

        while temp_node is not None:
            if temp_node.key == key:
                break
            else:
                temp_node = temp_node.next

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

    # Display the linked List.
    def display(self, is_cpu=False):

        temp_node = self.head
        if is_cpu is True:
            while temp_node is not None:

                print(self.template.format(temp_node.key,
                                           temp_node.arrival_time,
                                           temp_node.burst_time,
                                           temp_node.completion_time,
                                           temp_node.turn_around_time,
                                           temp_node.waiting_time))

                temp_node = temp_node.next

        else:
            while temp_node is not None:
                print(temp_node.data)
                temp_node = temp_node.next

    # Display in reverse manner.
    # (Used for checking the stability of the double linked list.)
    def display_reverse(self, is_cpu=False):

        temp_node = self.head

        while temp_node.next is not None:
            temp_node = temp_node.next

        if is_cpu is True:
            while temp_node is not None:
                print(self.template.format(temp_node.key,
                                           temp_node.arrival_time,
                                           temp_node.burst_time,
                                           temp_node.completion_time,
                                           temp_node.turn_around_time,
                                           temp_node.waiting_time))

                temp_node = temp_node.previous

        else:
            while temp_node is not None:
                print(temp_node.data)
                temp_node = temp_node.previous
