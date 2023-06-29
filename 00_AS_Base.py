import random
import math


# Functions go here...
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
    if low is not None and exit_code is not None:
        situation = "float"
    elif low is not None and exit_code is None:
        situation = "integer"
    while True:
        # First checks if the response was exit code
        response = input(var_question).lower()

        if response == exit_code:
            return response

        elif response == "":
            return response

        try:
            if situation == "integer":
                response = int(response)

            elif situation == "float":
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


# Main Routine goes here...
print()
print("📏📏📏 Welcome to Area of Shape Quiz 📏📏📏")

# List for Yes or No
yes_no_list = ["yes", "no"]

# List for Level of Difficulty
difficulty_list = ["easy", "medium", "hard"]

# List of Shapes
shape_list = ["Triangle", "Rectangle", "Circle"]


# Asks the user if they would like to see the Instructions
print()
show_instructions = list_checker("Hey Mathematician, would you like to see the Instructions (Yes/No)? ",
                                 yes_no_list, "Please answer Yes or No")

# If user inputs 'yes', shows user Instructions
if show_instructions == "yes":
    print()
    print("📢📢📢 Area Quiz Instructions 📢📢📢")
    print("Hey Mathematician, I see you're new here")
    print()
    print("1️⃣ Enter the number of questions you would like to answer or press <ENTER> to enter Infinite Mode")
    print("2️⃣ Select the Level of Difficult: Easy / E , Medium / M , Hard / H")
    print()
    print("❗Easy Level features Area of Rectangle, Triangle, and Circle. "
          "You get 3 tries to answer correctly for each question")
    print("❗Medium Level features Area of all the shapes listed above but the lengths of the shape are longer. "
          "You get 2 tries to answer correctly for each question")
    print("❗Hard Level features Area of all the shapes listed above, has the same length ranges of Medium Level,"
          " but also features Finding the Missing Side question for all three shapes. "
          "You get 1 try to answer correctly for each question")
    print()
    print("💡💡💡 Formula for Area of Rectangle: Area 🟰 Width ✖️ Height 💡💡💡")
    print("💡💡💡 Formula for Area of Triangle: Area 🟰 1/2 ✖️ Width ✖️ Height 💡💡💡")
    print("💡💡💡 Formula for Area of Circle: Area 🟰 π ✖️ Radius ✖️ Radius 💡💡💡")
    print()
    print("3️⃣ For each question, enter and answer or to quit enter <xxx>")
    print("4️⃣ You can then see the Quiz History and Quiz Result Summary")
    print("5️⃣ Choose to either Play Again or quit")
    print()
    print("👍👍👍 Good Luck Mathematician!!! 👍👍👍")


