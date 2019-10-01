from CPU.FCFS.FCFS import FCFS

fcfs = FCFS()
fcfs.startup_cpu(4)
fcfs.init_burst_time([5, 3, 8, 6])
fcfs.init_arrival_time([0, 1, 2, 3])
fcfs.compile()
fcfs.cpu_status()
