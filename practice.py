"""
n = int(input("n: "))
dsum = []
for i in range(1, n+1, 2):
	dsum.append(i)
fsum = sum(dsum)
print("sum: ", fsum)
"""

"""
num = int(input("number: "))
total = []
for i in range(1, num + 1):
	if num % i == 0:
		total.append(i)
total.remove(num)
total.remove(1)
print("factors are: ", total)
"""
"""
#p3
limit = int(input("enter upper limit for perfect number search: "))
n = 1
while n <= limit:

    sum = 0
    divisor = 1
    while divisor < n:
        if not n % divisor:
            sum += divisor
        divisor = divisor + 1
    if sum == n:
        print(n, "is a perfect number")
    n = n + 1
"""

# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2 
# 1
"""
row = int(input("rows: "))
for i in range(row, 0, -1):
	for j in range(1, i + 1):
		print(j, end = " ")
	print("")
"""
"""
x = 7
for i in range(4, 0, -1):
	x = 7
	for j in range(i, 0, -1):
		print(x, end = " ")
		x -= 2
	print()
"""

"""
x = int(input("rows: "))
for i in range(0, x):
	for j in range(0, i + 1):
		print("*", end = " ")
	print("")
"""
"""
x = int(input("base: "))
n = int(input("power: "))
fsum = 0
for i in range(0, n + 1):
	fsum += x**n
print(fsum)
"""
"""
x = int(input('ENTER THE BASE VALUE: '))
n = int(input('ENTER THE POWER VALUE: '))
s = 0

if n%2==0:
    for a in range(2,n+1,2):
        f1 = 1
        for i in range(1,a+1):
            f1 = f1*i
        s += (x**a)/f1

    for b in range(3,n,2):
        f2 = 1
        for i in range(1,b+1):
            f2 = f2*i
        s -= (x**b)/f2 
else:
    for a in range(2,n,2):
        f1 = 1
        for i in range(1,a+1):
            f1 = f1*i
        s += (x**a)/f1

    for b in range(3,n+1,2):
        f2 = 1
        for i in range(1,b+1):
            f2 = f2*i
        s -= (x**b)/f2
        
print(f'THE FINAL ANSWER IS {s+x}')
"""
"""
a = ["a", "b", "c"]
b = input("char: ")
for i in a:
	if(b in a):
		x = i + 1
print(x)
"""
"""
num = int(input("val: "))
num1 = 0
num2 = 1
series = 0
for i in range(num):
	print(series)
	num1 = num2
	num2 = series
	series = num1 + num2
"""
"""
even = 0
odd = 0
x = eval(input("list: "))
length = len(x)
for i in range(length):
	if i % 2 == 0:
		even = i
	else:
		odd = i
	x[even], x[odd] = x[odd], x[even]
print(x)
"""
"""
rows = int(input("rows: "))
for i in range(0, rows):
	for j in range(0, i+1):
		print("*", end = " ")
	print()
"""
"""
string = input("str: ")
l = len(string)
count = 0
s = string[::-1]
for i in range(l):
	print(string[i],"\t", s[i])
"""
vow = "AaEeIiOoUu"
st = input("str: ")
v, c, uC, lC = 0, 0, 0, 0
for i in st:
	if(i in vow):
		v += 1
	else:
		c += 1
	for j in range(65, 91):
		if(i == chr(j)):
			uC += 1
	for k in range(97, 123):
		if(i == chr(k)):
			lC += 1	
print(f"Vowels {v}, Consonants {c}, uppercase {uC}, lowercase {lC}")














			


