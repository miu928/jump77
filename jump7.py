for x in range(1,101):
    if x%7==0: 
        continue
    elif (x-7)%10==0:
        continue
    elif x//10==7:
        continue
    print(x)
