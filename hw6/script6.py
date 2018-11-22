import time


def digits(num):
    return len(str(num))


def reverse(num):
    return int(str(num)[::-1])


def bin_pal_chk(number):
    b = int(bin(number)[2:])
    if b == reverse(b):
        return True
    else:
        return False


res = []

t = time.clock()
polindromSum = 0
for i in range(1, 1000):

    if i < 10:
        if bin_pal_chk(i):
            res.append(i)

    num = i * 10 ** digits(i) + reverse(i)
    if bin_pal_chk(num):
        res.append(num)

    if i < 100:
        for j in range(10):
            num = i * 10 ** (digits(i) + 1) + j * 10 ** digits(i) + reverse(i)
            if bin_pal_chk(num):
                res.append(num)

for var in sorted(res, reverse=False):
    polindromSum += var
    print(str(var) + " = " + str(bin(var)[2:]))
print("Sum of Polindroms " + str(polindromSum))
print((time.clock() - t).__str__())
