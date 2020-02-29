import types

class Catch_mouse(object):
	def __init__(self, *args, **kwargs):
		self.power = kwargs.pop('power', None)
		if kwargs.get('catch_strategy', None):
		    self.catch_it = types.MethodType(kwargs.pop('catch_strategy'), self)
		
	def catch_it(self):
		print("No catch")
	
def by_hand(self):
    print("use hand catch mouse, power - {}".format(8))
		
def by_slipper(self):
	print("use slipper catch mouse, power - {}".format(5))
		
def by_poison(self):
	print("use poison catch mouse, power - {}".format(0))
		
def main():
    m1 = Catch_mouse(power=10)
    m1.catch_it()
    m2 = Catch_mouse(power=10, catch_strategy=by_hand)
    m2.catch_it()
    m3 = Catch_mouse(power=10, catch_strategy=by_slipper)	
    m3.catch_it()
    m4 = Catch_mouse(power=10, catch_strategy=by_poison)		
    m4.catch_it()
	
if __name__ == "__main__":
	main()	
						