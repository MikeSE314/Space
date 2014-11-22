from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import random, pygame
from pygame.locals import *
import objLoader, RectPrism, RectPyramid, Draw, Keys, Camera, ObjectList
import Plane, Quaternion, Player

#school:
#screenWidth, screenHeight = 1580., 800.
#macAir:
#screenWidth, screenHeight = 1366., 710.
#macPro:
screenWidth, screenHeight = 1280., 752.
SCREEN_SIZE = (int(screenWidth), int(screenHeight))
pygame.init()
window = pygame.display.set_mode(SCREEN_SIZE, HWSURFACE|OPENGL|DOUBLEBUF)
glViewport(0, 0, int(screenWidth), int(screenHeight))
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
gluPerspective(60., float(screenWidth) / screenHeight, .1, 1000.)
glMatrixMode(GL_MODELVIEW)
glLoadIdentity()


glShadeModel(GL_FLAT)
glClearColor(.2, .3, .8, 0.)
glClearDepth(1)

glEnable(GL_DEPTH_TEST)
glEnable(GL_COLOR_MATERIAL)
#glEnable(GL_LIGHTING)
#glEnable(GL_LIGHT0)
viewDivisor = 1000
msPF = float(30)
#glutInit()
#glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
#glutInitWindowSize(int(screenWidth), int(screenHeight))
#glutInitWindowPosition(0, 0)
#window = glutCreateWindow("Spaaace!")

dampner = .9

mat_red = [1., 0., 0., 1.]#In r, g, b, a
mat_red_02 = [.1, .1, .1, 1.]
mat_green = [0., 1., 0., 1.]
mat_blue = [.5, 0., 1., 1.]
mat_cyan = [0., 1., 1., 1.]
mat_magenta = [1., 0., 1., 1.]
mat_yellow = [1., 1., 0., 1.]
mat_black = [0., 0., 0., 1.]
mat_white = [1., 1., 1., 1.]

light_ambient = [.1, .1, .1, 1.]
light_diffuse = [.4, .4, .4, 1.]
light_specular = [.5, .5, .5, 1.]
light_position = [-100, 10., -70., 1.]
whiteSpecularLight = [1.0, 1.0, 1.0]
blackAmbientLight = [0.0, 0.0, 0.0]
whiteDiffuseLight = [1.0, 1.0, 1.0]
blankMaterial = [.04, 0.04, 0.04]
'''
glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient)
glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse)
glLightfv(GL_LIGHT0, GL_SPECULAR, light_specular)
glLightfv(GL_LIGHT0, GL_POSITION, light_position)
'''
draw = Draw.Draw()

#input = Input.Input()
keys = Keys.Keys()

objects = ObjectList.ObjectList()

objects.add_object(Player.Player(keys, draw, [0., 5., 0.],
                                       "SpaceShip.obj",
                                       Quaternion.Quaternion(.01, 0, 0, -1),
                                       Quaternion.Quaternion(.01, 0, 1, 0),
                                       "ship"))
objects.add_object(Plane.Plane(draw, Quaternion.Vector(0, 0, 0), "triangle.obj", "floor"))
objects.add_object(Plane.Plane(draw, Quaternion.Vector(0, 0, 0), "triangle_2.obj", "floor"))

camera = Camera.Camera(screenWidth, screenHeight, viewDivisor, objects, msPF)

window = 0
glClearColor(0., 0., 0., 0.)
#glutReshapeFunc(camera.reshape)
clock = pygame.time.Clock()
timePassed = 0
temp = keys.get_keys()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        elif keys.get_keys()[K_SPACE]:
            exit()
    clock.tick(30)
    camera.timer()
    pygame.display.set_caption("fps: " + str(clock.get_fps()))
    
    keys.get_pressed_keys()
    '''
    glLightfv(GL_LIGHT0, GL_SPECULAR, whiteSpecularLight)
    glLightfv(GL_LIGHT0, GL_AMBIENT, blackAmbientLight)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, whiteDiffuseLight)
    '''
    camera.display()

#glutMainLoop()