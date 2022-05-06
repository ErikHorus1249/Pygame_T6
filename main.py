import random
import pygame, sys 

# Khoi tao 
pygame.init()

game_active = True

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

base_image = pygame.transform.scale2x(base_image)
# base_image = pygame.transform.scale(base_image, (HEIGHT,1200))

# base position 
base_x_pos = 0
base_y_pos = 590

# create base rect 
# bird image loading 
bird_image = pygame.image.load("img/bluebird-midflap.png")
# bird_image = pygame.transform.scale2x(bird_image)
bird_image = pygame.transform.scale(bird_image,(52, 45))
bird_rect = bird_image.get_rect(center = (200, 200))
bird_movement = 0


Appearence = pygame.USEREVENT
pygame.time.set_timer(Appearence, 1400)

#---------------------Pipe---------------------------------------------------#
pipe_image = pygame.image.load("img/pipe-green.png")
# pipe list 
pipes = []

# Tao cột (1 cột trên - 1 cột dưới)
def create_newpipe():
    # pipe_height = [300, 330, 360, 390]
    pipe_height = [300, 400, 320, 330]
    # tao ra chieu cao ngau nhien cho ong nuoc
    random_height = random.choice(pipe_height)
    pipe_bottom = pipe_image.get_rect(midtop = (WIDTH, random_height)) 
    pipe_top = pipe_image.get_rect(midbottom = (WIDTH, random_height - 150))
    return pipe_bottom, pipe_top

# dùng để dịch chuyển cột 
def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= 1
    return pipes

# vẽ ra cột 
def draw_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom > HEIGHT/2:
            screen.blit(pipe_image, pipe)
        else:
            pipe_flip = pygame.transform.flip(pipe_image, False, True)
            screen.blit(pipe_flip, pipe)
            
def check_collison(pipes):
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            return False
        return True
            
def check_position():
    if bird_rect.centery > 0 and bird_rect.centery < HEIGHT - 147:
        print("avaiable position!")
    else:
        print("The bird is dead!")
        pygame.quit()
        sys.exit()

def draw_base():
    screen.blit(base_image, (base_x_pos, base_y_pos))
    screen.blit(base_image, (base_x_pos + 590, base_y_pos))

def draw_eve(img: str, posx, posy):
    screen.blit(img, (posx, posy))

# infinity loop 
while True:
    # dieu kien de exit game 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # exit game -> gameover !
            sys.exit() # sys - system -> sys.exit()
    
        # bird control 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_movement = 0
                bird_movement -= 4
                
        if event.type == Appearence:
            pipes.extend(create_newpipe())
            
    # hien thi ra bg 
    screen.blit(bg_image, (0,0))
    
      # Pipe 
    pipes = move_pipes(pipes)
    draw_pipes(pipes)
    
    # Base 
    base_x_pos -= 1
    if base_x_pos < -400: # dieu kien khi thanh base di ra ngoai man hinh
        base_x_pos = 0 # reset lai gia tri cua base
        
    # bird_movement = bird_movement + 0.25
    bird_movement += 0.25
    
    # bird_rect.centery = bird_rect.centery + bird_movement
    bird_rect.centery += bird_movement
    
    screen.blit(bird_image, bird_rect)
    
    draw_base() # ham hien thi base
    
    # if game_active:
    #     game_active = check_collison(pipes)
    #     print(game_active)
    print(check_collison(pipes=pipes))
    
    # update nhung gi chung ta hien thi         
    pygame.display.update()
    clock.tick(FPS)