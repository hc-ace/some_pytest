def prime(num):
    if(num<=1):
        return 0
    elif num==2:
        return 1        
    k=sqrt(num)
    for i in range(3,int(k+1),2):
        if num%i==0:
            return 0
    return 1
    
def findm(No):
    n=0
    num=2
    while n<No:
        m = pow(2,num)-1
        if prime(num) == 1 and prime(m) ==1:
            n+=1
        num+=1
    return int(m),num-1

for i in range(1,7):
    print(findm(i))