import abc
class Myinterface( abc.ABC ) :
    @abc.abstractclassmethod
    def disp():
        pass
class Myclass( Myinterface ) :
    pass
o1 = Myclass( )