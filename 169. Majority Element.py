n = [2,2,1,1,1,2,2]
d = {}
for v in n:
    if v in d:
        d[v] += 1
    else:
        d[v] = 1
for k in d:
    if d[k] > (len(n)//2):
        print(k)