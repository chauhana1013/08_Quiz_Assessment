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


# Put in loop for testing
while True:
    questions = num_check("How many questions would you like: ", 0)

    # Infinite Mode is activated if user presses <ENTER>
    if questions == "":
        print("Infinite Mode Activated")

    # Prints the amount of questions user wants to answer
    print(f"You want to answer {questions} questions")

