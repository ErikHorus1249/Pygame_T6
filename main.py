import pygame, sys 

# Khoi tao 
pygame.init()

# chieu dai va chieu rong cua man hinh 
WIDTH, HEIGHT = 400, 712

# Frame per seconds 
clock = pygame.time.Clock()
FPS = 120

# create game's window
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# them anh vao 
bg_image = pygame.image.load("img/background-day.png")

# chinh kich thuoc anh phu hop voi man hinh  
bg_image = pygame.transform.scale(bg_image, (WIDTH, HEIGHT))

# them anh 
base_image = pygame.image.load("img/base.png")

# base_image = pygame.transform.scale2x(base_image)
base_image = pygame.transform.scale(base_image, (HEIGHT,200))

base_x_pos = 0
base_y_pos = 590

def draw_base():
    screen.blit(base_image, (base_x_pos, base_y_pos))
    screen.blit(base_image, (base_x_pos + 590, base_y_pos))


# infinity loop 
while True:
    # dieu kien de exit game 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # hien thi ra bg 
    screen.blit(bg_image, (0,0))
    
    # screen.blit(base_image, (0,590))
    base_x_pos -= 1
    draw_base() # ham hien thi base
    if base_x_pos < -400: # dieu kien khi thanh base di ra ngoai man hinh
        base_x_pos = 0 # reset lai gia tri cua base
    
    # update nhung gi chung ta hien thi         
    pygame.display.update()
    clock.tick(FPS)