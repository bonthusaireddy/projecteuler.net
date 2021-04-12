n = 600851475143
import sympy
arr = [13195]
for i in range(1,arr[-1]):
    if n % i == 0:
        if sympy.isprime(i):
            arr.append(i)