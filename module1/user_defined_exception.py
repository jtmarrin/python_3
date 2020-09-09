#!/usr/bin/env python3

# define user-defined exceptions

class Error(Exception): 
    """Base class for other exceptions"""
    pass
class ValueTooSmallError(Error):  
    """Raised when the input is too small"""
    pass
class ValueTooLargeError(Error):  
    """Raised when the input is too large"""
    pass

# main program
# user guesses a number until they get it right
# need to guess this number
number = 10

while True:
    try:
        i_num = int(input("Enter a number: "))
        if i_num < number:
            raise ValueTooSmallError
        elif i_num > number:
            raise ValueTooLargeError
        break
    except ValueTooSmallError:
        print("This value is too small, try again!")
        print('')
    except ValueTooLargeError:
        print("This value is too Large, try again!")
        print('')
print("Congrats! You guessed it!")

