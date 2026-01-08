"""
乔治·修拉风格点彩画《大碗岛的星期日下午》简化局部
Georges Seurat-style pointillist painting - Simplified section of "A Sunday Afternoon on the Island of La Grande Jatte"

使用turtle.dot()方法绘制点彩画，遵循点彩派色彩并置原理
Uses turtle.dot() method to create pointillist artwork, following pointillist color juxtaposition principles
"""

import turtle
import random


def setup_canvas():
    """初始化画布设置 / Initialize canvas settings"""
    turtle.speed(0)  # 最快速度 / Fastest speed
    turtle.tracer(0)  # 关闭绘图动画 / Disable animation
    turtle.hideturtle()  # 隐藏海龟 / Hide turtle cursor
    screen = turtle.Screen()
    screen.bgcolor("white")  # 白色背景 / White background
    screen.setup(width=800, height=600)  # 设置画布大小 / Set canvas size
    return screen


def draw_sky():
    """绘制天空 - 浅蓝色和白色点 / Draw sky - light blue and white dots"""
    # 天空区域：画布上半部分 / Sky area: upper half of canvas
    dot_size = 3
    spacing = 1
    step = dot_size + spacing
    
    # 从上往下绘制天空 / Draw sky from top to bottom
    for y in range(300, 100, -step):
        for x in range(-400, 400, step):
            # 随机选择天空颜色，越往上白色越多（高光效果）
            # Randomly select sky color, more white towards top (highlight effect)
            if y > 250:
                color = random.choice(["white", "white", "#E0F6FF", "#B0E0E6"])
            elif y > 200:
                color = random.choice(["white", "#B0E0E6", "#87CEEB", "#ADD8E6"])
            else:
                color = random.choice(["#87CEEB", "#ADD8E6", "#B0E0E6", "white"])
            
            turtle.penup()
            turtle.goto(x, y)
            turtle.dot(dot_size, color)


def draw_grass():
    """绘制草地 - 草绿、黄绿、土黄色点 / Draw grass - green, yellow-green, and tan dots"""
    # 草地区域：画布中下部分 / Grass area: middle-lower part of canvas
    dot_size = 3
    spacing = 1
    step = dot_size + spacing
    
    # 绘制草地 / Draw grass
    for y in range(100, -100, -step):
        for x in range(-400, 400, step):
            # 近景草地使用更多黄绿色，远景使用更多绿色
            # Foreground uses more yellow-green, background uses more green
            if y < -50:
                # 前景 - 更亮的颜色 / Foreground - brighter colors
                color = random.choice(["#9ACD32", "#90EE90", "#BDB76B", "#228B22"])
            elif y < 0:
                # 中景 / Middle ground
                color = random.choice(["#32CD32", "#228B22", "#90EE90", "#9ACD32"])
            else:
                # 远景 - 较暗的颜色 / Background - darker colors
                color = random.choice(["#228B22", "#2E8B57", "#32CD32"])
            
            # 添加随机的土黄色点作为阴影 / Add random tan dots for shadows
            if random.random() < 0.15:
                color = random.choice(["#BDB76B", "#DAA520", "#8B7355"])
            
            turtle.penup()
            turtle.goto(x, y)
            turtle.dot(dot_size, color)


def draw_riverbank():
    """绘制河岸边缘 - 棕色和黑色点 / Draw riverbank edge - brown and black dots"""
    # 河岸区域：画布底部 / Riverbank area: bottom of canvas
    dot_size = 3
    spacing = 1
    step = dot_size + spacing
    
    # 绘制河岸 / Draw riverbank
    for y in range(-100, -200, -step):
        for x in range(-400, 400, step):
            # 底部使用更多黑色（阴影） / More black at bottom (shadows)
            if y < -150:
                color = random.choice(["black", "#2F1F10", "#654321", "#5C4033"])
            else:
                color = random.choice(["#8B4513", "#654321", "#A0522D", "#5C4033"])
            
            turtle.penup()
            turtle.goto(x, y)
            turtle.dot(dot_size, color)


