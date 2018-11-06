from threading import Thread
from time import sleep, ctime

loops = (4, 2)


def loop(nloop, nsec):
    print("Start loop", nloop, "at:", ctime())
    sleep(nsec)
    print("Done loop", nloop, "at:", ctime())


if __name__ == '__main__':
    print("Starting at:", ctime())

    threads = [Thread(target=loop, args=(nloop, nsec)) for nloop, nsec in enumerate(loops)]
    [thread.start() for thread in threads]
    [thread.join() for thread in threads]

    print("All Done at:", ctime())
