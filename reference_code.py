#PROGRAM TO FIND ELECTRICITY BILL TO BE PAID ACCORDING TO THE GIVEN CRIETERIA
'''
units = float(input('ENTER THE AMOUNT OF UNITS: '))

if units<0:
    print('PLEASE ENTER A POSITIVE VALUE')
elif (units>=0 and units<=100):
    bill = (units*50)+5000
    print(f'THE ELECTRICITY BILL TO BE PAID IS {bill} dihrams or {bill/100} riyals')
elif (units>100 and units<=200):
    new_units = units-100
    bill = (new_units*75)+5000+5000
    print(f'THE ELECTRICITY BILL TO BE PAID IS {bill} dihrams or {bill/100} riyals')
else:
    new_units = units-200
    bill = (new_units*100)+5000+7500+5000
    print(f'THE ELECTRICITY BILL TO BE PAID IS {bill} dihrams or {bill/100} riyals')
'''

#PROGRAM FOR SERIES: 1+(1+2)+(1+2+3)+....+(1+2+3+..+n)
'''
num = int(input('HOW MANY NUMBERS: '))
s = 0
count = 2

for a in range(num):
    for b in range(1,count):
        s += b
    count += 1

print(f'THE FINAL SUM IS {s}')
'''

#PROGRAM TO PRINT SERIES
'''
n = int(input('ENTER THE INITIAL NUMBER: '))
r = 0
for a in range(n):
    for b in range(n,r,-1):
        print(b, end='') 
    print('')
    r += 1
'''

#PROGRAM TO PRINT SPECIAL SERIES
'''
n = int(input('ENTER THE NUMBER OF ROWS: '))

for a in range(1,n+1):
    print(' '*(n-a)+'* '*a)
'''

#PROGRAM TO CALCULATE THE TOTAL FARE
'''
age = int(input('ENTER YOUR AGE: '))
fare = int(input('ENTER FARE OF TICKET: '))

if (age>0 and age<=6):
    print(f'NO FARE. ENJOY A FREE RIDE!')
elif (age>6 and age<=12):
    cost = fare/10
    print(f'FINAL AMOUNT TO BE PAID {cost}')
elif (age>12 and age<=60):
    print(f'FINAL AMOUNT IS {fare}')
elif age>60:
    cost = (fare*3)/10
    print(f'FINAL AMOUNT IS {cost}')
else:
    print('ENTER A VALID AGE!')
'''

#PROGRAM
'''
print('HI THERE!')
n = int(input('ENTER THE NUMBER UPTO WHICH THE SUM IS REQUIRED: '))
count = 0
s = 0
num = 1

while count<n:
    s += num
    num += 2
    count += 1

print(f'THE SUM OF {n} OFF ODD NUMBERS IS {s}')
'''

#PROGRAM
'''
print('HI THERE!')
n = int(input('ENTER THE REQUIRED NUMBER: '))
factors = []

for a in range(2,n):
    if n%a == 0:
        factors.append(a)
    else:
        continue

print(f'THE FACTORS OF THE GIVEN NUMBER ARE {factors}')
'''

#PROGRAM
'''
print('HI THERE!')
n = int(input('HOW MANY PERFECT NUMBERS: '))
i = 2
s = 0
count = 0
numbers = []
        
while count<n:
    for a in range(1, i):
        if i%a==0:
            s = s+a
    
    if s==i:
        numbers.append(i)
        i += 1
        count += 1
        s = 0
        continue
    else:
        i += 1
        s = 0
        continue

print(f'THE {n} PERFECT NUMBERS ARE {numbers}')
'''

#PROGRAM TO PRINT SERIES
'''
n = int(input('ENTER THE NUMBER OF ROWS: ')) #n=5
#i = n

for a in range(n,0,-1):    #outer loop for rows
    for b in range(1,a+1):    #inner loop for columns
        print(b, end='') #print column values 

    print('') #for outer loop - for new line
    #i -= 1    #for updating column values such as 5,4,3,2,1..
'''

#PROGRAM TO PRINT SERIES
'''
n = int(input('ENTER THE NUMBER OF ROWS: '))
r = 0

for a in range(n):
    for b in range(7,r,-2):
        print(b, end='')
    print('')
    r += 2
'''

#PROGRAM FOR SERIES: 1+(1+2)+(1+2+3)+....+(1+2+3+..+n)
'''
num = int(input('UNTIL WHICH NUMBER: '))
def print2():
    s = 0
    count = 2

    for a in range(num):
        for b in range(1,count):
            s += b
        count += 1

    print(f'THE FINAL SUM IS {s}')

print2()
'''

#PROGRAM FOR SERIES: 1*2*3 + 2*3*4 + 3*4*5 + .... + n*(n+1)*(n+2)
'''
num = int(input('ENTER A NUMBER: '))
s = 0
i = 1
r = 2

for a in range(num):
    for b in range(i,r):
        s += i*(i+1)*(i+2)
        i += 1
        r += 1

print(f'THE SUM OF THE FINAL SERIES IS {s}')
'''






