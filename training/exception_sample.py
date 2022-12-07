import logging


def AbyB(a , b):
	try:
		c = ((a+b) / (a-b))
	except ZeroDivisionError:
		logging.error ("a/b result in 0")
	else:
		logging.warning ("%d",c)
		
AbyB(2.0, 3.0)
AbyB(3.0, 10.0)