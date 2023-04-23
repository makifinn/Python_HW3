import random

# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

size = int(input("введите размер массива: "))

newArray = []

for i in range(size):
    array = random.randint(1,size)
    newArray.append(array)
print(*newArray)

x = int(input("какое число от 1 до {} нужно найти: ".format(size)))

count = 0

for j in newArray:
    if j == x:
        count += 1

print(count)


# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

size = int(input("введите размер массива: "))

newArray2 = []

for i in range(size):
    array = random.randint(1,size)
    newArray2.append(array)
print(*newArray2)

x = int(input("введите число: "))
	
indexCounter = 0
difUp = x
difDown = x

for i in newArray2:
    if i == x:
        difUp = 0
        break
    elif i > x and difUp >= i - x:
        difUp = i - x
    elif i < x and difDown >= x - i:
        difDown = x - i

if difUp == difDown:
    nearestDigits = [None, None]
else:
    nearestDigits = [None]

for i in newArray2:
    if difUp == difDown:
        if i == x:
            nearestDigits[0] = x
            break
        elif i == x - difDown:
            nearestDigits[0] = i
        elif i == x + difUp and difUp != difDown:
            nearestDigits[0] = i
        elif i == x + difUp and difUp == difDown:
            nearestDigits[1] = i
    else:
        if difUp < difDown and i == x + difUp:
            nearestDigits[0] = i
        elif difDown < difUp and i == x - difDown:
            nearestDigits[0] = i

if difUp == difDown:
    print("ближе всего: {} и {}".format(nearestDigits[0], nearestDigits[1]))
else:
    print("ближе всего: {}".format(nearestDigits[0]))


# Игра Скрабл

letters = {'aeiolnstrавеинорст' : 1,
     'dgдклмпу' : 2,
     'bcmpбгёья' : 3,
     'fhvwyйы' : 4,
     'kжхзцч' : 5,
     'jxшэю' : 8,
     'qzфщъ' : 10}

word = input("введите слово: ")

count = 0

for i in word:
    for i_key, i_value in letters.items():
        if i in i_key:
            count += i_value

print(count)