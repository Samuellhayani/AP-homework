# v1 : pareil mais au moins on peut sortir du programme
# avec la touche 'q', ou avec la souris en fermant la fenêtre
import numpy as np
from random import randint
import pygame as pg

pg.init()
screen = pg.display.set_mode((300, 300))
clock = pg.time.Clock()

def case_pix(x, y):
    return y*20, x*20

def draw_snake(snake):
    # snake est la liste des tuples de position du serpent
    for pix in snake:
     case = case_pix(*pix)
     rectangle = pg.Rect(*case, 20, 20)
     pg.draw.rect(screen, (0, 255, 0), rectangle)

def fruit(a,b):
    case = case_pix(a,b)
    rectangle = pg.Rect(*case, 20, 20)
    pg.draw.rect(screen, (255, 0, 0), rectangle)

snake = [(1, 1), (1, 2), (1, 3)]
direction = (0, 1)

a, b = np.random.randint(0, 15, 2)
while (a, b) in snake:
    a, b = np.random.randint(0, 15, 2)


running = True
while running:

    for x in range(0,30):
        for y in range(0,30):
            case = case_pix(x, y)
            rectangle = pg.Rect(*case, 20, 20)
            color = [ ( (x+y)%2 ) * 255 ] * 3
            pg.draw.rect(screen, color, rectangle)
    fruit(a, b)
    draw_snake(snake)
    pg.display.update()
    

    clock.tick(5)
    
        

    # on itère sur tous les évênements qui ont eu lieu depuis le précédent appel
    # ici donc tous les évènements survenus durant la seconde précédente
    for event in pg.event.get():
        # chaque évênement à un type qui décrit la nature de l'évênement
        # un type de pg.QUIT signifie que l'on a cliqué sur la "croix" de la fenêtre
        
        if event.type == pg.QUIT:
            running = False
        # un type de pg.KEYDOWN signifie que l'on a appuyé une touche du clavier
        
        elif event.type == pg.KEYDOWN:
        
            if event.key == pg.K_q:
                running = False
            if event.key == pg.K_UP:
                direction = (-1,0)
            if event.key == pg.K_DOWN:
                direction=(1,0)
            if event.key == pg.K_LEFT:
                direction=(0,-1)
            if event.key == pg.K_RIGHT:
                direction=(0,1)

    
    tete = (snake[-1][0]+direction[0], snake[-1][1]+direction[1])
    snake.append(tete)

    if snake[-1][0] < 0 or snake[-1][0] == 15:
        running = False
        print('GAME OVER')
    if snake[-1][1] < 0 or snake[-1][1] == 15:
        running = False
        print('GAME OVER')
    
    if snake[-1] != (a,b):
        del snake[0]
    
    else:
        while (a,b) in snake:
            a,b = np.random.randint(0, 15, 2)
        fruit(a, b)

    if snake[-1] in snake[:-1]:
        running = False
        print('GAME OVER')


        
# Enfin on rajoute un appel à pg.quit()
# Cet appel va permettre à Pygame de "bien s'éteindre" et éviter des bugs sous Windows
pg.quit()