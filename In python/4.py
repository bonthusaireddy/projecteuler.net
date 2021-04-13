greater = 0
for i in range(999, 99, -1):
    for j in range(999, 99, -1):
        product = i * j
        if product > greater:
            s = str(product)
            if s == s[::-1]:
                greater = product
print(greater)
