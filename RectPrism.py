from OpenGL.GL import *#from OpenGL.GLUT import *

import Draw, Object

class RectPrism(Object.SpaceObject):#GetRect!
    def draw(self):#draws by setting colors then drawing *gasp*
        if not self.id == "eye":
            glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, self.color)
            glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, self.color)
            glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, self.color)
            self.drawer.draw_rect_prism(self.Ps, self.Ds)