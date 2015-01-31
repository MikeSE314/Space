from OpenGL.GL import *
import pygame, objLoader
from pygame.locals import *
from Quaternion import *

class SpaceObject(object):
    def __init__(self, keys, drawer, positions, file, rotQuat = Quaternion(0, 0, 0, 0), oRotQuat = Quaternion(0, 0, 0, 0), id = "none"):
        self.keys = keys
        self.kp = self.keys.get_keys()
        self.drawer = drawer
        self.Ps = Vector(positions.x, positions.y, positions.z)
        self.q = rotQuat
        self.qo = oRotQuat
        self.id = id
        self.Vs = Vector(0, 0, 0)
        self.As = Vector(0, 0, 0)
        self.dampner = 1.0
        self.ztb = False
        self.zOn = False
        self.power = 10.5
        self.makeSomethingAwesome(objLoader.OBJ(file))

    def draw(self):
        self.drawer.draw_obj((self.q.w, self.q.x, self.q.y, self.q.z), self.Ps, self.obj.gl_list)

    def makeSomethingAwesome(self, obj):
        self.obj = obj

    def update(self):
        self.kp = self.keys.get_keys()
        self.Vs = self.Vs.add(self.As.div(30.)).mult(self.dampner)
        self.Ps = self.Ps.add(self.Vs.div(30.))
        self.As, self.dampner = Vector(0, 0, 0), 1.0

if __name__ == "__main__":
    print(dir(pygame.locals))
