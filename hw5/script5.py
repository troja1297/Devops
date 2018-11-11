import time

start_time = time.clock()
print("Введите несколько неотрицательных чисел через любой не числовой разделитель:")

str = sorted(map(int, input().split()), reverse=True)
res = 0
for i in str:
    if (i + 1) not in str:
        res = i + 1
print(res.__str__())
print((time.clock() - start_time).__str__() + " seconds")