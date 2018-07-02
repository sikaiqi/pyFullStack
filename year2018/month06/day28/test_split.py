#切片

a = ["11","22","33","44","55","66"]

print(a[1:]) #取到最后
print(a[1:-1]) #取到倒数第二值
print(a[1::2]) #从左往右一个隔一个取
print(a[3::-1])#从右往左取
print(a[-2::-2])#从右往左一个隔一个取

#切片后的列表是新的列表

# append insert
a.append("77")
print(a)
a.insert(1,"88")
print(a)

#修改
a[1] ="99"
print(a)
a[2:4]=["aa","bb","cc"]
print(a)

#删除 remove pop  del
a.remove(a[0])
print(a)
val = a.pop(0)
print(val)
print(a)
del(a[0])
print(a)
# del(a)
# print(a)

## count计数
b = ["to", "be","or", "not", "to", "be"]
print(b.count("be"))

# extend 方法
c = [1,2,3]
d = [4,5,6]
c.extend(d)
print(c)
print(d)