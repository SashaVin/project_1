import random as r
import time as t

def bindiv(lst, number, len_):
    if len_ == 1 and lst[0] != number:
        return None
    if len_ == 1:
        return 1
    if len_ % 2 == 1:
        if lst[(len_ // 2 + 1):].count(number) > 0:
            return len_ // 2 + 1 + bindiv(lst[(len_ // 2 + 1):], number, len(lst[(len_ // 2 + 1):]))
        else:
            return bindiv(lst[:(len_ // 2 + 1)], number, len(lst[:(len_ // 2 + 1)]))
    else:
        if lst[(len_ // 2):].count(number) > 0:
            return len_ // 2 + 1 + bindiv(lst[(len_ // 2):], number, len(lst[(len_ // 2):]))
        else:
            return bindiv(lst[:(len_ // 2)], number, len(lst[:(len_ // 2)]))


number = int(input())
a1 = r.randint(-32768, -3276)
a2 = r.randint(3276, 32768)
lst = []
for i in range(a1, a2):
    lst.append(i)


t2 = t.perf_counter()

print(bindiv(lst, number, len(lst)))

t3 = t.perf_counter()

f = 1
while len(lst) > 1:
    if lst.count(number) == 0:
        f = None
        break
    if len(lst) % 2 == 1:
        if lst[(len(lst) // 2 + 1):].count(number) > 0:
            f += len(lst) // 2 + 1
            lst = lst[(len(lst) // 2 + 1):]
        else:
            lst = lst[:(len(lst) // 2 + 1)]
    else:
        if lst[(len(lst) // 2):].count(number) > 0:
            f += len(lst) // 2 + 1
            lst = lst[(len(lst) // 2):]
        else:
            lst = lst[:(len(lst) // 2)]
t4 = t.perf_counter()
print(f)
print('Время выполнения рекурсивной функции:', ':{:.8f}'. format(t3 - t2))
print('Время выполнения цикла:', ':{:.8f}'. format(t4 - t3))
t5 = t.perf_counter()
print('Время выполнения всего проекта', t5)
