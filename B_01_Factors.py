
# generates headings (e.g: ----- Heading ----- )
def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")


# displays instructions
def instructions():
    statement_generator(statement="Instructions", decoration="-")

    print('''
Enter an integer between 1 and 200. This program will show the factors of the chosen integer.

It will also tell you if your number...
- is a prime number (has only two factors)
- is a perfect square

To exit the program, type 'xxx'.
''')


# checks that the number is a valid integer and is between 1 and 200
def int_check(question):

    error = f"please input an integer that is between 1 and 200"

    while True:

        response = input(question)
        if response == "xxx":
            return response

        try:
            # ask user for a number
            response = int(response)

            # check that number is between 1 and 200
            if 1 <= response <= 200:
                return response
            else:
                print(error)
        # checks that number is valid
        except ValueError:
            print(error)


# works out factors, returns sorted list
def factor(var_to_factor):
    factors = []
    factorcount = int(to_factor + 1)
    squareroot = 0
    for item in range(1, factorcount):
        remainder = var_to_factor % item
        if item * item == var_to_factor:
            squareroot = item

        if remainder == 0:
            factors.append(item)

    res = str(factors)[1:-1]
    # checks if the factor is a prime number, if it's not then it says a different message
    if len(factors) > 2:
        if squareroot != 0:
            print(f"The factors of {to_factor} are: " + res)
            print(f"{to_factor} is also a perfect square, it's square root is {squareroot}")
        else:
            print(f"The factors of {to_factor} are: " + res)
    else:
        print(f"{to_factor} is a prime number, it's only factors are: " + res)


# main routine goes here

statement_generator("Factor Calculator", "•")

# asks if the user wants to see the instructions
want_instructions = input("\nPress <enter> to read the instructions or any key to continue ")

# if they press enter without typing anything extra, display instructions
if want_instructions == "":
    instructions()

while True:
    to_factor = int_check("To factor: ")
    if to_factor == "xxx":
        print("Thank you for using the factor calculator")
        break
    print("You chose to factor", to_factor)
    if to_factor == 1:
        print("One is special, it is UNITY (has only one factor)")
    else:
        factor(to_factor)
