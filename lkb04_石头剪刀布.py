# 导入工具包
# 注意：在导入工具包的时候，切记需要放到文件开头！
import random


# 1.从控制台输入想要出的拳————石头（1）、剪刀（2）、布（3）
player = int (input("请输入你出的拳石头（1）、剪刀（2）、布（3）:>"))



# 2.电脑 随机出拳—
computer = random.randint(1,3)

print("玩家选择的拳头是:> %d"%player)
print("电脑选择的拳头是:> %d"%computer)

# 3.比较胜负
# 玩家获胜
if (player == 1 and computer == 2) or (player == 2 and computer == 3 ) or (player == 3 and computer == 1):
    print("恭喜你获胜！")

# 平局
elif (player == 1 and computer ==1) or (player == 2 and computer == 2) or (player == 3 and computer == 3) :
    print("平局！")

# 电脑获胜


else :
    print("电脑获胜！")