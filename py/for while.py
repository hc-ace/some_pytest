'''
a=["a","b","c","d"]
for i in range(2,7):
	print(i)
for i in a:
	print(i)
number= list(range(1,10,2))
for nu in number:
	print("nu:"+str(nu))
'''
#for循环,外部需要冒号,内部语句需要缩进
#range*(begin,end,步长)函数是生成一系列数
n =[value**3 for value in range(1,11)]
print(min(n))
print(max(n))
print(sum(n))
#for i in n:
#	print(i)