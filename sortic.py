from colorama import Fore

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


def custom_sort(a):
    b = []

    while a != sorted(a):
        while len(a) > 1:
            if a[0] == max(a[0], a[1]):
                b = r(p(b, a)[0])
                print(Fore.BLUE, "pb")
                print(Fore.GREEN, "rb")
            else:
                a = s(a)
                b = r(p(b, a)[0])
                print(Fore.MAGENTA, "sa")
                print(Fore.BLUE, "pb")
                print(Fore.GREEN, "rb")

        while len(b) > 1:
            if b[0] == min(b[0], b[1]):
                a = r(p(a, b)[0])
                print(Fore.YELLOW, "pa")
                print(Fore.BLACK, "ra")
            else:
                b = s(b)
                a = r(p(a, b)[0])
                print(Fore.RED, "sb")
                print(Fore.YELLOW, "pa")
                print(Fore.CYAN, "ra")

        a = r(p(a, b)[0])
        print(Fore.YELLOW, "pa")
        print(Fore.BLACK, "ra")
    print(a)


a = []
inp = input()
while inp != "!":
    a.append(int(inp))
    inp = input()

if len(a) > 0:
    custom_sort(a)