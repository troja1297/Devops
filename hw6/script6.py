import time


# calculate digits
def digits(num):
    return len(str(num))


# reverse order
def reverse(num):
    return int(str(num)[::-1])


# check binary counterpartner
def bin_pal_chk(number):
    b = int(bin(number)[2:])
    if (b == reverse(b)):
        return True
    else:
        return False


# list with all base 10 palindromes
palin = []
# calculate palindromes
t = time.clock()
for i in range(1, 1000000):
    # single digits
    if (i < 10):
        if bin_pal_chk(i):
            palin.append(i)
    # even digits
    num = i * 10 ** digits(i) + reverse(i)
    if bin_pal_chk(num):
        palin.append(num)
    # uneven digits
    if (i < 100):
        for j in range(10):
            num = i * 10 ** (digits(i) + 1) + j * 10 ** digits(i) + reverse(i)
            if bin_pal_chk(num):
                palin.append(num)
print(palin.__str__())
print((time.clock() - t).__str__())

# t = time.clock()
# for i in range (1, 100000000):
#     num_10 = str(i)
#     num_2 = str(bin(i)[2:])
#
#     if num_10 == num_10[::-1] and num_2 == num_2[::-1]:
#         print(str(num_10) + ' - ' + str(num_2))
#
# print((time.clock() - t).__str__())