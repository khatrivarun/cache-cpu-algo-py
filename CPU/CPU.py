from List.List import List
from abc import ABC


class CPU(ABC, List):
    def __init__(self):
        super().__init__()

    def startup_cpu(self, no):
        for i in range(1, no+1):
            self.add_last(data=i, key="P{}".format(i))

    def display_processes(self):
        self.display(True)

    def compile(self):
        pass
