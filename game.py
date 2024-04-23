import pygame
import os
from os import walk

WIDTH = 1000
HEIGHT = 600
pygame.init()

window = pygame.display.set_mode((WIDTH, HEIGHT))

menu_font = pygame.font.SysFont('Ariel', 40, True, False)

INACTIVE = (123, 23, 97)
ACTIVE = (140, 167, 222)

menu_active = False

start_surf = menu_font.render("START GAME!", True, INACTIVE)
start_rect = start_surf.get_rect(center=(120, 100))


def import_files(path):
    surface_list = []

    for i in walk(path):
        for j in i[2]:
            full_path = path + "/" + j
            img = pygame.image.load(full_path).convert_alpha()
            img = pygame.transform.rotozoom(img, 0, 0.3)
            surface_list.append(img)
    print(surface_list)
    return surface_list


player_idl_path = r"C:\Users\Lenovo\Desktop\Python\Halloween_game\images\player\idl"
player_walk_path = r"C:\Users\Lenovo\Desktop\Python\Halloween_game\images\player\walk"

player_anim = {
    'idl': import_files(player_idl_path),
    'walk': import_files(player_walk_path)
}

player_idx = 0
player_x = WIDTH / 2
player_y = HEIGHT - 150
player_speed = 5
player_forward = True

menu_surf_1 = pygame.image.load("images/fire/FlameParticle1_I.jpg").convert_alpha()
menu_surf_2 = pygame.image.load("images/fire/FlameParticle2_I.jpg").convert_alpha()
menu_surf_3 = pygame.image.load("images/fire/FlameParticle3_I.jpg").convert_alpha()
menu_surf_4 = pygame.image.load("images/fire/FlameParticle4_I.jpg").convert_alpha()

menu_surfs = [menu_surf_1, menu_surf_2, menu_surf_3, menu_surf_4]
menu_index = 0

clock = pygame.time.Clock()

game = True
menu = True

while game:
    if menu:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                game = False

            if event.type == pygame.MOUSEMOTION:
                mouse = event.pos
                if start_rect.collidepoint(mouse):
                    start_surf = menu_font.render("START GAME!", True, ACTIVE)
                    start_rect = start_surf.get_rect(center=(120, 100))
                    menu_active = True
                else:
                    start_surf = menu_font.render("START GAME!", True, INACTIVE)
                    start_rect = start_surf.get_rect(center=(120, 100))
                    menu_active = False

            if event.type == pygame.MOUSEBUTTONDOWN and menu_active:
                print("click")
                menu = False

        menu_index += 0.1
        if menu_index > len(menu_surfs)-1:
            menu_index = 0

        menu_surf = menu_surfs[int(menu_index)]
        menu_rect = menu_surf.get_rect(center=(WIDTH / 2, HEIGHT / 2))

        window.blit(start_surf, start_rect)
        window.blit(menu_surf, menu_rect)

        clock.tick(60)
        pygame.display.update()

    else:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                game = False
        player_status = 'idl'
        window.fill((0, 0, 0))

        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT] and player_x <= WIDTH - 60:
            player_forward = True
            player_status = "walk"
            player_x += player_speed
            print(player_x)

        if keys[pygame.K_LEFT] and player_x >= WIDTH - 930:
            player_forward = False
            player_status = "walk"
            player_x -= player_speed
            print(player_x)

        player_surf = player_anim[player_status][int(player_idx)]

        if player_forward:
            player_rect = player_surf.get_rect(center=(player_x, player_y))
        else:
            player_surf = pygame.transform.flip(player_surf, True, False)
            player_rect = player_surf.get_rect(center=(player_x, player_y))

        if player_idx >= 9:
            player_idx = 0

        player_idx += 0.2

        window.blit(player_surf, player_rect)
        clock.tick(60)
        pygame.display.update()

pygame.quit()


