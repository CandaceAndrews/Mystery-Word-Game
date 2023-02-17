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
    return diff_word_bank
    # Normal Mode 6 - 8 letter words
    # Hard Mode 8+ letter words


def choose_random_word(final_word_bank):
    """ pick random word from difficutly word bank
    """
    return random.choice(final_word_bank)


def test_print():
    test = word_bank()
    easy = difficulty_word_bank(test)
    for _ in easy:
        print(_)


test_print()


# def play_game():
# if __name__ == "__main__":
#     play_game()
