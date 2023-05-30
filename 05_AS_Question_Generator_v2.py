import random
import math


# Checks input is in a given list
def list_checker(question, valid_list, error):
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

            if response > low:
                return response

            # Displays this error message if user inputs integer
            # lower than or equal to low number
            print(f"Please enter an integer more than {low}")

        # If user inputs anything else, displays error message
        except ValueError:
            print("Please enter an integer")
            continue


# Loop for testing purposes
game_over = "no"
while game_over == "no":
    # List for Level of Difficulty
    difficulty_list = ["easy", "medium", "hard"]

    print()
    difficulty_level = list_checker("Level of Difficulty (Easy / Medium / Hard): ", difficulty_list,
                                    "Please choose from Easy, Medium, or Hard")
    while True:

        if difficulty_level == "easy":
            width = random.randint(2, 10)
            height = random.randint(2, 10)
            guesses = 3

            print(f"Width: {width}")
            print(f"Height: {height}")

        elif difficulty_level == "medium":
            questions_list = ["rectangle", "triangle"]
            question = random.choice(questions_list)
            width = random.randint(5, 20)
            height = random.randint(5, 20)
            guesses = 2

        elif difficulty_level == "hard":
            questions_list = ["rectangle", "triangle", "circle"]
            question = random.choice(questions_list)
            width = random.randint(11, 100)
            height = random.randint(11, 100)
            radius = random.randint(11, 100)
            guesses = 1

        if question == "circle":
            answer = math.pi * radius

        if question == "triangle":
            # Formula for Area of Triangle
            answer = 0.5 * width * height

        else:
            # Formula for Area of Rectangle
            answer = width * height

        print(answer)

        users_guess = num_check("Answer: ", 0, exit_code="xxx")

        if users_guess == "xxx":
            game_over = "yes"
            break

        elif users_guess == answer:
            print("Woohoo you got the answer correct")

        else:
            print("Incorrect Answer, keep going you got this")
            continue

print("Thanks for playing")

