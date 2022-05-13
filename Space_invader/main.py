# Tạo màn hình game 
import pygame

# tuple
MAN_HINH = (960, 540)

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
tau_bay = pygame.image.load("./assets/ship.png")
tau_bay = pygame.transform.scale(tau_bay, (50,50))

# Thien thach 
thien_thach = pygame.image.load("./assets/asteroid.png")
thien_thach = pygame.transform.scale(thien_thach, (50,50))

# background : anh nen 
anh_nen = pygame.transform.scale(pygame.image.load("./assets/bg.png"), MAN_HINH)\
# man_hinh.fill((0,0,0))

def ve_anh_nen():
    man_hinh.blit(anh_nen, (0,0))
    
def ve_tau_bay():
    man_hinh.blit(tau_bay, (300,400))
    
def ve_thien_thach():
    man_hinh.blit(thien_thach, (300, 300))

while True:
    # quit game 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            
    ve_anh_nen()
    ve_tau_bay()
    ve_thien_thach()
    
    pygame.display.update()