def find_numbers(n):
    if n <= 6:
        return
    for i in range(1, n):
        s = 1
        for j in range(2, i):
            if i % j == 0:
                s += j
            if s > i:
                break
        if s == i:
            print(i)


find_numbers(int(input()))
