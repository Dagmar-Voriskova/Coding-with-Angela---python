import random
from hangman_art import stages, logo
from hangman_words import word_list

print(logo)

chosen_word = random.choice(word_list)
#print(chosen_word)

placeholder = []
for letter in chosen_word:
    placeholder.append("_")
print("".join(placeholder))

guessed = []
#correct = []
#wrong = []
lives = 6

while "".join(placeholder) != chosen_word and lives >= 0:
    if lives == 0:
        print(f"Game over! The word was {chosen_word}.")
        break
    else:
        guess = input("Guess a letter: ").lower()
        if guess in guessed:
            print(f"You already guessed this letter, but no lives were lost. You still have {str(lives)} lives left.")
        elif guess not in chosen_word:
            #wrong.append(guess)
            lives -= 1
            if lives == 1:
                print(f"{guess} is not in the word. You lose a life. You now have only {str(lives)} life left.")
            elif lives == 0:
                print(f"{guess} was unfortunately not in this word and you have no lives left.")
            else:
                print(f"{guess} is not in the word. You lose a life. You now have {str(lives)} lives.")
        elif guess in chosen_word:
            #correct.append(guess)
            print(f"Yes! {guess} is in the word. You still have {str(lives)} lives left.")
        guessed.append(guess)

        #print(guessed)
        #print(correct)
        #print(wrong)
        #print(lives)
        print(stages[lives])

        for index, letter in enumerate(chosen_word):

            if letter == guess:
                placeholder[index] = guess

        print("".join(placeholder))

        if "".join(placeholder) == chosen_word:
            print(f"You guessed the word {chosen_word}!")
            print("********************!!!YOU WIN!!!********************")


