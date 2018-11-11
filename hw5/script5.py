import time

start_time = time.clock()
print("Введите несколько неотрицательных чисел через любой не числовой разделитель:")

str = list(map(int, input().split()))
str.sort()
res = 0
for i in str:
    if i + 1 in str:
        res = i + 2

print(res.__str__() + " " + (time.clock() - start_time).__str__() + " seconds")