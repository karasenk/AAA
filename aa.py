n, m = list(map(int, input().split()))
labirint = []
for i in range(n):
    st = input()
    s = []
    for j in range(m):
        if st[j] == ' ':
            s.append(0)
        else:
            s.append(-1)
    labirint.append(s)

    

def walk(x, y, step, dir_x, dir_y):
    step += 1
    if (x, y) == (n - 2, m - 2):
        return step
    labirint[x][y] += 1
    if all([all(n) for n in labirint]):
        return -1
    a = []
    if x + 1 < n and labirint[x + 1][y] >= 0:
        a.append((x + 1, y))
    if x - 1 >= 0 and labirint[x - 1][y] >= 0:
        a.append((x - 1, y))
    if y + 1 < m and labirint[x][y + 1] >= 0:
        a.append((x, y + 1))
    if y - 1 >= 0 and labirint[x][y - 1] >= 0:
        a.append((x, y - 1))
    if a:
        a = list(filter(lambda z: labirint[z[0]][z[1]] == labirint[a[0][0]][a[0][1]], sorted(a, key=lambda z: labirint[z[0]][z[1]])))
        if len(a) > 1:
            aa = list(filter(lambda z: z[0] - x == dir_x and z[1] - y == dir_y, a))
            print(aa)
            if aa:
                x1, y1 = aa[0]
            else:
               x1, y1 = a[0]
        else:
            print(a)
            x1, y1 = a[0]
            dir_x = x1 - x
            dir_y = y1 - y
        walk(x1, y1, step, dir_x, dir_y)
    return -1

print(str(walk(1, 1, 0, 1, 1)))