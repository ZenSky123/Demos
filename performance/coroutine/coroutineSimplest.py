def simple_coroutine():
    print("-> coroutine started")
    x = yield
    print('-> coroutine received:', x)


if __name__ == '__main__':
    my_coro = simple_coroutine()
    print(my_coro)
    next(my_coro)
    my_coro.send(42)
