#if a key you are trying to access is not found in the dictionary, a key error exception is raised.
try:
    a={1:'a',2:'b',3:'c'}
    print(a[4])
except LookupError:
    print("KeyInterrupt Exception raised")
else:
    print("Success no error")
    