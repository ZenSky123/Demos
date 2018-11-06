from threading import Thread, currentThread, Lock
from time import sleep, ctime
from random import randint


class CleanOutputSet(set):
    def __str__(self):
        return ', '.join(self)


loops = [randint(2, 5) for _ in range(randint(3, 7))]
lock = Lock()

remaining = CleanOutputSet()


def loop(nsec):
    name = currentThread().name
    with lock:
        remaining.add(name)
        print('[{}] Started {}'.format(ctime(), name))
    sleep(nsec)
    with lock:
        remaining.remove(name)
        print('[{}] Completed {} ({} secs)'.format(ctime(), name, nsec))
        print("    (remaining: {})".format(remaining or 'NONE'))


if __name__ == '__main__':
    threads = [Thread(target=loop, args=(nsec,)) for nsec in loops]
    [thread.start() for thread in threads]
    [thread.join() for thread in threads]
