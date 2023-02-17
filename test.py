import random
pet_list = ["cat", "dog", "bird", "ferret", "toad", "lizard", "snake"]


def count_pets(list):
    '''list out count of pets
    '''
    for count, value in enumerate(pet_list):
        print(count, value)


def pick_random_pet(list):
    '''pick random pet from list
    '''
    pet = random.choice(pet_list)
    return pet


choosen_pet = pick_random_pet(pet_list)


def game():
    layout = []
    for letter in choosen_pet:
        layout.append(letter)

    guess = input("guess word: ")
    for count, value in enumerate(layout):
        if guess == value:
            layout[count] = guess
        print(count, value)
    slots(layout)


def slots(word):
    '''make guessing slots
    '''
    word_slots = []
    for letter in word:
        word_slots.append(" _ ")
    print(word_slots)


game()
