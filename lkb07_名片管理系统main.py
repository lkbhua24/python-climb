import lkb07_tools

#无线循环！
while True:

    # TODO(LKBHUA/2711627633@QQ.COM)input返回的是字符串类型，我们用字符串变量进行接受
    lkb07_tools.show_menu()

    action_str = input("请选择希望执行的操作:> ")
    print("你选择的操作数是【%s】"%action_str)

    if action_str  in ["1", "2", "3"]:

        # 新增名片
        if action_str == "1":
            lkb07_tools.new_card()

        # 显示全部
        elif action_str == "2":
            lkb07_tools.show_allcard()

        # 查询名片
        else:
            lkb07_tools.search_card()


    elif action_str == "0":
        print("欢迎再次使用名片给管理系统！")
        break
        # pass是python中的占位符，可以用以不写任何分支内容时不会报错。
        # pass关键字也不会进行任何的操作！
        # pass
    else:
        print("输入错误，请重新输入！")