def draw_figures():
    """绘制简化人物剪影 - 红、蓝、白色点 / Draw simplified figure silhouettes - red, blue, white dots"""
    dot_size = 3
    spacing = 1
    step = dot_size + spacing
    
    # 人物1：左侧，蓝色服饰 / Figure 1: left side, blue clothing
    figure1_x = -150
    figure1_y_base = -20
    
    # 绘制人物1的头部 / Draw figure 1's head
    for y in range(figure1_y_base + 40, figure1_y_base + 60, step):
        for x in range(figure1_x - 8, figure1_x + 8, step):
            if (x - figure1_x) ** 2 + (y - (figure1_y_base + 50)) ** 2 < 100:
                color = random.choice(["#FFE4C4", "#F5DEB3", "#DEB887"])
                turtle.penup()
                turtle.goto(x, y)
                turtle.dot(dot_size, color)
    
    # 绘制人物1的身体（蓝色） / Draw figure 1's body (blue)
    for y in range(figure1_y_base, figure1_y_base + 40, step):
        for x in range(figure1_x - 15, figure1_x + 15, step):
            if abs(x - figure1_x) < 12:
                color = random.choice(["#000080", "#0000CD", "#4169E1", "#1E90FF"])
                # 添加白色高光 / Add white highlights
                if random.random() < 0.2:
                    color = random.choice(["white", "#E6F2FF"])
                turtle.penup()
                turtle.goto(x, y)
                turtle.dot(dot_size, color)
    
    # 人物2：右侧，红色服饰 / Figure 2: right side, red clothing
    figure2_x = 100
    figure2_y_base = -30
    
    # 绘制人物2的头部 / Draw figure 2's head
    for y in range(figure2_y_base + 35, figure2_y_base + 55, step):
        for x in range(figure2_x - 8, figure2_x + 8, step):
            if (x - figure2_x) ** 2 + (y - (figure2_y_base + 45)) ** 2 < 90:
                color = random.choice(["#FFE4C4", "#F5DEB3", "#DEB887"])
                turtle.penup()
                turtle.goto(x, y)
                turtle.dot(dot_size, color)
    
    # 绘制人物2的身体（红色） / Draw figure 2's body (red)
    for y in range(figure2_y_base, figure2_y_base + 35, step):
        for x in range(figure2_x - 12, figure2_x + 12, step):
            if abs(x - figure2_x) < 10:
                color = random.choice(["#8B0000", "#DC143C", "#CD5C5C", "#B22222"])
                # 添加白色高光 / Add white highlights
                if random.random() < 0.15:
                    color = random.choice(["white", "#FFE6E6"])
                # 添加深色阴影 / Add dark shadows
                if random.random() < 0.2 and x < figure2_x - 5:
                    color = random.choice(["#800000", "#4B0000"])
                turtle.penup()
                turtle.goto(x, y)
                turtle.dot(dot_size, color)


def main():
    """主函数 / Main function"""
    # 初始化画布 / Initialize canvas
    screen = setup_canvas()
    
    print("开始绘制点彩画... / Starting to draw pointillist painting...")
    print("绘制天空... / Drawing sky...")
    draw_sky()
    
    print("绘制草地... / Drawing grass...")
    draw_grass()
    
    print("绘制河岸... / Drawing riverbank...")
    draw_riverbank()
    
    print("绘制人物... / Drawing figures...")
    draw_figures()
    
    # 更新画面 / Update screen
    turtle.update()
    print("绘制完成！/ Drawing complete!")
    
    # 保持窗口打开 / Keep window open
    turtle.done()


if __name__ == "__main__":
    try:
        main()
    except turtle.Terminator:
        pass
    except Exception as e:
        if "invalid command name" in str(e):
            pass
        else:
            raise
