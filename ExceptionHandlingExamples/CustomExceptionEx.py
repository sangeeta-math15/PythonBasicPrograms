#Python has many built-in exceptions that you can use in your program. Still, sometimes,
#you may need to create custom exceptions with custom messages to serve your purpose.
class UnExpectedValueError(Exception):
    def __init__(self,data):
        self.data=data
    def __int__(self):
        return repr(self.data)
Total_marks=int(input("Enter total marks scored:"))
try:
    Num_of_section=int(input("Enter num of section:"))
    if Num_of_section<1:
        raise UnExpectedValueError("Number of section cont be less than 1")
except UnExpectedValueError as e:
    print("Recieved Error:" +e.data)