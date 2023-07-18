for i in range(100):
    if i< 10:
        print("0{},".format(i), end=' ')
    elif i != 89:
        if i%10 > i//10:
            print("{},".format(i), end = ' ')
        else: 
            continue
    else:
        print("{}".format(i), end='\n')
