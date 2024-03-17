def s(array):
    if len(array) > 1:
        array[0], array[1] = array[1], array[0]
    return array


def ss(firstArray, secondArray):
    return s(firstArray), s(secondArray)


def p(firstArray, secondArray):
    if len(secondArray) > 0:
        firstArray = [secondArray[0]] + firstArray
        secondArray.pop(0)
        return firstArray, secondArray


def r(array):
    temp = array.pop(0)
    array.append(temp)
    return array


def rr(firstArray, secondArray):
    return r(firstArray), r(secondArray)


def rab(lst):
    temp = lst.pop(len(lst) - 1)
    lst = [temp] + lst
    return lst


def rrr(firstArray, secondArray):
    return rab(firstArray), rab(secondArray)


a = []
b = []
commList = []

userInput = input()

while userInput != "!":
    a.append(int(userInput))
    userInput = input()

userInput = input()

while userInput != "*":
    commList.append(userInput)
    userInput = input()

tempoRar = sorted(a)

for x in commList:
    if x == "sa":
        a = s(a)
    if x == "sb":
        b = s(b)
    if x == "ss":
        temp = ss(a, b)
        a = temp[0]
        b = temp[1]
    if x == "pa":
        temp = p(a, b)
        a = temp[0]
        b = temp[1]
    if x == "pb":
        temp = p(b, a)
        b = temp[0]
        a = temp[1]
    if x == "ra":
        a = r(a)
    if x == "rb":
        b = r(b)
    if x == "rr":
        temp = rr(a, b)
        a = temp[0]
        b = temp[1]
    if x == "rra":
        a = rab(a)
    if x == "rrb":
        b = rab(b)
    if x == "rrr":
        temp = rrr(a, b)
        a = temp[0]
        b = temp[1]

if a == tempoRar:
    print("OK")
else:
    print("KO")
