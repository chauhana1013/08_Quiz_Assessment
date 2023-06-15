# Question Generator Version 2 - Nearly Base Level code for the Questions Component
# with missing parts and repeated code but doubled the types aof questions user might get
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

# Loop for testing purposes
playing_quiz = "yes"
while playing_quiz == "yes":

    # Asks user how many questions they would like
    total_questions = num_check("How many questions would you like: ", 0)

    if total_questions == "":
        print("♾♾♾ Entering Infinite Mode ♾♾♾")

    # List for Level of Difficulty
    difficulty_list = ["easy", "medium", "hard"]

    # Asks user how much hard they would like their questions
    print()
    difficulty_level = list_checker("Level of Difficulty (Easy / Medium / Hard): ", difficulty_list,
                                    "Please choose from Easy, Medium, or Hard")
    while True:

        print()
        # Infinite Mode is activated if user presses <ENTER>
        if total_questions == "":
            heading = f"♾♾♾ Infinite Mode: Question {questions_answered + 1} ♾♾♾"

        # Else the program outputs a heading including which question out of the total questions the user is on
        else:
            total_questions = int(total_questions)
            heading = f"Question {questions_answered + 1} of {total_questions}"
            if questions_answered == total_questions:
                playing_quiz = "no"
                break

        print(heading)

        # If difficulty level is easy, the random number range is from 1 to 10 for width
        # and for height the range is 1 to 5
        if difficulty_level == "easy":
            shape = "rectangle"
            width = random.randint(1, 10)
            height = random.randint(1, 5)
            question = "find_area"
        else:
            # List of Shapes
            shape_list = ["triangle", "rectangle", "circle"]

            # If difficulty level is medium, the random number range is from 5 to 15 for width
            # and for height, the range is 5 to 10
            if difficulty_level == "medium":
                shape = random.choice(shape_list)
                width = random.randint(5, 15)
                height = random.randint(5, 10)
                radius = random.randint(2, 5)
                question = "find_area"

            # If difficulty level is hard, the random number range is from 5 to 15 for width,
            # for height the range is 5 to 10 and for radius the range is 2 to 10
            # Hard level also has two types of questions: FInd the Area and Find the Side Length
            elif difficulty_level == "hard":
                shape = random.choice(shape_list)
                width = random.randint(5, 15)
                height = random.randint(5, 10)
                radius = random.randint(2, 10)
                question_type = ["find_area", "find_side_length"]
                question = random.choice(question_type)

        # If the shape is rectangle, program outputs question for either finding the area of the rectangle
        # and gives the width and height or to find the side length and gives the area and height
        if shape == "rectangle":
            # Formula for Area of Rectangle
            area = width * height
            if question == "find_side_length":
                print(f"Find Missing Side of Rectangle \t | \t Area: {area} \t | \t Height: {height}")
            else:
                print(f"Area of Rectangle \t | \t Width: {width} \t | \t Height: {height}")

        # If the shape is triangle, program outputs question for finding the area of the triangle
        # and gives the base and height or to find the side length and gives the area and height
        elif shape == "triangle":
            # Formula for Area of Triangle
            area = 0.5 * width * height
            if question == "find_side_length":
                print(f"Find Missing Side of Triangle \t | \t Area: {area} \t | \t Height: {height}")
            else:
                print(f"Area of Triangle \t | \t Base: {width} \t | \t Height: {height}")

        # If the shape is circle, program outputs question for finding the area of the circle
        # and gives the radius or to find the side length and gives the area
        else:
            # Formula for Area of Circle
            area = math.pi * radius * radius
            if question == "find_side_length":
                print(f"Find Radius of Circle \t | \t Area: {area}")
            else:
                print(f"Area of Circle \t | \t Radius: {radius}")

        # Prints the answer for testing purposes
        if question == "find_side_length":
            if shape == "rectangle" or shape == "triangle":
                valid_answer = math.ceil(width)
            else:
                valid_answer = math.ceil(radius)

        else:
            valid_answer = math.ceil(area)
        print(valid_answer)

        # Asks user to answer the question
        users_answer = num_check("Answer: ", 0, exit_code="xxx")

        # If user inputs the exit code, program breaks
        if users_answer == "xxx":
            playing_quiz = "no"
            break

        # If user gets the answer correct, program congratulates the user
        elif users_answer == valid_answer:
            print("Woohoo you got the answer correct")
            print()

        # If users gets the answer wrong, program tells the user that they were incorrect and shows the correct answer
        elif users_answer != valid_answer:
            print("Incorrect Answer, keep going you got this")
            print(f"The Correct Answer was: {valid_answer}")
            print()

        questions_answered += 1
# If game ends, program thanks the user for playing
print("Thanks for playing")
