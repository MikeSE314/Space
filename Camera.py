from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from pygame.locals import *

import random, pygame, math, Quaternion

class Camera:
    def __init__(self, screenWidth, screenHeight, viewDivisor, objects, millisecondsPerFrame):
        self.objects = objects
        self.ref = self.objects.list[0]
        self.Eyes = Quaternion.Vector(0, 100, 0)
        self.Centers = Quaternion.Vector(0, 1, 0)
        self.Ups = Quaternion.Vector(0, 0, 1)
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        self.viewDivisor = viewDivisor
        self.objects = objects
        self.msPF = millisecondsPerFrame
    def refresh2d(self, width, height):
        list = self.objects.list[0].kp
        self.Eyes = self.objects.list[0].Ps.add(Quaternion.Vector(0, 5, 12))
        self.Center = self.Eyes.add(self.objects.list[0].q.vecPart().mult(-1))
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glMatrixMode(GL_PROJECTION)
        glPushMatrix()
        gluPerspective(50, self.screenWidth / self.screenHeight, 1, 500)
        glPopMatrix()
        glMatrixMode(GL_MODELVIEW)
        gluLookAt(self.Eyes.x, self.Eyes.y, self.Eyes.z, self.Centers.x, self.Centers.y, self.Centers.z, self.Ups.x, self.Ups.y, self.Ups.z)
        glScalef(1.0, 1.0, 1.0)
    def reshape(self, width, height):
        glViewport(0, 0, int(self.screenWidth), int(self.screenHeight))
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glFrustum(width / -self.viewDivisor, width / self.viewDivisor + 1, height / -self.viewDivisor, height / self.viewDivisor + 1, 4, 500)
        glMatrixMode(GL_MODELVIEW)
    def display(self):
        glPushMatrix()
        self.refresh2d(self.screenWidth, self.screenHeight)
        for object in self.objects.list:
            object.draw()
        glPopMatrix()
        pygame.display.flip()
    def timer(self):
        for object in self.objects.list:
            object.update()