import random

def hangman(word):
    wrong = 0
    stages = ["",
             "_________",
             "|        |      ",
             "|        0      ",
             "|       /|\     ",
             "|       / \     ",
             "|               ",
             "|               "
              ]
    rem_letters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Welcome to Hangman!")

    while wrong < len(stages) - 1: 
        char = input("Guess a letter\n")
        if char in rem_letters:
            ind = rem_letters.index(char)
            board[ind] = char
            rem_letters[ind] = '$'
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0: e]))
        if "_" not in board:
            print("You win!")
            print(" ".join(board))
            win = True
            break

    if not win:
        print("\n".join(stages[0: wrong]))
        print("You lose! It was {}".format(word))

wordbunch = ["python", "java", "cobol", "fortran", "ada", "basic"]
hangman(wordbunch[random.randint(0, 5)])