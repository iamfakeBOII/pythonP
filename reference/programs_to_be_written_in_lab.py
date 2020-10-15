#PROGRAM1
#PROGRAM2
#PROGRAM3
#PROGRAM4
#PROGRAM5
#PROGRAM6
#PROGRAM7
#PROGRAM8
print('HI THERE!')
base = int(input('PLEASE ENTER THE BASE NUMBER: '))
power = int(input('PLEASE ENTER THE POWER: '))
nums = []

for a in range(0,power+1):
    final = base**a
    nums.append(final)

final_sum = sum(nums)
print('THE FINAL ANSWER OF THE SEQUENCE IS',final_sum)

#PROGRAM9
print('HI THERE!')
num1 = int(input('ENTER THE FIRST NUMBER REQUIRED: '))
num2 = int(input('ENTER THE SECOND NUMBER REQUIRED: '))
store = 0
factors1 = [num1]
factors2 = [num2]

for b in range(1,num1):
    div = num1%b
    if div == 0:
        factors1.append(b)

for b in range(1,num2):
    div = num2%b
    if div == 0:
        factors2.append(b)

if num1<num2:
    check = max(factors1)
    if check in factors2:
        print('THE GREATEST COMMON DIVISOR IN',num1,'AND',num2,'IS',check)
    else:
        print('THE TWO NUMBERS HAVE NO COMMON FACTORS. SO THE GREATEST COMMON DIVISOR IS 1')
else:
    check = max(factors2)
    if check in factors1:
        print('THE GREATEST COMMON DIVISOR IN',num1,'AND',num2,'IS',check)
    else:
        print(f'THE TWO NUMBERS HAVE NO COMMON FACTORS. SO THE GREATEST COMMON DIVISOR IS 1')
