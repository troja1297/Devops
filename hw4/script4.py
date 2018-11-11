import time
import re

start_time = time.clock()
print("Введите несколько неотрицательных чисел через пробел:")
str = re.split('\D+', input())

res = 0

for var in str:
    try:
        i = int(var)
        res += i
    except Exception as ex:
        pass


print(res.__str__() + " " + (time.clock() - start_time).__str__() + " seconds")
