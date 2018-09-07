'''
列表
查询时：索引指定为-1，返回列表最后一个元素
添加：append（）,向列表末尾加一个元素
	  insert(),插入元素
删除: del a[0],需要知道位置，删除后不再使用
	  pop  删除列表最后一个元素
	  remove 删除特定值
排序：sort正序
	  加一个参数 reverse=True 倒序
	  sorted 临时排序
倒置: reverse()
长度：len()
'''
a=[2,3,5]
print(a[-1])
a.append(3)
print(a[-1])
a.insert(0,100)
print(a[0])
message=a.pop()
print("当前最后： "+ str(a[-1]) )
print("删除： "+str(message))
a.remove(5)
print(a[-1])