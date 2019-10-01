from List.List import List
from abc import ABC


class CPU(ABC, List):
    def __init__(self):
        super().__init__()
        self.ready_queue = List()
        self.no_of_processes = 0
        self.clock = 0

    def startup_cpu(self, no):

        self.no_of_processes = no
        for i in range(1, no+1):
            self.enqueue(data=i, key="P{}".format(i))

    def init_arrival_time(self, arrival_times):

        temp_head = self.head
        if self.no_of_processes is not 0:
            for time in arrival_times:
                temp_head.arrival_time = time
                temp_head = temp_head.next

    def init_burst_time(self, burst_times):

        temp_head = self.head
        if self.no_of_processes is not 0:
            for time in burst_times:
                temp_head.burst_time = time
                temp_head = temp_head.next

    def compile(self):
        pass

    def cpu_status(self):
        pass
