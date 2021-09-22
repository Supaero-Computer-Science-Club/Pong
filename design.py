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
        self.vel_x = self.norm*math.cos(alpha)
        self.vel_y = self.norm*math.sin(alpha)
        self.x = ini_pos[0]
        self.y = ini_pos[1]
        self.color = color

    def draw(self,window):
        pg.draw.circle(window, self.color, (self.x,self.y) ,self.radius)



def update_window(window, P1, P2, ball):
    """ Ecran noir puis on redessine dessus"""
    window.fill((0,0,0))
    P1.draw(window)
    P2.draw(window)
    ball.draw(window)
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


