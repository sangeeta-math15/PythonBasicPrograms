#Abstract methods in user-defined classes should raise this exception when the derived classes override the method.

class BaseClass(object):
    """Define interfaces"""
    def __init__(self):
        super(BaseClass,self).__init__()
    def do_something(self):
        """Interface not implemented"""
        raise NotImplementedError(self.__class__.__name__+'do_something')

class SubClass(BaseClass):
    """Implemted interface"""
    def do_something(self):
        """Really does something"""
        print(self.__class__.__name__ +'do_something')


SubClass().do_something()
BaseClass().do_something()



