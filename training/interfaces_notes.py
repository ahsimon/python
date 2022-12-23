#In python classes contains no abstract methods
# Informal Interfaces
# python informal interface is also a class that defines methods that can be overridden but without force enforcement. An informal interface also called Protocols

class Fruits :
    def __init__( self, ele) :
        self.__ele = ele
    def __contains__( self, ele) :
        return ele in self.__ele
    def __len__( self ):
        return len( self.__ele)
Fruits_list = Fruits([ "Apple", "Banana", "Orange" ])
print(len(Fruits_list))
print("Apple" in Fruits_list)
print("Mango" in Fruits_list)
print("Orange" not in Fruits_list)

# As in the above example code, class Fruits implement the _len_, and _contains_ methods, so on the instance of the Fruits class,
#  we can directly use the len function to get the size and can check the membership by using the in operator. As in the above code, 
# the _iter_ method (iterable protocol) is not implemented, so we would not iterate over the instance of the Fruits.
#  Therefore an informal interface cannot be enforced formally.

