from Cache.Cache import Cache


# Inheriting from Cache Abstract Class.
class FIFO(Cache):

    def __init__(self, total_length):
        super().__init__(total_length=total_length)
        self.reference_node = None

    # Method to traverse to the last node of the list.
    def traverse_to_last(self):

        temp_node = self.head

        # Loop to traverse to the last.
        while temp_node.next:
            temp_node = temp_node.next

        # Return the last node.
        return temp_node

    # Main method to insert values into the cache memory.
    def set_value(self, value):

        temp_node = self.head
        check = self.is_full()

        # Inserting the first element and incrementing miss counter
        # and also creating reference to the inserted element.
        if self.head is None:

            self.miss += 1
            self.push(data=value)
            self.reference_node = self.head

        else:

            while temp_node:

                # Searching the node to check if it is present.
                if temp_node.data is value:
                    break
                else:
                    temp_node = temp_node.next

            if temp_node:

                # Incrementing hits counter if found.
                if temp_node.data is value:
                    self.hits += 1

                # If not found, proceed with replacing with the referenced node and also incrementing the miss counter.
                elif temp_node.data is not value:

                    if check:

                        self.miss += 1

                        # Replacing the value.
                        self.reference_node.data = value

                        # Checking if the referenced element is the first element.
                        if self.reference_node.previous is None:

                            # Traversing to the last node.
                            self.reference_node = self.traverse_to_last()
                        else:

                            # Incrementing Referenced Node value.
                            self.reference_node = self.reference_node.previous
                    else:

                        # If list is empty, push a new value.
                        self.push(value)

            # Incrementing miss counter if value not found.
            else:

                self.miss += 1

                # Checking if list is empty.
                # Replace value with the reference node else push a new value.
                if check:
                    self.reference_node.data = value

                    if self.reference_node.previous is None:

                        self.reference_node = self.traverse_to_last()
                    else:

                        self.reference_node = self.reference_node.previous
                else:
                    self.push(data=value)
