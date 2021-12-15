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

