from List.List import List
from abc import ABC


# Inheriting from the List Class and the ABC class for abstraction.
class CPU(ABC, List):

    # Constructor to initialize the no of processes and clock signal.
    def __init__(self):
        super().__init__()
        self.no_of_processes = 0
        self.clock = 0

    # Initialize the CPU with values for processes.
    def startup_cpu(self, no):

        self.no_of_processes = no
        for i in range(1, no+1):
            self.enqueue(data=i, key="P{}".format(i))

    # Initialize the arrival time values from a python list
    # and set them in the process list.
    def init_arrival_time(self, arrival_times):

        temp_head = self.head
        if self.no_of_processes is not 0:
            for time in arrival_times:
                temp_head.arrival_time = time
                temp_head = temp_head.next

    # Initialize the burst time values from a python list
    # and set them in the process list.
    def init_burst_time(self, burst_times):

        temp_head = self.head
        if self.no_of_processes is not 0:
            for time in burst_times:
                temp_head.burst_time = time
                temp_head = temp_head.next

    # Abstract function for compiling the values.
    def compile(self):
        pass

    # Abstract function for displaying the result.
    def cpu_status(self):
        pass
