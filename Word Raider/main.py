import random
from turtledemo.forest import start

# incorrect_words = []
game_name = "word raider"
word_bank = []
max_tries = 15

with open("assets/words.txt", "r") as file:
    for line in file:
        word_bank.append(line.strip())






def game():
    guess_word = random.choice(word_bank)
    letters = [letter for letter in guess_word]
    print(f"{letters}\n{(len(letters) * 5) * "-"}\n")

    tries_left = max_tries
    pre = """to exit type stop to get a list of wrong words type wrong"""

    print(f"{len(pre) * "_"}\n")
    print(pre)
    print(f"{len(pre) * "_"}\n")

    misplaced_letters = []
    incorrect_letters = []

    while tries_left > 0:
        prompt = f"Guess the word\nou have {tries_left} tries left: "
        guess = input(prompt).lower().strip()

        if guess == "stop":
            break

        if guess == "wrong":
            print(incorrect_words)


        if len(guess) != len(guess_word):
            len_chk = "Please enter a 5 letter word"
            print (len_chk)
            continue

        index = 0
        # guess_pro = ""

        for letter in guess:
            if letter == guess_word[index]:
                # guess_pro += letter
                print(letter,end=" ")

            elif letter in guess_word:
                if letter not in misplaced_letters:
                    misplaced_letters.append(letter)
                print("_",end=" ")
                # guess_pro += "_"

            else:
                if letter not in incorrect_letters:
                    incorrect_letters.append(letter)
                print("_", end=" ")
                # guess_pro += "_"
            index += 1
        # print(guess_pro)
        if guess == guess_word:
            print("Correct!")
            break

        tries_left -= 1


        print(f"\n{misplaced_letters}")
        print(incorrect_letters)


    if tries_left == 0:
        print("End of Game")



def main():
    while True:
        user_choice = input(
            "Press [Enter] to start or type exit to leave\n"
        ).lower().strip()
        if user_choice == "exit":
            print("goodbye")
            break

        game()

# print(word_bank)
# print(guess_word)


main()
# print(incorrect_words)


"""
things to do:
# wordbank should use different word length
# modify game rules
# create different levels

"""