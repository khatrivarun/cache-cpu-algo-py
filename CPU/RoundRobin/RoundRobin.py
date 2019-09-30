from CPU.CPU import CPU


class RoundRobin(CPU):
    def __init__(self, quantum_time):
        super().__init__()
        self.quantum_time = quantum_time

    def compile(self):
        temp_head = self.head

        while temp_head is not None:

            if temp_head.burst_time > self.quantum_time:

                self.clock += self.quantum_time

                self.ready_queue.enqueue(data=temp_head.data,
                                         key=temp_head.key,
                                         arrival_time=temp_head.arrival_time,
                                         burst_time=temp_head.burst_time - self.quantum_time,
                                         completion_time=temp_head.completion_time,
                                         turn_around_time=temp_head.turn_around_time,
                                         waiting_time=temp_head.waiting_time)

            elif temp_head.burst_time <= self.quantum_time:

                self.clock += temp_head.burst_time

                temp_head.completion_time = self.clock
                temp_head.turn_around_time = temp_head.completion_time - temp_head.arrival_time
                temp_head.waiting_time = temp_head.turn_around_time - temp_head.burst_time

            temp_head = temp_head.next

        queue_head = self.ready_queue.head

        while queue_head is not None:

            if queue_head.burst_time <= self.quantum_time:

                self.clock += queue_head.burst_time

                process = self.search(data=queue_head.data)

                process.completion_time = self.clock
                process.turn_around_time = process.completion_time - process.arrival_time
                process.waiting_time = process.turn_around_time - process.burst_time

            elif queue_head.burst_time > self.quantum_time:

                self.clock += self.quantum_time

                self.ready_queue.enqueue(data=queue_head.data,
                                         key=queue_head.key,
                                         arrival_time=queue_head.arrival_time,
                                         burst_time=(queue_head.burst_time - self.quantum_time),
                                         completion_time=queue_head.completion_time,
                                         turn_around_time=queue_head.turn_around_time,
                                         waiting_time=queue_head.waiting_time)

            queue_head = queue_head.next
            self.ready_queue.pop()
