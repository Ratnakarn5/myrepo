class Duck():
	# USING simple assigning of the indiviual value
	# def __init__(self, color='white'):
	# 	self._color = color  #_color make a local variable for our understaning
	# another way using constructor with keyword arguement
	# def __init__(self, **kwargs):
	# 	self._color=kwargs.get('color', 'white')
	# best way to use is this
	def __init__(self, **kwargs):
		self.varibles=kwargs['color']	# self.varible = kwargs[0] meaning
	
	def set_color(self, k, v):
		self.varibles[k]=v
		#self.varibles['color']=color
	
	def get_color(self,k):
		return self.varibles.get(k, None)
		#return self.varibles.get('color', None)

def main():
	donald = Duck(feet=2,color='brown')
	#print(donald.get_color())
	print(donald.get_color('color'))

if __name__ == '__main__':main()

