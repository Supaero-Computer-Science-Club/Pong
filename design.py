import pygame as pg
import math

pg.init()

class Raquette(object):
    def __init__(self, height, width, velocity,ini_pos, color):
        self.height = height
        self.width = width
        self.velocity = velocity   #je sais pas si j'en aurais vraiment besoin, je sais même pas ce que c'est
        self.x = ini_pos[0]
        self.y = ini_pos[1]
        self.color = color

    def draw(self, window):
        pg.draw.rect(window,self.color,(self.x,self.y,self.width,self.height))



class Balle(object):
    def __init__(self, radius, initial_velocity,alpha, ini_pos,color): # Initial_velocity est la norme
        self.radius = radius
        self.norm = initial_velocity
        self.angle = alpha
        self.vel_x = self.norm*math.cos(alpha)
        self.vel_y = self.norm*math.sin(alpha)
        self.x = ini_pos[0]
        self.y = ini_pos[1]
        self.color = color

    def draw(self,window):
        pg.draw.circle(window, self.color, (self.x,self.y) ,self.radius)



def update_window(window, P1, P2, ball, scoreJ1, scoreJ2):
    """ Ecran noir puis on redessine dessus"""
    window.fill((0,0,0))
    P1.draw(window)
    P2.draw(window)
    ball.draw(window)
    afficher_message(window, 'Score:  {}:{}'.format(scoreJ1, scoreJ2), 40, (255, 255, 255), (650, 30))
    pg.display.update()

def verif_contact(raquette, ball):
    """:return: bool"""
    if (raquette.y <= ball.y <= raquette.y + raquette.height):
        return True
    return False

def distribution_reflexion(raquette, ball, angle_max):
    ymax = raquette.height/2
    y = ball.y - raquette.y - ymax
    return angle_max*(y/ymax)**3

def afficher_message(window, message,taille, couleur,coordonnee):
    """:param: coordonne est le tuple de coordonnée du message à afficher"""
    font = pg.font.SysFont('Lato', taille)
    msg = font.render(message, True, couleur)
    window.blit(msg,coordonnee)

def debut_manche(window,P1,P2,ball,scoreJ1,scoreJ2,initial_velocity):
    window.fill((0,0,0))
    pg.display.update()
    pg.time.delay(500)
    P1.y = 400
    P2.y = 400
    ball.x, ball.y = (720,420)
    ball.norm = initial_velocity
    ball.vel_x = ball.norm*math.cos(ball.angle)
    ball.vel_y = ball.norm * math.sin(ball.angle)
    update_window(window, P1, P2, ball, scoreJ1, scoreJ2)
