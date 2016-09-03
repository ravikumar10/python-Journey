"""
Genric way of assigning  variable to different classes with different number of arguments  
It will take care of the positional arguements like :: s=Stock('apple','1','1200')
postiona arguemnts like :: p=points(x='10',y='10') 

"""
from inspect import Parameter, Signature

def make_signature(names):
	return Signature(
		Parameter(name,Parameter.POSITIONAL_OR_KEYWORD)
		for name in names)
class Structure():
	__signature__=make_signature([]) 
	def __init__(self,*args,**kwargs):
		bound=self.__signature__.bind(*args,**kwargs)
		for name,value in bound.arguments.items():
				setattr(self,name,value)
class Stock(Structure):
	__signature__=make_signature(['name','shares','price'])

class points(Structure):
	__signature__=make_signature(['x','y'])

class Address(Structure):
	__signature__=make_signature(['hostname','port'])

if __name__ == '__main__':
	s=Stock('apple','1','1200')
	print ("Stock price of %s for %s share is %s dollars"%(s.name,s.shares,s.price))

	p=points(x='10',y='10')
	print ("Points in the plane are X=%s , y=%s"%(p.x,p.y))