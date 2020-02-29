class Subscriber:
	def __init__(self, name):
		self.name = name
	def update(self, message):
		print('{} got message "{}"'.format(self.name, message))
        
class Publisher:
	def __init__(self,events):
		self.events = {event: dict() 
		                for event in events}
	def get_subscribers(self, event):
	    return self.events[event]
	def register(self, event, who, callback=None):
		if callback == None:
			callback = getattr(who, 'update')
		self.get_subscribers(event)[who] = callback
	def unregister(self, event, who):
		del self.get_subscribers(event)[who]
	def dispatch(self, event, message):
		for subscriber, callback in self.get_subscribers(event).items():
			callback(message)
			
def main():
    p = Publisher(['love','goodman'])
    cat = Subscriber('Catcat')
    rat = Subscriber('Ratrat')
    mic = Subscriber('Mickey')

    p.register("love",bat)
    p.register("goodman",rat)
    p.register("love",mic)
    p.register("goodman",mic)    
    
    p.dispatch("love","I Love you!")
    p.unregister("love",mic)
    p.dispatch("goodman","Your receive a good man card")
    
    
if __name__ == "__main__":
	main()	
				    