import random as r


def bindiv(lst, number, len_):
    if lst.count(number) == 0:
        return None
    if len_ == 1:
        return 0
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
print(bindiv(lst, number, len(lst)))
