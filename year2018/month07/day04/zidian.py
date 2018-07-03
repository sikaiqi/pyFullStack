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
a = [1,2]
print(a)
a = list([1,2])
print(a)
a = list((1,2))
print(a)

b = {"name":"alex","age":23}
print(b)
b = dict((("name","alex"),("age",23)))
print(b)
b = dict([["name","alex"],["age",23]])
print(b)