import copy

class Legs:
    def clone(self):
        return copy.deepcopy(self)

class Bee:
    def __init__(self):
        self.legs = [leg(), leg(), leg(), leg(), leg(), leg()]
    def clone(self):
        return copy.deepcopy(self)

class Bees:
    def __init__(self):
        self.prototypes = {}
    def addPrototype(self, type, bee):
        self.prototypes[type] = bee
    def getPrototype(self, type):
        return self.prototypes[type].clone()

honeybee = bee()
bumblebee = bee()
bees = Bees()
bees.addPrototype("Honey", honeybee)
bees.addPrototype("Bumble", bumblebee)
bumblePrototype = bees.getPrototype("Bumble")
