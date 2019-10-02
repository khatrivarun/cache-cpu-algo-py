from CPU.FCFS.FCFS import FCFS
from CPU.RoundRobin.RoundRobin import RoundRobin
from Cache.FIFO.FIFO import FIFO
from Cache.LRU.LRU import LRU

# Initializing required variables and data structures.
fifo_cache = None
lru_cache = None
fcfs_cpu = None
round_robin_cpu = None
init_burst_time = []
init_arrival_time = []

print("WELCOME TO CPU AND CACHE ALGORITHMS SIMULATOR!")
print("             - A Project by Varun Khatri (E064)")

# Continuous loop for UI.
while True:

    print("WHICH ALGORITHM DO YOU WISH TO EXECUTE FIRST?")
    print("0. EXIT THE PROGRAM\n1. CACHE ALGORITHMS\n2. CPU ALGORITHMS")
    choice = int(input("ENTER YOUR CHOICE: "))

    # CASE 0: EXIT THE PROGRAM
    if choice is 0:
        break

    # CASE 1: CACHE ALGORITHMS.
    elif choice is 1:
        print("WHICH ALGORITHM DO YOU WISH TO RUN FIRST?")
        print("1. LRU ALGORITHM\n2. FIFO ALGORITHM")
        algo_choice = int(input("ENTER YOUR CHOICE: "))
        pages = int(input("PLEASE ENTER NUMBER OF AVAILABLE PAGES: "))

        # CASE 1.1: LRU ALGORITHM.
        if algo_choice is 1:
            lru_cache = LRU(total_length=pages)

            # Loop for keeping the algorithm alive if user wants to.
            while True:
                data = int(input("ENTER DATA TO ENTER: "))
                lru_cache.set_value(data)
                lru_cache.display_cache()

                confirmation = str(input("DO YOU WISH TO CONTINUE? ENTER YES OR NO: "))

                if confirmation == "NO":
                    break
                else:
                    print("YOU WISHED TO CONTINUE")

        # CASE 1.2: FIFO ALGORITHM.
        elif algo_choice is 2:
            fifo_cache = FIFO(total_length=pages)

            # Loop for keeping the algorithm alive if user wants to.
            while True:
                data = int(input("ENTER DATA TO ENTER: "))
                fifo_cache.set_value(value=data)
                fifo_cache.display_cache()

                confirmation = str(input("DO YOU WISH TO CONTINUE? ENTER YES OR NO: "))

                if confirmation == "NO":
                    break
                else:
                    print("YOU WISHED TO CONTINUE")

        # ERROR CASE
        else:
            print("WRONG INPUT. TRY AGAIN")

    # CASE 2: CPU ALGORITHMS.
    elif choice is 2:
        print("WHICH CPU ALGORITHM DO YOU WISH TO START?")
        print("1. FIRST COME FIRST SERVE\n2. ROUND ROBIN")
        algo_choice = int(input("ENTER YOUR CHOICE: "))
        no_of_processes = int(input("ENTER NUMBER OF PROCESSES: "))

        # CASE 2.1: FCFS Algorithm.
        if algo_choice is 1:

            # Loop for keeping the algorithm alive if user wants to.
            while True:
                fcfs_cpu = FCFS()
                print("STARTING UP THE CPU.....")
                fcfs_cpu.startup_cpu(no=no_of_processes)

                # Number of processes cannot be 0.
                if no_of_processes is not 0:

                    # Arrival Times Input.
                    print("INITIALIZE ARRIVAL TIMES: ")
                    for i in range(0, no_of_processes):
                        time = int(input("ENTER ARRIVAL TIME FOR PROCESS P{} :".format(i)))
                        init_arrival_time.append(time)

                    # Burst Times Input.
                    print("INITIALIZE BURST TIMES: ")
                    for i in range(0, no_of_processes):
                        time = int(input("ENTER BURST TIME FOR PROCESS P{} :".format(i)))
                        init_burst_time.append(time)

                    fcfs_cpu.init_burst_time(burst_times=init_burst_time)
                    fcfs_cpu.init_arrival_time(arrival_times=init_arrival_time)

                    # Compile Start
                    fcfs_cpu.cpu_status()
                    print("STARTING TO COMPILE DATA...")
                    fcfs_cpu.compile()

                    # Compile end: Display Results.
                    print("STATUS OF THE CPU AFTER COMPILING")
                    fcfs_cpu.cpu_status()

                    # Choice if they want to redo it again.
                    confirmation = str(input("DO YOU WISH TO RE-ENTER VALUES AND COMPILE IT AGAIN? ENTER YES OR NO: "))

                    if confirmation == "NO":
                        break
                    else:
                        print("YOU WISHED TO CONTINUE")

                else:
                    print("0 IS NOT ALLOWED FOR NUMBER OF PROCESSES.")

        # CASE 2.2: Round Robin Algorithm.
        elif algo_choice is 2:

            # Loop for keeping the algorithm alive if user wants to.
            while True:
                quantum_time = int(input("ENTER THE QUANTUM TIME: "))
                round_robin_cpu = RoundRobin(quantum_time=quantum_time)
                print("STARTING UP THE CPU.....")
                round_robin_cpu.startup_cpu(no=no_of_processes)

                if no_of_processes is not 0:

                    # Arrival Times Input.
                    print("INITIALIZE ARRIVAL TIMES: ")
                    for i in range(0, no_of_processes):
                        time = int(input("ENTER ARRIVAL TIME FOR PROCESS P{} :".format(i)))
                        init_arrival_time.append(time)

                    # Burst Times Input.
                    print("INITIALIZE BURST TIMES: ")
                    for i in range(0, no_of_processes):
                        time = int(input("ENTER BURST TIME FOR PROCESS P{} :".format(i)))
                        init_burst_time.append(time)

                    round_robin_cpu.init_burst_time(burst_times=init_burst_time)
                    round_robin_cpu.init_arrival_time(arrival_times=init_arrival_time)

                    # Compile Start.
                    round_robin_cpu.cpu_status()
                    print("STARTING TO COMPILE DATA...")
                    round_robin_cpu.compile()

                    # Compile End: Display Results.
                    print("STATUS OF THE CPU AFTER COMPILING")
                    round_robin_cpu.cpu_status()

                    confirmation = str(input("DO YOU WISH TO RE-ENTER VALUES AND COMPILE IT AGAIN? ENTER YES OR NO: "))

                    if confirmation == "NO":
                        break
                    else:
                        print("YOU WISHED TO CONTINUE")

                else:
                    print("0 IS NOT ALLOWED FOR NUMBER OF PROCESSES.")

        # ERROR CASE
        else:
            print("WRONG INPUT. TRY AGAIN")

    # ERROR CASE
    else:
        print("WRONG INPUT. TRY AGAIN")

print("EXITING...")
