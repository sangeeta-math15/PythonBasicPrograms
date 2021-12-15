#When a non-existent attribute is referenced, and when that attribute reference or assignment fails,
# an attribute error is raised.
#Attributes class object has no attribute with the name attribute
class Attribute(object):
    a=2
    print(a)
try:
    object=Attribute()
    print(object.attribute)
except AttributeError:
    print("Attribute Error raised")
