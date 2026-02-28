sum = 0
n = [5, 4, -1, 7, 8]
mv = n[0]
for  v in n:
    sum += v
    mv = max(mv, sum)
    if sum < 0:
        sum = 0
print(mv) 