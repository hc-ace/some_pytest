from random import randint
x= randint(0,300)
print(x)
for count in range(5):
    dight=int(input('Please input a number:'))
    if dight==x:
        print('yes')
    elif dight>x:
        print("big")
    else:
        print("small")
#range(begin,end,step)
#range(end)
#range(begin,end)
#range 不包括end值