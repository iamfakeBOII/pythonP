#PROGRAM TO FIND INDEX VALUE

'''

l = eval(input('ENTER NUMBERS: '))

e = float(input('ENTER THE ELEMENT: '))



if e in l:

    print(f'{e} has {l.index(e)} index vlaue')

else:

    print('not found')

'''



#LARGEST/SMALLEST VALUE IN A LIST/TUPLE

'''

l = eval(input('ENTER ELEMENTS: '))

print(f'THE LARGEST VALUE IS {max(l)} AND {min(l)}')

'''



#SWAP ELEMENTS IN A LIST/TUPLE

'''

l = eval(input('ENTER ELEMENTS: '))

final = []



for a in l:

    if l.index(a)%2==0:

        temp = a

    else:

        final.append(a)

        final.append(temp)



print(final)

'''



#SEARCH ELEMENT FOR A SPECIFIC ELEMENT IN A LIST/TUPLE

'''

l = eval(input('ENTER ELEMENTS: '))

e = float(input('ENTER THE ELEMENT TO BE FOUND: '))



if e in l:

    print(f'THE ELEMENT {e} IS A PART OF THE SEQUENCE WITH INDEX VALUE {l.index(e)}')

else:

    print('NOT FOUND')

'''



#SEARCH FOR A ARMSTRONG NUMBER FROM A LIST/TUPLE AND PRINT THE LARGEST AND SMALLEST NUMBER

'''

l = eval(input('ENTER ELEMENTS: '))

nums = []                             #TO STORE FINAL ARMSTRONG NUMBERS



for a in l:  #TO CHECK ARMSTRONG NUMBER       

    check = a

    s = 0



    while a>0:           #TO CALCULATE THE ARMSTRONG NUMBER

        d = a%10

        s = s + (d**3)

        a = a//10



    if s == check:

        nums.append(check)

    else:

        continue



print(f'THE ARMSTRONG NUMBERS ARE {nums}')

print(f'THE LARGEST ARMSTRONG NUMBER IS {max(nums)} AND THE SMALLEST ARMSTRONG NUMBER IS {min(nums)}')

'''
