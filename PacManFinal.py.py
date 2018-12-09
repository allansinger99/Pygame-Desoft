# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 15:58:48 2018

@author: allansinger99
"""
from random import randint
import pygame, sys
from pygame.locals import *
from random import randrange
from os import path

width = 600
height = 800



################################ Classes ########################################

def draw_lives(surf, x, y, lives, img):
    for i in range(lives):
        img_rect = img.get_rect()
        img_rect.x = x + 30 * i
        img_rect.y = y
        surf.blit(img, img_rect)

class Pacman(pygame.sprite.Sprite):
    def __init__(self, arquivo_imagem, pos_x, pos_y, vel_x, vel_y):
        pygame.sprite.Sprite.__init__(self)
        self.vx = vel_x
        self.vy = vel_y
        self.image = pygame.image.load(arquivo_imagem)
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.lives = 3
        
        
    def move(self, vx, vy):
        self.rect.x += vx
        self.rect.y += vy
        
 
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                if vx > 0: # Moving right; Hit the left side of the wall
                    self.rect.right = wall.rect.left
                if vx < 0: # Moving left; Hit the right side of the wall
                    self.rect.left = wall.rect.right
                if vy > 0: # Moving down; Hit the top side of the wall
                    self.rect.bottom = wall.rect.top
                if vy < 0: # Moving up; Hit the bottom side of the wall
                    self.rect.top = wall.rect.bottom

       




class Ghost(pygame.sprite.Sprite):
    def __init__(self, arquivo_imagem, pos_x, pos_y, vel_x, vel_y):
        pygame.sprite.Sprite.__init__(self)
        self.vx = vel_x
        self.vy = vel_y
        self.image = pygame.image.load(arquivo_imagem)
        self.image = pygame.transform.scale(self.image,(30,30))
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
    
    
    def update(self):
        self.rect.x += self.vx
        self.rect.y += self.vy
        
        A = randint(0,4)
        
        
        for wall in walls:
            if self.rect.colliderect(wall.rect):
               
                    
                if self.vx > 0: # Moving right; Hit the left side of the wall
                    self.rect.right = wall.rect.left
                if self.vx < 0: # Moving left; Hit the right side of the wall
                    self.rect.left = wall.rect.right
                if self.vy > 0: # Moving down; Hit the top side of the wall
                    self.rect.bottom = wall.rect.top
                if self.vy < 0: # Moving up; Hit the bottom side of the wall
                    self.rect.top = wall.rect.bottom
            
                A
                if A==0:
                    self.vx = 0
                    self.vy = 7
                elif A == 1:
                    self.vx = 0
                    self.vy = -7
                elif A == 2:
                    self.vx = 7
                    self.vy = 0
                else:
                    self.vx = -7
                    self.vy = 0

       
class Wall(object):
    def __init__(self, pos):
       walls.append(self)
       self.rect = pygame.Rect(pos[0], pos[1], 25, 25)
      



#class Dots(object):
#    def __init__(self, pos):
       # coins.append(self)
        
        
    
############################# inicializacao #########################################################################


pygame.init()
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Pacman")
clock = pygame.time.Clock()
walls = []
#coins = []


white = (255,255,255)
black = (0,0,0)

fonte_nome = pygame.font.match_font('arial')

def texto_tela(surf, text, size, x, y):
    fonte = pygame.font.Font(fonte_nome, size)
    text_surface = fonte.render(text, True, white)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)



def initial_screen():
    screen.fill(black)
    texto_tela(screen, "PACMAN", 64, width / 2, height / 4)
    texto_tela(screen, "Use the arrow keys to move", 22, width / 2, height / 2)
    texto_tela(screen, "Press any key to begin", 19, width / 2, height * 3 / 4)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(60) 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                waiting = False

                
                
#############################Sprite da parede####################################################################################
                
level = [
"                                     ",
"                                     ",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
"W                 W                 W",
"W                 W                 W",
"W                 W                 W",
"W   WWWWW   WWW                     W",
"W   W   W   W W           W         W",
"W   W   W   W W        WWWWWWW      W",
"W   W   W   W W           W         W",
"W   W   W   W W           W         W",
"W   W   W   W W           W         W",
"W   W   W   W W                     W",
"W   WWWWW   WWW                     W",
"W                                   W",
"W                                   W",
"W                                   W",
"W   WWWWWWWWWWW                     W",
"W   W         W                     W",
"W   W         W                     W",
"W   W         W                     W",
"W   W         W                     W",
"W   WWWWWWWWWWW                     W",
"W                                   W",
"W                                   W",
"W                W   W              W",
"WWWWW            W   W    WWWW   WWWW",
"W    WWW         W   W    W         W",
"W      W         WWWWW    W         W",
"W      W                  WWWWW     W",
"W      W                  W         W",
"W                         W         W",
"W        WWWWWW    WWWWWWWW         W",
"W        W                          W",
"W        W                          W",
"W        W                          W",
"W        W          WWWWWW          W",
"W        W               W          W",
"W        W               W          W",
"W        W               W          W",
"W    WWWWW          WWWWWW          W",
"W                                   W",
"W                                   W",
"W                             WWW   W",
"W    WWWWWW        WWW      W       W",
"W         W          W      W       W",
"W         WWWWWW     WWWWWWWW       W",
"W         WWWWWW     WWWWWWWW       W",
"W                                   W",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW"
]



x = y = 0
for row in level:
    for col in row:
        if col == "W":
            Wall((x, y))
 #       elif col =="C":
  #          Dots((x,y))
        x += 16
    y += 16
    x = 0




#bloco = pygame.draw(screen, white, 4, width = 0)                
                
                


#Sprite Pacman####
    
pac = Pacman("pacmancerto.png", 300, 400, 1, 1)
#pac2 = Pacman("pacmanspriteaberto.png",pos_x, pos_y, vel_x, vel_y)
#pac3 = Pacman("pacmanspritefechado.png",pos_x, pos_y, vel_x, vel_y)
pac_Group = pygame.sprite.Group()
pac.image = pygame.transform.scale(pac.image, (30, 30))
pac.rect = pac.image.get_rect()
pac.rect.x = 300
pac.rect.y = 400
pac_Group.add(pac)

#player_mini_img = pygame.transform.scale(pac, (25, 19))
#player_mini_img.set_colorkey(black)
#Sprite Fantasmas####

ghost1 = Ghost("ghost1.png", 300, 400, 1, 1)
ghost2 = Ghost("ghost2.png", 200, 100, 1, 1)
ghost3 = Ghost("ghost3.png", 50, 300, 1, 1)
ghost4 = Ghost("ghost4.png", 70, 100, 1, 1)
ghost_Group = pygame.sprite.Group()
#ghost1.image = pygame.transform.scale(ghost1.image, (30, 30))
#ghost2.image = pygame.transform.scale(ghost2.image, (30, 30))
#ghost3.image = pygame.transform.scale(ghost3.image, (30, 30))
#ghost4.image = pygame.transform.scale(ghost4.image, (30, 30))
ghost_Group.add(ghost1, ghost2, ghost3, ghost4)



##################Game Loop###################################

vel_x = 0
vel_y = 0

lol = True
running = True
while running:
    if lol:     
        initial_screen()
        lol = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False
            pygame.display.quit()
            pygame.quit()        
            sys.exit()   
            

    
    
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                vel_x = -5
                vel_y = 0
            if event.key == pygame.K_RIGHT:
                vel_x = 5
                vel_y = 0
            if event.key == pygame.K_UP:
                vel_y = -5
                vel_x = 0
            if event.key == pygame.K_DOWN:
                vel_y = 5
                vel_x = 0
                
  
    for wall in walls:
        pygame.draw.rect(screen, (0,0,255), wall.rect) 
   # for coin in coins:
    #    pygame.draw.circle(screen, white, 7, width=0)             
    pac_Group.draw(screen)
    pac.move(vel_x, vel_y)
    ghost_Group.draw(screen)
    texto_tela(screen, "HighScore", 18, width/2, 10)
    draw_lives(screen, width - 100, 5, 3, pac.image)
    for ghost in ghost_Group:
        ghost.update()
    pygame.display.update()
    screen.fill((black))
    
pygame.display.quit()
pygame.quit()        