import design
import pygame as pg
import random
import math

pg.init()

clock = pg.time.Clock()
# Fenêtre
window = pg.display.set_mode((1420,840))
pg.display.set_caption("Pong")

run = True

J1 = design.Raquette(250, 50, 15, (50,400), (255,0,0))
J2 = design.Raquette(250, 50, 15, (1320,400), (255,0,0))
ball = design.Balle(25, 15, random.randrange(-50,50)*math.pi/180, (720,420), (0,255,0))

cpt = 0
# Boucle infinie du jeu
while run:
    clock.tick(40)

# Quitter proprement
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

# Gestion des raquettes
    keys = pg.key.get_pressed() #Liste de booléen donnnant l'état de toutes les touches du clavier,
    # Index fait en indiquant la touche du clavier
    if keys[pg.K_z] and (J1.y - J1.velocity) > 0:
        J1.y -= J1.velocity
    if keys[pg.K_s] and (J1.y + J1.height + J1.velocity) < 840:
        J1.y += J1.velocity
    if keys[pg.K_o] and (J2.y - J2.velocity) > 0:
        J2.y -= J2.velocity
    if keys[pg.K_l] and (J2.y + J2.height + J2.velocity) < 840:
        J2.y += J2.velocity

# Gestion de la balle
    # Rebond sur les bords de la fenêtre
    if (ball.y - ball.radius + ball.vel_y) < 0 or (ball.y + ball.radius + ball.vel_y) > 840:
        ball.vel_y *= -1
    # Rebond sur les raquettes avec distribution d'angles (ca marche po)
    # if design.verif_contact(J1, ball) and (ball.x - ball.radius + ball.vel_x) <= (J1.x + J1.width):
    #     nouvel_angle = design.distribution_reflexion(J1, ball, 55)
    #     print(nouvel_angle, 'J1')
    #     ball.vel_x = ball.norm*math.cos(nouvel_angle)
    #     ball.vel_y = ball.norm*math.sin(nouvel_angle)
    #
    # if design.verif_contact(J2, ball) and (ball.x + ball.radius + ball.vel_x) >= J2.x:
    #     nouvel_angle = design.distribution_reflexion(J2, ball, 55)
    #     print(nouvel_angle, 'J2')
    #     ball.vel_x = -ball.norm * math.cos(nouvel_angle)
    #     ball.vel_y = ball.norm * math.sin(nouvel_angle)

    # Rebond sur les raquettes avec une réflexion physique
    if design.verif_contact(J1, ball) and (ball.x - ball.radius + ball.vel_x) <= (J1.x + J1.width):
        ball.vel_x = -ball.vel_x

    if design.verif_contact(J2, ball) and (ball.x + ball.radius + ball.vel_x) >= J2.x:
        ball.vel_x = -ball.vel_x

# Gestion des scores
    if ball.x + ball.vel_x < 0:
        pass
    if ball.x + ball.vel_x > 1420:
        pass

    ball.x += ball.vel_x
    ball.y += ball.vel_y

    design.update_window(window, J1, J2, ball)
    cpt += 1

pg.quit()
