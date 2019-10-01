from CPU.CPU import CPU
from List.Node import Node


class FCFS(CPU):
    def __init__(self):
        super().__init__()
        self.template = "PROCESS ID: {}\n" \
                        "ARRIVAL TIME: {}\n" \
                        "BURST TIME: {}\n" \
                        "SERVICE TIME: {}\n" \
                        "WAITING TIME: {}\n\n"

    def compile(self):
        temp_head: Node = self.head

        while temp_head is not None:
            temp_head.service_time = self.clock
            temp_head.waiting_time = temp_head.service_time - temp_head.arrival_time
            self.clock += temp_head.burst_time

            temp_head = temp_head.next

    def cpu_status(self):
        temp_head: Node = self.head

        while temp_head is not None:
            print(self.template.format(temp_head.key,
                                       temp_head.arrival_time,
                                       temp_head.burst_time,
                                       temp_head.service_time,
                                       temp_head.waiting_time))

            temp_head = temp_head.next
