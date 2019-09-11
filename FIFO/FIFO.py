from DoublyLinkedList.DoublyLinkedList import DoublyLinkedList


# Inheriting from Doubly Linked List.
class FIFO(DoublyLinkedList):

    # Constructor for length of cache memory
    # and initializing hits and misses.
    def __init__(self, total_length):
        super().__init__(total_length)
        self.hits = 0
        self.miss = 0
        self.reference_node = None

    def traverse_to_last(self):

        temp_node = self.head

        while temp_node.next:
            temp_node = temp_node.next

        return temp_node

    def set_value(self, value):

        temp_node = self.head
        check = self.is_full()

        if self.head is None:

            self.miss += 1
            self.push(value)
            self.reference_node = self.head

        else:

            while temp_node:

                if temp_node.data is value:
                    break
                else:
                    temp_node = temp_node.next

            if temp_node:

                if temp_node.data is value:
                    self.hits += 1

                elif temp_node.data is not value:

                    if check:

                        self.miss += 1

                        self.reference_node.data = value

                        if self.reference_node.next is None:

                            self.reference_node = self.traverse_to_last()
                        else:

                            self.reference_node = self.reference_node.previous
                    else:
                        self.push(value)

            else:

                self.miss += 1

                if check:
                    self.reference_node.data = value

                    if self.reference_node.previous is None:

                        self.reference_node = self.traverse_to_last()
                    else:

                        self.reference_node = self.reference_node.previous
                else:
                    self.push(value)

    # Display Cache Status.
    def display_cache(self):
        print("HITS: {}".format(self.hits))
        print("MISSES: {}".format(self.miss))
        print("COUNTER: {}".format(self.counter))
        print("TOTAL LENGTH: {}".format(self.total_length))
        print("CACHE STATUS: \n")
        self.display()
