class ObjectList:
    def __init__(self):
        self.list = []
    def add_object(self, object):
        self.list.append(object)
    def render_objects(self):
        for obj in self.list:
            obj.draw()