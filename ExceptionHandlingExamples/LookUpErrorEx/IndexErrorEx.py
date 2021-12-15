#When you are trying to access an index (sequence) of a list that does not exist in that list or is out of range of that list, an index error is raised.
try:
    a = ['a', 'b', 'c']
    print(a[4])
except LookupError:
    print("Index Error Exception Raised, list index out of range")
else:
    print("Success, no error!")
