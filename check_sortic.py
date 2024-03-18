def sa_sb(a):
    if len(a) > 1:
        a[0], a[1] = a[1], a[0]
    return a


def ss(a, b):
    return sa_sb(a), sa_sb(b)


def pa_pb(a, b):
    if len(b) > 0:
        a = [b[0]] + a
        b.pop(0)
        return a, b


def ra_rb(a):
    c = a.pop(0)
    a.append(c)
    return a


def rr(a, b):
    return ra_rb(a), ra_rb(b)


def raa_rab(a):
    c = a.pop(len(a) - 1)
    a = [c] + a
    return a


def rrr(a, b):
    return raa_rab(a), raa_rab(b)


a = []
b = []
comm = []
inp = input()
while inp != "!":
    a.append(int(inp))
    inp = input()
inp = input()
while inp != "*":
    comm.append(inp)
    inp = input()
sortic = sorted(a)
for command in comm:
    if len(a) > 0:
        if command == "sa":
            a = sa_sb(a)
        if command == "sb":
            b = sa_sb(b)
        if command == "ss":
            c = ss(a, b)
            a = c[0]
            b = c[1]
        if command == "pa":
            c = pa_pb(a, b)
            a = c[0]
            b = c[1]
        if command == "pb":
            c = pa_pb(b, a)
            b = c[0]
            a = c[1]
        if command == "ra":
            a = ra_rb(a)
        if command == "rb":
            b = ra_rb(b)
        if command == "rr":
            c = rr(a, b)
            a = c[0]
            b = c[1]
        if command == "rra":
            a = raa_rab(a)
        if command == "rrb":
            b = raa_rab(b)
        if command == "rrr":
            c = rrr(a, b)
            a = c[0]
            b = c[1]

if a == sortic:
    print("OK")
else:
    print("KO")
