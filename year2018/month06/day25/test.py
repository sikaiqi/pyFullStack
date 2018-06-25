print("this is my first python program")

#占位符的使用  %s  %d  %f
name = input("Name:")
age = int(input("age:"))
job = input("job:")
salary = input("salary:")

if(salary.isdigit()):
    salary = int(salary)
# else:
#     # print("must input digit")
#     exit("must input digit")

msg = '''
-----info of %s -----
Name:%s
age:%d
job:%s
salary:%f
''' %(name,name,age,job,salary)

print(msg)