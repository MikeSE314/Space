from OpenGL.GL import *
from pygame.locals import *
from Quaternion import *

import Object, objLoader

class Player(Object.SpaceObject):
    def update(self):
        super(Player, self).update()
        if not self.ztb and self.kp[K_z]:
            if self.zOn:
                self.zOn = False
            else:
                self.zOn = True
        if self.kp[K_z]:
            self.ztb = True
        else:
            self.ztb = False
        if self.kp[K_q]:# the appropriate operation
            self.As = self.As.add(Vector(0, 0, self.power))
        if self.kp[K_w]:
            self.As = self.As.add(Vector(0, self.power, 0))
        if self.kp[K_e]:
            self.As = self.As.subtract(Vector(0, 0, self.power))
        if self.kp[K_a]:
            self.As = self.As.add(Vector(self.power, 0, 0))
        if self.kp[K_s]:
            self.As = self.As.subtract(Vector(0, self.power, 0))
        if self.kp[K_d]:
            self.As = self.As.subtract(Vector(self.power, 0, 0))
        if self.kp[K_x]:
            self.Vs = self.Vs.mult(0)
        if self.zOn:
            self.dampner *= .9
        if self.kp[K_KP8] or self.kp[K_UP]:
            self.q = self.q.multByQuat(Quaternion(math.pi / 32., -1, 0, 0))
        if self.kp[K_KP4] or self.kp[K_LEFT]:
            self.q = self.q.multByQuat(Quaternion(math.pi / 32., 0, 0, -1))
        if self.kp[K_KP6] or self.kp[K_RIGHT]:
            self.q = self.q.multByQuat(Quaternion(math.pi / 32., 0, 0, 1))
        if self.kp[K_KP2] or self.kp[K_KP5] or self.kp[K_DOWN]:
            self.q = self.q.multByQuat(Quaternion(math.pi / 32., 1, 0, 0))