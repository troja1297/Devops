from functools import reduce


print(reduce((lambda x, y: x * y), [(int((''.join([str(i) for i in range(200000)]))[10**i])) for i in range(0,7)]))
