def fib(n):
    a, b, c = 1, 1, 1
    while c < n:
        c += 1
        yield a
        a, b = b, a + b


for x in fib(20):
    print(x)
