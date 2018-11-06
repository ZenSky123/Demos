from random import randint
from time import ctime, sleep
from threading import BoundedSemaphore, Lock, Thread

lock = Lock()
candytray = BoundedSemaphore(5)


def refill():
    with lock:
        print("Refilling candy...")
        try:
            candytray.release()
        except ValueError:
            print('Full, skipping!')
        else:
            print('OK')


def buy():
    with lock:
        print("Buying candy...")
        if candytray.acquire(False):
            print('OK')
        else:
            print('Empty, skipping!')


def producer(loops):
    for _ in range(loops):
        refill()
        sleep(randint(0, 3))


def consumer(loops):
    for _ in range(loops):
        buy()
        sleep(randint(0, 3))


if __name__ == '__main__':
    print("Starting at:", ctime())
    nloops = randint(2, 6)
    print("THE CANDY MACHINE (full with 5 bars)!")
    Thread(target=consumer, args=(randint(nloops, nloops + 7),)).start()
    Thread(target=producer, args=(nloops,)).start()
