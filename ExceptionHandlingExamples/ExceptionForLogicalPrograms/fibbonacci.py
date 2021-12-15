import logging

#pass the name of the file in which you want to record the events.
logging.basicConfig(filename='fibbonacci.log',format='%(asctime)s %(message)s',filemode='w')

# Creating an object
logger = logging.getLogger()

# Setting the threshold of logger to DEBUG
# threshold for tracking based on the numeric values assigned to each level.
logger.setLevel(logging.DEBUG)
logger.debug("debug mode")

def rec_fibo(i):
    """
    :param i:
    :return:
    """
    if i<=1:
        return i
    else:
        return(rec_fibo(i-1)+rec_fibo(i-2))

try:
    # take input from the user
        nterm = int(input("how many terms?"))
        print("Please enter the positive integre")
        if nterm <= 0:
                raise ValueError("That is not a positive number!")
except ValueError as ve:
        print(ve)

else:
    print("Fibonacci Sequence")
    for i in range(nterm):
        print(rec_fibo(i))

if __name__=='__main__':
    rec_fibo(i)

