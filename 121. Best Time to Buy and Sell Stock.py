P =[7,1,5,3,6,4]
b = P[0]
Pf = 0
for i in range(1, len(P)):
    if b < P[i]:
        Pf = max(Pf, (P[i] - b))
    if b > P[i]:
        b = P[i] 
print(Pf)