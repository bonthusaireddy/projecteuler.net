import sympy
count = 0
i = 2
while(True):
    if sympy.isprime(i):
        count = count + 1
    if count == 10001:
        print(i)
        break
    i = i + 1