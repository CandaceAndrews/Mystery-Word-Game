import random


def word_bank():
    """ entire word bank
    """
    word_bank = []
    with open("words.txt") as word_txt:
        for spot in word_txt:
            word = spot.replace("\n", "")
            word_bank.append(word)
    return word_bank
    # print(word_bank)


def difficulty_word_bank(word_bank):
    """ filter word bank by difficulty
    """
    difficulty_setting = input(
        "Enter difficulty: EASY, NORMAL, or HARD:  ").lower()
    diff_word_bank = []
    # Easy Mode 4 - 6 letter words
    if difficulty_setting == "easy":
        for word in word_bank:
            if len(word) >= 4 and len(word) <= 6:
                diff_word_bank.append(word)
    # Normal Mode 6 - 8 letter words
    elif difficulty_setting == "normal":
        for word in word_bank:
            if len(word) >= 6 and len(word) <= 8:
                diff_word_bank.append(word)
    # Hard Mode 8+ letter words
    elif difficulty_setting == "hard":
        for word in word_bank:
            if len(word) >= 8:
                diff_word_bank.append(word)
    return diff_word_bank


def choose_random_word(final_word_bank):
    """ pick random word from difficutly word bank
    """
    return random.choice(final_word_bank)


def guessing_slots(word_to_guess):
    mystery_word = []
    for spot in word_to_guess:
        mystery_word.append(" _ ")
    return mystery_word


def main_game(computer_chosen_word, mystery_word_slots):
    """ main flow of the game
    """
    turn = 2
    while turn > 0:
        guess = input("Please choose a letter or EXIT: ").lower()
        if guess in computer_chosen_word:
            for count, value in enumerate(computer_chosen_word):
                if guess == value:
                    mystery_word_slots[count] = guess
        elif guess == "exit":
            break
        else:
            turn -= 1
            print("Letter not in the word, please try again.")
        print(mystery_word_slots)


def play_game():
    """ contains combined functions to run the game
    """
    entire_word_bank = word_bank()
    word_bank_for_chosen_difficulty = difficulty_word_bank(entire_word_bank)
    computer_chosen_word = choose_random_word(word_bank_for_chosen_difficulty)
    mystery_word_slots = guessing_slots(computer_chosen_word)

    print(computer_chosen_word)
    print()
    print(mystery_word_slots)
    print()
    main_game(computer_chosen_word, mystery_word_slots)


if __name__ == "__main__":
    play_game()
