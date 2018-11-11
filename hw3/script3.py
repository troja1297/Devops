import time
import re

def deduplicate(symbols):
    """
    This is delete duplicate and counting words/symbols
    :param symbols: list with words/symbols
    :return: list without duplicate words/symbols
    """
    buf = list()
    res = list()
    for symbol in symbols:
        buf.append([symbol, symbols.count(symbol)])
    for val in buf:
        if val not in res:
            res.append(val)

    return res

start_time = time.clock()
print("Введите несколько слов:")

res = deduplicate(input().lower().split())
sorted(res, reverse=False)

f = res[0][1]
for var in res:
    if f == var[1]:
        print(var[0] + " - " + var[1].__str__())

print((time.clock() - start_time).__str__() + " seconds")
