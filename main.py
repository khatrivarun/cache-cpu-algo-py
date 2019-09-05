from DoublyLinkedList.DoublyLinkedList import DoublyLinkedList

linked_list = DoublyLinkedList(3)
linked_list.push(1)
linked_list.push(2)
linked_list.push(3)
linked_list.dequeue()
linked_list.push(4)

linked_list.display()
linked_list.display_reverse()
