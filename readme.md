# Demos

记录在学习过程中记录的一些Demo，就好像学数学要不停的看例题一样，在实际开发中我总是会回到某第三方库的初始文档然后看一些东西，而这些东西恰恰是官方文档中已经记录进tutorial板块的内容，所以我想将这些代码记录下来，加上一些辅助性的内容——一些基本的说明，使用说明等等，作为日后自己学习的辅助工具。

## web
- django
    - mysite 根据django官方教程编写的一个最简单的投票应用
    - tutorial 根据django-rest-framework中的教程节走完的代码
- RPC
    - XML_RPC 使用xmlrpc实现简单的RPC
    - ListenerRPC 使用multiprocessing的conection库来完成RPC 
- socket
    - TCPSimplest socket最简单应用，服务器接受一个字符串加上时间戳返回给客户端
    - UDPSimplest socket最简单应用，服务器接受一个字符串加上时间戳返回给客户端
    - SocketServerSimplest socketserver最简单应用，服务器接受一个字符串加上时间戳返回给客户端
- WSGI
    - WSGISimplest 最简单的WSGI应用
    - WSGIWithMiddleware 增加一个中间件函数来扩展WSGI应用
    - WSGIWithMiddlewareClass 增加一个中间件类来扩展WSGI应用
    
## performance
- multithread
    - mtConditionSimplest Condition同步最简单的例子
    - mtEventSimplest Event同步最简单的例子
    - mtSimplestWithFunc 使用原生Thread类进行多线程编程
    - mtSimplestWithClass 继承Thread类进行多线程编程
    - mtLockSimplest 同步原语-锁的最简单的例子（去除锁之后上下输出可能乱序，请读者自己尝试）
    - mtPoolSimplest 线程池最简单的例子
    - mtSemaphoreSimplest 同步原语-信号量最简单的例子
    - mtQueueSimplest 使用队列模拟生产者-消费者模型
    - mtQueueTaskSimplest 使用队列的基本同步功能模拟生产者-消费者模型
- coroutine
    - coroutineHard 较难的协程使用
    - coroutineSimplest 简单的协程使用
- concurrency
    - spider
        - SpiderInOrder 单线程顺序爬虫
        - SpiderWithAsyncio 使用Asyncio库完成爬虫
        - SpiderWithAsyncioExecutor 异步保存文件优化
        - SpiderWithAsyncioSemaphore 限制请求数量
        - SpiderWithFuture 使用Future完成爬虫
        - SpiderWithFutureV2 使用Future完成爬虫的版本二
        - util 爬虫需要用到的一些公用函数
    - server
        - charfinder server要用到的一些函数
        - ServerWithAsyncio 使用Asyncio构建的一个服务器（要使用telnet测试）
    - ActorSimplest 同步的生成器Actor
    - AsyncActorSimplest 异步Actor
## hack
- builtin
    - bisect_demo 使用bisect的一些demo
    - inspect_demo 使用inspect的一些demo
    - format_demo 使用format的一些demo
    - iter 迭代器的相关一些demo
- class
    - UglyStateMachine 丑陋的实现状态机的方案
    - ElegantStateMachine 优雅的实现状态机的方案
    - PerfectStateMachine 我最喜欢的实现状态机的方案