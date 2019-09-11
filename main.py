from FIFO.FIFO import FIFO

fifo = FIFO(10)
for i in range(1, 11):
    fifo.set_value(i)
for i in range(1, 10):
    fifo.set_value(i)
fifo.display_cache()
