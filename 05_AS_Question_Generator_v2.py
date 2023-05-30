# version 2 - finding to
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
def num_check(var_question, low=None, exit_code=None):
    while True:
        response = input(var_question).lower()
        if response == exit_code:
            return response

        elif response == "":
            return response

        try:
            response = float(response)

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
    total_questions = num_check("How many questions would you like: ", 0)

    # Infinite Mode is activated if user presses <ENTER>
    if total_questions == "":
        
    # List for Level of Difficulty
    difficulty_list = ["easy", "medium", "hard"]

    print()
    difficulty_level = list_checker("Level of Difficulty (Easy / Medium / Hard): ", difficulty_list,
                                    "Please choose from Easy, Medium, or Hard")
    while True:

        if difficulty_level == "easy":
            quiz_question = "rectangle"
            width = random.randint(1, 10)
            height = random.randint(1, 10)
            guesses = 3

        elif difficulty_level == "medium":
            questions_list = ["rectangle", "triangle"]
            quiz_question = random.choice(questions_list)
            width = random.randint(1, 15)
            height = random.randint(1, 15)
            guesses = 2

        elif difficulty_level == "hard":
            questions_list = ["rectangle", "triangle", "circle"]
            quiz_question = random.choice(questions_list)
            width = random.randint(5, 15)
            height = random.randint(5, 15)
            radius = random.randint(2, 10)
            guesses = 1

        if quiz_question == "rectangle":
            # Formula for Area of Rectangle
            answer = width * height
            print(f"Area of Rectangle \t | \t Width: {width} \t | \t Height: {height}")

        elif quiz_question == "triangle":
            # Formula for Area of Triangle
            answer = 0.5 * width * height
            print(f"Area of Triangle \t | \t Base: {width} \t | \t Height: {height}")

        else:
            # Formula for Area of Circle
            answer = math.pi * radius * radius
            print(f"Area of Circle \t | \t Radius: {radius}")

        answer = round(answer, 2)
        print(answer)

        users_guess = num_check("Answer: ", 0, exit_code="xxx")

        if users_guess == "xxx":
            game_over = "yes"
            break

        elif users_guess == answer:
            print("Woohoo you got the answer correct")
            print()

        else:
            print("Incorrect Answer, keep going you got this")
            print(f"The Answer was: {answer:.0f}")
            print()
            continue

print("Thanks for playing")
