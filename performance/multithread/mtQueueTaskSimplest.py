from queue import Queue
from threading import Thread


def producer(out_q):
    for i in range(3):
        out_q.put(i)


def consumer(in_q):
    while True:
        try:
            data = in_q.get(timeout=5.0)
            print("[consumer] get", data)
            in_q.task_done()
        except:
            break


q = Queue()
t1 = Thread(target=consumer, args=(q,))
t2 = Thread(target=producer, args=(q,))

t1.start()
t2.start()
q.join()
