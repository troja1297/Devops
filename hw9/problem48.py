arr = []
for i in range(1001):
    arr.append(i ** i)
print(str(sum(arr))[-10:])


print(str(sum([i**i for i in range(1001)]))[-10:])
