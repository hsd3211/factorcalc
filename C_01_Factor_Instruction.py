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

# main routine goes here


# asks if the user wants to see the instructions
want_instructions = input("\nPress <enter> to read the instructions or any key to continue ")

# if they press enter without typing anything extra, display instructions
if want_instructions == "":
    instructions()

print("\nprogram continues")