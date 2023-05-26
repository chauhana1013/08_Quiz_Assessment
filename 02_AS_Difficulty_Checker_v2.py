# Version 2 - checks that response is in a given list

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

# Main Routine goes here
# Lists for checking responses
difficulty_list = ["easy", "medium", "hard"]

# Loop for testing purposes
while True:

    # Ask user for choice and check it's valid
    difficulty_level = user_choice("Level of Difficulty (Easy / Medium / Hard): ", difficulty_list,
                                   "Please choose from Easy, Medium, or Hard")

    # Print out choice for comparison purposes
    print()
    print("You chose {}".format(difficulty_level))
    print()
