import random


def word_bank():
    """entire word bank
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
        "Choose your difficulty (easy, normal, hard): ").lower()
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
    """ make slots for mystery word
    """
    mystery_word = []
    for _ in word_to_guess:
        mystery_word.append("_")
    return mystery_word


def store_guessed_letters(turn, computer_chosen_word, mystery_word_slots, word_bank_for_chosen_difficulty):
    """ main flow of the game
    """
    game_running = True
    used_letters = []
    while game_running is True:
        while turn > 0 and "_" in mystery_word_slots:
            guess = input("Please guess a letter: ").lower()
            if len(guess) > 1:
                print("One letter ONLY!")
            else:
                if guess not in used_letters:
                    used_letters.append(guess)
                    if guess in computer_chosen_word:
                        for count, value in enumerate(computer_chosen_word):
                            if guess == value:
                                mystery_word_slots[count] = guess
                    else:
                        turn -= 1
                    print("_________________________________")
                    print("Wrong guess!")
                    # print(computer_chosen_word)
                    print(f"Turn:  |{turn}|")
                    print(f"Letters Guessed:  {used_letters}")
                    print()
                    print(' '.join(mystery_word_slots))
                else:
                    print("_________________________________")
                    print(f"You've already guessed {guess}")
                    # print(computer_chosen_word)
                    print(f"Turn:  |{turn}|")
                    print(f"Letters Guessed:  {used_letters}")
                    print()
                    print(' '.join(mystery_word_slots))
        if "_" not in mystery_word_slots:
            print("_________________________________")
            print(
                f"Congratulations, you won! The word was {computer_chosen_word}")
            play_again = input("Play again? |YES or NO|  ").lower()
            if play_again == "yes":
                play_game()
            else:
                game_running = False
                break
        else:
            print("_________________________________")
            print(f"You lose! The word was {computer_chosen_word}")
            # Play again section ----
            play_again = input("Play again? |YES or NO|  ").lower()
            if play_again == "yes":
                play_game()
            else:
                game_running = False
                break


def play_game():
    """ runs combined functions to start the game
    """
    turn = 8
    entire_word_bank = word_bank()
    word_bank_for_chosen_difficulty = difficulty_word_bank(entire_word_bank)
    computer_chosen_word = choose_random_word(word_bank_for_chosen_difficulty)
    mystery_word_slots = guessing_slots(computer_chosen_word)

    # Print for 1st Round
    print(f"Turn:  |{turn}|")
    # print(computer_chosen_word)
    print()
    print(' '.join(mystery_word_slots))

    store_guessed_letters(turn, computer_chosen_word,
                          mystery_word_slots, word_bank_for_chosen_difficulty)


if __name__ == "__main__":
    play_game()
