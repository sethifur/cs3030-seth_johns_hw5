#!/usr/bin/env python3
import sys


def GetInput():
    """
    Function: 
        asks for a pin input <9876>
        validates the size, type, and number.
        returns pin if correct
        if incorrect 3 times exits program
    """
    for index in range(3):
        try:
            pin = int(input('Enter your pin: '))
            if (pin >= 1000 and pin < 10000):
                if pin == 1234:
                    return pin
                else:
                    print('Your PIN is incorrect')
            else:
                print('Invalid PIN lenth. Correct format is: <9876>')
        except ValueError:
            print('Invalid PIN character. Correct format is: <9876>')

    print('Your bank card is blocked.')
    exit(1)


# Main Function
def main():
    validation = GetInput()
    print('Your PIN is correct.')
    return

if __name__ == '__main__':
    #Call Main
    main()

    exit(0)
