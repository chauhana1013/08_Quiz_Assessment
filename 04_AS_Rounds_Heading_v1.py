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


questions_answered = 0

# Ask user for # of rounds, press <enter> for infinite mode
end_game = "no"
while end_game == "no":
    total_questions = num_check("How many questions would you like: ", 0)

    while True:
        print()
        # Infinite Mode is activated if user presses <ENTER>
        if total_questions == "":
            heading = f"♾♾♾ Infinite Mode: Question {questions_answered + 1} ♾♾♾"

        # Else the program outputs a heading including which question out of the total questions the user is on
        else:
            heading = f"Question {questions_answered + 1} of {total_questions}"
            if questions_answered == total_questions:
                end_game = "yes"
                break

        print(heading)

        user_guess = num_check("Answer: ", 0, exit_code="xxx")

        # If user enters the exit code, program breaks
        if user_guess == "xxx":
            break

        # Rest of the loop / game
        print(f"You chose {user_guess}")

        questions_answered += 1

print("Thanks for playing")
