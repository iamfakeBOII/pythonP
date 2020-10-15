#SWAPPING OF VARIABLES
#METHOD1
#principal@dpsmisdoha.com
#soma@dpsmisdoha.com

'''
a,b = 5,10

print(a,b)

a,b = b,a

print(a,b)
'''
#METHOD2
'''
a,b = 5,10

print(a,b)

c = a
a = b
b = c

print(a,b)
'''
#METHOD3
'''
a,b = 5,10
print(a,b)

a = a+b
b = a - b
a = a - b

print(a,b)
'''

# STRING IS A NON-MUTABLE DATA TYPE
# LIST IS A MUTABLE DATA TYPE
'''
a = 10
a%=5
print(a)
'''


#QUESSTION
'''
prin = float(input('PLEASE ENTER THE PRINCIPLE AMOUNT: '))
rate = 2.5
time = 2

simple_interest = (prin*rate*time)/100

print(f'The simple interest is {simple_interest}')
'''

#IN AND IS OPERATOR
'''
a = 's'
b = 'computers'

if a in b:
    print('WOKRS')
else:
    print('DOESNT WORK')

c = 's'
if a is c:
    print('WORKS')
else:
    print('DOESNT')
'''

#EXPONENTS, DIVISION/MULTIPLICATION/MODULUS ADDITION/SUBTRACTION ---> BODMAS IN PYTHON

#PUNCTUATING
import re
import turtle
noel = turtle.turtle()

text = 'The;quick;brown;fox;jumps;over;the;lazy*dog'
print(re.split(';|,|\*|\n', text))


