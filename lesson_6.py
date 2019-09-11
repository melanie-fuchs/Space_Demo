#More Python Programming for the Absolute Beginner - Jonathan S. Harbour
#Lesson 6, Challenges 1, 2 and 3
#Solutions by Melanie Fuchs
"""
Using the formula for the circumference of a circle, calculate
the distance travelled by the ship in one complete orbit based
on its radius and display the answer on the screen."""


import pygame, random, math, sys
from pygame.locals import *

#to move the ship, we need the centers of the moon and the ship
class Point(object):
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    #X property
    def getx(self):
        return self.__x
    def setx(self, x):
        self.__x = x
    x = property(getx, setx)
    
    #Y property
    def gety(self):
        return self.__y
    def sety(self, y):
        self.__y = y
    y = property(gety, sety)

    def __str__(self):
        return "{X" + "{:.0f}".format(self.__x) + \
               ", Y:" + "{:.0f}".format(self.__y) + "}"

#print_text function
def print_text(font, x, y, text, color = (255, 255, 255)):
    imgText = font.render(text, True, color)
    screen.blit(imgText, (x, y))

#wrap_angle function
def wrap_angle(angle):
    return angle % 360
    
#main program begins
pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Orbit Demo")
font= pygame.font.Font(None, 18)

#load bitmaps
space = pygame.image.load("space.jpg").convert()
#Converting is needed to convert it into native color depht of the program
#as an opzimization. When not doing that at loading time, it will be
#converted every time it's drawn.convert_alpha is for drawing with transparency

planet = pygame.image.load("mun.png").convert_alpha()

#create the spaceship and scale it down
ship = pygame.image.load("ship.png").convert_alpha()
width, height = ship.get_size()
ship = pygame.transform.smoothscale(ship, (width // 5, height // 5))
ship_instant_rot = wrap_angle(-90)
ship = pygame.transform.rotate(ship, ship_instant_rot)

radius = 180
angle = 0.0
#two instances of the class Point
pos = Point(0,0)
old_pos = Point(0,0)
speed = 0.1
rounds = 0
distance = 0


#repeating loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        sys.exit()

    if keys[K_KP_PLUS]:
        if speed < 0.25:
            speed += 0.0001

    if keys[K_KP_MINUS]:
        if speed > 0.008:
            speed -= 0.0001

    #draw background:
    screen.blit(space, (0, 0))

    #draw the planet centered
    width, height = planet.get_size()
    screen.blit(planet, (300 - width/2, 200 - height/2))
    #draw the spaceship, floating around the planet
    #moving the ship in the orbit around the moon
    angle = wrap_angle(angle - speed)
    pos.x = math.sin(math.radians(angle)) * radius
    pos.y = math.cos(math.radians(angle)) * radius
    if angle < 0.1:
        rounds += 1
        angle = 0
    distance += int(2 * math.pi * radius * rounds)
    #rotate the ship so it points to where its going to
    #The function math.atan2() takes 2 arguments, here the delta in x and y
    delta_x = (pos.x - old_pos.x)
    delta_y = (pos.y - old_pos.y)
    rangle = math.atan2(delta_y, delta_x) #represents the radian angle calculated by atan2
    rangled = wrap_angle(-math.degrees(rangle))
    scratch_ship = pygame.transform.rotate(ship, rangled)
    #draw the ship
    #new ship:
    width, height = scratch_ship.get_size()
    x = 300 + pos.x - width // 2
    y = 200 + pos.y - height // 2
    screen.blit(scratch_ship, (x, y))

    print_text(font, 0, 0, "Orbit: " + "{:.0f}".format(angle))
    print_text(font, 0, 20, "Rotation: " + "{:.2f}".format(rangle))
    print_text(font, 0, 40, "Position: " + str(pos))
    print_text(font, 0, 60, "Old Pos: " + str(old_pos))
    print_text(font, 0, 80, "Distance: " + str(distance))    
    print_text(font, 0, 100, "Rounds: " + str(rounds))  
    print_text(font, 0, 120, "Current speed: " + str(round(speed, 3)))
    
    
        
    
    
    pygame.display.update()

    #remember the old position
    old_pos.x = pos.x
    old_pos.y = pos.y











