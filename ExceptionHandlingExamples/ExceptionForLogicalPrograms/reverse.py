# Python 3 program to reverse digits of a number
rev_num = 0
base_pos = 1
# Recursive function to reverse digits of num
def reversDigits(num):
    """
    :param num:
    :return:
    """
    global rev_num
    global base_pos
    if num > 0:
        reversDigits((int)(num / 10))
        rev_num += (num % 10) * base_pos
        base_pos *= 10
    return rev_num

if __name__=='__main__':
    try:
        num = int(input("Enter a number: "))
        if num<0:
            raise ValueError("That is not a positive number!")
    except ValueError as ve:
            print(ve)
    else:
        print("Reverse of no. is ",reversDigits(num))



