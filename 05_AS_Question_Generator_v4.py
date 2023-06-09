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


questions_answered = 0
answer_tries = 0

# Loop for testing purposes
playing_quiz = "yes"
while playing_quiz == "yes":
    total_questions = num_check("How many questions would you like: ", 0)

    if total_questions == "":
        print("♾♾♾ Entering Infinite Mode ♾♾♾")

    # List for Level of Difficulty
    difficulty_list = ["easy", "medium", "hard"]
    # List of Shapes
    shape_list = ["Triangle", "Rectangle", "Circle"]

    print()
    difficulty_level = list_checker("Level of Difficulty (Easy / Medium / Hard): ", difficulty_list,
                                    "Please choose from Easy, Medium, or Hard")
    end_quiz = "no"
    while end_quiz == "no":

        print()
        # Infinite Mode is activated if user presses <ENTER>
        if total_questions == "":
            heading = "♾♾♾ Infinite Mode: Question {} ♾♾♾".format(questions_answered + 1)

        else:
            total_questions = int(total_questions)
            heading = f"Question {questions_answered + 1} of {total_questions}"
            if questions_answered == total_questions:
                playing_quiz = "no"
                break

        print(heading)

        shape = random.choice(shape_list)
        question = "Area"
        if difficulty_level == "easy":
            width = random.randint(1, 10)
            height = random.randint(1, 5)
            radius = random.randint(1, 3)
            answer_tries = 3

        else:
            width = random.randint(5, 15)
            height = random.randint(1, 5)
            radius = random.randint(2, 5)

            if difficulty_level == "medium":
                answer_tries = 2

            elif difficulty_level == "hard":
                question_type = ["Find Missing Side", "Area"]
                question = random.choice(question_type)
                answer_tries = 1

        height = height * 2

        if shape == "Rectangle":
            # Formula for Area of Rectangle
            area = width * height

        elif shape == "Triangle":
            # Formula for Area of Triangle
            area = 0.5 * width * height
            area = math.ceil(area)

        elif shape == "Circle":
            # Formula for Area of Circle
            area = math.pi * radius * radius

        if question == "Find Missing Side":
            if shape == "Triangle" or shape == "Rectangle":
                print(f"{question} of {shape} \t | \t Area: {area} \t | \t Height: {height}")
                valid_answer = width
            else:
                print(f"Find Radius of {shape} \t | \t Area: {area:.2f}")
                valid_answer = radius

        elif question == "Area":
            if shape == "Rectangle" or shape == "Triangle":
                print(f"{question} of {shape} \t | \t Width: {width} \t | \t Height: {height}")
                valid_answer = math.ceil(area)
            else:
                print(f"Area of Circle \t | \t Radius: {radius}")
                valid_answer = round(area, 2)

        print(valid_answer)

        while True:
            users_answer = num_check("Answer: ", 0, exit_code="xxx")

            if users_answer == "xxx":
                playing_quiz = "yes"
                end_quiz = "yes"
                break

            answer_tries -= 1

            if users_answer == valid_answer:
                print("Woohoo you got the answer correct")
                break

            elif answer_tries == 0:
                if shape == "Circle" and question == "Area":
                    print(f"The Correct Answer was: {valid_answer:.2f}")
                else:
                    print(f"The Correct Answer was: {valid_answer}")
                break

            elif users_answer != valid_answer:
                print("Incorrect Answer, keep going you got this")
                print(f"Tries Left: {answer_tries}")

        questions_answered += 1

print("Thanks for playing")
