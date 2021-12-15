#When an assert statement is failed, an Assertion Error is raised.
try:
    a=10
    b="Sangeeta"
    assert a==b
except AssertionError:
    print("Assertion Exception Raised.")
else:
    print("Success, no error!")