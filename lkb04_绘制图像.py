import pygame.display
import pygame.event
import pygame

pygame.init()

# 1.创建游戏的窗口
screen = pygame.display.set_mode((480, 700))  # 设置窗口大小
pygame.display.set_caption("飞机大战")  # 设置窗口标题

# 1>绘制背景图像
# 首先加载图像数据
bg =  pygame.image.load("./images/background.png")

# blit 绘制图像
screen.blit(bg, (0, 0))

# update负责更新屏幕的显示
pygame.display.update()

# 绘制英雄的飞机
hero = pygame.image.load("./images/me1.png")
screen.blit(hero, (200, 500))
pygame.display.update()

# 2.事件循环
running = True
while running:
    # 获取事件
    for event in pygame.event.get():
        # 检测是否点击了关闭按钮
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
