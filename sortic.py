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


def rab(array):
    temp = array.pop(len(array) - 1)
    lst = [temp] + array
    return lst


def rrr(firstArray, secondArray):
    return rab(firstArray), rab(secondArray)


a = []
b = []
userInput = input()

while userInput != "!":
    a.append(int(userInput))
    userInput = input()

if len(a) > 0:
    tempoRar = sorted(a)
    while a != tempoRar:
        while len(a) > 1:
            if a[0] == max(a[0], a[1]):
                temp = p(b, a)
                print("pb")
                a = temp[1]
                b = r(temp[0])
                print("rb")
            else:
                a = s(a)
                print("sa")
                temp = p(b, a)
                print("pb")
                a = temp[1]
                b = r(temp[0])
                print("rb")
        while len(b) > 1:
            if b[0] == min(b[0], b[1]):
                temp = p(a, b)
                print("pa")
                b = temp[1]
                a = r(temp[0])
                print("ra")
            else:
                b = s(b)
                print("sb")
                temp = p(a, b)
                print("pa")
                b = temp[1]
                a = r(temp[0])
                print("ra")
        temp = p(a, b)
        print("pa")
        b = temp[1]
        a = r(temp[0])
        print("ra")

print(f"{a}")
