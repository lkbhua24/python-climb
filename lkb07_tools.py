# 记录所有的名片字典
card_list = []


def show_menu():
    """
    显示菜单 
    """
    print("*"*50)
    print("欢迎使用【名片管理系统】V1.0")
    print("")
    print("1.新增名片")
    print("2.显示全部")
    print("3.搜索名片")
    print("0.退出系统")

    print("*"*50)

def new_card():
    """新增名片函数"""
    print("-"*50)
    print("新增名片")
    # 1.提示用户输入名片的详细信息
    name_str = input("请输入名字:>")
    phone_str = input("请输入电话:>")
    qqnumber_str = input("请输入qq号码:>")
    email_str = input("请输入你的邮箱地址:>")

    # 2.使用用户输入的信息建立一个名片字典
    card_dict={"name":name_str,
               "phone":phone_str,
               "qqnumber":qqnumber_str,
               "email":email_str
               }


    # 3.将名片字典添加到列表中，提示用户输入成功
    card_list.append(card_dict)

    print(card_list)

    print("添加%s成功！"%name_str)



def show_allcard():
    """显示全部函数"""
    print("-"*50)
    print("显示全部")


    # 判断是否有名片记录，没有就提示用户进行输入且返回
    if len(card_list) == 0:
        print("请输入名片记录，使用新增功能！")

        # 可以返回一个函数的执行结果，同时不会执行下方的代码！
        # 如果return 后没有加任何内容
        # 表示：会返回到调用函数的位置
        return

    # 1.打印表头
    for name in ["姓名","电话","QQ","邮箱"]:
        print(name,end="\t\t\t\t")
    print("")


    # 2.打印分割线
    print("-"*50)


    # 3.遍历名片列表依次输出字典信息
    for card_dict in card_list:
        print("%s\t\t\t\t%s\t\t\t\t%s\t\t\t\t%s\t\t\t\t"%(card_dict["name"],
                                                          card_dict["phone"],
                                                          card_dict["qqnumber"],
                                                          card_dict["email"]))
    print("")
    print("-"*50)

def search_card():
    """搜索名片"""
    print("-"*50)
    print("搜索名片")

    # 1.提示用户输入要搜索的姓名
    find_name = input("请输入要搜索的姓名:>")

    # 2.遍历名片列表，查询要搜索的姓名，如果没有找到，需要提示用户
    for card_dict in card_list:

        if card_dict["name"] == find_name:
            print("找到了！")
            print("姓名\t\t\t\t电话\t\t\t\tQQ\t\t\t\t邮箱\t\t\t\t")
            print("-"*50)
            print("%s\t\t\t\t%s\t\t\t\t%s\t\t\t\t%s\t\t\t\t" % (card_dict["name"],
                                                                card_dict["phone"],
                                                                card_dict["qqnumber"],
                                                                card_dict["email"]))
            # TODO 针对找到的名片记录进行修改和删除的操作
            deal_card(card_dict)

            break
    else:
        print("抱歉没有找到%s！"%find_name)



def deal_card(find_dict):
    """ """
    print(find_dict)

    action_str = input("请选择要执行的操作:> "
                       "【1】.修改名片 【2】.删除名片 【0】.返回上级菜单")

    if action_str == "1":
        print("修改名片:>")
        find_dict["name"] = input_card_info(find_dict["name"],"请修改姓名:>")
        find_dict["phone"] = input_card_info(find_dict["phone"],"请修改号码:>")
        find_dict["qqnumber"] = input_card_info(find_dict["qq"],"请修改qq号码:>")
        find_dict["email"] = input_card_info(find_dict["email"],"请修改邮箱:>")

        print("已经成功修改名片！")

    elif action_str == "2":
        print("删除名片:>")
        card_list.remove(find_dict)
        print("已经成功删除%s"%find_dict)
    else:
        print("<UNK>")



def input_card_info(dict_value,tip_message):
    """输入名片信息

    :param dict_value:字典中原有的值
    :param tip_message:输入的提示文字
    :return:如果用户输入了内容，直接返回结果，否则就返回原有的字典！
    """
    """
    1. 提示用户输入内容
    2. 针对用户的输入进行判断
    3. 输入了内容直接返回结果
    4. 没有输入内容，返回字典原有的内容
    """
    result_str = input(tip_message)

    if len(result_str) > 0:
        return result_str

    else:
        return dict_value
