# Tạo màn hình game 
import pygame

# tuple
MAN_HINH = (960, 540)

# kich thuoc cua tau bay  
TAU_BAY = (100, 120)
# man_hinh_x = 960
# man_hinh_y = 540

# khởi tạo game 
pygame.init() 

# icon
icon = pygame.image.load("./assets/icon.png")
pygame.display.set_icon(icon)

# Caption 
pygame.display.set_caption("Space game")

# Tạo màn hình cho game 
man_hinh = pygame.display.set_mode(MAN_HINH)

# Tao tau cho nguoi choi 
tau_bay = pygame.image.load("./assets/spaceship.png")
tau_bay = pygame.transform.scale(tau_bay, TAU_BAY)

# Thien thach 
thien_thach = pygame.image.load("./assets/asteroid.png")
thien_thach = pygame.transform.scale(thien_thach, (50,50))

# tọa độ ban đầu của tàu 
bandau_x = MAN_HINH[0]/2 - TAU_BAY[0]/2
bandau_y = MAN_HINH[1]/2 - TAU_BAY[1]/2 
thaydoi_x = 0
thaydoi_y = 0

# background : anh nen 
anh_nen = pygame.transform.scale(pygame.image.load("./assets/bg.png"), MAN_HINH)\
# man_hinh.fill((0,0,0))

def ve_anh_nen():
    man_hinh.blit(anh_nen, (0,0))
    
def ve_tau_bay(x: tuple):
    man_hinh.blit(tau_bay, x)
    
def ve_thien_thach():
    man_hinh.blit(thien_thach, (300, 300))

while True:
    # quit game 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                thaydoi_x += 10
            if event.key == pygame.K_a:
                thaydoi_x -= 10 # neu nhan -> -5, -10, -15
            if event.key == pygame.K_w:
                thaydoi_y -= 10
            if event.key == pygame.K_s:
                thaydoi_y += 10
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_d or event.key == pygame.K_s or event.key == pygame.K_a:
                thaydoi_x, thaydoi_y = (0,0)
          
    ve_anh_nen()
    bandau_x += thaydoi_x
    bandau_y += thaydoi_y
    ve_tau_bay((bandau_x, bandau_y))
    ve_thien_thach()
    
    pygame.display.update()