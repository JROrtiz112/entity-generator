class Attribute:
    default = ''
    name = ''
    type = ''

    def __init__(self, default, name, type):
        self.default = default
        self.name = name
        self.type = type

    def default(self):
        return self.default

    def default(self, default):
        self.default = default
    
    def name(self):
        return self.name

    def name(self, name):
        self.name = name

    def type(self):
        return self.type
    
    def type(self, type):
        self.type = type

    def getDictionary(self):
        return dict(default=self.default, attribute=self.name, type=self.type)