from random import randint
from time import sleep, ctime
from queue import Queue
from threading import Thread

q = Queue(32)


def writeQ():
    print("Producing object for Q...")
    q.put('xxx')
    print("Size now", q.qsize())


def readQ():
    val = q.get()
    print("Consumed object from Q... size now", q.qsize())


def writter(loops):
    for _ in range(loops):
        writeQ()
        sleep(randint(1, 3))


def reader(loops):
    for _ in range(loops):
        readQ()
        sleep(randint(2, 5))


if __name__ == '__main__':
    nloops = randint(2, 5)
    threads = [
        Thread(target=writter, args=(nloops,)),
        Thread(target=reader, args=(nloops,))
    ]
    [thread.start() for thread in threads]
    [thread.join() for thread in threads]
