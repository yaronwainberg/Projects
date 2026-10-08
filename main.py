import random

# incorrect_words = []
game_name = "word raider"
word_bank = []
max_tries = 15

with open("assets/words.txt", "r") as file:
    for line in file:
        word_bank.append(line.strip())

guess_word = random.choice(word_bank)

letters = [letter for letter in guess_word]
print(letters)




def game():

    incorrect_words = []
    tries_left = max_tries
    pre = """to exit type stop to ge a list of wrong words type wrong"""

    print(f"{len(pre) * "_"}\n")
    print(pre)
    print(f"{len(pre) * "_"}\n")

    while tries_left > 0:

        prompt = f"guess the letters\nou have {tries_left} tries left: "
        guess = input(prompt).lower().strip()
        if guess == "stop":
            break
        elif guess == "wrong":
            print(incorrect_words)
            continue
        elif guess in letters:
            print("you guessed a letter\n")
        else:
            print("wrong letter, try again\n")
            incorrect_words.append(guess)
        tries_left -= 1
    return incorrect_words

def main():
    while True:
        user_choice = input(
            "press [Enter] to start or exit to exit"
        ).lower().strip()
        if user_choice == "exit":
            print("goodbye")
            break

        game()

# print(word_bank)
# print(guess_word)


main()
print(incorrect_words)