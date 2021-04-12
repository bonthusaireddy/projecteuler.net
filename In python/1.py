n = int(input("Enter a natural numbaer: "))
sum3 = 0
sum5 = 0
for i in range(n):
    if i % 3 == 0:
        sum3 = sum3 + i
        continue
    if i % 5 == 0:
        sum5 = sum5 + i
print(sum3+sum5)
