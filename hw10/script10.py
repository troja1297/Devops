def kollatch(number, stepcount=0):
    res = 0
    if number != 1:
        if number % 2 == 0:
            res = number / 2
        else:
            res = (number * 3) + 1

    if res < 1:
        print("Колличество шагов: " + str(stepcount + 1))
    else:
        print(str(int(res)))
        stepcount += 1
        kollatch(res, stepcount)


print("Введите любое натуральное число")
kollatch(int(input()))
