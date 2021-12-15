#The Overflow Error is raised when the result of an arithmetic operation is out of range.

try:
    import math
    print(math.exp(1000))
except OverflowError:
    print("OverFlow Exception Raised.")
else:
    print("Success, no error!")
