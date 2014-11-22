from OpenGL.GLUT import *

class Input:
    def __init__(self):
        self.keys = []
    def keyboard(self, key, x, y):
        if key == " ":
            glutDestroyWindow(1)
            exit()
        self.keys.append(key)
    def keyboardUp(self, key, x, y):
        self.keys.remove(key)