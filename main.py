import pygame, sys 

# Khoi tao 
pygame.init()

# chieu dai va chieu rong cua man hinh 
WIDTH, HEIGHT = 400, 712

# Frame per seconds 
clock = pygame.time.Clock()
FPS = 120

# icon load image 
icon = pygame.image.load("img/yellowbird-upflap.png")
pygame.display.set_icon(icon)

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

# bird image loading 
bird_image = pygame.image.load("img/bluebird-midflap.png")
bird_image = pygame.transform.scale2x(bird_image)
bird_rect = bird_image.get_rect(center = (200, 200))
bird_movement = 0


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
    
        # bird control 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_movement = 0
                bird_movement -= 10
    
    # print(f"Toc do cua con chim {bird_movement}")
    # hien thi ra bg 
    screen.blit(bg_image, (0,0))
    
    # screen.blit(base_image, (0,590))
    base_x_pos -= 1
    draw_base() # ham hien thi base
    if base_x_pos < -400: # dieu kien khi thanh base di ra ngoai man hinh
        base_x_pos = 0 # reset lai gia tri cua base
    
    # hien thi con chim 
    # bird_movement = bird_movement + 0.25
    bird_movement += 0.25
    
    # bird_rect.centery = bird_rect.centery + bird_movement
    bird_rect.centery += bird_movement
    
    screen.blit(bird_image, bird_rect)
        
    # update nhung gi chung ta hien thi         
    pygame.display.update()
    clock.tick(FPS)