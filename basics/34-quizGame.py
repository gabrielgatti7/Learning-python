def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 0

    for key in questions:
        print(key)
        for i in options[question_num]:
            print(i)
        guess = input("A, B, C or D?: ").upper()
        guesses.append(guess)
        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1
        print("------------------------------------------")
    print("------------------------------------------")
    display_score(correct_guesses, guesses)

def check_answer(answer, guess):
    if(answer == guess):
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0

def display_score(correct_guesses, guesses):
    print("CORRECT ANSWERS: ", end='')
    for value in questions.values():
        print(value, end=' ')
    print("\nYOUR GUESSES:    ", end='')
    for i in guesses:
        print(i, end=' ')
    print("\nScore: "+str(int(correct_guesses*100/len(guesses)))+"%")


def play_again():
    again = input("Would you like to play again? (Y/N): ").upper()
    if again != "Y":
        return False
    else:
        return True

#dictionary
questions = {
    "Who created Python?: " : "A",
    "What year was Python created?: " : "B",
    "Python is tributed to which comedy group?: " : "C",
    "Is the Earth round?: " : "A"
}

options = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerberg"],
           ["A. 1989", "B. 1991", "C. 2000", "D. 2002"],
           ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
           ["A. True", "B. False", "C. sometimes", "D. What's Earth?"]]

new_game()

while play_again():
    new_game()