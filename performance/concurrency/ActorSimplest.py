def print_actor():
    while True:
        try:
            msg = yield
            print("Got:", msg)
        except GeneratorExit:
            print("Actor terminating")
            break


p = print_actor()
next(p)  # 激活生成器
p.send("Hello")
p.send("World")
p.close()
