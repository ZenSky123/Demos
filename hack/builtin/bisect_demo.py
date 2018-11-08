import bisect
import random


def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
    i = bisect.bisect(breakpoints, score)
    return grades[i]


def insort():
    my_list = []
    for _ in range(10):
        number = random.randrange(20)
        bisect.insort(my_list, number)
    return my_list


if __name__ == '__main__':
    print("60分的等级为：", grade(60))
    print("使用insrot随机插入10个在[0,20)之间的数结果为：", insort())
