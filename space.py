from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import random, pygame
from pygame.locals import *
import objLoader, RectPrism, RectPyramid, Draw, Keys, Camera, ObjectList
import Plane, Quaternion, Player

#school:
#screenWidth, screenHeight = 1580., 800.
#macBookAir:
screenWidth, screenHeight = 1366., 768.
#macBookPro:
#screenWidth, screenHeight = 1280., 752.
SCREEN_SIZE = (int(screenWidth), int(screenHeight))
pygame.init()
pygame.display.set_icon(pygame.image.load(os.path.join(os.getcwd(), "resources/SpaceIcon.jpg")))
window = pygame.display.set_mode(SCREEN_SIZE, HWSURFACE | OPENGL | DOUBLEBUF)
glViewport(0, 0, int(screenWidth), int(screenHeight))
glMatrixMode(GL_PROJECTION)
gluPerspective(60., float(screenWidth) / screenHeight, .1, 1000.)
glMatrixMode(GL_MODELVIEW)

glShadeModel(GL_FLAT)

glEnable(GL_DEPTH_TEST)
glEnable(GL_COLOR_MATERIAL)
viewDivisor = 1000
msPF = float(30)

draw = Draw.Draw()

keys = Keys.Keys()

objects = ObjectList.ObjectList()

objects.add_object(Player.Player(keys, draw, Quaternion.Vector(0, 5, 0), "Spaceship.obj", Quaternion.Quaternion(.01, 0, 0, -1), Quaternion.Quaternion(.01, 0, 1, 0), "ship"))
objects.add_object(Plane.Plane(keys, draw, Quaternion.Vector(0, 0, 0), "triangle.obj", Quaternion.Quaternion(.01, 0, 0, -1), Quaternion.Quaternion(.01, 0, 1, 0), "floor"))
objects.add_object(Plane.Plane(keys, draw, Quaternion.Vector(0, 0, 0), "triangle_2.obj", Quaternion.Quaternion(.01, 0, 0, -1), Quaternion.Quaternion(.01, 0, 1, 0), "floor"))

camera = Camera.Camera(screenWidth, screenHeight, viewDivisor, objects, msPF)

glClearColor(0., 0., 0., 0.)
clock = pygame.time.Clock()
timePassed = 0

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        elif keys.get_keys()[K_SPACE]:
            exit()
    clock.tick(30)
    camera.timer()
    pygame.display.set_caption("Space!")
    
    keys.get_pressed_keys()
    camera.display()
