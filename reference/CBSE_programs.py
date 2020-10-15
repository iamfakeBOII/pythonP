#PRINT THE FOLLOWING SERIES: 1-x^1+x^2-x^3+x^4+ ......... x^n
'''
print('HI THERE!')
x = int(input('ENTER BASE VALUE: '))
n = int(input('ENTER POWER VALUE: '))
even_nums = []
odd_nums = []

def even():
    for a in range(2,n+1,2):
        val_1 = x**a
        even_nums.append(val_1)

    for b in range(1,n,2):
        val_2 = x**b
        odd_nums.append(val_2)

    final_1 = sum(even_nums)
    final_2 = sum(odd_nums)
    final_answer = 1+(final_1 - final_2)
    print(f'THE FINAL VALUE OF THE SERIES IS {final_answer}')

def odd():
    for a in range(1,n+1,2):
            val_1 = x**a
            odd_nums.append(val_1)    
    for b in range(2,n,2):
        val_2 = x**b
        even_nums.append(val_2)
                
    final_1 = sum(even_nums)
    final_2 = sum(odd_nums)

    final_answer = 1+(final_1 - final_2)
    print(f'THE FINAL VALUE OF THE SERIES IS {final_answer}')

if n<0:
    print('ENTER POSITIVE VALUE')
elif n == 0:
    print('THE FINAL VALUE OF THE SERIES IS 0')
else:
    if n%2 == 0:
        even()
    else:
        odd()
'''
 
#PRINT THE FOLLOWING SERIES: 1 + (x^1)/1! + (x^2)/2! + ... + (x^n)/n!
'''
print('HI THERE!')
x = int(input('ENTER BASE VALUE: '))
n = int(input('ENTER POWER AND FACTORIAL VALUE: '))
final_bottom = 1
final_sum = []

def main():
    for a in range(2,n+1):
        final_top = x**a
        for b in range(1,a+1):
            final_bottom = 1*b
    div = (final_top)/(final_bottom)
    final_sum.append(div)
    final_answer = 1 + x + sum(final_sum)
    print(f'THE FINAL VALUE OF THE SERIES IS {final_answer}')

if n < 0:
    print('NOT POSSIBLE')
elif n == 0:
    print(f'THE FINAL VALUE OF THE SERIES IS {2+x}')
elif n == 1:
    print(f'THE FINAL VALUE OF THE SERIES IS {1+(2*x)}')
else:
    main()
'''

#A.P
'''
print('HI THERE!')
a = int(input('ENTER FIRST VALUE: '))
r = int(input('ENTER SECOND VALUE: '))
n = int(input('ENTER POWER VALUE: '))
sum = 0

for g in range(0,n+1):
    prod = a*(r**g)
    sum += prod

print(f'THE FINAL VALUE OF THE SERIES IS {sum}') 
'''

#SERIES
print('HI THERE!')
x = int(input('ENTER BASE VALUE: '))
n = int(input('ENTER POWER AND FACTORIAL VALUE: '))
final_bottom_1 = final_bottom_2 = 1
even_num = []
odd_num = []

def odd():
    for a in range(2,n,2):
        final_top_1 = x**a
        for b in range(1,a+1):
            final_bottom_1 = 1*b
    div_1 = (final_top_1)/(final_bottom_1)
    even_num.append(div_1)

    for c in range(3,n+1,2):
        final_top_2 = x**c
        for d in range(1,c+1):
            final_bottom_2 = 1*d
    div_2 = (final_top_2)/(final_bottom_2)
    odd_num.append(div_2)

    final_sum = sum(even_num)-sum(odd_num)
    final_ans = x + final_sum
    print(f'THE FINAL VALUE OF THE SERIES IS {final_ans}')

def ev():
    for a in range(2,n+1,2):
        final_top_1 = x**a
        for b in range(1,a+1):
            final_bottom_1 = 1*b
    div_1 = (final_top_1)/(final_bottom_1)
    even_num.append(div_1)

    for c in range(3,n,2):
        final_top_2 = x**c
        for d in range(1,c+1):
            final_bottom_2 = 1*d
    div_2 = (final_top_2)/(final_bottom_2)
    odd_num.append(div_2)

    final_sum = sum(even_num)-sum(odd_num)
    final_ans = x + final_sum
    print(f'THE FINAL VALUE OF THE SERIES IS {final_ans}')

    
if n < 0:
    print('NOT POSSIBLE')
elif n == 0:
    print(f'THE FINAL VALUE OF THE SERIES IS {2+x}')
elif n == 1:
    print(f'THE FINAL VALUE OF THE SERIES IS {1+(2*x)}')
else:
    if n%2 == 0:
        ev()
    else:
        odd()











