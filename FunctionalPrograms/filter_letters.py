# Python program to demonstrate working
# of the filter.
import logging
logging.basicConfig(filename='filter.log',filemode='w')

# function that filters vowels
def fun(variable):
    """

    :param variable:List sequence
    :return: boolean value
    """
    letters = ['a', 'e', 'i', 'o', 'u']

    if (variable in letters):
        return True
    else:
        return False

if __name__=='__main__':
    # sequence
    sequence = ['g', 'j', 'e','k', 's', 'p', 'r']

    # using filter function
    filtered = filter(fun, sequence)

    print('The filtered letters are:')

    for s in filtered:
        print(s)
