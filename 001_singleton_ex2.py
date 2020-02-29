class SheepOnlyFarm:
	__blackdot = None
	def getInstance():
		if SheepOnlyFarm.__blackdot == None:
			SheepOnlyFarm();
		return SheepOnlyFarm.__blackdot
	def __init__(self):
		if SheepOnlyFarm.__blackdot != None:
			raise Exception("This can be single sheep only")
		else:
			SheepOnlyFarm.__blackdot = self
sheep1 = SheepOnlyFarm()
print(sheep1)

sheep2 = SheepOnlyFarm.getInstance()
print(sheep2)
	
sheep3 = SheepOnlyFarm.getInstance()
print(sheep3)