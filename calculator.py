"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code
while True:
    # take user input
    user_input = input('Type in the arithmetic problem here: ')

    # tokenize the input into a list eg: pow 4 5 => ['pow', 4, 5]
    tokens = user_input.split(' ')

    # if the first input is 'q', then quit
    if tokens[0] == 'q':
        break