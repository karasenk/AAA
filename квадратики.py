n = int(input())
field = [list(map(int, input().split())) for _ in range(n)]

res = 0
for i in range(n - 1):
    for j in range(n - 1):
        if len({field[i][j], field[i + 1][j], field[i + 1][j + 1], field[i][j + 1]}) == 4:
               res += 1
print(res)
