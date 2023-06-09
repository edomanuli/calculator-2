"""CLI application for a prefix-notation calculator."""

from arithmetic import (
    add,
    subtract,
    multiply,
    divide,
    square,
    cube,
    power,
    mod,
)


# Replace this with your code
while True:
    # take user input
    user_input = input("Type in the arithmetic problem here: ")

    # tokenize the input into a list eg: pow 4 5 => ['pow', 4, 5]
    tokens = user_input.split(" ")

    # if the first input is 'q', then quit
    if tokens[0] == "q":
        break
    elif tokens[0] == "+":  # create the add function with user input
        print(add(int(tokens[1]), int(tokens[2])))

    elif tokens[0] == "-":  # create the subtract function with user input
        print(subtract(int(tokens[1]), int(tokens[2])))

    elif tokens[0] == "*":  # create the multiply function with user input
        print(multiply(int(tokens[1]), int(tokens[2])))

    elif tokens[0] == "/":  # create the division function with user input
        print(divide(int(tokens[1]), int(tokens[2])))

    elif tokens[0] == "square":  # create the square function with user input
        print(square(int(tokens[1])))

    elif tokens[0] == "cube":  # create the cube function with user input
        print(cube(int(tokens[1])))

    elif tokens[0] == "pow":  # create the power function with user input
        print(power(int(tokens[1]), int(tokens[2])))

    elif tokens[0] == "mod":  # modulo/remainder function with user input
        print(mod(int(tokens[1]), int(tokens[2])))

    else:
        print("please enter a valid input.")

print("Goodbye!")
