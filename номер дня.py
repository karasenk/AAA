d = int(input())
m = int(input())
g = int(input())

res = d

res += (m // 2) * 31
if m > 3:
    res += (m // 2 - 2) * 30
    if g % 4 == 0:
        if g % 100 == 0:
            if g % 400 == 0:
                res += 29
            else:
                res += 28
        else:
            res += 29
    else:
        res += 28
if m == 9:
    res += 31
print(res)
    
