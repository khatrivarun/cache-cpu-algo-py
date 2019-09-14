from Cache.LRU.LRU import LRU

lru = LRU(3)
lru.set_value(10)
lru.set_value(20)
lru.set_value(30)
lru.set_value(40)
lru.set_value(20)
lru.display_cache()
