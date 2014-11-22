from OpenGL.GL import *
import math

class Draw:
    def __init__(self):
        pass
    def normal(self, p1, p2, p3):
        U = (p2[0] - p1[0], p2[1] - p1[1], p2[2] - p1[2])
        V = (p3[0] - p1[0], p3[1] - p1[1], p3[2] - p1[2])
        return (U[1] * V[2] - U[2] * V[1], U[2] * V[0] - U[0] * V[2],
                U[0] * V[1] - U[1] * V[0])
    def draw_rect(self, x, y, z, width, height):
        glBegin(GL_POINTS)
        glVertex3f(x, y, z)
        glVertex3f(x + width, y, z)
        glVertex3f(x + width, y + height, z)
        glVertex3f(x, y + height, z)
        glEnd()
    def draw_triangle(self, p1, p2, p3):
        glBegin(GL_TRIANGLES)
        n = self.normal(p1, p2, p3)
        glNormal(n[0], n[1], n[2])
        glVertex3f(p1[0], p1[1], p1[2])
        glVertex3f(p2[0], p2[1], p2[2])
        glVertex3f(p3[0], p3[1], p3[2])
        glEnd()
    def draw_rect(self, x, y, z, width, height):
        glBegin(GL_POINTS)
        glVertex3f(x, y, z)
        glVertex3f(x + width, y, z)
        glVertex3f(x + width, y + height, z)
        glVertex3f(x, y + height, z)
        glEnd()
    def draw_rect_prism(self, Ps, Ds):
        p1 = (Ps.x - Ds.x / 2, Ps.y - Ds.y / 2, Ps.z - Ds.z / 2)#l b b
        p2 = (Ps.x - Ds.x / 2, Ps.y + Ds.y / 2, Ps.z - Ds.z / 2)#l t b
        p3 = (Ps.x - Ds.x / 2, Ps.y + Ds.y / 2, Ps.z + Ds.z / 2)#l t f
        p4 = (Ps.x - Ds.x / 2, Ps.y - Ds.y / 2, Ps.z + Ds.z / 2)#l b f
        p5 = (Ps.x + Ds.x / 2, Ps.y - Ds.y / 2, Ps.z - Ds.z / 2)#r b b
        p6 = (Ps.x + Ds.x / 2, Ps.y + Ds.y / 2, Ps.z - Ds.z / 2)#r t b
        p7 = (Ps.x + Ds.x / 2, Ps.y + Ds.y / 2, Ps.z + Ds.z / 2)#r t f
        p8 = (Ps.x + Ds.x / 2, Ps.y - Ds.y / 2, Ps.z + Ds.z / 2)#r b f
        """
            Calculates the eight
            vertices of a
            rectangular prism
                 2_______6
                /|      /|
               /       / |
              /  |    /  |
             /  (1)_ /  _5
            3___/___7   /
            |       |  /
            |       | /
            |/      |/
            4_______8
            
            The sides are
            in code
            as follows:
            """
        self.draw_triangle(p1, p2, p6)#back;
        self.draw_triangle(p6, p5, p1)
        self.draw_triangle(p2, p3, p7)#top;
        self.draw_triangle(p7, p6, p2)
        self.draw_triangle(p3, p4, p8)#front;
        self.draw_triangle(p8, p7, p3)
        self.draw_triangle(p4, p1, p5)#bottom;
        self.draw_triangle(p5, p8, p4)
        self.draw_triangle(p1, p4, p3)#left;
        self.draw_triangle(p3, p2, p1)
        self.draw_triangle(p5, p6, p7)#right;
        self.draw_triangle(p7, p8, p5)
    def draw_rect_pyramid(self, Ps, Ds):
        p1 = (Ps.x - Ds.x / 2, Ps.y - Ds.y / 2, Ps.z - Ds.z / 2)#l b b
        p2 = (Ps.x, Ps.y + Ds.y / 2, Ps.z)#top middle
        p3 = (Ps.x - Ds.x / 2, Ps.y - Ds.y / 2, Ps.z + Ds.z / 2)#l b f
        p4 = (Ps.x + Ds.x / 2, Ps.y - Ds.y / 2, Ps.z + Ds.z / 2)#r b f
        p5 = (Ps.x + Ds.x / 2, Ps.y - Ds.y / 2, Ps.z - Ds.z / 2)#r b b
        '''
                 
                 
                 
                                             2
                                           ....
                                          ......
                                        .. .. ...
                                       .. ..   ...
                                     ..  ..    ....
                                    ..  ..      ....
                                  ..   ..       .. ..
                                 ..   ..         .. ..
                               ..    ..          ..  ..
                              ..    ..            ..  ..
                            ..     ..             ..   ..
                           ..     ..              ..    ..
                         ..      ..               ..     ..
                        1....../../.......         ..     ..
                        ....../../................\..\......5
                       ..     ..                    ..     ..
                       ..    ..                     ..     ..
                      ..    ..      Sweet,           ..   ..
                      ..   ..          Sweet         ..   ..
                     ..   ..         completion      ..  ..
                     ..  ..                          ..  ..
                    ..  ..                           .. ..
                    .. ..                             ....
                   .. ..                               ..
                   ....                                ..
                   ..................                 ..
                   3...................................4
                 
                 
                 
                 
                 
        '''
        self.draw_triangle(p3, p1, p5)
        self.draw_triangle(p5, p4, p3)
        self.draw_triangle(p3, p4, p2)
        self.draw_triangle(p4, p5, p2)
        self.draw_triangle(p5, p1, p2)
        self.draw_triangle(p1, p3, p2)
    def draw_obj(self, Rs, Ps, obj):
        glPushMatrix()
        glRotatef(math.acos(Rs[0]) * 180. / math.pi, Rs[1], Rs[2], Rs[3])
        glTranslate(Ps.x, Ps.y, Ps.z)
        glCallList(obj)
        glPopMatrix()