playing_quiz = "yes"
while playing_quiz == "yes":

    questions_answered = 0
    answer_tries = 0
    correct_answer = 0
    incorrect_answer = 0

    # List of Answered Questions
    quiz_history = []

    # Asks user how many questions they would like
    print()
    total_questions = num_check("How many questions would you like (Enter Number or <ENTER> for Infinite Mode): ", 0)

    if total_questions == "":
        print("♾️♾️♾️ Entering Infinite Mode ♾️♾️♾️")

    # Asks user how much hard they would like their questions
    print()
    difficulty_level = list_checker("Level of Difficulty (Easy (E) / Medium (M)/ Hard (H)): ", difficulty_list,
                                    "Please choose from Easy, Medium, or Hard")
    end_quiz = "no"
    while end_quiz == "no":
        print()
        # Infinite Mode is activated if user presses <ENTER>
        if total_questions == "":
            heading = f"♾️♾️♾️ Infinite Mode: Question {questions_answered + 1} ♾️♾️♾️"

        # Else the program outputs a heading including which question out of the total questions the user is on
        else:
            total_questions = int(total_questions)
            heading = f"➕➖✖️➗ Question {questions_answered + 1} of {total_questions} ➕➖✖️➗"
            if questions_answered == total_questions:
                playing_quiz = "no"
                break

        print(heading)

        shape = random.choice(shape_list)
        question = "Area"

        # If difficulty level is easy, the random number range is from 1 to 10 for width,
        # for height the range is 1 to 5 and for radius the range is 1 to 3
        # The user gets 3 tries to answer the question
        if difficulty_level == "easy":
            width = random.randint(1, 10)
            height = random.randint(1, 5)
            radius = random.randint(1, 3)
            answer_tries = 3

        else:
            # For both hard and medium, the random number range is from 5 to 15 for width,
            # for height the range is 5 to 10 and for radius the range is 2 to 5
            width = random.randint(5, 15)
            height = random.randint(1, 5)
            radius = random.randint(2, 5)

            # If difficulty level is medium, the user gets 2 tries to answer the question
            if difficulty_level == "medium":
                answer_tries = 2

            # If difficulty level is medium, the user gets 2 tries to answer the question
            # Hard level also has two types of questions: Find the Area and Find the Side Length
            # The user gets 1 tries to answer the question
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

        elif shape == "Circle":
            # Formula for Area of Circle
            area = math.pi * radius * radius

        # Program outputs question to find the side length and gives the area and height or just area for the circle
        if question == "Find Missing Side":
            if shape == "Triangle" or shape == "Rectangle":
                print(f"{question} of {shape} \t | \t Area: {area} \t | \t Height: {height}")
                valid_answer = width
            else:
                shape = "Circle"
                question = "Finding Radius"
                print(f"{question} of {shape} \t | \t Area: {area:.2f}")
                valid_answer = radius

        # Program outputs question for finding the area of the circle and gives the width and height or radius
        elif question == "Area":
            if shape == "Rectangle" or shape == "Triangle":
                print(f"{question} of {shape} \t | \t Width: {width} \t | \t Height: {height}")
                valid_answer = math.ceil(area)
            else:
                print(f"Area of Circle \t | \t Radius: {radius} (Remember to ROUND to the 2 d.p.)")
                valid_answer = round(area, 2)

        # List of Answers
        already_answered = []

        # Prints the answer for testing purposes
        # print(valid_answer)

        while True:

            # Asks user to answer the question
            users_answer = num_check("Answer ('xxx' to quit): ", 0, exit_code="xxx")

            # If user inputs the exit code, program breaks
            if users_answer == "xxx":
                playing_quiz = "no"
                end_quiz = "yes"
                break

            if users_answer == "":
                print("Please enter a number")
                continue

            # Checks if user's answer was a whole number or number with decimals
            if users_answer % 1 == 0:
                users_answer = math.ceil(users_answer)
            else:
                users_answer = round(users_answer, 2)

            # If user's input is already in the List of Answers, it displays error message
            if users_answer in already_answered:
                print(f"You've already answered {users_answer}! You still have {answer_tries} tries left.")
                continue

            answer_tries -= 1
            already_answered.append(users_answer)

            # If user gets the answer correct, program congratulates the user
            if users_answer == valid_answer:
                print("✅✅✅ Woohoo you got the answer correct ✅✅✅")
                correct_answer += 1
                incorrect_answer -= 1
                question_result = f"✅ {question} of {shape} | Correct ✅"
                break

            # If tries are all used then program shows the answer
            if answer_tries == 0:
                print("❌❌❌ Incorrect Answer ❌❌❌")
                print(f"💡💡💡 The Correct Answer was: {valid_answer} 💡💡💡")
                question_result = f"❌ {question} of {shape} | You answered: {users_answer} | " \
                                  f"Correct Answer: {valid_answer} ❌"
                break

            # If users gets the answer wrong, program tells the user that they were incorrect and shows tries left
            elif users_answer != valid_answer:
                print(f"❌❌❌ Incorrect Answer | Tries Left: {answer_tries} ❌❌❌")

        # If the user did not enter the exit code, it enters the user's answer into a list
        if users_answer != "xxx":
            outcome = f"«{questions_answered + 1}» {question_result} "
            quiz_history.append(outcome)
            questions_answered += 1
            incorrect_answer += 1

    # If user quits on the first question, displays message
    if questions_answered == 0:
        print("🐔🐔🐔 You chickened out 🐔🐔🐔")

    else:
        print()
        see_quiz_history = list_checker("Would you like to see Quiz History? ", yes_no_list,
                                        "Please answer Yes or No") .lower()
        # If user wants to see Quiz History, program displays Quiz History for the whole game
        if see_quiz_history == "yes":
            print()
            print("✅ Quiz History ❌")
            for outcome in quiz_history:
                print(outcome)

        # Calculates the Percentage for how much the user got correct
        correct_percentage = correct_answer / questions_answered * 100
        correct_percentage = math.ceil(correct_percentage)

        # Displays the Quiz Summary
        print()
        print("✅ Quiz Result Summary ❌")
        if incorrect_answer != 0:
            print(f"✅ Correct Answers: {correct_answer} ✅|❌ Incorrect Answers: {incorrect_answer} ❌")
            print(f"📋 Question Answered: {questions_answered} 📋")
            print(f"🎯🎯🎯 Accuracy: {correct_percentage}% 🎯🎯🎯")

            # If user scored a percentage more than or equal to 80 and less than 100, user passes the quiz
            if 80 <= correct_percentage < 100:
                print("🥳🥳🥳 Great Job, You've passed the Quiz 🥳🥳🥳")

                # Otherwise, program tells them to work harder
            else:
                print("👍👍👍 Work a little harder, you got this 👍👍👍")
        # If user got all answers correct, this message is displayed
        else:
            print(f"👑👑👑 Absolute Legend, "
                  f"You got all {correct_answer} out of {questions_answered} answers correct 👑👑👑")

    # After the quiz has ended, program asks the user if they would like to play again
    print()
    play_again = list_checker("🔃 Play Again (Yes/No) 🔃: ", yes_no_list, "Please answer Yes or No")

    # If user wants to play again, the quiz restarts
    if play_again == "yes":
        playing_quiz = "yes"

# If game ends, program thanks the user for playing
print()
print("👋👋👋 Thanks for playing 👋👋👋")
