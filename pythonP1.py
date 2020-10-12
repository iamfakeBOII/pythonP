# 1 + x^1/1! + x^2/2!+..... + x^n/n! 
"""
x = int(input("x "))
n = int(input("n "))
dsum = []
de = 1
for i in range(2, n + 1):
    nu = x ** i
    for j in range(2, n + 1):
        de = de * j
    fdiv = nu/de
    dsum.append(fdiv)
    fsum = sum(dsum) + 1 + x
    print("the sum of the series is, ", fsum)
   """ 


