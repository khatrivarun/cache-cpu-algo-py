# Singular node for a double linked list.
class Node:
    def __init__(self,
                 data,
                 key=None,
                 arrival_time=None,
                 burst_time=None,
                 completion_time=None,
                 turn_around_time=None,
                 waiting_time=None):

        self.waiting_time = waiting_time
        self.turn_around_time = turn_around_time
        self.completion_time = completion_time
        self.burst_time = burst_time
        self.arrival_time = arrival_time
        self.data = data
        self.key = key
        self.next = None
        self.previous = None
