import logging

try:
	printf("Angelica,Lakshmi")
except Exception as Argument:
	f = open("name.txt", "a")

	f.write(str(Argument))
	
	f.close()