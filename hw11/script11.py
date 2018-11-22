def letters_range(start, stop):
    arr = []
    for i in range(65, 91):
        arr.append(chr(i).lower())
    try:
        return arr[arr.index(start):arr.index(stop) + 1]
    except ValueError:
        print("There is no such symbol")


print(letters_range("a", "d"))
