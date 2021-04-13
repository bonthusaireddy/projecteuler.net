n = 1000000000
for i in range(2,n):
    for j in range(2,20):
        if i % j != 0:
            break
    else:
        print(i)
        break