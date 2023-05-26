# Functions go here...
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


