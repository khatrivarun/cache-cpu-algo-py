from Cache.Cache import Cache


# Inheriting from Cache Abstract Class.
class LRU (Cache):

    # Move an element from already present position to first position.
    def move_to_front(self, data):
        temp_node = self.head

        # Finding Element to move to front.
        while temp_node.data is not data:
            temp_node = temp_node.next

        # Checking if the element to be moved was the head itself and
        # Decreasing the counter to push in a new element.
        if self.head.data is not data:
            temp_node.previous.next = temp_node.next
            self.counter -= 1
            self.push(data=data)

    # Main function to put values in cache memory
    def set_value(self, value):
        temp_node = self.head
        check = self.is_full()

        # Checking if value is already present
        while temp_node:

            if temp_node.data is value:
                break

            else:
                temp_node = temp_node.next

        # Checking if there is no new element.
        if temp_node:

            # Checking if value is already present
            # in the current state of node.
            if temp_node.data is value:
                self.hits += 1
                self.move_to_front(data=value)
            elif temp_node.data is not value:
                self.miss += 1
                if check:
                    self.remove_last()
                self.push(data=value)
        else:
            self.miss += 1
            if check:
                self.remove_last()
            self.push(data=value)
