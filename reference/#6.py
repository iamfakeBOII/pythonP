'''
import re
sample = 'MY*NAME*IS*PETER*AND*I*AM*26*YEARS*OLD'

print(re.split('\*', sample))
'''

#DEFINING FUNCTIONS
roll_num = int(input('PLEASE ENTER YOUR ROLL NUMBER: '))

def nominal_roll():
    if roll_num <= 15:
        print('GROUP1')
    elif roll_num <= 23:
        print('GROUP 2')
    else:
        print('GROUP 3')

    nominal_roll()
