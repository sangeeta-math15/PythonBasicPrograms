#Name Error is raised when a local or global name is not found.
#ans variable is not defined.Hence, you will get a name error.

try:
    print(ans)
except NameError:
    print("NameError: name 'ans' is not defined")
else:
    print("Success, no error")
