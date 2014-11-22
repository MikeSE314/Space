import math

class Quaternion:
    def __init__(self, w, x, y, z, norm = True):
        self.w = w
        self.x = x
        self.y = y
        self.z = z
        if(norm):
            self.doTheTrigStuff()
    def doTheTrigStuff(self):#hopefully unneeded
        self.x = self.x * math.sin(self.w / 2)
        self.y = self.y * math.sin(self.w / 2)
        self.z = self.z * math.sin(self.w / 2)
        self.w = math.cos(self.w / 2)
    def vecPart(self):
        return(Vector(self.x, self.y, self.z).Normalised())
    def inverse(self):
        return(Quaternion(self.w, -self.x, -self.y, -self.z, False))
    def Get_length(self):#s
        return((self.w ** 2 + self.x ** 2 + self.y ** 2 + self.z ** 2) ** (1. / 2.))
    def Normalised(self):#v
        return(self.divElem(self.Get_length()))
    def multByQuat(self, q2):
        tempVec1 = Vector(self.x, self.y, self.z)
        tempVec2 = Vector(q2.x, q2.y, q2.z)
        w = self.w * q2.w - tempVec1.Dot(tempVec2)#s
        tempVec3 = tempVec1.mult(q2.w).add(tempVec2.mult(self.w)).add(tempVec1.Cross(tempVec2))
        return(Quaternion(w, tempVec3.x, tempVec3.y, tempVec3.z, False))
    def multByVec(self, v2):
        tempQuat1 = Quaternion(0, v2.x, v2.y, v2.z)
        tempVec1 = Vector(self.x, self.y, self.z)
        tempVec2 = tempVec1.Cross(v2)
        return(v2.add(tempVec2.mult(self.w * 2)).add(tempVec1.Cross(tempVec2).mult(2)))
    def divElem(self, s):#q
        return(Quaternion(self.w / s,
                          self.x / s, self.y / s, self.z / s, False))
    def Slerp(self, q2, s):
        pass
    def p(self):
        return(self.w, self.x, self.y, self.z)

class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def Get_length(self):#s
        return((self.x ** 2 + self.y ** 2 + self.z ** 2) ** (1. / 2.))
    def Normalised(self):#v
        return(self.div(self.Get_length()))
    def Cross(self, v2):#v
        return(Vector(self.y * v2.z - self.z * v2.y,
            self.z * v2.x - self.x * v2.z,
            self.x * v2.y - self.y * v2.x))
    def Rotated_vector_around_angle(self, nHat, theta):
        nHat = nHat.Normalised()
        return(self.mult(math.cos(theta)).add(nHat.mult(self.Dot(nHat)).mult(1 - math.cos(theta))).add(nHat.Cross(self).mult(math.sin(theta))))
    def Dot(self, v2):#s
        return(self.x * v2.x + self.y * v2.y + self.z * v2.z)
    def add(self, v2):#v
        return(Vector(self.x + v2.x, self.y + v2.y, self.z + v2.z))
    def subtract(self, v2):#v
        return(Vector(self.x - v2.x, self.y - v2.y, self.z - v2.z))
    def mult(self, s):#v
        return(Vector(self.x * s, self.y * s, self.z * s))
    def div(self, s):#v
        return(Vector(self.x / s, self.y / s, self.z / s))
    def p(self):
        return(self.x, self.y, self.z)

if __name__ == "__main__":
    myVector = Vector(1, 0, 0)
    myVector = myVector.Normalised()
    print("m", myVector.p())
    myQuaternion = Quaternion(math.pi / 4, myVector.x, myVector.y, myVector.z)
    print("t", myQuaternion.p())
    myQuaternion = myQuaternion.Normalised()
    print(myQuaternion.inverse().p())