from CPU.CPU import CPU
from List.List import List


# Inheriting from the CPU Class.
class RoundRobin(CPU):
    def __init__(self, quantum_time):
        super().__init__()
        self.ready_queue = List()
        self.quantum_time = quantum_time
        self.template = "PROCESS ID: {}\n" \
                        "ARRIVAL TIME: {}\n" \
                        "BURST TIME: {}\n" \
                        "COMPLETION TIME: {}\n" \
                        "TURN AROUND TIME: {}\n" \
                        "WAITING TIME: {}\n\n"

    # Implementing Abstract method from CPU to compile te given data and display the result.
    def compile(self):
        temp_head = self.head

        # Running through the data first to prepare the initial ready queue.
        while temp_head is not None:

            # Case 1: If the burst time is more than the allowed quantum time,
            # increment the clock with quantum time and queue the process in the ready queue.
            if temp_head.burst_time > self.quantum_time:

                self.clock += self.quantum_time

                self.ready_queue.enqueue(data=temp_head.data,
                                         key=temp_head.key,
                                         arrival_time=temp_head.arrival_time,
                                         burst_time=temp_head.burst_time - self.quantum_time,
                                         completion_time=temp_head.completion_time,
                                         turn_around_time=temp_head.turn_around_time,
                                         waiting_time=temp_head.waiting_time,
                                         service_time=temp_head.service_time)

            # Case 2: If the burst time is less or equal to the allowed time,
            # increment the clock with burst time and calculate the other required fields.
            elif temp_head.burst_time <= self.quantum_time:

                self.clock += temp_head.burst_time

                temp_head.completion_time = self.clock
                temp_head.turn_around_time = temp_head.completion_time - temp_head.arrival_time
                temp_head.waiting_time = temp_head.turn_around_time - temp_head.burst_time

            temp_head = temp_head.next

        queue_head = self.ready_queue.head

        # Now processing the ready queue.
        while queue_head is not None:

            # Case 1: If the burst time is more than the allowed quantum time,
            # increment the clock with quantum time and queue the process in the ready queue.
            if queue_head.burst_time <= self.quantum_time:

                self.clock += queue_head.burst_time

                process = self.search(data=queue_head.data)

                process.completion_time = self.clock
                process.turn_around_time = process.completion_time - process.arrival_time
                process.waiting_time = process.turn_around_time - process.burst_time

            # Case 2: If the burst time is more than the allowed quantum time,
            # increment the clock with quantum time and queue the process in the ready queue.
            elif queue_head.burst_time > self.quantum_time:

                self.clock += self.quantum_time

                self.ready_queue.enqueue(data=queue_head.data,
                                         key=queue_head.key,
                                         arrival_time=queue_head.arrival_time,
                                         burst_time=(queue_head.burst_time - self.quantum_time),
                                         completion_time=queue_head.completion_time,
                                         turn_around_time=queue_head.turn_around_time,
                                         waiting_time=queue_head.waiting_time,
                                         service_time=queue_head.service_time)

            queue_head = queue_head.next
            self.ready_queue.pop()

    # Display the current status of CPU after/before/in between of Round Robin execution.
    def cpu_status(self):
        temp_node = self.head

        while temp_node is not None:
            print(self.template.format(temp_node.key,
                                       temp_node.arrival_time,
                                       temp_node.burst_time,
                                       temp_node.completion_time,
                                       temp_node.turn_around_time,
                                       temp_node.waiting_time))

            temp_node = temp_node.next


