def s(array):
    if len(array) > 1:
        array[0], array[1] = array[1], array[0]
    return array

def p(firstArray, secondArray):
    if len(secondArray) > 0:
        firstArray = [secondArray[0]] + firstArray
        secondArray.pop(0)
        return firstArray, secondArray

def r(array):
    temp = array.pop(0)
    array.append(temp)
    return array

def rab(lst):
    temp = lst.pop(len(lst) - 1)
    lst = [temp] + lst
    return lst

def ss(firstArray, secondArray):
    return s(firstArray), s(secondArray)

def rr(firstArray, secondArray):
    return r(firstArray), r(secondArray)

def rrr(firstArray, secondArray):
    return rab(firstArray), rab(secondArray)

arr = []
userInput = input("Введите число или '!' для завершения ввода: ")

while userInput != "!":
    arr.append(int(userInput))
    userInput = input("Введите число или '!' для завершения ввода: ")

def sort_array(arr):
    a = arr
    b = []

    while a != sorted(a):
        while len(a) > 1:
            if a[0] == min(a):
                temp = p(b, a)
                a = temp[1]
                b = r(temp[0])
            else:
                a = ss(a, a)[0]
                temp = p(b, a)
                a = temp[1]
                b = r(temp[0])

        while len(b) > 0:
            temp = p(a, b)
            b = temp[1]
            a = r(temp[0])

    return a

sorted_arr = sort_array(arr)
print(sorted_arr)