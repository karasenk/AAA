n = int(input())
seq = [1, 2, 3, 5]
num = [2, 3, 5]
i = 1
j = 0
while len(seq) < n:
    a = seq[i] * num[j % 3]
    if a not in seq:
        seq.append(a)
    j += 1
    if j % 3 == 0:
        i += 1
print(seq)
    
