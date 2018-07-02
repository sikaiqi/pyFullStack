# 购物车程序
#         salary = 5000
#         1.  iphone6s  5800
#         2.  mac book    9000
#         3.  coffee      32
#         4.  python book    80
#         5.  bicyle         1500
#       >>>:1
#          余额不足，-3000
#       >>>:5
#       已加入bicyle 到你的购物车， 当前余额:3500
#       >>>:quit
#       您已购买一下商品
#       bicyle    1500
#       coffee    30
#       您的余额为:2970
#       欢迎下次光临


salary = 5000

a = ["1=iphone6s:5800","2=mac book:9000","3=coffee:32","4=python book:80","5=bicyle:1500"]
b = [];#记录已经购买的东西


while(1==1):
    c = input(">>>:")

    sign = ""
    name = ""
    price = ""

    for i in a:
        d = i.split("=")
        sign = d[0]

        if(c == sign):
            name = d[1].split(":")[0]
            price = d[1].split(":")[1]
            print(sign +":" +name+":"+price)
            break

    if(c == "quit"):
        print("您已购买以下商品")
        for i in b:
            print(i)
        print("您的余额为："+str(salary))
        print("欢迎下次光临")
        break

    if(name == "" or price == ""):
        print("错误的商品编号。。。")
        exit()

    if(salary - int(price)>=0):
        salary = salary - int(price)
        b.append(name+"\t"+price)
        print("已加入%s到你的购物车， 当前余额:%d"%(name,salary))
    else:
        print("余额不足，"+str(salary - int(price)))




