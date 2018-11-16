from threading import Thread, Event
import time


def countdown(n: int, started_evt: Event):
    print('countdown starting')
    started_evt.set()
    while n > 0:
        print('T-minus', n)
        n -= 1
        time.sleep(5)

started_evt=Event()

print("Launching countdown")
t=Thread(target=countdown,args=(10,started_evt))
t.start()

started_evt.wait()
print('countdown is running')