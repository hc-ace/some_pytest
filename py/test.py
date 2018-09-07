#28
def age(n):
    if(n==1):
        c=10
    else:
        c=age(n-1)+2
    return c
print(age(5)) 
#http://www.runoob.com/python/python-100-examples.html
#一百道练习题