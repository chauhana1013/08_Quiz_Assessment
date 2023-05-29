import random


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

while True:
    # List for Level of Difficulty
    difficulty_list = ["easy", "medium", "hard"]

    print()
    difficulty_level = user_choice("Level of Difficulty (Easy / Medium / Hard): ", difficulty_list,
                                   "Please choose from Easy, Medium, or Hard")

    if difficulty_level == "easy":
        width = random.randint(1, 10)
        height = random.randint(1, 10)
        guesses = 3

    elif difficulty_level == "medium":
        width = random.randint(1, 20)
        height = random.randint(1, 20)
        guesses = 2

    elif difficulty_level == "hard":
        width = random.randint(1, 100)
        height = random.randint(1, 100)
        guesses = 1

    print(f"Width: {width}")
    print(f"Height: {height}")

    answer = width * height

    users_guess = int(input("Answer: "))






