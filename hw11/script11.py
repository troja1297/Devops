def letters_range(start, stop, step=1):
    arr = []
    for i in range(65, 91):
        arr.append(chr(i).lower())
    try:
        if start == stop:
            return []
        else:
            return arr[arr.index(start):arr.index(stop):step]
    except ValueError:
        print("There is no such symbol")


print(letters_range('b', 'w', 2))
print(letters_range('a', 'g'))
print(letters_range('g', 'p'))
print(letters_range("p", "g", -2))
print(letters_range("a", "a"))
