"""
import pygame

pygame.init()

# 1.创建游戏的窗口
screen = pygame.display.set_caption("<UNK>")


pygame.quit()

"""
import pygame.display
import pygame.event
import pygame

pygame.init()

# 1.创建游戏的窗口
screen = pygame.display.set_mode((480, 700))  # 设置窗口大小
pygame.display.set_caption("飞机大战")  # 设置窗口标题


# 2.事件循环
running = True
while running:
    # 获取事件
    for event in pygame.event.get():
        # 检测是否点击了关闭按钮
        if event.type == pygame.QUIT:
            running = False

pygame.quit()