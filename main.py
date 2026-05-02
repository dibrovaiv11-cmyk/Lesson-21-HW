import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800, 600))
font = pygame.font.Font(None, 50)
bg_color = pygame.Color(0, 0, 130)
land_y = 450
land_rect = pygame.Rect(0, land_y, 800, 600)
land_color = pygame.Color(0, 130, 0)
clock = pygame.time.Clock()

mushrooms = []
for _ in range(10):
    mush_x = random.randint(0, 800 - 20)
    mushrooms.append(pygame.Rect(mush_x, land_y - 10, 20, 20))
mushroom_color = (130, 0, 0)

leafs = []
for _ in range(10):
    leaf_x = random.randint(0, 800 - 15)
    leafs.append(pygame.Rect(leaf_x, land_y - 10, 15, 15))
leaf_color = pygame.Color(0, 100, 0)

player = pygame.Rect(100, land_y - 130, 70, 150)
player_color = (128, 128, 128)
inventory = {
    "mushrooms": 0,
    "leafs": 0
}

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                for mush in mushrooms[:]:
                    if mush.colliderect(player):
                        mushrooms.remove(mush)
                        if inventory.get('mushrooms') is not None:
                            inventory['mushrooms'] += 1
                        else:
                            inventory['mushrooms'] = 1
                        print("Picked up a mushroom! Total:", inventory['mushrooms'])
                for leaf in leafs[:]:
                    if leaf.colliderect(player):
                        leafs.remove(leaf)
                        if inventory.get('leafs') is not None:
                            inventory['leafs'] += 1
                        else:
                            inventory['leafs'] = 1
                        print("Picked up a leaf! Total:", inventory['leafs'])

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= 5
    if keys[pygame.K_RIGHT]:
        player.x += 5

    screen.fill(bg_color)
    pygame.draw.rect(screen, land_color, land_rect)
    for mushroom in mushrooms:
        pygame.draw.rect(screen, mushroom_color, mushroom)
    for leaf in leafs:
        pygame.draw.rect(screen, leaf_color, leaf)

    pygame.draw.rect(screen, player_color, player)
    text = font.render(f"Mushroom count: {inventory['mushrooms']}", True, (255, 255, 255))
    text1 = font.render(f"Leaf count: {inventory['leafs']}", True, (255, 255 ,255))
    screen.blit(text, (300, 500))
    screen.blit(text1, (300, 550))
    pygame.display.flip()
    clock.tick(60)