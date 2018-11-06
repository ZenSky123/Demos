# Demos

记录在学习过程中记录的一些Demo，就好像学数学要不停的看例题一样，在实际开发中我总是会回到某第三方库的初始文档然后看一些东西，而这些东西恰恰是官方文档中已经记录进tutorial板块的内容，所以我想将这些代码记录下来，加上一些辅助性的内容——一些基本的说明，使用说明等等，作为日后自己学习的辅助工具。

## web
- django
    - mysite 根据django官方教程编写的一个最简单的投票应用
- socket
    - TCPSimplest socket最简单应用，服务器接受一个字符串加上时间戳返回给客户端
    - UDPSimplest socket最简单应用，服务器接受一个字符串加上时间戳返回给客户端
    - SocketServerSimplest socketserver最简单应用，服务器接受一个字符串加上时间戳返回给客户端
    
## performance
- multithread
    - mtSimplestWithFunc 使用原生Thread类进行多线程编程
    - mtSimplestWithClass 继承Thread类进行多线程编程
    - mtLockSimplest 同步原语-锁的最简单的例子（去除锁之后上下输出可能乱序，请读者自己尝试）
    - mtSemaphoreSimplest 同步原语-信号量最简单的例子
    - mtQueueSimplest 使用队列模拟生产者-消费者模型