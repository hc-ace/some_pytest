'''
#for循环if条件
for j in range(2,101):
    k=int(sqrt(j))
    flag=1
    for i in range(2,k+1):
        if(j%i==0):
            flag=0
            break
    if(flag):
        print(j)
'''
#自定义函数
def add1(x):
    'add'
    return(x+x)
#察看自定义函数文档
print(add1.__doc__)
#自定义函数
def isprime(x):
    if x==1:
        return 0
    k=int(sqrt(x))
    for i in range(2,k+1):
        if(j%i==0):
            return 0
    return 1
#传递函数
def sel(f,y):
    print(f(y))
#匿名函数 lambda 
for j in range(2,101):
    if(isprime(j)):
        print(j,end=' ')
#汉诺塔
def hanoi(a,b,c,n):
    if(n==1):
        print(a,'->',c)
    else:
        hanoi(a,c,b,n-1)
        print(a,'->',c)
        hanoi(b,a,c,n-1)
