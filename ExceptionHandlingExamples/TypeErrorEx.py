#Type Error Exception is raised when two different or unrelated types of operands or objects are combined.

try:
    a=10
    b="Sangeeta"
    c=a+b
except TypeError:
    print("TypeError: Exception raised")
else:
    print('Success no error!')