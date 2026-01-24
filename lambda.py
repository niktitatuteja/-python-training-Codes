add = lambda a,b: a+b
print(add(40,60))

print((lambda a,b: a+b)(10,20))
 
fact = lambda n : n * fact(n-1) if n > 0 else 1
print(fact(6))
