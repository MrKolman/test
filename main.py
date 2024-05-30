import pygame
import time

pygame.init()
window = pygame.display.set_mode((800, 600))
pickels = pygame.image.load('C:\\Users\\alfred.kallberg\\Desktop\\pygamebilder\\pickels_pygame.png')
fiend = pygame.image.load('C:\\Users\\alfred.kallberg\\Desktop\\pygamebilder\\pickels_pygame.png')
black = (0, 0, 0)
pygame.display.set_caption("The Kålgame")
acceleration = []

class CreatePlayer:
    def __init__(self):
        self.x = 100
        self.y = 325
        self.lives = 3
        self.jumping = False
        self.horizontal = False
        self.speed = 0
        self.a = 0.4
        self.hitbox = pygame.Rect(self.x + 20, self.y, 28, 60)
    
    def update_hitbox(self):
        self.hitbox = pygame.Rect(self.x + 20, self.y, 28, 60)

class CreateEnemy:
    def __init__(self):
        self.x = 800
        self.y = 325
        self.a = 0.8
        self.speed = 5
        self.hitbox = pygame.Rect(self.x + 20, self.y, 28, 60)
    
    def update_hitbox(self):
        self.hitbox = pygame.Rect(self.x + 20, self.y, 28, 60)

def graphics(player, enemy):
    window.fill((211, 211, 211))
    pygame.draw.rect(window, black, pygame.Rect(0, 400, 800, 200))
    window.blit(pickels, (player.x, player.y))
    window.blit(fiend, (enemy.x, enemy.y))

    pygame.display.update()

def game(player, enemy):
    clock = pygame.time.Clock()
    
    while True:
        graphics(player, enemy)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.jumping = True
                    player.speed = 9
                    player.horizontal = True
                    player.x += 30
                    player.update_hitbox()

                if event.key == pygame.K_f:
                    if player.a > 0.2:
                        player.a = 0.2
                    else:
                        player.a = 0.4
        
        if player.jumping:
            player.y -= player.speed
            player.speed -= player.a
        if player.y >= 325:
            player.jumping = False
            player.speed = 0
            player.y = 325
        if player.y == 325 or player.x == 140:
            player.x = 100
        
        player.update_hitbox()

        enemy.x -= 1
        if enemy.x < -40:
            enemy.x = 900
            acceleration.append("1")
        
        enemy.update_hitbox()
        
#Enemy hitbox skit 
        if player.hitbox.colliderect(enemy.hitbox):
            player.lives -= 1
            enemy.x = 800
            print(f"Lives left: {player.lives}")
            if player.lives <= 0:
                pygame.quit()
                return
        
        clock.tick(144)

def main():
    enemy = CreateEnemy()
    player = CreatePlayer()
    game(player, enemy)

main()