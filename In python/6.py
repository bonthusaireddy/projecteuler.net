n = 100
s = 0
sq = 0
for i in range(n+1):
    s = s + i
    sq = sq + i*i
print(s*s - sq)