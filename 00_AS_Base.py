# Functions go here...
# Checks input is in a given list
def user_choice(question, valid_list, error):
    while True:
        # Ask user for choice (and put choice in lowercase)
        response = input(question).lower()

        # Iterates through list and if response is an item
        # In the list (or the first letter of an item),
        # the full item name is returned
        for item in valid_list:
            if response == item[0] or response == item:
                response = item
                return response

        # Output error if item not in list
        print(error)
        print()


# Checks input is exit code or integer and over low number
def num_check(question, low=None, exit_code=None):
    while True:
        response = input(question).lower()
        if response == exit_code:
            return response

        elif response == "":
            return response

        try:
            response = int(response)
            if low < response:
                return response

            # Displays this error message if user inputs integer
            # lower than or equal to low number
            print(f"Please enter an integer more than {low}")

        # If user inputs anything else, displays error message
        except ValueError:
            print("Please enter an integer")
            continue


# Main Routine goes here...
print("📐📐📐 Welcome to Area of Shape Quiz 📐📐📐")

# List for Yes or No
yes_no_list = ["yes", "no"]

# Asks the user if they would like to see the Instructions
print()
show_instructions = user_choice("Hey Mathematician, would you like to see the Instructions? ",
                                yes_no_list, "Please answer Yes or No")

# If user inputs 'yes', shows user Instructions
if show_instructions == "yes":
    print()
    print("***** Instructions go here *****")

# List for Level of Difficulty
difficulty_list = ["easy", "medium", "hard"]

# Ask user for choice and check it's valid
print()
difficulty_level = user_choice("Level of Difficulty (Easy / Medium / Hard): ", difficulty_list,
                               "Please choose from Easy, Medium, or Hard")

questions = num_check("How many questions would you like: ", 0)

# Infinite Mode is activated if user presses <ENTER>
if questions == "":
    print("Infinite Mode Activated")

# Prints the amount of questions user wants to answer
print(f"You want to answer {questions} questions")


