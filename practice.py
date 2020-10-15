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

x = 7
for i in range(4, 0, -1):
	x = 7
	for j in range(i, 0, -1):
		print(x, end = " ")
		x -= 2
	print()


























			


