
def difficulty_checker(question):
    while True:
        response = input(question).lower()
        if response == "easy" or response == "e":
            return "easy"

        elif response == "medium" or response == "m":
            return "medium"

        elif response == "hard" or response == "h":
            return "hard"

        else:
            print("Please choose either Easy / Medium / Hard")
            print()


while True:
    difficulty_level = difficulty_checker("Level of Difficulty (Easy / Medium / Hard): ")

    if difficulty_level == "easy":
        print("You selected Easy Difficulty")

    elif difficulty_level == "medium":
        print("You selected Medium Difficulty")

    elif difficulty_level == "hard":
        print("You selected Hard Difficulty")
    print()
