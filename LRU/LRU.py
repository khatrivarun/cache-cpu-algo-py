from DoublyLinkedList.DoublyLinkedList import DoublyLinkedList


class LRU (DoublyLinkedList):

    def __init__(self, total_length):
        super().__init__(total_length)
        self.total_length = total_length
        self.hits = 0
        self.miss = 0

    def move_to_front(self, data):
        temp_node = self.head

        while temp_node.data is not data:
            temp_node = temp_node.next

        if self.head.data is not data:
            temp_node.previous.next = temp_node.next

        self.counter -= 1
        self.push(data)

    def set_value(self, value):
        temp_node = self.head
        check = self.is_full()

        while temp_node:

            if temp_node.data is value:
                break

            else:
                temp_node = temp_node.next

        if temp_node:
            if temp_node.data is value:
                self.hits += 1
                self.move_to_front(value)
            elif temp_node.data is not value:
                self.miss += 1
                if check:
                    self.dequeue()
                self.push(value)
        else:
            self.miss += 1
            if check:
                self.dequeue()
            self.push(value)

    def display_cache(self):
        print("HITS: {}".format(self.hits))
        print("MISSES: {}".format(self.miss))
        print("COUNTER: {}".format(self.counter))
        print("TOTAL LENGTH: {}".format(self.total_length))
        print("CACHE STATUS: \n")
        self.display()
