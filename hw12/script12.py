def fib(n):
    i = 2
    f1 = f2 = 1
    print(1)
    while i < n:
        f_sum = f2 + f1
        f1 = f2
        f2 = f_sum
        i += 1
        print(f_sum)
    return f_sum


fib(100)
