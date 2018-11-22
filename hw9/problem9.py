# for a in {x for x in range(int(1000 / 3))}:
#     b = a + 1
#     for b in {x for x in range(int(1000 / 2))}:
#         c = 1000 - a - b
#         if a ** 2 + b ** 2 == c ** 2:
#             print(int(a * b * c))


print([a * b * c for a in range(int(1000 / 3)) for b in range(a + 1, int(1000 / 2)) for c in range(1000 - a - b, 1000 - a - b + 1) if (a ** 2 + b ** 2 == c ** 2) and (a + b + c == 1000)][0])