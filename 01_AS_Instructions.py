# Component 1 - Instructions
def yes_no(question):
    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"

        elif response == "no" or response == "n":
            return "no"

        else:
            print("Please answer Yes or No")
            print()

# Asks the user if they would like to see the Instructions
show_instructions = yes_no("Hey Mathematician, would you like to see the Instructions? ")
# If user inputs 'yes', shows user Instructions
if show_instructions == "yes":
    print()
    print("***** Instructions go here *****")
# If user inputs 'no' show
else:
    print("Program continues")
