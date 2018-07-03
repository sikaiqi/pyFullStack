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


#列表和元组来包含所有产品
product_list = [("iphone6s",5800),("mac book",9000),("coffee",32),("python book",80),("bicyle",1500)]
shopping_car = []

salary = input("please input your salary >>>:")

if salary.isdigit():
    salary = int(salary)

    while True:

        for i,j in enumerate(product_list,1):
            print(i,">>>>>",j)

        choice = input("please input shopping item 【Quit:q】:")

        if choice.isdigit():
            choice = int(choice)
            if 0<choice<=len(product_list):
                p_item = product_list[choice-1]
                p_price = int(p_item[1])

                if(p_price<salary):
                    salary -= p_price
                    shopping_car.append(p_item)
                else:
                    print("余额不足，请充值！余额：%s"%salary)

            else:
                print("shopping item number is not exist!")
        elif choice == "q":
            print("------购物车清单-----")
            for i in shopping_car:
                print(i)
            print("余额：%s",salary)
            print("谢谢惠顾！")
            break
        else:
            print("invalid item number")




