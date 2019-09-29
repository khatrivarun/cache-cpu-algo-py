from CPU.CPU import CPU

cpu = CPU()
cpu.startup_cpu(5)
cpu.init_arrival_time([0, 1, 2, 3, 4])
cpu.init_burst_time([10, 12, 20, 93, 44])
cpu.display(True)
