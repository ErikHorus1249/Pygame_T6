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

# infinity loop 
while True:
    # dieu kien de exit game 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # hien thi ra bg 
    screen.blit(bg_image, (0,0))
    
    # update nhung gi chung ta hien thi         
    pygame.display.update()
    clock.tick(FPS)