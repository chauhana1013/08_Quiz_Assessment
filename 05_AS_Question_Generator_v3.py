# version 2 - finding to
import random
import math


# Checks input is in a given list
def list_checker(var_question, valid_list, error):
    while True:
        # Ask user for choice (and put choice in lowercase)
        response = input(var_question).lower()

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


questions_answered = 0
answer_tries = 0

# Loop for testing purposes
game_over = "no"
while game_over == "no":
    total_questions = num_check("How many questions would you like: ", 0)

    if total_questions == "":
        print("♾♾♾ Entering Infinite Mode ♾♾♾")

    # List for Level of Difficulty
    difficulty_list = ["easy", "medium", "hard"]

    print()
    difficulty_level = list_checker("Level of Difficulty (Easy / Medium / Hard): ", difficulty_list,
                                    "Please choose from Easy, Medium, or Hard")
    while True:

        print()
        # Infinite Mode is activated if user presses <ENTER>
        if total_questions == "":
            heading = "♾♾♾ Infinite Mode: Question {} ♾♾♾".format(questions_answered + 1)

        else:
            total_questions = int(total_questions)
            heading = f"Question {questions_answered + 1} of {total_questions}"
            if questions_answered == total_questions:
                end_game = "yes"
                break

        print(heading)

        if difficulty_level == "easy":
            shape = "rectangle"
            width = random.randint(1, 10)
            height = random.randint(1, 5)
            question = "find_area"
            answer_tries = 3
        else:
            shape_list = ["triangle", "rectangle", "circle"]

            if difficulty_level == "medium":
                shape = random.choice(shape_list)
                width = random.randint(5, 15)
                height = random.randint(5, 10)
                radius = random.randint(2, 5)
                question = "find_area"
                answer_tries = 2

            elif difficulty_level == "hard":
                shape = random.choice(shape_list)
                width = random.randint(5, 15)
                height = random.randint(5, 10)
                radius = random.randint(2, 10)
                question_type = ["find_area", "find_side_length"]
                question = random.choice(question_type)
                answer_tries = 1

        if shape == "rectangle":
            # Formula for Area of Rectangle
            area = width * height
            if question == "find_side_length":
                print(f"Find Missing Side of Rectangle \t | \t Area: {area} \t | \t Height: {height}")
            else:
                print(f"Area of Rectangle \t | \t Width: {width} \t | \t Height: {height}")

        elif shape == "triangle":
            # Formula for Area of Triangle
            area = 0.5 * width * height
            if question == "find_side_length":
                print(f"Find Missing Side of Triangle \t | \t Area: {area} \t | \t Height: {height}")
            else:
                print(f"Area of Triangle \t | \t Base: {width} \t | \t Height: {height}")

        else:
            # Formula for Area of Circle
            area = math.pi * radius * radius
            if question == "find_side_length":
                print(f"Find Radius of Circle \t | \t Area: {area}")
            else:
                print(f"Area of Circle \t | \t Radius: {radius}")

        if question == "find_side_length":
            if shape == "rectangle" or shape == "triangle":
                valid_answer = math.ceil(width)
            else:
                valid_answer = math.ceil(radius)

        else:
            valid_answer = math.ceil(area)
        print(valid_answer)

        while True:
            users_answer = num_check("Answer: ", 0, exit_code="xxx")

            if users_answer == "xxx":
                break
            answer_tries -= 1

            if users_answer == valid_answer:
                print("Woohoo you got the answer correct")
                break

            elif answer_tries == 0:
                print(f"The Correct Answer was: {valid_answer}")
                print()
                game_over = "yes"
                break

            elif users_answer != valid_answer:
                print("Incorrect Answer, keep going you got this")
                print(f"Tries Left: {answer_tries}")

        questions_answered += 1

print("Thanks for playing")
