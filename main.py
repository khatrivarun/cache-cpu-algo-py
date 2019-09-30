from CPU.RoundRobin.RoundRobin import RoundRobin

rr = RoundRobin(quantum_time=3)

rr.startup_cpu(4)

rr.init_arrival_time([0, 1, 2, 3])
rr.init_burst_time([10, 4, 5, 3])
rr.compile()
rr.display(is_cpu=True)
