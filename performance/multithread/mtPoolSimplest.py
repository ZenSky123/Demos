from concurrent.futures import ThreadPoolExecutor
import time
import random


def task(*args):
    nticks = random.randint(1, 3)
    time.sleep(nticks)
    print("Task({}) has done with {} seconds ".format(args, nticks))
    return args


pool = ThreadPoolExecutor(4)
a = pool.submit(task, '1', '2')
b = pool.submit(task, 'a', 'b')

print(a.result())
print(b.result())
