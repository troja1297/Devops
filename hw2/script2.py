import time

s_time = time.clock()
print("Введите последовательность символов: ")
str = input().lower()
buf = list()
for char in str:
    if char not in buf:
        buf.append(char)
res = ""
for char in buf:
    res += char
print(res + " " + (time.clock() - s_time).__str__() + " seconds")


