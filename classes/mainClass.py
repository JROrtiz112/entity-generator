from classes.attribute import Attribute


from .attribute import Attribute

class Class:
    name = ''
    attributes = []

    def __init__(self, name):
        self.name = name
        self.list = []

    def append(self, item):
        attribute = Attribute(item[0], item[1], item[2])
        self.attributes.append(attribute)    

    def getData(self):
        data = []
        for attribute in self.attributes:
            data.append(attribute.getDictionary())
        return data