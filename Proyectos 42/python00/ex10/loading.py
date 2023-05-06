
# EX09 - GUESS.PY #

import time

def ft_progress(lst):
    
    total = len(lst)
    start_time = time.time()
    
    for i, item in enumerate(lst):
        elapsed_time = time.time() - start_time
        eta = elapsed_time * (total / (i+1) - 1)
        progress = (i+1) * 100 // total
        bar = "=" * (progress//5) + ">" + " " * (20 - progress//5)
        print("\rETA: {:.2f}s [{}%][{}] {}/{} | elapsed time {:.2f}s".format(eta, progress, bar, i+1, total, elapsed_time), end="")
        yield item
    print()

listy = range(0, -100, -1)
ret = 0
for elem in ft_progress(listy):
    ret += (elem + 3) % 5
    time.sleep(0.01)
print()
print(ret)

listy = range(3333)
ret = 0
for elem in ft_progress(listy):
    ret += elem
    time.sleep(0.005)
print()
print(ret)