import time


def deduplicate(symbols):
    """
    This is delete duplicate words/symbols
    :param symbols: list with words/symbols
    :return: list without duplicate words/symbols
    """
    buf = list()
    for symbol in symbols:
        buf.append([symbol, symbols.count(symbol)])
    for val in buf:
        if val in buf:
            buf.remove(val)
    return buf

start_time = time.clock()
print("Введите несколько слов:")
str = input().lower().split()
res = deduplicate(str).__str__()

print(res + " " + (time.clock() - start_time).__str__() + " seconds")
