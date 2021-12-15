#When the divisor (second argument of the division) or the denominator is zero, then the resultant
# raises a zero division error.
try:
    a=100/0
    print(a)
except ZeroDivisionError:
    print("ZeroDivisor Exception raised")
else:
    print("Succuss,no error")
