# Checks input is exit code or integer and over low number
def num_check(question, low=None, exit_code=None):
    while True:
        response = input(question).lower()
        if response == exit_code:
            return response

        elif response == "":
            return response

        try:
            response = float(response)
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

    # Rounds Heading
    print()
    # Infinite Mode is activated if user presses <ENTER>
    if total_questions == "":
        heading = "Infinite Mode: Round {}".format(questions_answered + 1)

    else:
        total_questions = int(total_questions)
        heading = f"Round {questions_answered + 1} of {total_questions}"
        if questions_answered == total_questions - 1:
            end_game = "yes"

    print(heading)

    user_guess = num_check("Answer: ")

    if user_guess == "xxx":
        break

    # Rest of the loop / game
    user_guess = int(user_guess)
    print(f"You chose {user_guess}")

    questions_answered += 1

print("Thanks for playing")
