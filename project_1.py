import random as r
import time as t

def bindiv(lst, number, l):
    if len(lst) == 1 and number == lst[0]:
        return l + 1
    elif len(lst) == 1 and number != lst[0]:
        return None
    if number >= lst[len(lst) // 2]:
        l += len(lst) // 2
        return bindiv( lst[int((len(lst)) / 2):len(lst) + 1], number, l)
    elif number < int(lst[int(len(lst) / 2)]):
        return bindiv(lst[:int(len(lst) / 2)], number, l)


number = int(input())
a1 = r.randint(-32768, -3276)
a2 = r.randint(3276, 32768)
lst = []
for i in range(a1, a2):
    lst.append(i)
l = 0

t2 = t.perf_counter()

print(bindiv(lst, number, l))

t3 = t.perf_counter()

f = 1
while len(lst) > 1:
    if lst.count(number) == 0:
        f = None
        break
    if number < lst[len(lst) // 2]:
        lst = lst[:len(lst) // 2]
    elif number >= lst[len(lst) // 2]:
        f += len(lst) // 2
        lst = lst[(len(lst) // 2):len(lst) + 1]
t4 = t.perf_counter()
print(f)
print('Время выполнения рекурсивной функции:', ':{:.8f}'. format(t3 - t2))
print('Время выполнения цикла:', ':{:.8f}'. format(t4 - t3))
t5 = t.perf_counter()
print('Время выполнения всего проекта', t5)
