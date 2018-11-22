
def numbermagnifier(mInputString):

    if mInputString % 2 == 0:
        print(str(mInputString / 2))
    else:
        print(str(mInputString * 3 + 1))


while True:
    inputString = ""
    try:
        print("Введите число")
        inputString = input()
        numbermagnifier(int(inputString))
    except ValueError:
        print("Не удалось преобразовать введенный текст в число. ")
        if inputString == "cancel":
            break