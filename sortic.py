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


one = []
two = []
userInput = input()

while userInput != "!":
    one.append(int(userInput))
    userInput = input()

if len(one) > 0:
    tempoRar = sorted(one)
    while one != tempoRar:
        while len(one) > 1:
            if one[0] == max(one[0], one[1]):
                temp = p(two, one)

                print("pb")

                one = temp[1]
                two = r(temp[0])

                print("rb")
            else:
                one = s(one)

                print("sa")

                temp = p(two, one)

                print("pb")

                one = temp[1]
                two = r(temp[0])

                print("rb")
        while len(two) > 1:
            if two[0] == min(two[0], two[1]):
                temp = p(one, two)

                print("pa")

                two = temp[1]
                one = r(temp[0])

                print("ra")
            else:
                two = s(two)

                print("sb")

                temp = p(one, two)

                print("pa")

                two = temp[1]
                one = r(temp[0])

                print("ra")

        temp = p(one, two)

        print("pa")

        two = temp[1]
        one = r(temp[0])

        print("ra")

print(one)