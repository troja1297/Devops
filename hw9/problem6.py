# x = 0
# y = 0
# for a in range(101):
#     x += a ** 2
#     y += a
#
# print(int(y ** 2 - x))

print(sum([y for y in range(101)])**2 - sum([x**2 for x in range(101)]))