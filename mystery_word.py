import random


def word_bank():
    '''entire word bank
    '''
    word_bank = []
    with open("words.txt") as word_txt:
        for spot in word_txt:
            word = spot.replace("\n", "")
            word_bank.append(word)
    # print(word_bank)


def difficulty_word_bank(word_bank):
    '''filtered word bank for each difficulty
    '''
    difficulty_setting = input(
        "Enter difficulty: EASY, NORMAL, or HARD:  ").lower
    diff_word_bank = []
    # Easy Mode 4 - 6 letter words
    # Normal Mode 6 - 8 letter words
    # Hard Mode 8+ letter words


# def play_game():
if __name__ == "__main__":
    play_game()
