# Ask user for width until they enter a number larger than zero

def int_check(question):

    error = f"please input an integer that is between 1 and 200\n"

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

# Main routine goes here


for item in range(0, 2):
    to_factor = int_check("To factor: ")
    if to_factor == "xxx":
        print("Thank you for using the factor calculator")
        break
    print("You chose to factor", to_factor)

