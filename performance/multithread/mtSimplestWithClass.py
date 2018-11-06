import threading
from time import ctime, sleep

loops = (4, 2)


class MyThread(threading.Thread):
    def __init__(self, func, args, name=''):
        super().__init__()
        self.func = func
        self.args = args
        self.name = name

    def run(self):
        self.func(*self.args)


def loop(nloop, nsec):
    print("Start loop", nloop, "at:", ctime())
    sleep(nsec)
    print("Done loop", nloop, "at:", ctime())


if __name__ == '__main__':
    print("Starting at:", ctime())

    threads = [MyThread(func=loop, args=(nloop, nsec), name=loop.__name__) for nloop, nsec in enumerate(loops)]
    [thread.start() for thread in threads]
    [thread.join() for thread in threads]

    print("All Done at:", ctime())
