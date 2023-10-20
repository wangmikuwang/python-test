# 导入pygame模块
import pygame

# 定义一些常量
SCREEN_WIDTH = 800  # 屏幕宽度
SCREEN_HEIGHT = 600  # 屏幕高度
CELL_SIZE = 10  # 细胞大小
DEAD_COLOR = (0, 0, 0)  # 死亡颜色
ALIVE_COLOR = (255, 255, 255)  # 存活颜色

# 初始化pygame
pygame.init()
# 创建一个窗口
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# 设置窗口标题
pygame.display.set_caption('Life Game')
# 设置时钟
clock = pygame.time.Clock()


# 定义一个函数，根据细胞状态返回对应颜色
def get_color(state):
    if state == 0:
        return DEAD_COLOR
    else:
        return ALIVE_COLOR


# 定义一个函数，根据当前细胞状态和邻居数量返回下一代细胞状态
def get_next_state(current_state, neighbor_count):
    if current_state == 0 and neighbor_count == 3:
        return 1  # 死亡细胞周围有正好三个存活邻居，复活
    elif current_state == 1 and (neighbor_count < 2 or neighbor_count > 3):
        return 0  # 存活细胞周围有少于两个或超过三个存活邻居，死亡
    else:
        return current_state  # 其他情况，状态不变


# 定义一个函数，根据当前网格返回下一代网格
def get_next_grid(current_grid):
    # 获取网格的行数和列数
    rows = len(current_grid)
    cols = len(current_grid[0])
    # 创建一个新的空网格
    next_grid = [[0 for col in range(cols)] for row in range(rows)]
    # 遍历每个细胞
    for row in range(rows):
        for col in range(cols):
            # 获取当前细胞的状态
            current_state = current_grid[row][col]
            # 计算当前细胞周围的存活邻居数量
            neighbor_count = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if i == 0 and j == 0:
                        continue  # 跳过自己
                    neighbor_row = (row + i) % rows  # 邻居行号（取模防止越界）
                    neighbor_col = (col + j) % cols  # 邻居列号（取模防止越界）
                    neighbor_state = current_grid[neighbor_row][neighbor_col]  # 邻居状态
                    neighbor_count += neighbor_state  # 累加邻居状态
            # 获取下一代细胞的状态
            next_state = get_next_state(current_state, neighbor_count)
            # 将下一代细胞的状态赋值给新网格
            next_grid[row][col] = next_state
    # 返回新网格
    return next_grid


# 定义一个函数，绘制网格
def draw_grid(grid):
    # 获取网格的行数和列数
    rows = len(grid)
    cols = len(grid[0])
    # 遍历每个细胞
    for row in range(rows):
        for col in range(cols):
            # 获取细胞的状态
            state = grid[row][col]
            # 获取细胞的颜色
            color = get_color(state)
            # 获取细胞的矩形区域
            rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            # 填充细胞的颜色
            screen.fill(color, rect)


# 创建一个随机的初始网格
import random

grid = [[random.randint(0, 1) for col in range(SCREEN_WIDTH // CELL_SIZE)] for row in range(SCREEN_HEIGHT // CELL_SIZE)]

# 主循环
running = True
while running:
    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  # 点击关闭按钮，退出循环
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                grid = [[random.randint(0, 1) for col in range(SCREEN_WIDTH // CELL_SIZE)] for row in
                        range(SCREEN_HEIGHT // CELL_SIZE)]  # 按空格键，重新生成随机网格

    # 更新网格
    grid = get_next_grid(grid)

    # 绘制网格
    draw_grid(grid)

    # 更新屏幕
    pygame.display.flip()

    # 设置帧率
    clock.tick(10)

# 退出pygame
pygame.quit()
