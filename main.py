from LRU.LRU import LRU

lru = LRU(4)
lru.push(1)
lru.push(2)
lru.push(3)
lru.push(4)
lru.move_to_front(3)
lru.display()
