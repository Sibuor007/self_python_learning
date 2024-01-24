import random
import hangman_images

word_list = ["apple", "beautiful", "potato"]
chosen_word = random.choice(word_list)
print(chosen_word)
lives_ = 7

display_ = []
for letter in chosen_word: # we can also use range
    display_ += '_'
print(display_)
game_over = False

while not game_over:
    guess_letter = input("Guess a letter: ").lower()
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess_letter:
            display_[position] = letter
    print(display_)

    if guess_letter not in chosen_word:
        lives_ -= 1
        if lives_ == 0:
            game_over = True
            print("You Lose!")
    if '_' not in display_:
        game_over = True
        print("You Win")
    print(hangman_images.stages_0[lives_])
