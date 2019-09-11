from DoublyLinkedList.DoublyLinkedList import  DoublyLinkedList


class LRU (DoublyLinkedList):

    def __init__(self, total_length):
        super().__init__(total_length)

    def move_to_front(self, data):
        temp_node = self.head

        while temp_node.data is not data:
            temp_node = temp_node.next

            temp_node.previous.next = temp_node.next

        self.counter -= 1
        self.push(data)
