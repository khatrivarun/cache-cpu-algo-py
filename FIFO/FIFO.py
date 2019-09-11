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
