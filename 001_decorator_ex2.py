
class Dessert(object):
	def __init__(self, type, budget):
		self._type = type
		self._budget = budget
		self.name = ""
		
	def make_dessert(self):
		my_menu = ""
		if self._type == "food":
			my_menu = dessert_food(self)
		elif self._type == "drink":
			my_menu = dessert_drink(self)
		else:
			my_menu = dessert_other(self)
		print(my_menu)	
		
	def wripped_cream(func):
		def func_wrapper(self):
			return "[wrapped_cream]{0}".format(func())
		return func_wrapper
		
	def blueberry(func):
		def func_wrapper(self):
			return "[blueberry]{0}".format(func())
		return func_wrapper			

	def caramel(func):
		def func_wrapper(self):
			return "[caramel]{0}".format(func())
		return func_wrapper			
		
	def icecream(func):
		def func_wrapper(self):
			return "{0} [icecream]".format(func())
		return func_wrapper			
	
	@wripped_cream
	@blueberry						
	def dessert_food(self):
		return "waffle"
		
	@wripped_cream
	@caramel						
	def dessert_drink(self):
		return "coffee"		
		
	@wripped_cream
	@icecream						
	def dessert_other(self):
		return "sorbet"		
		
def main():
	menu1 = Dessert("food",10)
	print(menu1)
	menu2 = Dessert("drink",10)
	print(menu2)	
	menu3 = Dessert("other",10)
	print(menu3)	
	
		
if __name__ == "__main__":
    main()		
				
		
		
		
		