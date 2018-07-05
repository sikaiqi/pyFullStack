#字典
    # 特点：无序，键唯一


# 数据类型
#     整形
#     布尔
#     字符串
#     列表
#     元组
#     字典
#
# 其中整形、字符串、元组 是不可变类型，可以拿来作为字典的键

# 定义字典，键是不可变类型
# dic = {"name":"alex","age":43,"height":170}
# print(dic)
# print(dic["age"])

# 定义字典，键是可变类型报错 TypeError: unhashable type: 'list'
# dic = {"name":"alex","age":43,"height":170,["1","2"]:"aa"}
# print(dic)
# print(dic["age"])

# 列表和字典通过函数创建
# a = [1,2]
# print(a)
# a = list([1,2])
# print(a)
# a = list((1,2))
# print(a)
#
# b = {"name":"alex","age":23}
# print(b)
# b = dict((("name","alex"),("age",23)))
# print(b)
# b = dict([["name","alex"],["age",23]])
# print(b)

# 增
# dic1 = {"name":"alex"}
# dic1["age"] = 18 #直接元素赋值来添加
# print(dic1)
# ret = dic1.setdefault("hobby","girl")  #通过内置方法来添加元素，当key 不存在，添加后则返回新的value
# print(ret)
# print(dic1)
# ret = dic1.setdefault("age",24) #age在字典中存在，则原有的value不会被替换，返回原有的value
# print(ret)
# print(dic1)

# 删
# dic2 = {"name":"alex","age":22,"hobby":"girl","height":180}
# del dic2["name"] #删除name的键值对
# print(dic2)
# print(dic2.pop("age")) #删除键为age的键值对，返回value值
# print(dic2)
# print(dic2.popitem()) #随机删除键值对，并返回被删除的键值对
# print(dic2)
# dic2.clear() #清空字典
# print(dic2)


# 改
# dic3 = {"name":"alex","age":22}
# dic3["age"] = 33 #直接修改
# print(dic3)
#
# dic_tmp = {"11":"22","33":"44","name":"lilei"}
# dic3.update(dic_tmp) #dic3 增加dic_tmp中的元素，如果key重合，dic3中key的value会被替换
# print(dic3)
# print(dic_tmp)



# 查
# dic4 = {"name":"alex","age":22,"hobby":"girl","height":180}
# print(dic4["name"]) #查某个键的值
# print(dic4.keys()) #查所有的键，但返回的是一个类:<class 'dict_keys'>
# print(type(dic4.keys())) #<class 'dict_keys'>
# print(list(dic4.keys())) #<class 'dict_keys'> 可用list()方法转换为列表
# print(list(dic4.values())) #获取所有的values 列表
# print(list(dic4.items())) #获取所有的键值对列表


#其他方式创建字典
# dic5 = dict.fromkeys(["host1","host2"],"test")
# print(dic5) #{'host1': 'test', 'host2': 'test'}

# dic5 = dict.fromkeys(["host1","host2","host3"],["test1","test2"])
# print(dic5) #{'host1': ['test1', 'test2'], 'host2': ['test1', 'test2'], 'host3': ['test1', 'test2']}
# dic5["host1"][1] ="test3"
# print(dic5) #{'host1': ['test1', 'test3'], 'host2': ['test1', 'test3'], 'host3': ['test1', 'test3']}

#字典排序(列表可以有自有方法.sort()方法排序，而字典没有，只能用sorted())
# dic = {5:"222",3:"666",4:"555"}
# print(sorted(dic)) #默认按key排序
# print(sorted(dic.values())) #按value排序
# print(sorted(dic.items())) #默认按key排序

#字典的遍历
# dic = {"name":"alex","age":22,"hobby":"girl","height":180}
# for i in dic:
#     print(i) # 默认i为key
#     print(i,dic[i])  # key 和 value  效率高

# for i,j in dic.items():
#     print(i,j) #key 和 value  字典数据量大时，效率低
