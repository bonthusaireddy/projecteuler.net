n, a, b, ans = 4000000, 1, 1, 0
while(b < n):
    a, b = b, (a+b)
    if a % 2 == 0:
        ans = ans + a
    