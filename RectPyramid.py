from OpenGL.GL import *

import Draw, Object

class RectPyramid(Object.SpaceObject):
    def draw(self):
        glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, self.color)
        glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, self.color)
        glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, self.color)
        self.drawer.draw_rect_pyramid(self.Ps, self.Ds)