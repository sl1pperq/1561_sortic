def s(lst):
    if len(lst) > 1:
        lst[0], lst[1] = lst[1], lst[0]
    return lst


def ss(lst1, lst2):
    return s(lst1), s(lst2)


def p(lst1, lst2):
    if len(lst2) > 0:
        lst1 = [lst2[0]] + lst1
        lst2.pop(0)
        return lst1, lst2


def r(lst):
    temp = lst.pop(0)
    lst.append(temp)
    return lst


def rr(lst1, lst2):
    return r(lst1), r(lst2)


def rab(lst):
    temp = lst.pop(len(lst) - 1)
    lst = [temp] + lst
    return lst


def rrr(lst1, lst2):
    return rab(lst1), rab(lst2)


a = []
b = []
inp = input()

while inp != "!":
    a.append(int(inp))
    inp = input()

if len(a) > 0:
    temporar = sorted(a)
    while a != temporar:
        while len(a) > 1:
            if a[0] == max(a[0], a[1]):
                temp = p(b, a)
                a = temp[1]
                b = r(temp[0])
            else:
                a = s(a)
                temp = p(b, a)
                a = temp[1]
                b = r(temp[0])
        while len(b) > 1:
            if b[0] == min(b[0], b[1]):
                temp = p(a, b)
                b = temp[1]
                a = r(temp[0])
            else:
                b = s(b)
                temp = p(a, b)
                b = temp[1]
                a = r(temp[0])
        temp = p(a, b)
        b = temp[1]
        a = r(temp[0])

print(a)
