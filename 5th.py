n, c = int(input()), 0
while n: n, c = n - 1 if { '1', '3', '5', '7', '9' } & set(str(n)) else n // 2, c + 1
print(c)



