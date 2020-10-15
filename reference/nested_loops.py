#NUMBER 1 - ASCENDING
'''
num = int(input('ENTER HOW MANY ROWS ARE REQUIRED: '))
count = 1
for b in range(num):
    for i in range(count):
        print('1', end=" ")
    print('')
    count +=1
    continue
'''

#NUMBER 1 - DESCENDING
'''
num = int(input('ENTER HOW MANY ROWS ARE REQUIRED: '))
count = num
for b in range(num):
    for i in range(count):
        print('1', end=" ")
    print('')
    count -=1
    continue
'''

#NUMBER - 1,2,3,4 - ASCENDING
'''
num_numbers = int(input('UNTIL WHICH NUMBER IS THE TRIANGLE REQUIRED: '))
count = 1
number = 2
for b in range(num_numbers):
    for i in range(count, number):
        print(i, end=" ")
    print('')
    #count += 1
    number +=1
    continue
'''

#NUMBER - 1,2,3,4 - DESCENDING
'''
num_numbers = int(input('FROM WHICH NUMBER IS THE TRIANGLE REQUIRED: '))
count = num_numbers
number = count 
for b in range(num_numbers):
    for i in range(count):
        print(number, end=" ")
    print('')
    count -= 1
    number -=1
    continue
'''

#NUMBER - 1,3,5,7.. - ODD - ASCENDING
'''
new_num = int(input('HOW MANY ROWS ARE REQUIRED: '))
count = 1
number = 1
for b in range(new_num):
    for i in range(count):
        print(number, end=" ")
    print('')
    count += 2
    number += 2
    continue
'''

#NUMBER - ODD - DESCENDING 
'''
new_num = int(input('HOW MANY ROWS ARE REQUIRED: '))
count = new_num*2
number = new_num*2
for b in range(new_num):
    for i in range(count):
        print(number, end=" ")
    print('')
    count -= 2
    number -= 2
    continue
'''

#NUMBERS - 2,4,6,8... - EVEN - DESCENDING
'''
new_num = int(input('HOW MANY ROWS ARE REQUIRED: '))
count = new_num*2
number = new_num*2
for b in range(new_num):
    for i in range(count):
        print(number, end=" ")
    print('')
    count -= 2
    number -= 2
    continue
'''



#WORD SERIES
word = input('ENTER A STRING: ')
rows = len(word)
count = 0
right = 1

for b in range(rows):
    for i in range(count, right):
        final = word[i]
        print(final, end=" ")
    print('')
    right += 1
    























