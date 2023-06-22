question_answered = 0
correct_answer = 0
incorrect_answer = 0
quiz_history = []

for item in range(1, 6):
    question_result = input("Choose result: ").lower()

    if question_result == "correct":
        correct_answer += 1
        question_result = "✅✅✅ Correct ✅✅✅"

    elif question_result == "incorrect":
        incorrect_answer += 1
        question_result = "❌❌❌ Incorrect ❌❌❌"

    outcome = f"Question {item}: {question_result}"

    quiz_history.append(outcome)
    question_answered += 1

see_quiz_history = input("Would you like to see Quiz History? ").lower()

if see_quiz_history == "yes":
    print("| Quiz History |")
    for question_result in quiz_history:
        print(question_result)

correct_percentage = correct_answer / question_answered * 100
print()
print("| Quiz Result Summary |")
print(f"✅ Correct Answers: {correct_answer} ✅|❌ Incorrect Answers: {incorrect_answer} ❌|"
      f" 📋 Question Answered: {question_answered} 📋")
print(f"🎯🎯🎯 Accuracy: {correct_percentage}% 🎯🎯🎯")
