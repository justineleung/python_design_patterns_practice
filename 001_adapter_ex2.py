class Korean:
	def __init__(self):
		self.name = "Korean"
		
	def bapmokgosoyo(self):
		return "KimChi"
		
class Chinese:
	def __init__(self):
		self.name = "KeungKokYan"
	def chichichi(self):
		return "Rice"
		
class German:
	def __init__(self):
		self.name= "German"
	def abendbrot(self):
		return "Suppe"
		
class Coder:
	def __init__(self, energy_level):
		self.name= "IT"
		self._energy_level = energy_level
	def energy(self):
		food = ""
		for x in range(self._energy_level):
			food += "Kaffee"
		return food
		
class Adapter:
	def __init__(self, obj, **adapted_methods):
		self.obj = obj
		self.__dict__.update(adapted_methods)
	def __getattr__(self, attr):
		return getattr(self.obj, attr)
	def original_dict(self):
		return self.obj.__dict__
		
def main():
	objects= []
	korean = Korean()
	objects.append(Adapter(korean, hungry=korean.bapmokgosoyo))
	
	chinese = Chinese()
	german = German()
	coder = Coder(3)
	objects.append(Adapter(chinese, hungry=chinese.chichichi))
	objects.append(Adapter(german, hungry=german.abendbrot))
	objects.append(Adapter(coder, hungry=coder.energy))	
			
	for obj in objects:
		print("A {0} hungry, so he gets {1}".format(obj.name, obj.hungry()))
		
if __name__ == "__main__":
    main()		
		
		