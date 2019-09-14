from List.List import List
from abc import ABC


# Abstract class Cache inheriting from List and ABC
# for abstraction.
class Cache(List, ABC):

    # Constructor for initializing cache with hits, misses and
    # page length with reference_node for FIFO.
    def __init__(self, total_length):
        super().__init__(total_length)
        self.hits = 0
        self.miss = 0
        self.reference_node = None

    # Abstract Method for pushing value in Cache and also
    # look for hits, misses and page replacement.
    def set_value(self, value):
        pass

    # Non Abstract Method for displaying cache status.
    def display_cache(self):
        print("HITS: {}".format(self.hits))
        print("MISSES: {}".format(self.miss))
        print("COUNTER: {}".format(self.counter))
        print("TOTAL LENGTH: {}".format(self.total_length))
        print("CACHE STATUS: \n")
        self.display()

