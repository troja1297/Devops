def kollatch(number, stepcount=0):
    res = 0
    if number != 1:
        if number % 2 == 0:
            res = number / 2
        else:
            res = (number * 3) + 1

    if res < 1:
        return stepcount
    else:
        stepcount += 1
        return kollatch(res, stepcount)


print("Введите число;")
print(kollatch(int(input())))
