import random
number = random.randint(-10000, 10000)
x = str(number)
if number >=0 and x[-1] > '5':
    print("last digit of {} is {} and is greater than 5".format(number, x[-1]), end='\n')
elif number >= 0 and x[-1] < '6' and x[-1] != '0':
    print("last digit of {} is {} and is less than 6 and not 0".format(number, x[-1]), end='\n')
elif number >= 0 and x[-1] == '0':
    print("last digit of {} is {} and is 0".format(number, x[-1]), end='\n')
elif number < 0 and x[-1] != '0':
    print("last digit of {} is -{} and is less than 6 and not 0".format(number, x[-1]), end='\n')
else:
    print("last digit of {} is {} and is 0".format(number, x[-1]), end='\n')