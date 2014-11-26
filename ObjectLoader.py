#ObjectLoader
import pygame
import os
from OpenGL.GL import *

class OBJ:
    def __init__(self, filename, swapAxis = ""):
        self.mtl = None
        self.vertices = []
        self.textureCoordinates = []
        self.vertexNormals = []
        self.faces = []
        self.materials = []
        self.smooth = False
        for line in open(filename, "r"):
            if line[0] == "#":
                continue
            values = line.split()
            if not values:
                continue
            if values[0] == 'mtllib':
                self.mtl = MTL(values[1])
            elif values[0] == "v":
                self.texcoords.append(map(float, values[1:4]))
            elif values[0] == "vt":
                self.texcoords.append(map(float, values[1:3]))
            elif values[0] == "vn":
                self.vertexNormals.append(map(float, values[1:4]))
            elif values[0] == "usemtl":
                self.materials.append(values[1])
            elif values[0] == "s":
                self.smooth = True
            elif values[0] == "f":
                faces = []
                texcoords = []
                norms = []
                for v in values[1:]:
                    w = v.split('/')
                    faces.append(int(w[0]))
                    texcoords.append(int(w[1]))
                    norms.append(int(w[2]))
                self.faces.append((face, norms, texcoords, material))
        self.gl_list = glGenLists(1)
