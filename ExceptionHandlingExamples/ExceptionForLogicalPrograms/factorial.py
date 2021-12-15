import logging

#pass the name of the file in which you want to record the events.
logging.basicConfig(filename='factorial.log',format='%(asctime)s %(message)s',filemode='w')

# Creating an object
logger = logging.getLogger()

# Setting the threshold of logger to DEBUG
# threshold for tracking based on the numeric values assigned to each level.
logger.setLevel(logging.DEBUG)

def recur_factorial(n):
    """
    :param n is number given as input
    :return factorial og given number
    """
    if n == 1:
       return n
    else:
       return n*recur_factorial(n-1)

if __name__=='__main__':
    try:
            # take input from the user
            num = int(input("Enter a number: "))
            # check is the number is negative
            if num < 0:
                raise ValueError("That is not a positive number!")
            elif num == 0:
                raise ValueError("The factorial of 0 is 1")
    except ValueError as ve:
        print(ve)
        logger.error("Error message")
    else:
        print("The factorial of ",num,"is",recur_factorial(num))

